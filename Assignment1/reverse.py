'''If a five-digit number is input through the keyboard, write a program to reverse the number.'''
num=(int(input("Enter number to reverse: ")))
rev=0
while(num>0):
    a=num%10
    rev=rev*10+a
    num=num//10
print("Reverse number is: ",rev)