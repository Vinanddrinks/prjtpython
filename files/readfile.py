#lis le fichier partition.txt et le return en dictionaire 
import io
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
#retourne le dictionaire stocké dans pdata.json
def readfilejson():
    import json
    with open ('pdata.json') as json_file:
        data = json.load(json_file)
        return data

#écris un dictionnaire dans pdata.json
def writejson(partitions):
    import json
    with open("pdata.json", "w") as write_file:
        json.dump(partitions, write_file)