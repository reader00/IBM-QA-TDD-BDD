def area_of_a_triangle(base: float, height: float):
    """Calculates area of a triangle given non-negative numbers"""

    # Check type
    if type(base) not in [int, float]:
        raise TypeError('Base must be a number')
    if type(height) not in [int, float]:
        raise TypeError('Height must be a number')

    if base < 0:
        raise ValueError('Base must be a positive number')
    if height < 0:
        raise ValueError('Height must be a positive number')

    return (base/2)*height
