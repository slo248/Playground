from HouseBuilder import *
from Director import *

b = HouseBuilder()

d = LuxuryDirector(b)
d.make()

print(b.getResult())

