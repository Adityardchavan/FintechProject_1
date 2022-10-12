# This code is incorrect - you need to fix it so that it provides the desired output!
import math
divide_by = 2
subtract_by = 3
multiply_by = 5

var = 1
var1 = int(var)-subtract_by
print("Subtracting your value of",var," by ",subtract_by,"will give", var1)

var2 = var1 / divide_by
print("Dividing ",var1," by ",divide_by," will give ",var2)

var_2 = input("Please provide a real number between 0 and 1: ")
print("The ceiling of",var_2,"is", math.ceil(float(var_2)))

var4 = 2
var5 = 3

print("Multiplying", var, "by", var5, "will give", var4*int(var5))
print("Multiplying", var4, "by", var5, "will give", int(var4)*int(var5))
print("Multiplying", float(var4), "by", var5, "will give", float(var4)*int(var5))