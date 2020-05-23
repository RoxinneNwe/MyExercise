
cars = ["BMW", "Ford", "Alfa Romeo"]
for x in cars:
    print(x)

model = input("Choose a model from the above list: ")


if model == "BMW":
    bmw = (80000 * 0.05) + 80000
    print("BMW costs", bmw )
elif model == "Ford":
    ford = (75000 * 0.05) + 75000
    print("Ford costs", ford)
elif model == "Alfa Romeo":
    alfar = (125000 * 0.05) + 125000
    print("Alfa Romeo costs", alfar)
else:
    print("Your choice is not on the list")