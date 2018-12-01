# from time import sleep
def main():
    frequency = 0
    with open('input.txt') as f:
        data = f.read().splitlines()

    frequencies = {0}
    while True:
        for i in data:
            frequency += int(i)
            if frequency in frequencies:
                print(frequency)
                return
            frequencies.add(frequency)


if __name__ == "__main__":
    main()
