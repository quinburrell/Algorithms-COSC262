import matplotlib.pyplot as plt
class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
	    self.x = x
	    self.y = y
	
    def __add__(self, other):
	return Vec(self.x + other.x, self.y + other.y)
	
    def __sub__(self, other):
	return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
	return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
	return self.x * other.x + self.y * other.y

    def lensq(self):
	return self.dot(self)
    
    def __repr__(self):
	return "({}, {})".format(self.x, self.y)
    
def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are collinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y

def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise; at a, turning from b to c is ccw"""
    area = signed_area(a, b, c) # As earlier
    # May want to throw an exception if area == 0
    return area > 0 

def is_on_segment(p, a, b):
    """True if point p is on the vector from a to b"""
    return signed_area(b, p, a) == 0 and (p - a).lensq() <= (a - b).lensq() and (p - b).lensq() <= (a-b).lensq()

def intersecting(a, b, c, d):
    """True if a to b intersects c to d"""
    return is_ccw(a, d, b) != is_ccw(a, c, b) and is_ccw(c, a, d) != is_ccw(c, b, d)
    
def is_strictly_convex(vertices):
    """True if the given polygon is strictly convex"""
    for vert in range(len(vertices)):
	if not is_ccw(vertices[vert-2], vertices[vert-1], vertices[vert]):
	    return False
    return True

def gift_wrap(points):
    """finds the convex hull by making a cicuit around the outside edge"""
    min_y = points[0]
    for point in points:
	if point.y < min_y.y:
	    min_y = point
    hull = [min_y]
    while 1:
	candidate = None
	for p in points:
	    if p == hull[-1]:
		pass
	    elif candidate is None or not is_ccw(hull[-1], p, candidate):
		candidate = p
	if candidate == hull[0]:
	    break
	hull.append(candidate)
    return hull