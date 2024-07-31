import json
import pdb

dataPath = "/home/louis/Documents/Projekte/SystematicReview/data/time explain | interpre | explanat | xai/"

# import json data
with open(dataPath + "query1.json") as dataFile:
  data = json.load(dataFile)

# get only formal publications and their amount
formalPubCount = 0
formalPubs = []

# iterate over all entries
for elem in data['result']['hits']['hit']:
  if elem['info']['type'] == 'Informal and Other Publications' or \
     int(elem['info']['year']) < 2014:
    pass
  else:
    formalPubs.append(elem)
    formalPubCount = formalPubCount + 1

# write result to file
with open(dataPath + "formalPubs.json", "w") as result:
    json.dump(formalPubs, result)
 
print(formalPubCount)
