from random import choice


class RandomWalk:
    """Класс для генерирования случайных блужданий."""

    def __init__(self, num_points=2500):
        """Инициализирует атрибуты блуждания."""
        self.num_points = num_points

        # Все блужданий начинаются с точки (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def will_walk(self):
        """Вычесляет все точки блужданий."""

        # Шаги генерируются до достижения нужной длины.
        while len(self.x_values) < self.num_points:
            def get_step():
                direction = choice([1, -1])
                distance = choice(range(2))
                step = direction * distance
                return step
            x_step = get_step()
            y_step = get_step()

            # Откланение нулевых перемещений.
            if x_step == 0 and y_step == 0:
                continue

            # Вычисление слудующих значений x и y.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
