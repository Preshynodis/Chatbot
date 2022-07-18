
class User: 
    name = ""


def welcomeUser():
    name = input('What is your name?')
    print(f'Hello, welcome {name}')
    User.name = name


newUser = User.name
welcomeUser()