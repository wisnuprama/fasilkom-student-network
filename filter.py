import json
from collections import OrderedDict

if __name__ == '__main__':
  result = None
  with open('./result.json', 'r') as j:
    result = json.load(j)

  preprocessed = {}
  for p in result:
    preprocessed[p.get('publicIdentifier')] = p

  new_result = dict()

  for p_id in preprocessed:
    person = preprocessed[p_id]
    filtered_connections = []
    for ci in person.get('connections'):
      if ci.get('publicIdentifier') in preprocessed and ci not in filtered_connections:
        filtered_connections.append(ci)

    # dont mutate the original
    new_person = dict(person)
    new_person.update({'connections': filtered_connections})

    new_result[p_id] = new_person

  with open('./result_filtered.json', 'w') as j:
    json.dump(OrderedDict(new_result), fp=j, indent=2)
