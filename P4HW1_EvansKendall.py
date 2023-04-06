#CTI-110
#P4HW1 - Score List
#Kendall Evans
#April 6, 2023
#


score_list = []

#Ask for the desired number of scores

num_scores = int(input("How many scores would you like to enter? "))

#Loop until it reaches the desired number of scores

while len(score_list) < num_scores:
    score = int(input(f"Enter score #{len(score_list)+1}: "))

#Setup the range for valid scores

    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100.")
        score = int(input(f"Enter score #{len(score_list)+1}: "))
    score_list.append(score)

#Find the lowest score, remove lowest score from list, find average, find letter grade

lowest_score = min(score_list)
score_list.remove(lowest_score)

average_score = sum(score_list) / len(score_list)

if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

#display results

print('\n')
print('Results')

print(f"Lowest score entered: {lowest_score}")
print(f"Modified list: {score_list}")
print(f"Average score: {average_score:.2f}")
print(f"Letter grade: {letter_grade}")
