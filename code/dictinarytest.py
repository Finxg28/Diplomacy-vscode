import json
import pandas as pd

with open('testjson.json') as json_file:
    counter = 0
    for dictionary in json_file:
        print(counter)
        diplomacy_dict = json.loads(dictionary)
        game_score = diplomacy_dict['game_score']
        
        print(diplomacy_dict['game_score'])
        
