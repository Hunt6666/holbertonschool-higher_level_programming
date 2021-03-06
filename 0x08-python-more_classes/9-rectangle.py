#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = '#'

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        perimeter = (self.__width * 2) + (self.__height * 2)
        return perimeter

    def __str__(self):
        strr = ''
        if self.__height == 0 or self.__width == 0:
            return strr
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                strr = strr + str(self.print_symbol)
            if i != self.__height - 1:
                strr = strr + '\n'
        return strr

    def __repr__(self):
        strr = "Rectangle(" + str(self.__width) + ', '
        strr += str(self.__height) + ')'
        return strr

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        ar1 = rect_1.area()
        ar2 = rect_2.area()
        if ar1 >= ar2:
            return rect_1
        else:
            return rect_2

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
