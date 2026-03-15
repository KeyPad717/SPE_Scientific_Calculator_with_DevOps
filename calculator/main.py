from calculator.operations import *
import math
#comment
def isNumber(x):

    if x.count('.') <= 1:

        if x.replace('.', '', 1).isdigit():
            return True

        if x.startswith('-') and x[1:].replace('.', '', 1).isdigit():
            return True

    return False
#test1

def main():

    while True:

        print("\nScientific Calculator")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("5. factorial")
        print("6. ln")
        print("7. power")
        print("8. sqrt")
        print("9. exit")

        choice = input("Enter choice (1-9): ")

        match choice:

            case "1":

                x = input("Enter first number: ")
                y = input("Enter second number: ")

                if not isNumber(x) or not isNumber(y):
                    print("Invalid input")
                    continue

                result = add(float(x), float(y))

                if result == None:
                    print("Error")
                else:
                    print("Result:", result)

            case "2":

                x = input("Enter first number: ")
                y = input("Enter second number: ")

                if not isNumber(x) or not isNumber(y):
                    print("Invalid input")
                    continue

                result = subtract(float(x), float(y))

                if result == None:
                    print("Error")
                else:
                    print("Result:", result)

            case "3":

                x = input("Enter first number: ")
                y = input("Enter second number: ")

                if not isNumber(x) or not isNumber(y):
                    print("Invalid input")
                    continue

                result = multiply(float(x), float(y))

                if result == None:
                    print("Error")
                else:
                    print("Result:", result)

            case "4":

                x = input("Enter numerator: ")
                y = input("Enter denominator: ")

                if not isNumber(x) or not isNumber(y):
                    print("Invalid input")
                    continue

                result = divide(float(x), float(y))

                if result == None:
                    print("Error")
                else:
                    print("Result:", result)

            case "5":

                n = input("Enter integer (0-170): ")

                if not n.isdigit():
                    print("Invalid input")
                    continue

                result = factorial(int(n))

                if result == None:
                    print("Error")
                else:
                    print("Result:", result)

            case "6":

                x = input("Enter number: ")

                if not isNumber(x):
                    print("Invalid input")
                    continue

                result = ln(float(x))

                if result == None:
                    print("Error")
                else:
                    print("Result:", result)

            case "7":

                x = input("Enter base: ")
                y = input("Enter exponent: ")

                if not isNumber(x) or not isNumber(y):
                    print("Invalid input")
                    continue

                result = power(float(x), float(y))

                if result == None:
                    print("Error")
                else:
                    print("Result:", result)

            case "8":

                x = input("Enter number: ")

                if not isNumber(x):
                    print("Invalid input")
                    continue

                result = sqrt(float(x))

                if result == None:
                    print("Error")
                else:
                    print("Result:", result)

            case "9":
                print("Exiting calculator")
                break

            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()