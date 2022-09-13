import numpy as np

a1 = np.array([1,2,3,4]) #to creat a 1 dimensional array array 

a2 = np.array([[1,2,3,4],[5,6,7,8]]) #to create a 2 dimensional array

ar = np.arange(1,9) # to arange an array where 1 = start and 10 = Stop

ar.reshape(2,4)

ar.shape = (2,4) #to change the shape of an array

a1.shape # to know the shape of a1
ar.shape # to know the shape of ar

#print(a1.shape)
#print(ar.shape)

A = np.identity(2) #gives identity matrix
#print(A)

a = np.zeros((4,5)) #Matrix is 4 by 5 in zeros
#print(a)

B = np.ones((4,5))
#print(B)

b = np.zeros_like((4,5))
#print(b)

C = np.ones_like((4,5))
print(C + 3)


 