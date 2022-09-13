import numpy as np

A = np.arange(1,6)

C = np.arange(1,26).reshape(5,5)

#A = array([1,2,3,4,5]) #This is how A looks

#C = array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]) #this is how C looks after reshape


#In python Array are 0 indexed
#print(A[2]) # to access 3 in array A

#print(C[2,3]) # to access 14 from C (2) is the colomn and 3 is the row in which 14 is present 

A[2] = -3 # to change the value of 3 to minus 3
C[2,3] = - 14 #to change the value of 14 to -14
C[-1] = [1,2,6,0,0] # to change complete row 
C[-1] = 2 # Another method to change the last row to all numbers 2 

Slice = C[0:3,2] #slicing the array 0 = Start, 3 = stop , 2 = colomn index
Slice = C[2,0:3]# [row,colomn]

Slice = C[1,1:3] #H.w
Slice = C[0:4,0] #H.w
Slice = C[1:5,0] #H.W
Slice = C[1:3,2:4]#h.w


#print(A)

print(Slice)



