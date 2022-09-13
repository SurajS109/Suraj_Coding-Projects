#f = open("C:/Users/suraj/Desktop/Loading-Data-From-Files-Codefiles/pendulum.txt",'r')

#pend = f.read() #to read what's in the file 

#pend_list = pend.splitlines()  # split function is used to read the file in the form of list
#print(pend_list)

#f.close() #to closen the file

#f = open("C:/Users/suraj/Desktop/Loading-Data-From-Files-Codefiles/pendulum.txt") # to reopen the files
 
#for line in f:    #to iterate the lines in the files
    #print(line)

line_list = []

for line in open("C:/Users/suraj/Desktop/Loading-Data-From-Files-Codefiles/pendulum.txt"):
    line_list.append(line)
print(line_list)