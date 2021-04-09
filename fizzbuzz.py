
for number in range (1,101) :
    message = ""

    if (number%3)==0:
        message += "fizz"
    if (number%5)==0:
        message += "buzz"
    if (number%7)==0:
        message += "hazz"
    print(number, message)
