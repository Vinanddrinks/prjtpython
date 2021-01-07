# authors : Vincent Labouret
#open partitions.txt and return it's content as a dictionary (key = music title value = sheet)
def readfiletxt():
    partitions = open("partitions.txt",encoding="utf-8")
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
#open pdata.json and return the loaded dictionary
def readfilejson():
    import json
    with open ('pdata.json') as json_file:
        data = json.load(json_file)
        return data

#accept partition as a dictionary and create or overwrite pdata.json with this dictionary as content 
def writejson(partitions):
    import json
    with open("pdata.json", "w") as write_file:
        json.dump(partitions, write_file)