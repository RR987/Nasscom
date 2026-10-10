a=True
while a:
    choice=input("1: +   2: -   3: *    4: /    5: %    6:exit\nEnter your choice: ")
    match choice:
        case '1': 
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print(f"Result is: {a+b}")
        case '2':
            a=int(input("Enter first number: "))            
            b=int(input("Enter second number: "))
            print(f"Result is: {a-b}")
        case '3':
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print(f"Result is: {a*b}")
        case '4':
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print(f"Result is: {a/b}")
        case '5':
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print(f"Result is: {a%b}")      
        case '6':
            a=False 
