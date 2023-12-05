import os

day = 0
path = 0

for i in range(1, 26):
    day = str(i)
    path = str(os.getcwd()) + "/day" + day
    # Create folder from input
    try:
        os.mkdir(path)
        break
    except OSError:
        print("Creation of the directory %s failed" % path)

# Create and Write to part1.py
part1 = path + "/part1.py"
f = open(part1, "a")
f.write("from aocd import get_data\n")
f.write("dataRaw = get_data(year=2023, day=" + day + ")\n\n")
f.write('data = dataRaw.split("\\n")\n')
f.close()

# Create and Write to part1.py
part2 = path + "/part2.py"
f = open(part2, "a")
f.write("from aocd import get_data\n")
f.write("dataRaw = get_data(year=2023, day=" + day + ")\n\n")
f.write('data = dataRaw.split("\\n")\n')
f.close()

# Success?!
print(str(path) + " and adjacent files created!")
