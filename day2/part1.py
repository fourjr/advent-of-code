from collections import Counter


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    two = []
    three = []
    for i in data:
        top = Counter(i).most_common(None)
        c_two = False
        c_three = False
        for f, n in top:
            if n == 2 and not c_two:
                two.append(f)
                c_two = True
            if n == 3 and not c_three:
                three.append(f)
                c_three = True

    print(len(two) * len(three))


if __name__ == "__main__":
    main()
