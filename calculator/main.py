from calculator import arithmetic,scientific

def main():
    while True:
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Sine (Scientific)")
        print("6. Cosine (Scientific)")
        print("7. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7): ")
        
        if choice == '7':
            print("Exiting the calculator.")
            break
        
        if choice in ['1', '2', '3', '4']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if choice == '1':
                print("Result:", arithmetic.add(a, b))
            elif choice == '2':
                print("Result:", arithmetic.sub(a, b))
            elif choice == '3':
                print("Result:", arithmetic.mul(a, b))
            elif choice == '4':
                print("Result:", arithmetic.div(a, b))
        
        elif choice in ['5', '6']:
            c = float(input("Enter angle in degrees: "))
            
            if choice == '5':
                print("Sine of angle:", scientific.sine(c))
            elif choice == '6':
                print("Cosine of angle:", scientific.cosine(c))
        
        else:
            print("Invalid choice. Please try again.")

main()