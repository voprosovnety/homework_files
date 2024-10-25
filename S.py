school_winners = {}
max_score = 0

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        _, _, school, score = line.split()
        school = int(school)
        score = int(score)
        if score > max_score:
            max_score = score
            school_winners = {school: 1}
        elif score == max_score:
            if school in school_winners:
                school_winners[school] += 1
            else:
                school_winners[school] = 1

max_winners_count = max(school_winners.values())
max_winner_schools = [school for school, count in school_winners.items() if count == max_winners_count]

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(' '.join(map(str, sorted(max_winner_schools))))
