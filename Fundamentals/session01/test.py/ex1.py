# bài test đầu vào khóa CI (Code intensive by OOP)
# Bài 1: Nhập vào 1 dãy số và in dãy số vừa nhập mỗi số 1 hàng
# Bài 2: cho 1 dãy số, tính xem tích của cặp số nào bằng 128, nếu bằng 128 in ra số thứ tự của số dó


# Ex2:
print("*****************Bài tập 2***************")
list = ["1", "2", "24", "34", "5", "64", "128"]

print("Day so cho san:", end=" ")
print(*list, sep=", ")

for index1, item1 in enumerate(list):
    for index2, item2 in enumerate(list):
        item = int(item1) * int(item2)
        if item == 128:
            print("""tích cặp số bằng 128 ở vị trí thứ {0} và {1}"""
            .format(index1 +1 , index2 + 1))

print("*****************************************")

# bài 1 :
print()
print("***************Bài tập 1*****************")
numb = input("Enter a list of number: ")
list_numb = numb.split()
print("Update list of number: ")
print(*list_numb, sep="\n")

# bài 3 : nhập vào 1 dãy số, tính xem có cặp số nào có tích bằng 128
# nếu có in ra giống như bài 2, nếu k thì in ra "You can try again"
print()
print("****************Bài tập 3*****************")
number = input("Enter a list of number : ")
list_number = number.split()
# print( *list_number, sep=", ")

for index1, item1 in enumerate(list_number):
    for index2, item2 in enumerate(list_number):
        item = int(item1) * int(item2)
        # print(item)
        if item == 128:
            print("""vị trí số {0} và số {1} """
            .format(index1 + 1, index2 + 1)) 


