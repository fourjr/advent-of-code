def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    for i in data:
        for j in data:
            diff = 0
            for a, b in zip(enumerate(i), j):
                if a[1] != b:
                    diff += 1
                    diff_char = a[0]
            if diff == 1:
                print(i[:diff_char] + i[diff_char + 1:])
                return


if __name__ == "__main__":
    main()
