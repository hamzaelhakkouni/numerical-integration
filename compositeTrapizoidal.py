import math
def CompositeTrapizoidal(function , a , b , n) :
    h = ( b - a ) / n 
    s = function(a) + function(b)
    for i in range(1 , n):
        x = a + (i * h )
        s = s + (2 * function(x))
    result = (h/2) * s
    return result

# My  Function

def function(x):
    res = (x * x ) + 2
    return res

# Test 
## For Function : x ^ 2 + 2
print("Integration between 0 and 1 is : " , CompositeTrapizoidal(function, 0 , 1 , 6))


## For cos :
print("Integration between 1 and 2 is : " , CompositeTrapizoidal(math.cos , 1 , 2 , 4))

