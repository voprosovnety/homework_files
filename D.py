sum_score = {9: 0, 10: 0, 11: 0}
count_score = {9: 0, 10: 0, 11: 0}

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        _, _, grade, score = line.split()
        grade = int(grade)
        score = int(score)
        sum_score[grade] += score
        count_score[grade] += 1

with open('output.txt', 'w') as outfile:
    outfile.write(
        f'{sum_score[9] / count_score[9]} {sum_score[10] / count_score[10]} {sum_score[11] / count_score[11]}')
