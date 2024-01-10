def repeater():
  a = eval(input("Enter the First Number : "))
  b = eval(input("Enter the Second Number : "))
  operator = int(
      input('''
  Enter the operator : 
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    Please entetr the Index Number.

  Operator : '''))

  print("")

  if operator == 1:
    print(f"Sum : {a+b}")
    repeater()

  elif operator == 2:
    print(f"Subtracted Values : {a-b} \n")
    repeater()

  elif operator == 3:
    print(f"Multiplied Values : {a*b} \n")
    repeater()

  elif operator == 4:
    if b==0:
        print("You can't divide by zero. \n")
        repeater()
    else:
      print(f"Divided Values : {a/b} \n")
      repeater()

  else:
    print("Invalid Operators choose between 1 to 4 \n")
    repeater()


repeater()
