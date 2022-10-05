#number of stocks available
import math
energy = 24
metals = 12
telecom = 11

total_stock = energy + metals + telecom
print("Percentage of energy stock is : ",round((energy/total_stock)*100), "%")
print("Percentage of metals stock is : ",round((metals/total_stock)*100), "%")
print("Percentage of telecom stock is : ",round((telecom/total_stock)*100), "%")