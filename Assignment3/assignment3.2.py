r=0.12
annual_earning=1000
cost=6000
salvage=2000
y=1
for t in range(1, y+1):
    while True:

        presentvalue_earnings = 0
        presentvalue_earnings += annual_earning/(1+r)**t
        presentvalue_salvage= salvage/ (1+r)**y
        total_presentvalue = presentvalue_earnings+ presentvalue_salvage
        if total_presentvalue >= cost:
            break
    y+=1
print(f"The minimum life of the machine to make it a more attractive invesment is:{y} years")