import requests

url = r"https://explorer.natureserve.org/api/data/speciesSearch/"
params = {"criteriaType" : "species",
          "locationCriteria": [
              {"paramType": "subnation",
               "subnation": "ON",
               "nation": "ca"}],
          "statusCriteria": [
              {"paramType": "globalRank",
               "globalRank": "G1"}]}

{'criteriaType': 'species',
 'locationCriteria': [
     {'paramType': 'subnation',
      'subnation': "ON'",
      'nation': 'ca'}],
 'statusCriteria': [
     {'paramType': 'globalRank',
      'globalRank': 'G1'}]}

result = requests.post(url, json=params).json()
#animals = [animal['primaryCommonName'] for animal in result['results']]
print(result.keys())
