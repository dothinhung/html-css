n = 10

li = []

for i in range(n):
    num = int(input("Nhập vào số ở vị trí thứ {} : ".format(i+1)))
    li.append(num)

print("Trong dãy số : ",*li)


for index1, item1 in enumerate(li):
    for index2, item2 in enumerate(li):
        res = int(item1) * int(item2)
        if res == 128:
            print("Vị trí thứ : {0} và {1}".format(index1+1, index2+1))
