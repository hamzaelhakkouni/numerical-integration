import math
def CompositeSimpson(function , a , b , n):
    h = ( b - a ) / n
    x = []
    x.append(a) 
    result = function(x[0])
    for i in range(1 , n):
        x.append(a + ( i * h ))
        if (i % 2) != 0 :
            result = result + ( 4 * function(x[i]))
        else :
            result = result + ( 2 * function(x[i]))

    x.append(b) 
    result = result + function(x[n])
    result = result * ( h / 3)
    return result

# ------- Create a function x ^ 2 - 1
def function(x):
    return ( x * x) - 1

# -------- Test for this function 
print("integral between 2 and 3 is : " , CompositeSimpson(function , 2 , 3 , 4))


# ---------Test for ln(x)
print("integral between 1 and 2 is : " , CompositeSimpson(math.log2 , 1 , 2 , 4))
