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
        tmp_x, tmp_y, tmp_t = [], [], []

        try:

            xs = np.arange(0, line_count - 1, int((line_count - 1) / 35))
            t_full = np.arange(0, t[line_count-1], t[line_count-1]/300)

            for i in xs:
                tmp_x.append(x[i])
                tmp_y.append(y[i])
                tmp_t.append(t[i])

            x = np.array(tmp_x)
            y = np.array(tmp_y)
            t = np.array(tmp_t)

            spline_x = CubicSpline(t, x)
            spline_y = CubicSpline(t, y)

            fig, ax = plt.subplots(2)
            fig.suptitle("Cubic - Spline of " + csv_file_name)

            ax[0].plot(t, x, 'o', label='data')
            ax[0].plot(t_full, spline_x(t_full), label="s(t)")
            ax[0].plot(t_full, spline_x(t_full, 1), label="v(t)")
            #ax[0].plot(t_full, spline_x(t_full, 2), label="a(t)")
            ax[0].legend(loc='lower left', ncol=2)

            ax[1].plot(t, y, 'o',label='data')
            ax[1].plot(t_full, spline_y(t_full), label="s(t)")
            ax[1].plot(t_full, spline_y(t_full, 1), label="v(t)")
            #ax[1].plot(t_full, spline_y(t_full, 2), label="a(t)")
            ax[1].legend(loc='lower left', ncol=2)

            plt.show()
        except:
            traceback.print_exc()

    @staticmethod
    def get_cords(csv_file_name):

        with open(csv_file_name, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = -1
            x = []
            y = []
            t = []

            last_t = 0

            for row in csv_reader:
                if line_count == -1:
                    # print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    # print(row)
                    if float(row[2]) > last_t:
                        last_t = float(row[2])
                        x.append(round(float(row[0]), 3))
                        y.append(round(float(row[1]), 3))
                        t.append(round(float(row[2]), 3))
                        line_count += 1
            # print(f'Processed {line_count} lines.')

            return x, y, t, line_count
