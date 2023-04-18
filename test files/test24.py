'''n = int(input())

file = open("numbers.txt", "w+")
#your code goes here
for i in range(1,n+1):
    file.write(str(f"\n{i}"))
file.close()
f = open("numbers.txt", "r")
print(f.read())
f.close()'''



'''You are given a books.txt file, which includes book titles, each on a separate line.
Create a program to output how many words each title contains, in the following format:
Line 1: 3 words
Line 2: 5 words

with open("newfile.txt") as f:
        s = 1
        for i in f.readlines():
                print('line '+str(s)+':',len(i.split(' ')),'words')
                s+=1
       
Harry Potter
The Hunger Games
Pride and Prejudice
Gone with the Wind'''


'''file = open("newfile.txt", "r")

for line in file:
    
        i = line.split()
        for word in i:
            print("".join(word[0]))

file.close()


file = open("newfile.txt", "r") #ваш код 
for line in file: 
    i = line.split() 
    print("".join(word[0] for word in i)) 
file.close()'''


txt = 'we live in cruel world'
def lon(txt):
    words = txt.split()
    lon_word = words[0]
    for i in words:
        if len(i)>len(lon_word):
            lon_word = i

    return lon_word
  


print(lon(txt))

