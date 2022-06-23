import json

clacit = []
with open("text.txt", "r", encoding="UTF-8") as string:
    for _ in string.readlines():
        clacit.append(json.loads(_))

print(len(clacit))
with open("dima_pars.txt","w",encoding="UTF-8") as string:
    for _ in clacit:
        string.writelines(f"{_['url']}\n")
