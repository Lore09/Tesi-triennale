import yaml
import io

from PyQt5.QtCore import QDir


class SettingsParser:
    def __init__(self):

        with open(QDir.currentPath() + "/settings.yaml") as stream:
            try:
                self.data = yaml.safe_load(stream)
                print(self.data)
            except yaml.YAMLError as exc:
                print(exc)

    def get_paint_size_scaled(self):

        size = self.data["area_settings"]["paint_square_size"]

        scale = []
        scale.append(int(size[0] * 700 / size[1]))
        scale.append(700)

        return scale

    def get_area_size_meters(self):

        return self.data["area_settings"]["paint_square_size"]

    def get_trajectory_path(self):
        path = self.data["trajectory_manager"]["saves_directory"]
        return path

    def get_scale_factor(self):

        x_size, y_size = self.get_area_size_meters()
        x_widget, y_widget = self.get_paint_size_scaled()

        y_dist = int(y_widget / y_size)
        x_dist = int(x_widget / x_size)

        if x_dist == y_dist:
            return x_dist
        else:
            return 0
