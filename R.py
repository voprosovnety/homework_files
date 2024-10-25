school_scores = {}

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        _, _, school, score = line.split()
        school = int(school)
        score = int(score)
        if school not in school_scores:
            school_scores[school] = {'total': 0, 'count': 0}
        school_scores[school]['total'] += score
        school_scores[school]['count'] += 1

average_scores = [(school, data['total'] / data['count']) for school, data in school_scores.items()]
sorted_schools = sorted(average_scores, key=lambda x: (-x[1], x[0]))

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(' '.join(map(str, [school for school, _ in sorted_schools])))
