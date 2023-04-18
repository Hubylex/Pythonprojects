
'''# write mode - rewriting the contents of a file
open("filename.txt", "w")

# read mode - 
open("filename.txt", "r")


# append mode - adding new conten to the end 0f the file
open("filename.txt","a")


# binary write mode - 
open("filename.txt", "wb")
 
 #FILE MODES: "r" Read from file - YES            Write to file - NO                        
 # Create file if not exists - NO 
Truncate file to zero length - NO         Cursor position - BEGINNING 

"r+" Read from file - YES                 Write to file - YES 
Create file if not exists - NO            Truncate file to zero length - NO
Cursor position - BEGINNING

"w" Read from file - NO                   Write to file - YES 
Create file if not exists - YES          Truncate file to zero length - YES 
Cursor position - BEGINNING

 "w+" Read from file - YES
Write to file - YES                         Create file if not exists - YES
Truncate file to zero length - YES          Cursor position - BEGINNING 

"a" Read from file - NO Write to file - YES 
Create file if not exists - YES          Truncate file to zero length - NO 
Cursor position - END 
"a+" Read from file - YES
Write to file - YES                   Create file if not exists - YES 
Truncate file to zero length - NO     Cursor position - END

'''



file = open("newfile.txt", "r+") 
file.write("This has been written to a file") 
print(file.read()) 
file.close()