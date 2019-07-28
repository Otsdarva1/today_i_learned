import fractions


def lcm(a, b):
    return a * b // fractions.gcd(a, b)


def f(x, a, b):
    return x - x // a - x // b + x // lcm(a, b)


def main():
    a, b, c, d = map(int, input().split())
    print(f(b, c, d) - f(a - 1, c, d))


if __name__ == '__main__':
    main()
