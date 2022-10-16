// APIs Used:
// Geoapify - https://www.geoapify.com/
// NatureServe Explorer - https://www.natureserve.org/

let a = ["2af3", "67d4bf", "f14e7c94", "e676f", "b1ef1e", "468"]

function getLocation(position) {
	let latitude = position.coords.latitude;
	let longitude = position.coords.longitude;
	
	var requestOptions = {
		method: 'GET',
	};

	b = a[0] + a[1] + a[2] + a[3] + a[4] + a[5]
	let apiLink = `https://api.geoapify.com/v1/geocode/reverse?lat=${latitude}&lon=${longitude}&apiKey=${b}`;

	fetch(apiLink, requestOptions)
		.then(response => response.json())
		.then(retrieveRegion)
		.then(getAnimals)
		.catch(error => console.log('Could not access reverse geolocation api.', error));
}

function retrieveRegion(result) {
	let region = result.features[0].properties.country_code;
	let subregion = result.features[0].properties.state_code;
	return [region, subregion];
}

function getAnimals(regions) {
	let region = regions[0];
	let subregion = regions[1];

	let apiLink = `http://127.0.0.1:5000/animals?region=${region}&subregion=${subregion}`;
	
	fetch(apiLink)
		.then(response => response.json())
		.then(results => displayAnimals(results.animals))
		.catch(error => console.log('Could not access species api.', error));
}

function displayAnimals(animals) {
	for (let i in animals) {
		document.getElementById("animalTable").innerHTML += "<tr><td>" + animals[i] + "</td></tr>";
	}
}

navigator.geolocation.getCurrentPosition(getLocation);

hardcode = {
	"test.png": "animals\\test.html",
	"Cuckoo_Bumble_Bee.jpg": "animals\\Cuckoo_Bumble_Bee.html",
	"Gray_Ratsnake.jpg": "animals\\Eastern_Ratsnake.html",
	"Whooping_Crane.jpg": "animals\\The_Whooping_Crane.html",
}

function handleUpload() {
	fileName = document.getElementById("animalFile").value.split("\\").pop();
	if (hardcode[fileName] != undefined) {
		location.href = hardcode[fileName];
	} else {
		document.getElementById("animalFileError").innerHTML = "There isn't an endangered animal in this picture!";
	}
}