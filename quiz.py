while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oopls! That was n valid number. Try again...")