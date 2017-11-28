# CHNU_PythonLabs
# by Zhufyak V.V.
# zhufyakvv@gmail.com
# t.me/zhufyakvv
# 22/11/17 7:56 AM
import tkinter

from math import sqrt


def is_triangle(a, b, c):
    """
    Checks if three lines can create triangle
    :param a:
    :param b:
    :param c:
    :return: bool
    """
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def get_p_of_triangle(a, b, c):
    """
    Gets P of triangle
    :param a:
    :param b:
    :param c:
    :return:
    """
    return a + b + c


def get_s_of_triangle(a, b, c):
    """
    Gets S of triangle
    :param a:
    :param b:
    :param c:
    :return:
    """
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


class MyUglyForm:
    def __init__(self):
        self.root = tkinter.Tk()
        self.a_label = tkinter.Label(self.root, text="a:")
        self.b_label = tkinter.Label(self.root, text="b:")
        self.c_label = tkinter.Label(self.root, text="c:")

        self.var = tkinter.IntVar()

        self.p_label = tkinter.Label(self.root, text="Perimeter")
        self.s_label = tkinter.Label(self.root, text="Area")

        self.result = tkinter.StringVar()
        self.result_label = tkinter.Label(self.root, textvariable=self.result)

        self.a = tkinter.Entry(self.root)
        self.b = tkinter.Entry(self.root)
        self.c = tkinter.Entry(self.root)

        self.p = tkinter.Radiobutton(self.root, variable=self.var, value=1)
        self.s = tkinter.Radiobutton(self.root, variable=self.var, value=2)

        self.run = tkinter.Button(self.root, text='Calculate', command=self.command)

        self.grid()

    def grid(self):
        self.a_label.grid(row=0, column=1)
        self.a.grid(row=0, column=2)

        self.b_label.grid(row=1, column=1)
        self.b.grid(row=1, column=2)

        self.c_label.grid(row=2, column=1)
        self.c.grid(row=2, column=2)

        self.p_label.grid(row=3, column=1)
        self.p.grid(row=3, column=2)

        self.s_label.grid(row=4, column=1)
        self.s.grid(row=4, column=2)

        self.run.grid(row=5, column=2)

        self.result_label.grid(row=6, column=2)

    def command(self):
        try:
            a = float(self.a.get())
            b = float(self.b.get())
            c = float(self.c.get())

            result = []
            if is_triangle(a, b, c):
                result.append("Is Triangle.")
                if self.var.get() == 1:
                    result.append("P:" + "{:.2f}".format(get_p_of_triangle(a, b, c)))
                if self.var.get() == 2:
                    result.append("S:" + "{:.2f}".format(get_s_of_triangle(a, b, c)))
            else:
                result.append("Try another numbers.")
        except Exception:
            result = ['Error.']
        print(result)
        self.result.set('\n'.join(result))

if __name__ == '__main__':
    form = MyUglyForm()
    form.root.mainloop()
