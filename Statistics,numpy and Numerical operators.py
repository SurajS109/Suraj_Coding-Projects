import numpy as np

#loadtext = to load the file in tthe form of an array
#delimiter = to specify the chararcter that is separated by
#Usecols = to specify the columns to be used

L = np.loadtxt("C:/Users/suraj/Desktop/Parsing-data-Codefiles/student_record.txt",usecols=(3,4,5,6,7), delimiter =';')
 

#print(L[0]) # to access marks of only tthe first students

Total_marks = sum(L[0]) #sum the total marks of all subjects of the first student

mean = Total_marks/len(L[0]) #to know the mean of the marks by 1st students

print(mean)