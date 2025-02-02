f = open("Perepis.txt","r")
a = list()
count = 0
for i in f:
    a.append(i[:-1])
for i in a:
    if int(i[-4:]) < 1978:
        count+=1
        print(i[:i.find(' ')])
b = int(input("Введите начало диапазона "))
c = int(input("Введите конец диапазона "))
for i in a:
    if int(i[-4:]) > b and int(i[-4:]) < c:
        print(i)
