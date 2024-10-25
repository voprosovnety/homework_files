max_scores = {9: 0, 10: 0, 11: 0}
winner_counts = {9: 0, 10: 0, 11: 0}

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        _, _, grade, score = line.split()
        grade = int(grade)
        score = int(score)
        if score > max_scores[grade]:
            max_scores[grade] = score
            winner_counts[grade] = 1
        elif score == max_scores[grade]:
            winner_counts[grade] += 1

with open('output.txt', 'w') as outfile:
    outfile.write(f'{winner_counts[9]} {winner_counts[10]} {winner_counts[11]}')
