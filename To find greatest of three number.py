num_1 = int(input('Enter the first number : '))
num_2 = int(input('Enter the second number : '))
num_3 = int(input('Enter the third number : '))

if num_1 > num_2 :
    if num_1 > num_3:
        print(num_1, 'is the largest number')
    else:
        print(num_3, 'is the greatest number')
elif num_2 > num_3:
    print(num_2, 'is the greatest number')
else:
    print(num_3,'is the greatest number')
        