file = open('my file.txt','w')
file.write('this is my new text')            
file.close()



a = open('my file.txt','r')
print(a.read())
a.close()




file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

a = open("newfile.txt", "r")
print(a.read())
a.close()




file2 = open("mine.txt", "w+") 
print(file2.write("This has been written to a file now"))        #writes to the file and also stores the length of characters
file2.seek(0)
print(file2.read()) 
file2.close()










'''file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()'''