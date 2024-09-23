# write a program for the basketball selection,
# 	take height (float) as the input from the user and verify whethetr his height is 6.0 and above if yes
# 	he is selected , if height is less that 6.0 please print not selected


a=float(input("Please enter your height"))
if (a>6.0):
    print("he is selected")
else:
    print("not selected")




# Write a program for the school registry exmple
# please take total marks as input from user for max 600
# calculate the percentage of the total marks and verify if sthe student has passed in which grade
#
# >=0 and  <35    ----> FAIL
# >=35 and < 50   ====> passed in third class
# >=50 and < 60  ====> passed in second class
# >=60 and <85 ====> passed in first class
# >=85 and <= 100  ==> distinction
# apart above any other percentage comes its invalid entry


marks=int(input(" ENTER YOUR MARKS = "))
if(marks >=0 and  marks <35):
    print("FAIL")
elif(marks >=35 and marks< 50):
    print("passed in 3rd class")
elif(marks>=50 and marks< 60):
    print("Passed in 2nd class")
elif(marks>=60 and marks<85):
    print("passed in 1st class")
elif(marks>=85 and marks<= 100):
    print("Passed with distinction")
