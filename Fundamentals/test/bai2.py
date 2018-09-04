numb = input("Nhập vào 1 dãy số: ")
li = numb.split()

print("Trong dãy số: ")
print(*li, sep=", ")
print()
print("Có những cặp số sau có tích bằng 128 : ")

for i in range(len(li)):
    for j in range(i, len(li)):
        res = int(li[i]) * int(li[j])
        if res == 128:
            print("{0} và {1} tại vị trí số {2} và {3}".format(li[i], li[j], i+1, j+1))

