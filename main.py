from shape_module import *
def main():
    square = Square((2, 3), 4)
    rectangle = Rectangle((4, 5), 5, 10)
    circle = Circle((1, 6), 6)
    ellipse = Ellipse((6, 7), 4, 10)
    list_figure = [square, rectangle, circle, ellipse]

    def save_figure(shapes: Shape):
        shape.save()

    for shape in list_figure:
        save_figure(shape)


if __name__ == '__main__':
    main()