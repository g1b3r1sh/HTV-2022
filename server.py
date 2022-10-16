from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)

@app.route('/')
@cross_origin()
def hello_world():
   return jsonify(test_response)

@app.route('/animals')
@cross_origin()
def animals():
   region = request.args.get('region')
   subregion = request.args.get('subregion')
   animals = get_animals(region, subregion)
   print("animals:", animals)
   return jsonify({'animals': animals})

def get_animals(region, subregion):
   url = r"https://explorer.natureserve.org/api/data/speciesSearch/"
   params = create_region_params(region, subregion)
   results = requests.post(url, json=params).json()
   return [animal['primaryCommonName'] for animal in results['results']]
   #return_dict = {}
   #for animal in results['results']:
   #   return_dict[animal['primaryCommonName']] = get_description(animal['primaryCommonName'])
   #   print("Searching for " + animal['primaryCommonName'])
   #return return_dict

   #return {
   #   animal['primaryCommonName']:get_description(animal['primaryCommonName']) for animal in results['results']
   #}

# def get_description(animal_name):
#    page_title = get_page(animal_name)
#    if page_title == "":
#       return ""
#    url = r"https://en.wikipedia.org/api/rest_v1/page/summary/" + page_title
#    results = requests.get(url)
#    return results.json()['extract']

# def get_page(animal_name):
#    url = r"https://en.wikipedia.org/w/api.php?action=opensearch&search=" + animal_name + "&limit=1&namespace=0&format=json"
#    results = requests.get(url)
#    return results.json()[1][0]

def create_region_params(region, subregion):
   if subregion == '':
      return {
         "criteriaType" : "species",
         "locationCriteria": [{
            "paramType": "nation",
            "nation": region}],
         "statusCriteria": [
            {"paramType": "globalRank",
            "globalRank": "G1"}]
         }
   return {
      "criteriaType" : "species",
      "locationCriteria": [{
         "paramType": "subnation",
         "subnation": subregion,
         "nation": region}],
      "statusCriteria": [
         {"paramType": "globalRank",
            "globalRank": "G1"}]
      }

if __name__ == '__main__':
   app.run()
