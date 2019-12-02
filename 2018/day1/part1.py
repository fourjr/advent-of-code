def main():
    frequency = 0
    with open('input.txt') as f:
        data = f.read().splitlines()

    for i in data:
        frequency += int(i)

    print(frequency)


if __name__ == "__main__":
    main()
