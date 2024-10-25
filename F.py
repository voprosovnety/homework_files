max_score = 0
winners_count = 0

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        last_name, first_name, _, score = line.split()
        score = int(score)
        if score > max_score:
            max_score = score
            winners_count = 1
            winner_name = f'{last_name} {first_name}'
        elif score == max_score:
            winners_count += 1

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(winner_name if winners_count == 1 else str(winners_count))
