import json
fast_food = {
    "MacDonald's": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}
print(type(fast_food))  


fast_food_string = json.dumps(fast_food)
print(type(fast_food_string)) 
print(fast_food_string)

fast_food_dic = json.loads(fast_food_string)
print(type(fast_food_dic))  
print(fast_food_dic)
