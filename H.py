max_score = 0
max_score_count = 0
second_max_score = 0
second_max_score_count = 0

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        _, _, _, score = line.split()
        score = int(score)
        if score > max_score:
            second_max_score = max_score
            second_max_score_count = max_score_count
            max_score = score
            max_score_count = 1
        elif score == max_score:
            max_score_count += 1
        elif score > second_max_score:
            second_max_score = score
            second_max_score_count = 1
        elif score == second_max_score:
            second_max_score_count += 1

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(f'{second_max_score} {second_max_score_count}')
