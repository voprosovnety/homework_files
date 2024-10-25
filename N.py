max_score = 0
schools_with_winners = set()

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        _, _, school, score = line.split()
        school = int(school)
        score = int(score)
        if score > max_score:
            max_score = score
            schools_with_winners = {school}
        elif score == max_score:
            schools_with_winners.add(school)

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(' '.join(map(str, sorted(schools_with_winners))))
