list_hello = []

with open("VK_100M.txt", "r") as f:
    for line in f:
        print(line)
        if "Мятлюк" in line:
            list_hello.append(line)

print(list_hello)
