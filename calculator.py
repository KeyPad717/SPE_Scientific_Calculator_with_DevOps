import math

# factorial calculation
def factorial(n):
    fact = 1.0
    for i in range(1, n + 1):
        fact *= i
        if math.isinf(fact):
            print("Error! Factorial result too large.")
            return -1
    return fact

# numeric validation
def isNumber(x):
    if x.count('.') <= 1 and (x.replace('.', '', 1).isdigit() or (x.startswith('-') and x[1:].replace('.', '', 1).isdigit())):
        return True
    return False

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

            case "1":  # add
                x = input("Enter first number (-∞ to ∞): ")
                y = input("Enter second number (-∞ to ∞): ")

                if not isNumber(x) or not isNumber(y):
                    print("Error! Invalid input type.")
                    continue

                result = float(x) + float(y)

                if math.isinf(result):
                    print("Error! Result too large.")
                    continue

                print("Result:", result)

            case "2":  # subtract
                x = input("Enter first number (-∞ to ∞): ")
                y = input("Enter second number (-∞ to ∞): ")

                if not isNumber(x) or not isNumber(y):
                    print("Error! Invalid input type.")
                    continue

                result = float(x) - float(y)

                if math.isinf(result):
                    print("Error! Result too large.")
                    continue

                print("Result:", result)

            case "3":  # multiply
                x = input("Enter first number (-∞ to ∞): ")
                y = input("Enter second number (-∞ to ∞): ")

                if not isNumber(x) or not isNumber(y):
                    print("Error! Invalid input type.")
                    continue

                result = float(x) * float(y)

                if math.isinf(result):
                    print("Error! Result too large.")
                    continue

                print("Result:", result)

            case "4":  # divide
                x = input("Enter numerator (-∞ to ∞): ")
                y = input("Enter denominator (-∞ to ∞, but ≠ 0): ")

                if not isNumber(x) or not isNumber(y):
                    print("Error! Invalid input type.")
                    continue

                x = float(x)
                y = float(y)

                if y == 0:
                    print("Error! Division by zero.")
                    continue

                result = x / y

                if math.isinf(result):
                    print("Error! Result too large.")
                    continue

                print("Result:", result)

            case "5":  # factorial
                n = input("Enter integer (0 ≤ n ≤ 170): ")

                if not n.isdigit():
                    print("Error! Invalid input type.")
                    continue

                n = int(n)

                if n < 0 or n > 170:
                    print("Error! Factorial defined only for 0 ≤ n ≤ 170.")
                    continue

                result = factorial(n)

                if result == -1:
                    continue

                print("Result:", result)

            case "6":  # ln
                x = input("Enter number (0 < x < ∞): ")

                if not isNumber(x):
                    print("Error! Invalid input type.")
                    continue

                x = float(x)

                if x <= 0:
                    print("Error! ln(x) defined for x > 0.")
                    continue

                print("Result:", math.log(x))

            case "7":  # power
                x = input("Enter base (-∞ to ∞): ")
                y = input("Enter exponent (-∞ to ∞): ")

                if not isNumber(x) or not isNumber(y):
                    print("Error! Invalid input type.")
                    continue

                x = float(x)
                y = float(y)

                if x == 0 and y == 0:
                    print("Error! 0^0 is undefined.")
                    continue

                result = math.pow(x, y)

                if math.isinf(result):
                    print("Error! Result too large.")
                    continue

                print("Result:", result)

            case "8":  # sqrt
                x = input("Enter number (0 ≤ x < ∞): ")

                if not isNumber(x):
                    print("Error! Invalid input type.")
                    continue

                x = float(x)

                if x < 0:
                    print("Error! Square root undefined for negative numbers.")
                    continue

                print("Result:", math.sqrt(x))

            case "9":
                print("Exiting calculator.")
                break

            case _:
                print("Error! Invalid menu choice.")

if __name__ == "__main__":
    main()