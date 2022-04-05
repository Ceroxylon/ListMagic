import csv

# Initialize lists
bigList = []
compare = []
finish = []

# Open files for comparison, change the pathway to your files.
# Files must be a single column! The next update will have multi column utility
with open('/Path/To/First/File.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        bigList.append(row[0])
with open('/Path/To/Second/File.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        compare.append(row[0])

# Compare the two lists and write the difference in the new file.
finish = [x for x in bigList if x not in compare]

finish = list(dict.fromkeys(finish))

# Prints list in Terminal and saves to local drive
# Comment out the print if you do not need it in the Terminal
print(finish)

with open('/Path/To/Export/Destination', 'w') as out:
    write = csv.writer(out)
    write.writerow(finish)

# Close files that you open for reading in the CSV module or bad things will happen!
inputfile.close()
