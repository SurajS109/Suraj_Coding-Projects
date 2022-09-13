'''
name = range(2,10,3)                                       #(start,stop,step)
for x in name:
    print(x)
'''

'''
for i in range(1,10,2):
    print(i, end = ' ')                 #(end = " ") is used to print in the same line 
'''

'''    
i = 1
while i <=10:
    print(i, end = ' ')                 #same above problem but in while loop
    i = i + 2
'''

'''
for i in range(10):
    print(i,end = " ")
'''

'''
num = int(input('Enter the number : '))
for i in range(1,13):                                       # multiplication tabel 
    print(num, 'x', i,'=', i * num,)
'''   

'''
num =int(input('Enter the number : '))
if num == 0:
    f = 1
f = 1                                                       # factorial number
for i in range(1,num+1):
    f = f*i
print("Factorial of", num, 'is',f)        
'''

num = int(input('Enter the number : '))
sum = 0.0
for i in range(1,num+1):
    x = float(i)/(i+1)
    sum = sum + x
print('The sum of the series is', sum)    
    