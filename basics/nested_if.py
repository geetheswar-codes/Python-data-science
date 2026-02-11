# Nested if  example
marks = int(input("Enter your markes: "))

if marks > 50:
  print(" You passed")
  if marks >= 90:
    print("Grade 'A'")
  elif marks >= 75:
    print("Grade 'B'")
  elif marks >= 60:
    print("Grade 'c'")
  else:
    print("Grade 'D'")
else:
  print("Failed")
