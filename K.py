school_counts = {}

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        _, _, school, _ = line.split()
        school = int(school)
        if school in school_counts:
            school_counts[school] += 1
        else:
            school_counts[school] = 1

min_count = min(school_counts.values())
min_schools = [school for school, count in school_counts.items() if count == min_count]

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(' '.join(map(str, sorted(min_schools))))
