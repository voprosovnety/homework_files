participants = []

with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        last_name, first_name, _, score = line.split()
        score = int(score)
        participants.append((last_name, first_name, score))


with open('output.txt', 'w', encoding='utf-8') as outfile:
    for last_name, first_name, score in sorted(participants):
        outfile.write(f'{last_name} {first_name} {score}\n')
