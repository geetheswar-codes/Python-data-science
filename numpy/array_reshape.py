# Reshaping arrays
import numpy as np
arr = np. array([10,20,30,40,50,60])

print("Original array:",arr)
# reshaping into 2 rows and 3 columns
reshaped = arr.reshape(2,3)
print("Reshaped array:",reshaped)

print("New shape:",reshaped.shape) 
