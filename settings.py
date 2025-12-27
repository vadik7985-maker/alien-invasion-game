class Settings():
    """Класс для хранения всех настроект игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 200, 200)
        self.ship_speed = 0.5