def main():
    for num in range(1500, 2001):
        if num % 100 == 0 and num % 400 == 0:
            print(num)
        elif num % 4 == 0 and num % 100 != 0:
            print(num)


if __name__ == "__main__":
    main()
