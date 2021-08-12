import json

import pandas as pd   
test_diplomacy_dictionary = {}
# Opens the test diplomacy json file

with open('train.json') as json_file:

    # Creates an empty dictionary for us to store all the game dictionaries in


    # Initialise the counter at zero to number each diplomacy game

    counter = 0

    # for loop for every game saved in the json

    for dictionary in json_file:

        # read the json of the game into python as a dictionary

        diplomacy_dict = json.loads(dictionary)

        # adds the game dictionary to the overall test dictionary

        test_diplomacy_dictionary[counter] = diplomacy_dict

        # updates the counter so the next game is 1 etc.

        counter += 1
lie_countdict={}
gamesc_countdict={}

for i in range (0,13):
    lie_countdict[i]={"austria":0,"germany":0,"italy":0,"turkey":0,"russia":0,"england":0,"france":0}
for i in range (0,13):
    gamesc_countdict[i]={"austria":0,"germany":0,"italy":0,"turkey":0,"russia":0,"england":0,"france":0}
    
# lie_countdict= {0:{"austria":0,"germany":0,"italy":0,"turkey":0,"russia":0,"england":0,"france":0},
# 1:{"austria":0,"germany":0,"italy":0,"turkey":0,"russia":0,"england":0,"france":0},
# 2:{"austria":0,"germany":0,"italy":0,"turkey":0,"russia":0,"england":0,"france":0}}  
# print(lie_countdict)
    # Example of the first game
for item in test_diplomacy_dictionary.keys():
    print(test_diplomacy_dictionary[item]["speakers"],flush=True)
    print(test_diplomacy_dictionary[item]["game_id"],flush=True)
    print(test_diplomacy_dictionary[item]["game_score"],flush=True)
    internal_counter=0
    for label in test_diplomacy_dictionary[item]["sender_labels"]:
        if  label is not True:
            lie_countdict[int(test_diplomacy_dictionary[item]["game_id"])][test_diplomacy_dictionary[item]["speakers"][internal_counter]]+=1 
            gamesc_countdict[int(test_diplomacy_dictionary[item]["game_id"])][test_diplomacy_dictionary[item]["speakers"][internal_counter]]+=1 
        internal_counter+=1           
    
print(lie_countdict)  
print(gamesc_countdict)

# gamesc_countdict= {"game_id":""


