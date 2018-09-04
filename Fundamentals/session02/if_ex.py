yob = int(input("Year of birth : "))

age = 2018 -  yob

print(age)

if age < 15 :
    print ("Baby")
elif 15 < age < 19:
    print("Teenage")
elif 20 < age < 50:
    print("Adult")
elif age > 50:
    print("older")