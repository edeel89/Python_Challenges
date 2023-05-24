from random import randint

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Ellipse, Color

class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.snake_speed = 1
        self.snake_size = 20
        self.food_size = 10
        self.grid_size = 20
        self.snake_pos = [(10, 10)]
        self.food_pos = (50, 50)
        self.direction = "right"
        with self.canvas:
            self.snake_color = Color(1, 1, 0)
            self.food_color = Color(1, 1, 1)
            self.snake = [Ellipse(pos=pos, size=(self.snake_size, self.snake_size)) for pos in self.snake_pos]
            self.food = Ellipse(pos=self.food_pos, size=(self.food_size, self.food_size))
        self.bind(pos=self.update_snake)
        self.bind(size=self.update_snake)
        Clock.schedule_interval(self.move_snake, 1 / self.snake_speed)
    
    def on_key_down(self, window, key, *args):
        if key == 274:  # arrow down
            self.direction = "down"
        elif key == 273:  # arrow up
            self.direction = "up"
        elif key == 276:  # arrow left
            self.direction = "left"
        elif key == 275:  # arrow right
            self.direction = "right"


    def update_snake(self, *args):
        self.food.pos = self.food_pos
        for i, snake in enumerate(self.snake):
            snake.pos = self.snake_pos[i]
            snake.size = (self.snake_size, self.snake_size)

    def move_snake(self, dt):
        x, y = self.snake_pos[0]
        if self.direction == "right":
            x += self.grid_size
        elif self.direction == "left":
            x -= self.grid_size
        elif self.direction == "up":
            y += self.grid_size
        elif self.direction == "down":
            y -= self.grid_size

        # Check if the snake has hit the edge of the screen
        if x < 0 or x > self.width - self.snake_size or y < 0 or y > self.height - self.snake_size:
            self.game_over()
            return

        self.snake_pos.insert(0, (x, y))
        if (x, y) != self.food_pos:
            self.snake_pos.pop()
        else:
            self.spawn_food()

    def spawn_food(self):
        self.food_pos = (randint(0, (self.width - self.food_size) / self.grid_size) * self.grid_size,
                         randint(0, (self.height - self.food_size) / self.grid_size) * self.grid_size)
        self.food.pos = self.food_pos

    def game_over(self):
        Clock.unschedule(self.move_snake)

class SnakeApp(App):
    def build(self):
        game = SnakeGame()
        Window.bind(on_key_down=game.on_key_down)
        return game

if __name__ == '__main__':
    SnakeApp().run()

           
