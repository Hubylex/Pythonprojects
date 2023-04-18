pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  12: "True",
}

print(pairs.get(1))
print(pairs.get(7, 42))
print(pairs.get(True))
print(pairs.get(12345, "not found"))

print(len(pairs))

print('\n')

print(1 in pairs)
print('hey' not in pairs)