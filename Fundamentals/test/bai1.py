print("***************Bài tập 1*****************")
numb = input("Nhập vào 1 dãy số: ")
list_numb = numb.split()
print("Dãy số vừa nhập: ")
print(*list_numb, sep="\n")