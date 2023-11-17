def classify_triangle(a, b, c):
    """
    This function will classify the type of triangle based on the lengths of its sides.
    
    Args:
    a, b, c (float): The lengths of the sides of the triangle.

    Returns:
    str: The type(s) of triangle.
    """

    if a + b <= c or a + c <= b or b + c <= a:
        return "Neveljaven trikotnik"

    types = []

    if a == b == c:
        types.append("Enakostranični")
    elif a == b or b == c or a == c:
        types.append("Enakokraki")

    sides = sorted([a, b, c])
    if sides[2]**2 == sides[0]**2 + sides[1]**2:
        types.append("Pravokotni")

    if a != b and b != c and a != c:
        types.append("Raznostranični")

    return ' in '.join(types)