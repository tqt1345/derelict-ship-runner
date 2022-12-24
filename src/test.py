

def mainMenu():
    prompt = ("Enter a number:\n"
              "    -1. Option one\n"
              "    -2. Option two\n"
              "=>:")
    while True:
        try:
            selection = int(input(prompt))
            if selection == 1:
                subMenu()
            elif selection == 2:
                subMenu2()
        except ValueError:
            print("Enter 1-2")
    exit()

def subMenu():
    pass

def subSubMenu():
    pass


def subMenu2():
    pass

def subSubMenu2():
    pass


mainMenu()