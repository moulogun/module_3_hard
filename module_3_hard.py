def calculate_structure_sum(data_structure):
    total = 0
    for item in data_structure:
        if isinstance(item, int) == True or isinstance(item, float) == True:
            total += item
        elif isinstance(item, str) == True:
            total += len(item)
        elif isinstance(item, dict) == True:
            for key, value in item.items():
                if isinstance(value, int) == True or isinstance(value, float) == True:
                    total += value
                elif isinstance(value, str):
                    total += len(value)
                if isinstance(key, int) == True or isinstance(key, float) == True:
                    total += key
                elif isinstance(key, str):
                    total += len(key)
        else:
            total += calculate_structure_sum(item)
    return total


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)