import json

with open('best_results.json') as json_file:
    data = json.load(json_file)
    print(json.dumps(data, indent=4))