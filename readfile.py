#lis le fichier partition.txt et le return en dictionaire 
def readfiletxt():
    partitions = open("partitions.txt")
    partidic = {}
    ln = 0
    for line in enumerate(partitions):
        if ln % 2 == 0:
            temp = line[1]
            partidic[temp] = 0
        else:
            partidic[temp] = line[1]
        ln += 1
    partitions.close()
    return partidic
#retourne le dictionaire stocké dans p data.json
def readfilejson():
    import json
    with open ('pdata.json') as json_file:
        data = json.load(json_file)
        return data

