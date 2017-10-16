import csv

with open('logs2.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(": ") for line in stripped if line)
    with open('logs2.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)
