#!/usr/bin/python3
"""Square class"""


class square():
    """Representation of square class"""
    width = 0
    height = 0

    def __init__(self, width, height):
        """initiazation of class"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """str representation of square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """program check"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
