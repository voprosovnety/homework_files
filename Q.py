school_counts = {}

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        _, _, school, _ = line.split()
        school = int(school)
        if school not in school_counts:
            school_counts[school] = 0
        school_counts[school] += 1

sorted_schools = sorted(school_counts.items(), key=lambda x: (-x[1], x[0]))

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(' '.join(map(str, [school for school, _ in sorted_schools])))
