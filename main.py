from shape_module import *


def main():
    square = Square((2, 3), 4)
    rectangle = Rectangle((4, 5), 5, 10)
    circle = Circle((1, 6), 6)
    ellipse = Ellipse((6, 7), 4, 10)
    list_figure = [square, rectangle, circle, ellipse]

    def save_figure(shapes: Shape):
        shapes.save()

    # for shape in list_figure:
    #     save_figure(shape)

    def output_figures(figure: Shape):
        figure.output(figure.load())

    for figure in list_figure:
        output_figures(figure)


if __name__ == '__main__':
    main()
