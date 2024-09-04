weather = input("What's the weather like today? 1 - Sunny, 2 - Rainy, 3 - Windy, 4 - Snowing\n")
if weather == '1':
    print("It's awfully nice out today! You should go touch some grass!")
elif weather == '2':
    print("Welp! You should probably do something like read a book!")
elif weather == '3':
    print("Well that's not helpful at all!")
elif weather == '4':
    print("Nice!")
askfood = str(input("Are you eating something right now?\n"))
if askfood == 'Yes' or askfood == 'yes':
    food = input("Nice! What are you eating?\n")
    print('You are making me hungry! Now I want to eat ' + food)
elif askfood == 'No' or askfood == 'no':
    print('Oh, I thought you were eating something yummy')
else:
    print("I didn't quite catch that, can you repeat again?")