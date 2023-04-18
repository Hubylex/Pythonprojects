string = '1 0 0 1 0 1'
binary = string.replace(' ','') ## binary = string[::2] 
result = int(binary,2)
print(result)