import math

from scipy.interpolate import CubicSpline, PPoly
import matplotlib.pyplot as plt
import numpy as np
import csv
import traceback


class DrawSpline:

    def __init__(self):

        self.x, self.y = None, None

    @staticmethod
    def plot_cubic_spline(csv_file_name, figure, ax, num_interpolation):

        x, y, t, line_count = DrawSpline.get_cords(csv_file_name)

        try:
            t_full = np.linspace(0, t[line_count - 1], 500)
            x, y, t = DrawSpline.__distance_interpolation__(x, y, t, line_count, num_interpolation)

            spline_x = CubicSpline(t, x)
            spline_y = CubicSpline(t, y)

            tmp = csv_file_name.split('/')
            file_name = tmp[len(tmp) - 1]
            message = f'Cubic - Spline of {file_name}'

            figure.suptitle(message)

            x1, = ax[0].plot(t, x, 'o', label='int. points')
            x2, = ax[0].plot(t_full, spline_x(t_full), label="s(t)")
            x3, = ax[0].plot(t_full, spline_x(t_full, 1), label="v(t)")
            x4, = ax[0].plot(t_full, spline_x(t_full, 2), label="a(t)")
            ax[0].legend(loc='lower left', ncol=2)
            ax[0].set_ylabel("x")
            ax[0].set_xlabel("t (seconds)")

            y1, = ax[1].plot(t, y, 'o', label='int. points')
            y2, = ax[1].plot(t_full, spline_y(t_full), label="s(t)")
            y3, = ax[1].plot(t_full, spline_y(t_full, 1), label="v(t)")
            y4, = ax[1].plot(t_full, spline_y(t_full, 2), label="a(t)")
            ax[1].legend(loc='lower left', ncol=2)
            ax[1].set_ylabel("y")
            ax[1].set_xlabel("t (seconds)")

            return [x1, x2, x3, x4], [y1, y2, y3, y4]

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

    @staticmethod
    def __time_interpolation__(x, y, t, line_count, num_interpolation):

        tmp_x, tmp_y, tmp_t = [], [], []

        xs = np.arange(0, line_count - 1, int((line_count - 1) / num_interpolation))

        for i in xs:
            tmp_x.append(x[i])
            tmp_y.append(y[i])
            tmp_t.append(t[i])

        return np.array(tmp_x), np.array(tmp_y), np.array(tmp_t)

    @staticmethod
    def __distance_interpolation__(x, y, t, line_count, num_interpolation):

        tmp_x, tmp_y, tmp_t = [], [], []
        tmp_x.append(x[0])
        tmp_y.append(y[0])
        tmp_t.append(t[0])
        total_distance = 0
        for i in range(line_count - 1):
            total_distance += math.dist([x[i], y[i]], [x[i + 1], y[i + 1]])
        interval = total_distance / num_interpolation

        tmp_dist = 0
        for i in range(line_count - 1):
            if tmp_dist > interval:
                tmp_x.append(x[i])
                tmp_y.append(y[i])
                tmp_t.append(t[i])
                tmp_dist = 0
            else:
                tmp_dist += math.dist([x[i], y[i]], [x[i + 1], y[i + 1]])

        return np.array(tmp_x), np.array(tmp_y), np.array(tmp_t)

    @staticmethod
    def print_poly_to_file(csv_file_name, output_file_name, num_interpolation):

        x, y, t, line_count = DrawSpline.get_cords(csv_file_name)
        x, y, t = DrawSpline.__distance_interpolation__(x, y, t, line_count, num_interpolation)

        spline_x = CubicSpline(t, x)
        spline_y = CubicSpline(t, y)

        try:
            csv_file = open(output_file_name, 'w')

            csv_file.write('t_start, t_stop, ax^3, bx^2, cx, d, ay^3, by^2, cy, d\n')

            for i in range(num_interpolation):
                t_start = spline_x.x[i]
                t_stop = spline_x.x[i + 1]
                x_poly = spline_x.c[:, i]
                y_poly = spline_y.c[:, i]

                csv_file.write(
                    f'{t_start}, {t_stop}, {x_poly[0]}, {x_poly[1]}, {x_poly[2]}, {x_poly[3]}, {y_poly[0]}, {y_poly[1]}, {y_poly[2]}, {y_poly[3]}\n')

            csv_file.flush()
            csv_file.close()

        except:
            traceback.print_exc()
