lst = []
sum = 0

for i in range(3) :
    lst.append(int(input()))
max = 0

for i in lst :
    sum += i
    if(max < lst.count(i)) :
        max = lst.count(i)
 
if(sum == 180) :
    if(max == 1) :
        print("Scalene")
    elif(max == 2) :
        print("Isosceles")
    else :
        print("Equilateral")
        
else :
    print("Error")