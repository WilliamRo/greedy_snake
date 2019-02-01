import tkinter as tk
import configs
from canvas import Canvas


class Game(object):

  def __init__(self):
    # Initialize tk root
    self.master = tk.Tk()
    self._init_master()

    # Initialize canvas
    self.canvas = Canvas(self.master)


  def _init_master(self):
    self.master.title('Greedy Snake')
    self.master.resizable(False, False)

    # Press Escape to quit
    self.master.bind('<Escape>', lambda _: self.master.quit())
    self.master.bind('<Key>', lambda e: self._on_key_press(e))

    # Place window on center screen
    win_width = configs.grid_width * configs.grid_size
    win_height = configs.grid_height * configs.grid_size
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    start_position_x = int((screen_width - win_width) / 2)
    start_position_y = int((screen_height - win_height) / 2)
    self.master.geometry('{}x{}+{}+{}'.format(
      win_width, win_height, start_position_x, start_position_y))


  def _on_key_press(self, event):
    # Sanity check
    assert isinstance(event, tk.Event)
    key_symbol = getattr(event, 'keysym')

    if key_symbol in ('space', 'Return'):
      if self.canvas.state == configs.STATES.welcome:
        self.canvas.state = configs.STATES.gaming
        # Initialize canvas
        self.canvas.initialize_objects()
      elif self.canvas.state == configs.STATES.game_over:
        self.canvas.state = configs.STATES.welcome
      self.canvas.refresh()
    elif key_symbol in ('Up', 'Down', 'Left', 'Right'):
      indices = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
      self.canvas.snakes[0].set_direction(
        configs.DIRECTIONS[indices[key_symbol]])
    elif key_symbol in ('a', 'w', 's', 'd'):
      if len(self.canvas.snakes) < 2: return
      indices = {'w': 0, 's': 1, 'a': 2, 'd': 3}
      self.canvas.snakes[1].set_direction(
        configs.DIRECTIONS[indices[key_symbol]])
    else:
      print('>> Unknown key `{}` pressed.'.format(key_symbol))


  def start(self):
    self.master.mainloop()


