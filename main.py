
from calculator import operations, factorial, table

def run_calculator():
    print("Welcome to Advanced Modular Calculator\n")

    while True:
        print("\nChoose an operation:")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exponent")
        print("6. Factorial\n7. Multiplication Table\n8. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                a, b = float(input("A: ")), float(input("B: "))
                print("Result:", operations.add(a, b))
            elif choice == 2:
                a, b = float(input("A: ")), float(input("B: "))
                print("Result:", operations.subtract(a, b))
            elif choice == 3:
                a, b = float(input("A: ")), float(input("B: "))
                print("Result:", operations.multiply(a, b))
            elif choice == 4:
                a, b = float(input("Numerator: ")), float(input("Denominator: "))
                print("Result:", operations.divide(a, b))
            elif choice == 5:
                base, power = float(input("Base: ")), float(input("Power: "))
                print("Result:", operations.exponent(base, power))
            elif choice == 6:
                n = int(input("Number: "))
                print("Factorial:", factorial.factorial(n))
            elif choice == 7:
                n = int(input("Table of: "))
                print("\n".join(table.multiplication_table(n)))
            elif choice == 8:
                print("Thanks for using the calculator!")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    run_calculator()
