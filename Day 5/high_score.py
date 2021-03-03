student_scores = input('Please type the scores separated by space: ').split()
high_score = 0

for score in student_scores:
    if high_score < int(score):
        high_score = int(score)

print(f'The highest score is {high_score}.')
