
class Color(object):
  def __init__(self, *args):
    self._r = 1.0
    self._g = 1.0
    self._b = 1.0
    self._a = 1.0
    
    if len(args) != 0:
      self.set(*args)
      
  def _mode(self, val):
    if val < 0 or val > 255:
      return -1
    if val > 1:
      return 255
    return 1
    
  def _1_to_255(self, val):
    return int(round(val * 255))
    
  def _255_to_1(self, val):
    return val / 255.0
      
  def _init_str(self, hexstr):
    hexstr = hexstr.lower()
    st = ''
    if hexstr.startswith('#'):
      st = hexstr[1:]
    elif hexstr.startswith('0x'):
      st = hexstr[2:]
      
    if len(st) in (3,4):
      st = ''.join([c*2 for c in list(st)])
    if len(st) in (6,8):
      pass
    else:
      raise Exception('Invalid hexadecimal color string format: must be length 3 or 6')
      
    for c in st:
      if c not in '0123456789abcdef':
        raise Exception('Invalid hexadecimal color string format: contains invalid hexadecimal values (not 0-f)')
      
    rs = st[:2]
    gs = st[2:4]
    bs = st[4:6]
    al = 'ff' if len(st) != 8 else st[6:]
    
    r = int(rs, 16)
    g = int(gs, 16)
    b = int(bs, 16)
    a = int(al, 16)
    
    self._r = self._255_to_1(r)
    self._g = self._255_to_1(g)
    self._b = self._255_to_1(b)
    self._a = self._255_to_1(a)
    
  def _init_rgba(self, vals):
    mode = 1
    for v in vals:
      if v < 0:
        raise Exception('Invalid rgba values: cannot be negative')
      if v > 255:
        raise Exception('Invalid rgba values: must be less than or equal to 255')
      if v > 1:
        mode = 255
    r,g,b = vals[:3]
    a = mode if len(vals) == 3 else vals[3]
    
    self._r = r if mode == 1 else self._255_to_1(r)
    self._g = g if mode == 1 else self._255_to_1(g)
    self._b = b if mode == 1 else self._255_to_1(b)
    self._a = a if mode == 1 else self._255_to_1(a)
    
  def set(self, *args):
    if len(args) == 1 and type(args[0]) in [list, tuple]:
      args = args[0]
    
    if len(args) == 1 and type(args[0]) == str:
      self._init_str(args[0])
    elif len(args) in [3, 4, 6, 8]:
      self._init_rgba(args)
    else:
      raise Exception('Invalid arguments: must be either a hexadecimal string, or rgb(a) values passed as separate arguments.')
  
  def as_rgba(self):
    return (self._r, self._g, self._b, self._a)
  
  def as_tuple(self):
    return self.as_rgba()
    
  def as_int_rgba(self):
    return (self._1_to_255(self._r), 
            self._1_to_255(self._g), 
            self._1_to_255(self._b), 
            self._1_to_255(self._a))
    
  def as_rgb(self):
    return (self._r, self._g, self._b)
    
  def as_int_rgb(self):
    return (self._1_to_255(self._r), 
            self._1_to_255(self._g), 
            self._1_to_255(self._b))
    
  def as_hex6(self):
    irgb = self.as_int_rgb()
    return '#{:02x}{:02x}{:02x}'.format(*irgb)
    
  def as_hex8(self):
    irgba = self.as_int_rgba()
    return '#{:02x}{:02x}{:02x}{:02x}'.format(*irgba)
    
  def as_hex(self):
    if self._a == 1:
      return self.as_hex6()
    else:
      return self.as_hex8()
      
  def __repr__(self):
    return self.as_hex()
    
  @property
  def r(self):
    return self._r
    
  @r.setter
  def r(self, val):
    mode = self._mode(val)
    if mode < 0:
      raise Exception('Argument Error: value must be between 0-255.')
    elif mode == 255:
      self._r = self._255_to_1(val)
    else:
      self._r = val
    
  @property
  def g(self):
    return self._g
    
  @g.setter
  def g(self, val):
    mode = self._mode(val)
    if mode < 0:
      raise Exception('Argument Error: value must be between 0-255.')
    elif mode == 255:
      self._g = self._255_to_1(val)
    else:
      self._g = val
    
  @property
  def b(self):
    return self._b
    
  @b.setter
  def b(self, val):
    mode = self._mode(val)
    if mode < 0:
      raise Exception('Argument Error: value must be between 0-255.')
    elif mode == 255:
      self._b = self._255_to_1(val)
    else:
      self._b = val
    
  @property
  def a(self):
    return self._a
    
  @a.setter
  def a(self, val):
    mode = self._mode(val)
    if mode < 0:
      raise Exception('Argument Error: value must be between 0-255.')
    elif mode == 255:
      self._a = self._255_to_1(val)
    else:
      self._a = val
      
      
if __name__ == '__main__':
  c = Color()
  c.set('#12345678')
  print(c)
