
#3.1
# failed to calculate overtime. is set as 65 so that 3.2 which is second program to run.

hours=float(input("Enter Hours: "))
rate=float(input("Enter Rate: "))
pay=float(hours*rate)
overtime= 65
# overtime=(40*10)+ x=hours over 40 * 1.5 *10

if hours <= 40:
    pay == float(hours*rate)
    print(pay)
elif hours > 40:
    overtime ==  65
    print(overtime)
else:
    print("Unk cmd")


#3.2 
#overtime = 65 just for the program to run when you insert string
try:
    hours=float(input("Enter Hours: "))
    rate=float(input("Enter Rate: "))
    pay=float(hours*rate)
    overtime= 65     #overtime=(40*10)+ #x=hours over 40 * 1.5 *10
    if hours <= 40:
        pay == float(hours*rate)
        print(pay)
    elif hours > 40:
        overtime == 65
        print(overtime)
    else:
        print("Unk cmd")
except:
    print("Error, please enter a numeric input")


#3.3

score = float(input("Enter score: "))

#for x in range(0.0,0.9):
if score <= 1.0 and score >= 0.9:
    print("A")
elif score <= 0.89 and score >= 0.8:
    print("B")
elif score <= 0.79 and score >= 0.7:
    print("C")
elif score <= 0.69 and score >= 0.6:
    print("D")
elif score <= 0.59 and score >=0.0:
    print("F")
else:
    print("unk cmm")