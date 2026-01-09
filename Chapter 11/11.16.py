def main():
    # 11.16.
    # а) 10 первых членов арифметической прогрессии с первым членом a и разностью p;
    # б) 20 первых членов геометрической прогрессии с первым членом a и знаменателем z.
    a, p = map(float, input().split())
    a2, z = map(float, input().split())

    arith = [a + i * p for i in range(10)]
    geom = [a2 * (z ** i) for i in range(20)]

    print("arith:", *arith)
    print("geom:", *geom)


if __name__ == "__main__":
    main()
