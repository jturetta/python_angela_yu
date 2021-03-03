student_heights = input('Input a list of student heights separated by space: ').split()
total_height = 0
total_students = 0

for height in student_heights:
    total_height += int(height)
    
for student in student_heights:
    total_students += 1

average_height = round(total_height / total_students)
print(f'The average height is {average_height} cm.')


'''

#now using len() and sum()

for i in range (0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
    
average_height = round(sum(student_heights) / len(student_heights))
print(f'The average_height is {average_height} cm.')

'''


