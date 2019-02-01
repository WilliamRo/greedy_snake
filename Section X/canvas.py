import numpy as np
import tkinter as tk
from snake import Snake
import configs


class Canvas(tk.Canvas):

  def __init__(self, master):
    # Call parent's constructor
    super().__init__(master)

    # Init state
    self.state = configs.STATES.welcome
    self.game_over_text = None

    # Grid and objects
    self.grids = set()
    self.snakes = []
    self.apple = None

    # Do some initialization
    self._init_tk()
    self._init_grids()

    self.initialize_objects()

    # Refresh
    self.refresh()

  # region : Properties

  @property
  def width(self):
    return configs.grid_size * configs.grid_width

  @property
  def height(self):
    return configs.grid_size * configs.grid_height

  @property
  def available_grids(self):
    grids = self.grids
    for snake in self.snakes:
      assert isinstance(snake, Snake)
      grids = grids - set(snake.body)
    return grids

  # endregion : Properties

  # region : Public Methods

  def refresh(self):
    if self.state == configs.STATES.welcome:
      self.show_welcome()
    elif self.state == configs.STATES.game_over:
      self.show_game_over()
    else:
      assert self.state == configs.STATES.gaming

      # Predict next bodies
      bodies = [s.get_next_body(self.apple) for s in self.snakes]
      apple_eaten = False
      dead_indices = []
      for i, snake in enumerate(self.snakes):
        assert isinstance(snake, Snake)
        head = bodies[i][0]
        # Test apple
        apple_eaten = apple_eaten or head == self.apple
        # Test gg
        if not self._in_bound(head):
          dead_indices.append(i)
        # Test collision
        for j, body in enumerate(bodies):
          b = body[1:] if i == j else body
          if head in b:
            dead_indices.append(i)
            break
        # Move snake if necessary
        if len(dead_indices) == 0:
          snake.move(self.apple)

      # Game over test
      if len(dead_indices) > 0:
        if configs.snake_num == 1:
          self.game_over_text = 'Game Over'
        elif configs.snake_num == 2:
          if len(dead_indices) == 2:
            self.game_over_text = 'Tie'
          else:
            self.game_over_text = 'Player {} won!'.format(
              1 if dead_indices[0] == 1 else 2)
        else: assert False
        # Refresh
        self.state = configs.STATES.game_over
        self.refresh()

      # Refresh apple if necessary
      if apple_eaten: self._refresh_apple()

      # Draw current playground
      self._draw_objects()
      self.after(configs.time_interval, self.refresh)

  def initialize_objects(self):
    self._init_snakes()
    self._refresh_apple()

  def show_game_over(self):
    self.delete(tk.ALL)
    self.create_text(
      int(self.width / 2), int(self.height / 2),
      anchor=tk.CENTER, text=self.game_over_text, fill=configs.gg_color,
      font=configs.gg_font)

  def show_welcome(self):
    self.delete(tk.ALL)
    self.create_text(
      int(self.width / 2), int(self.height / 2),
      anchor=tk.CENTER, text='Welcome', fill=configs.welcome_color,
      font=configs.welcome_font)

  # endregion : Public Methods

  # region : Private Methods

  def _refresh_apple(self):
    grids = tuple(self.available_grids)
    self.apple = grids[np.random.choice(list(range(len(grids))))]

  def _init_grids(self):
    grid_list = []
    for x in range(configs.grid_width):
      for y in range(configs.grid_height):
        grid_list.append((x + 1, y + 1))
    self.grids = set(grid_list)

  def _init_snakes(self):
    self.snakes = []
    for i in range(configs.snake_num):
      direction = configs.DIRECTIONS[i]
      if i == 0:
        head = (1, configs.grid_height - configs.init_snake_len + 1)
      elif i == 1:
        head = (configs.grid_width, configs.init_snake_len)
      else:
        raise AssertionError('!! Currently only support at most 2 snakes')
      self.snakes.append(Snake(head, direction))

  def _init_tk(self):
    self.config(bg='white')
    self.config(width=self.width, height=self.height)
    self.pack()

  @staticmethod
  def _in_bound(coord):
    x, y = coord
    return 0 < x <= configs.grid_width and 0 < y <= configs.grid_height

  def _draw_rectangle(self, coord, color):
    assert self._in_bound(coord)

    x, y = coord
    x1 = (x - 1) * configs.grid_size
    x2 = x1 + configs.grid_size - 1
    y1 = (y - 1) * configs.grid_size
    y2 = y1 + configs.grid_size - 1

    # Calculate pixel range
    self.create_rectangle(
      x1, y1, x2, y2, fill=color, outline='')

  def _draw_snakes(self):
    for i, snake in enumerate(self.snakes):
      # Draw head
      self._draw_rectangle(snake.body[0], configs.head_colors[i])
      # Draw body
      for coord in snake.body[1:]:
        self._draw_rectangle(coord, configs.body_colors[i])

  def _draw_objects(self):
    self.delete(tk.ALL)
    # Draw snakes
    self._draw_snakes()
    # Draw apple
    self._draw_rectangle(self.apple, configs.apple_color)

  # endregion : Private Methods







