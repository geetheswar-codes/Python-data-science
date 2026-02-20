# mini project:student marks analysis
import numpy as np
# mark of 5 students in 3 subjects
marks = np.array([
    [85,90,78],
    [76,88,75],
    [90,65,70],
    [60,65,70],
    [88,76,95]
])
print("Marks of students:")
print(marks)

#Total marks of each student
total_marks = np.sum(marks,axis = 1)
print("\nTotal marks of each student:",total_marks)

#  Average marks in each subject
average_marks = np.mean(marks,axis = 0)
print("Average marks in each subject:",average_marks)

# highest marks in each subject
highest_marks = np.max(marks,axis = 0)
print("\nHighest marks in each subject:",highest_marks)

# overall class average
class_average = np.mean(total_marks)
print("\nOverall class average:",class_average)
