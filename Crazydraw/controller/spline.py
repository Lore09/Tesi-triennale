from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np
import csv


class DrawSpline:

    def __init__(self):

        self.x, self.y = None, None

    @staticmethod
    def plot_cubic_spline(csv_file_name):

        x, y, line_count = DrawSpline.get_cords(csv_file_name)

        x = np.array(x)
        y = np.array(y)
        cs = CubicSpline(x, y)
        xs = np.arange(x[0], x[line_count - 2], 50)
        fig, ax = plt.subplots(figsize=(6.5, 4))
        fig.canvas.manager.set_window_title("Cubic - Spline of " + csv_file_name)
        ax.plot(x, y, label='data')
        ax.plot(xs, cs(xs), label="s(t)")
        ax.plot(xs, cs(xs, 1), label="v(t)")
        ax.plot(xs, cs(xs, 2), label="a(t)")
        ax.set_xlim(x[0]-50, x[line_count - 2]+50)
        ax.legend(loc='lower left', ncol=2)
        plt.show()


    @staticmethod
    def get_cords(csv_file_name):

        with open(csv_file_name, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            x = []
            y = []

            last_x = 0

            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    if len(row) != 0:
                        #print(row)
                        if last_x < float(row[0]):
                            last_x = float(row[0])
                            x.append(round(float(row[0]), 2))
                            y.append(round(float(row[1]), 2))
                            line_count += 1
            #print(f'Processed {line_count} lines.')

            return x, y, line_count
