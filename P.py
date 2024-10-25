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

max_average_score = max(data['total'] / data['count'] for data in school_scores.values())
max_average_schools = [
    school for school, data in school_scores.items()
    if (data['total'] / data['count']) == max_average_score
]

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(' '.join(map(str, sorted(max_average_schools))))
