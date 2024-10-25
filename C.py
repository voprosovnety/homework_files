max_scores = {9: 0, 10: 0, 11: 0}

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        _, _, grade, score = line.split()
        grade = int(grade)
        score = int(score)
        if score > max_scores[grade]:
            max_scores[grade] = score

with open('output.txt', 'w') as outfile:
    outfile.write(f'{max_scores[9]} {max_scores[10]} {max_scores[11]}')
