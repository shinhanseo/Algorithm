num = int(input())
money = []
rest = {
    "Quarter" : 0,
    "Dime" : 0,
    "Nikel" : 0,
    "Penny" : 0
}

for i in range(num) :
    money.append(int(input()))

for i in range(num) :
    rest["Quarter"] = money[i] // 25
    rest["Dime"] = (money[i] % 25) // 10
    rest["Nikel"] = ((money[i] % 25) %10) // 5
    rest["Penny"] = ((money[i] % 25) % 10) % 5

    for key in rest.keys() :
        print(f"{rest[key]} ", end="")
    print("")


