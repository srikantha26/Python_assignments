# fruits = ["apple","peach","pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit+"pie")
#
# print(fruits)
student_scores = [150,148,142,125,120,90,87,100,111,199,123,125,87,86,85,94,83,82,81]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

score_sum = 0
for score in student_scores:
    score += score
print(score_sum)

total_exam_scores = sum(student_scores)

print(total_exam_scores)
