# Simple calculator
a = float(input("Enter First number:"))
b = float(input("Enter second number:"))

print("choose operation:")

print(" 1. Addition")
print(" 2. Subtracion")
print(" 3. Multiplication")
print(" 4. Division")

choice = int(input("Enetr choice (1-4):"))

if choice == 1:
  result = a + b
elif choice == 2:
  result = a - b
elif choice == 3:
  result = a * b
elif choice == 4:
  if b != 0:
    result = a / b
  else:
    result ="cannot divide by zero"
else:
  result = "invalid choice"
print("Result:",result)
