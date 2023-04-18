'''Input:
S: loonbalxballpoon
Output: 2
Explanation:
Here, the number of occurence of 'b' = 2
of occurence of 'a' = 2
of occurence of 'l' = 4
of occurence of 'o' = 4
of occurence of 'n' = 2
So, we can form 2 "balloon" using the letters.

'''

def maxInstance(s):
    main = {'b': 1,  'a': 1, 'l':2 , 'o':2, 'n':1}
    s_data = {}  #{'l': 4, 'o': 4, 'n': 2, 'b': 2, 'a': 2}
    for i in s:
        if i not in s_data and i in main.keys():
            s_data[i]=1
        elif i in s_data and i in main.keys():
            s_data[i]+=1
        else:
            continue

   
    for n in range(1,100):
        for i in s_data:
            if s_data.get(i)>= main.get(i)* n :
                continue
            else:
                 return n-1
    
            
 
        

print(maxInstance('nlaebolko'))