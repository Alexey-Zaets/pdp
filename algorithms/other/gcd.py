def gcd(x: int, y: int) -> int:
    larger, smaller = max(x, y), min(x, y)

    remainder = larger % smaller
    if remainder == 0:
        return smaller

    return gcd(smaller, remainder)
