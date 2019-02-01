import numpy as np
import configs


class Snake(object):

  def __init__(self, head, direction):
    assert isinstance(head, tuple) and len(head) == 2
    assert direction in configs.DIRECTIONS
    self.direction = direction
    self.next_direction = direction
    self.body = [head]
    for _ in range(configs.init_snake_len - 1):
      self.body.append(tuple(np.array(self.body[-1]) - np.array(direction)))


  @property
  def length(self):
    return len(self.body)


  @property
  def next_coord(self):
    return tuple(np.array(self.body[0]) + np.array(self.next_direction))


  def move(self, apple):
    assert isinstance(apple, bool)
    self.body.insert(0, self.next_coord)
    if not apple: self.body.pop(-1)
    self.direction = self.next_direction


  def set_direction(self, d):
    assert d in configs.DIRECTIONS
    if tuple(np.array(self.direction) + np.array(d)) != (0, 0):
      self.next_direction = d


