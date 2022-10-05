import math

C=2000
n=7
i=0.05

FV = C*((math.pow(1+i,n)-1)/i)
print("The Future value of the amount invested over a period of 7 years is : ", FV)