school_scores = {}
total_score = 0
total_count = 0

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        _, _, school, score = line.split()
        school = int(school)
        score = int(score)
        total_score += score
        total_count += 1
        if school not in school_scores:
            school_scores[school] = {'total': 0, 'count': 0}
        school_scores[school]['total'] += score
        school_scores[school]['count'] += 1

average_score = total_score / total_count
high_average_schools = [
    school for school, data in school_scores.items()
    if (data['total'] / data['count']) > average_score
]

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(' '.join(map(str, sorted(high_average_schools))))
