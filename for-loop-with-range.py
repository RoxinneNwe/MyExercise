n = int(input("Enter number of values: "))

for i in range(n):
    a = input("Enter value {} ".format(i+1))
    print("value {0} was {1}".format(i+1, a))