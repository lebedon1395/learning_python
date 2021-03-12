def fizz_buzz(number: int) -> str:
    """
    Play the Fizz Buzz game
    :param number: the number to check
    :return: `fizz ` if `number` is divisible by 3
    `buzz` if `number` is divisible by 5
    `fizz buzz` if `number` is divisible by both 3 and 5
    `number` otherwise
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


input("Welcome to fizz buzz.  Press Enter to begin.\n")

for i in range(1,101):
    if (i % 2) != 0:
        print(f": {fizz_buzz(i)}")
    else:
        if input(": ") != fizz_buzz(i):
            print(f"The correct answer was '{fizz_buzz(i)}'\nGame Over")
            break
else:
    print("Congratulations!")