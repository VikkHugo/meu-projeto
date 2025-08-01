def equilateral(sides):
    a, b, c = sorted(sides)
    return a == b == c and a > 0

def isosceles(sides):
    a, b, c = sorted(sides)
    return (a + b > c) and (a > 0) and ((a == b) or (b == c))

def scalene(sides):
    a, b, c = sorted(sides)
    return (a + b > c) and (a > 0) and (a != b and b != c and a != c)