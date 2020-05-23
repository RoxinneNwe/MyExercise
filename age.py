#age = 30;

#print(age, "This is the original integer")

#age = age *2;

#print(age, "double its year")

#age = 0;

#print(age, "age dead")

age = int(input("Type your age: "))

if int(age) == 18:
    print("Eligible to vote")
elif int(age) > 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

