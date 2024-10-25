max_scores = {9: 0, 10: 0, 11: 0}
second_max_scores = {9: 0, 10: 0, 11: 0}

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        _, _, grade, score = line.split()
        grade = int(grade)
        score = int(score)

        if score > max_scores[grade]:
            second_max_scores[grade] = max_scores[grade]
            max_scores[grade] = score
        elif max_scores[grade] > score > second_max_scores[grade]:
            second_max_scores[grade] = score

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(f'{second_max_scores[9]} {second_max_scores[10]} {second_max_scores[11]}\n')
