def square_root(x: int, y: int, tolerance: float) -> int:
    error = tolerance * 2
    while error > tolerance:
        z = x/y
        y = (y + z) / 2
        error = y**2 - x
    return y

# square_root(5, 1, .000000000000001) = 2.23606797749979 = math.sqrt(5) = 5 ** 0.5