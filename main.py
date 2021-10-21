def conj(x):
    while x != 1:
        if (x % 2 == 0):
            x = x/2
            print(x)
        elif (x % 2 != 0):
            x = (3 * x) + 1
            print(x)

definite = input("Do you want to run the program for a specific x? \n (enter the number or just press enter for no): ")
print(definite)
if definite.isdigit():
    definite = int(definite)
    conj(definite)


endless = input("Do you want to keep increasing x? [press ctrl+c to end] (y/n): ")
if endless == 'y':
    y = 1
    while True:
        print("Running the program for " + str(y))
        conj(y)
        y = y + 1