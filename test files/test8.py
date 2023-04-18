import re
path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'
check = r'youtube'
print(f'path1: {re.search(check,path1)}')
print(f'path2: {re.search(check,path2)}')