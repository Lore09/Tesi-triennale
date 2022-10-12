from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np
import csv
import traceback


class DrawSpline:

    def __init__(self):

        self.x, self.y = None, None

    @staticmethod
    def plot_cubic_spline(csv_file_name):

        x, y, t, line_count = DrawSpline.get_cords(csv_file_name)

        x = np.array(x)
        y = np.array(y)
        t = np.array(t)

        try:
            spline_x = CubicSpline(t, y)
            xs = np.arange(t[0], t[line_count - 2], float(t[line_count - 2]/5))
            fig, ax = plt.subplots(figsize=(6.5, 4))
            fig.canvas.manager.set_window_title("Cubic - Spline of " + csv_file_name)
            ax.plot(t, y, label='data')
            ax.plot(xs, spline_x(xs), label="s(t)")
            ax.plot(xs, spline_x(xs, 1), label="v(t)")
            #ax.plot(xs, spline_x(xs, 2), label="a(t)")
            ax.legend(loc='lower left', ncol=2)
            plt.show()
        except:
            traceback.print_exc()

    @staticmethod
    def get_cords(csv_file_name):

        with open(csv_file_name, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            x = []
            y = []
            t = []

            last_t = 0

            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(row)
                    if float(row[2]) > last_t:
                        last_t = float(row[2])
                        x.append(round(float(row[0]), 3))
                        y.append(round(float(row[1]), 3))
                        t.append(round(float(row[2]), 3))
                        line_count += 1
            # print(f'Processed {line_count} lines.')

            return x, y, t, line_count
