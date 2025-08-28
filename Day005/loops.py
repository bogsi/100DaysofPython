student_scores = [
    150,
    142,
    185,
    120,
    171,
    160,
    130,
    145,
    155,
    165,
    180]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)
