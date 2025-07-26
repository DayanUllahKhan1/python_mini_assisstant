# Greet user by name (user input + string methods)
# Ask them what they want to do:
#   Do a calculation
#   Convert weight or temperature
#   Tell them a joke (madlibs-style)

name = input("Hello There! Please Enter your name: ")
print(f"Good to see you {name}!")
print(f"So, {name} What would you want me to do for you today?")
print("Would you want me to:")
print("A. Do a calculation for you?")
print("B. Do you want to convert 1.Weight 2.Temperature?")
print("C. Do you me to play a fun game with you?")
choice = input("Please enter an option (A/B/C): ").upper()

if choice == "A":
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    op = input("Enter an operator (+, -, *, /): ")
    if op == "+":
        result = num1 + num2
        print(f"The sum of both numbers is {result}")
    elif op == "-":
        result = num1 - num2
        print(f"The difference of both numbers is {result}")
    elif op == "*":
        result = num1 * num2
        print(f"The product of both numbers is {result}")
    elif op == "/":
        result = num1 / num2
        print(f"The quotient of both numbers is {result}")
    else:
        print("{op} is not a valid operator.")
elif choice == "B":
    choice2 = input("Do you want you convert 1.Weight or 2.Temperature (1/2): ")
    if choice2 == "1":
        weight = float(input("What is your weight (integers only): "))
        unit = input("Is your weight in Kilograms or Pounds (K/L): ").upper()
        if unit == "K":
            weight = weight * 2.205
            print(f"Your weight is {weight} Lbs.")
        elif unit == "L":
            weight = weight / 2,205
            print(f"Your weight is {weight} Kgs.")
        else:
            print("Error invalid inputs")
    elif choice2 == "2":
        temp = float(input("Enter the temperature that your you want to convert: "))
        unit = input("Is this temperature in Celcius, Fahrenheit or Kelvin (C/F/K): ").upper()
        unit2 = input("Do you want to convert this temperature into Celcius, Fahrenheit or Kelvin (C/F/K): ").upper()
        if unit == "C" and  unit2 == "F":
            temp = (temp * 9/5) + 32
            print(f"The temperature is {temp}°F.")
        if unit == "C" and  unit2 == "K":
            temp = temp + 273.15
            print(f"The temperature is {temp}K.")
        if unit == "F" and  unit2 == "C":
            temp = (temp - 32) * 5/9
            print(f"The temperature is {temp}°C.")
        if unit == "F" and  unit2 == "K":
            temp = (temp - 32) * 5/9 + 273.15
            print(f"The temperature is {temp}K.")
        if unit == "K" and  unit2 == "C":
            temp = temp - 273.15
            print(f"The temperature is {temp}°C.")
        if unit == "K" and  unit2 == "F":
            temp = (temp - 273.17) * 9/5 + 32
            print(f"The temperature is {temp}°F.")
        else:
            print("Error Invalid inputs")
elif choice == "C":
    adjective1 = input("Enter an adjective: ")
    animal = input("Enter the name of an animal: ")
    place = input("Enter the name of a place: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adjective2 = input("Enter an adjective: ")
    noun2 = input("Enter a noun: ")
    adjective3 = input("Enter an adjective: ")
    noun3 = input("Enter a noun: ")
    adverb = input("Enter an adverb: ")
    verb2 = input("Enter a verb: ")

    print(f"The {adjective1} {animal} went to the {place} to find some {noun1}. It {verb1} all the way there, hoping to find a {adjective2} {noun2}. When it arrived, it saw a {adjective3} {noun3} and {adverb} {verb2} away")
else:
    print(f"{choice} is invalid choice.")