'''The distance between two cities (in km.) is input through the keyboard. Write a program to
convert and print this distance in meters, feet, inches and centimeters.'''

d=int(input("Enter distance in km:"))
m=d*1000
ft=m*3.28
inches=ft*12
cm=inches*2.54
print("Distance in meters:",m,"mtr")
print("Distance in feet:",ft,"feet")
print("Distance in inches:",inches,"inches")
print("Distance in centimeters:",cm,"centimeters")
