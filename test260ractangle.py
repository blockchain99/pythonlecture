# __init__, self

class Rectangle:
   def __init__(self, name, length, breadth, unit_cost=0):
       self.name = name
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
   def get_area(self):
       return self.length * self.breadth
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost

r = Rectangle("James",160, 120, 2000)
print("Hey %s, Area of Rectangle: %s sq units" % (r.name, r.get_area()))