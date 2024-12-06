'''If the marks obtained by a student in five different subjects are input through the keyboard,
find out the aggregate marks and percentage marks obtained by the student. Assume that the
maximum marks that can be obtained by a student in each subject is 100.'''

Sub1=int(input("Enter the marks in subject 1:"))
Sub2=int(input("Enter the marks in subject 2:"))
Sub3=int(input("Enter the marks in subject 3:"))
Sub4=int(input("Enter the marks in subject 4:"))
Sub5=int(input("Enter the marks in subject 5:"))
sum=Sub1+Sub2+Sub3+Sub4+Sub5
avg=sum/5
print("Avg marks is:",avg,"%")
