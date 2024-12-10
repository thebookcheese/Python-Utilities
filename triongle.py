import math
Want = input('Do you want to work out the area of a triangle or the angles in a triangle').lower()
if Want == "area":
  x= float(input("input the width of the triangle "))
  y= float(input("input the height of the triangle "))
  result= (x*y)/2
  print("the area of your triangle is", result, "units squared")
elif Want == "angles":
  HaveHypotenuse = input("Do you have the hypotenuse").lower()
  if HaveHypotenuse == "y":
    HypoLength = float(input('What is the length of the hypotenuse'))
    OtherSideLength  = float(input('What is the length of the other side'))
    print(f'The angle is {OtherSideLength/HypoLength}')

question=input("do you want to return to home? y/n: ")

if question == "y":
  import main
else:
  print("quitting...")