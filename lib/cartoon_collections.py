

def roll_call_dwarves(dwarf_names):

    for index, dwarf in enumerate(dwarf_names, start=1):
        print(f"{index}. {dwarf}")
    

def summon_captain_planet(planeteer_calls):
    splitted_words = []

    for planet in planeteer_calls:
        results = planet[0].upper() + planet[1:] + '!'

        splitted_words.append(results)
        
    return splitted_words

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
        
    return False
    

def find_the_cheese(strings):

    cheese = ["cheddar", "gouda", "camembert"]

    for string in strings:
        if string in cheese:
            return string
    return None
    
