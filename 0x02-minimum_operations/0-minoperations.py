#!/usr/bin/python3

def minOperation(n):
    if n <= 1:
        return 0
    print("n before loop:", n)

    divisor = 2
    num_of_operations = 0

    while n > 1:
        if n % divisor == 0:
            n = n // divisor  
            num_of_operations += divisor  
            print("n = n / divisor:", n)
        else:
            divisor += 1
            print("divisor after increment:", divisor)

    return num_of_operations

n = 12
print(minOperation(n))  
