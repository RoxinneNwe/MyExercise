def login(x):
    for i in range(3):
        username = input("Please enter your username: ")
        if username == "rox".lower: #or username == "jon".lower():
            password = input ("Please enter your password: "))
            if password == "macarena":
                print("Welcome back, ", username, "!")
                break
            else:
                print("Wrong password, please try again")
        else:
            print("The username does not exist")

