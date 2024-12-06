'''The length & breadth of a rectangle and radius of a circle are input through the keyboard.
Write a program to calculate the area & perimeter of the rectangle, and the area &
circumference of the circle.'''
l=int(input("Enter length of Rectangle:"))
b=int(input("Enter breadth of Rectangle:"))
a=l*b
p=2*(l+b)
print("Area of rectangle:",a)
print("Perimeter of rectangle:",p)
r=int(input("Enter the radius of the circle:",))
c=2*3.14*r
cr=3.14*(r**2)
print("Area of circle:",cr)
print("Circumference of circle:",c)



