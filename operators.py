#assignment operator 
# = simple assignment operator
# shift value from right to left variable 

var1 = 20 #20 assigned to var1 
print(var1)

var1, var2 = 35,45
print(var1,var2)

var1, var2 = var2, var1
print(var1,var2)

#multiple assignment
var1 = var2 = var3 = 100 
print(var1,var2,var3)
print(id(var1))
print(id(var2))
print(id(var3))

# short-hand assignment operator
num1 = 20 
print(id(num1))
#num1 = num1+5
num1+=5
print(id(num1))
print(num1)

# 2.arithmetic operators
# + Addition 
from array import array
n1 = array('i', [3,4,5])
n2 = array('i', [6,7,8])
n3= n1+ n2 
print(n3)
