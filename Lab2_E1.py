line_1= "Python was created by Guiodo van Rossum a Dutch programmer."
line_2="First version of Python 0.9.0 was developed in Centrum, Wiskunde & Informatica(CWI) in the Netherlands in 1991."
line_3 = "Python 3.0, was released on 3 December 2008."

print(type(line_1))
print(type(line_2))
print(type(line_3))

a,b,c = True, True, True

#method1
print(type(line_1) == type(line_2) == type(line_3))

#method2
print(type(line_1)==str)
print(type(line_1)==str)
print(type(line_1)==str)

print(line_1,line_2,line_3)