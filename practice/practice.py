from collections import namedtuple
from collections import Counter

# Named tuple
Point = namedtuple('Point', ['x', 'y'])

p1 = Point(x=1.0, y=5.0)
p2 = Point(x=2.5, y=1.5)
print(p1.x, p2.x)

C = Counter('gallahad')
print(C['a'])