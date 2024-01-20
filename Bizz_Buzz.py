for num in range(1,21):
    if (num % 2 == 0 and num % 3 == 0):
        print("BizzBuzz")
    elif (num % 2 == 0):
        print("Bizz")
    elif (num % 3 == 0):
        print("Bizz")
    else:
        print(num)
