# a = int(input("Enter any value between 5 and 9"))

# if(a<5  or a>9):
#   raise  ValueError("Value should be between 5 and 9")

while True:
  a = input("Enter the value butween 5 and 9: ")
  if (a == "quit"):
    print("ohk")
    break
  elif (int(a)>=5 and int(a)<=9):
    print("you entered a valid number",a)
    break
  try:
    num = int(a)
    if num < 5 or num > 9:
      raise ValueError("The value should be between 5 and 9")

    print(f"The number {num} is within the range.")
  except ValueError as e:
    print(e)