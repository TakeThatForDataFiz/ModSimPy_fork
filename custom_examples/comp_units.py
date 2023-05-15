from pint import UnitRegistry
from numpy import sqrt

# generate units object
units = UnitRegistry()

# use units object to get meters, second, etc.
meter = units.meter
second = units.second

# use meter and second units to create earth acceleration variable
a = 9.8 * meter / second**2

# quantity objects have magnitude (9.8) and units (meters/second^2)
print(a.magnitude)
print(a.units)

# use * operator to tie magnitude to units
t = 3.4 * second
h = 381 * meter

# quantity objects can be computed
t = sqrt(2 * h / a)
print(t)

# quantity objects can also be combined without losing units
v = a * t
print(v)

# pint allows for simple conversion between units
mile = units.mile
hour = units.hour

mph = v.to(mile/hour)
print(mph)
