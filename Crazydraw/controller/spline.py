from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np
import csv


class DrawSpline:

    def __init__(self):

        self.x, self.y = None, None

    @staticmethod
    def plot_trajectory(csv_file_name):

        with open(csv_file_name, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            x = []
            y = []

            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    if len(row) != 0:
                        print(row)
                        x.append(row[0])
                        y.append(row[1])
                        line_count += 1
            print(f'Processed {line_count} lines.')

            x = np.array(x)
            y = np.array(y)
            cs = CubicSpline(x, y)
            xs = np.arange(-0.5, 9.6, 0.1)
            fig, ax = plt.subplots(figsize=(6.5, 4))
            ax.plot(x, y, 'o', label='data')
            ax.plot(xs, np.sin(xs), label='true')
            ax.plot(xs, cs(xs), label="S")
            ax.plot(xs, cs(xs, 1), label="S'")
            ax.plot(xs, cs(xs, 2), label="S''")
            ax.plot(xs, cs(xs, 3), label="S'''")
            ax.set_xlim(-0.5, 9.5)
            ax.legend(loc='lower left', ncol=2)
            plt.show()
