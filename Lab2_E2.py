import math

C=2000
n=7
i=0.05

#Future Value
FV = C*((math.pow(1+i,n)-1)/i)
print("The Future value of the amount invested over a period of 7 years is : ", round(FV,2))

#Present Value

D = 1000
n =5
i =0.05

PV = D*((1-math.pow(1+i,-n))/i)*(1+i)
print("The Present Value is :", round(PV,2))



