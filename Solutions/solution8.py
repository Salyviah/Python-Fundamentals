def merge_dicts(dict1, dict2):
    
    merged_dict = dict1.copy()
    
    
    for key, value in dict2.items():
        if key in merged_dict:
            
            merged_dict[key] += value
        else:
            
            merged_dict[key] = value
    
    return merged_dict


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 50, 'c': 150, 'd': 250}


merged_dict = merge_dicts(dict1, dict2)


print(merged_dict)
