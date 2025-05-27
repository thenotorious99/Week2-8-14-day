name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")


def mini_pro():
    my_dict = {"name": name, "email": email, "password": password}
    with open("file.txt", "a") as file:
        file.write(str(my_dict) + "\n")

    with open("file.txt", "r") as file:
        my_file = file.read()

    print(my_file)

mini_pro()