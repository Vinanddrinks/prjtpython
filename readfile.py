#!/usr/bin/python
partitions = open("partitions.txt", "r")
dic = {

}

for line_number, lines in enumerate(partitions):
    if (line_number % 2) == 0:
        dic[lines] = 1
for key in dic:
    for line_number, lines in enumerate(partitions):
        if (line_number % 2) != 0:
            dic[key] = lines

print(dic)


