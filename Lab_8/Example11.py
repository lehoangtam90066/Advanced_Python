best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains)) 


import json


best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string)) 
print(best_food_chains_string)


best_food_chains_list = json.loads(best_food_chains_string)
print(type(best_food_chains_list))  
print(best_food_chains_list)
