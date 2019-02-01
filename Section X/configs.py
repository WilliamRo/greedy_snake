class STATES:
  welcome = 0
  gaming = 1
  game_over = 2


DIRECTIONS = (
  ( 0, -1),  # Up
  ( 0,  1),  # Down
  (-1,  0),  # Left
  ( 1,  0),  # Right
)


grid_height = 20
grid_width = 20
grid_size = 30

time_interval = 500

snake_num = 1
init_snake_len = 3
apple_color = 'IndianRed2'
head_colors = ('light blue', 'plum1')
body_colors = ('light cyan', 'thistle1')

welcome_font = 'Times 40'
welcome_color = 'dodger blue'
gg_font = 'Times 40'
gg_color = 'OrangeRed3'
