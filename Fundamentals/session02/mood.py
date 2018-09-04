from random import randint

mood = randint(0, 100)
print(mood)

if mood < 30:
    print("I feel Sad")
elif 30 < mood < 60:
    print("I feel Ok")
elif mood > 60:
    print("I feel Good")