school_counts = {}

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        _, _, school, _ = line.split()
        school = int(school)
        if school in school_counts:
            school_counts[school] += 1
        else:
            school_counts[school] = 1

max_count = max(school_counts.values())
max_schools = [school for school, count in school_counts.items() if count == max_count]

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(' '.join(map(str, sorted(max_schools))))
