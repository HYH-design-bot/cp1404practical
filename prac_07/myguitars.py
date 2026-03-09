from guitar import Guitar

in_file = open('guitars.csv', 'r')
in_file.readline()
guitars = []
for line in in_file:
    parts = line.strip().split(',')
    guitar = Guitar(parts[0], parts[1], parts[2])
    guitars.append(guitar)
    # Add the language we've just constructed to the list
# Close the file as soon as we've finished reading it
in_file.close()

guitars.sort()

for guitar in guitars:
    print(guitar)