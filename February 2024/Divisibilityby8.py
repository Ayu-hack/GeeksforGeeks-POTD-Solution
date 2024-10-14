def DivisibleByEight(s: str) -> int:
    last_three_digits = s[-3:]
    num = int(last_three_digits)
    if num % 8 == 0:
        return 1
    else:
        return -1
