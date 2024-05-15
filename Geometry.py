#  File: Geometry.py

#  Description: Use object oriented programming to develop several classes that are fundamental in Solid Geometry - Point, Sphere, Cube, and Cylinder.

#  Student Name: Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 1/ 25/ 2023

#  Date Last Modified: 1/ 30/ 2023
import sys
import math

class Point (object):
   # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    str_Point = '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    return str_Point
  
  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance(self, other):
    point_distance = math.hypot (self.x - other.x, self.y - other.y, self.z - other.z)
    return point_distance

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-6 
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol))

class Sphere (object):

  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.radius = float(radius)
    self.center = Point(x,y,z)

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    str_center = "Center: (" + str(self.x) +", " + str(self.y)+", " +str(self.z) + ")," + " Radius: " + str(self.radius)
    return str_center

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    calc_area = (self.radius ** 2) * 4 * math.pi
    return calc_area

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    calc_vol = (4/3) * math.pi * (self.radius **3)
    return calc_vol

  def get_maxes(self):
    x_max = self.center.x + self.radius
    y_max = self.center.y + self.radius
    z_max = self.center.z + self.radius

    return (x_max, y_max, z_max)

  def get_mins(self):
    x_min = self.center.x - self.radius
    y_min = self.center.y - self.radius
    z_min = self.center.z - self.radius

    return (x_min, y_min, z_min)

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    return self.center.distance(p) < self.radius

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    distance_center = self.center.distance(other.center)
    return (distance_center + other.radius) < self.radius

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    verticies_list = a_cube.verticies()

    for x in verticies_list:
      if((x.distance(self.center) < self.radius) == False):
        return False
      
    return True

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    centers_distance = self.center.distance(other.center)

    return (centers_distance <= (self.radius + other.radius) and not(self.is_inside_sphere(other)))

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
    if self.is_inside_cube(a_cube) == False and \
        a_cube.is_inside_sphere(self) == False and \
        Cylinder.is_outside(self, a_cube) == False:
        does_intersect = True
    else:
        does_intersect = False

    return does_intersect
  
# determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
    center = Point(self.x, self.y, self.z)
    cylinder_height = a_cyl.height / 2

    vertex1 = Point(a_cyl.x + a_cyl.radius, a_cyl.y, a_cyl.z + cylinder_height)
    vertex2 = Point(a_cyl.x - a_cyl.radius, a_cyl.y, a_cyl.z + cylinder_height)
    vertex3 = Point(a_cyl.x, a_cyl.y + a_cyl.radius, a_cyl.z + cylinder_height)
    vertex4 = Point(a_cyl.x, a_cyl.y - a_cyl.radius, a_cyl.z + cylinder_height)
    vertex5 = Point(a_cyl.x + a_cyl.radius, a_cyl.y, a_cyl.z - cylinder_height)
    vertex6 = Point(a_cyl.x - a_cyl.radius, a_cyl.y, a_cyl.z - cylinder_height)
    vertex7 = Point(a_cyl.x, a_cyl.y - a_cyl.radius, a_cyl.z - cylinder_height)
    vertex8 = Point(a_cyl.x, a_cyl.y + a_cyl.radius, a_cyl.z - cylinder_height)

    return (center.distance(vertex1) < self.radius) and (center.distance(vertex2) < self.radius) and \
      (center.distance(vertex3) < self.radius) and (center.distance(vertex4) < self.radius) and \
        (center.distance(vertex5) < self.radius) and (center.distance(vertex6) < self.radius) and \
          (center.distance(vertex7) < self.radius) and (center.distance(vertex8) < self.radius)

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    diameter = self.radius * 2
    side = (diameter / (math.sqrt(3)))
    cube = Cube(self.center.x, self.center.y, self.center.z, side)

    return cube

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.side = float(side)
    self.center = Point(x,y,z)

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
    str_cube = "Center: (" + str(self.x)+", "+ str(self.y)+", " +str(self.z)+ "), " + "Side: " + str(self.side)
    return str_cube
  
  def verticies(self):
    self.list = []
    side = self.side /2
    # add .5 side to x coordinate both front and back
    coordinates_1 = Point(self.x + side, self.y + side, self.z - side )
    self.list.append(coordinates_1)

    coordinates_2 = Point(self.x + side, self.y - side, self.z - side)
    self.list.append(coordinates_2)

    coordinates_3 = Point(self.x - side, self.y - side, self.z - side)
    self.list.append(coordinates_3)

    coordinates_4 = Point(self.x - side, self.y  + side, self.z - side)
    self.list.append(coordinates_4)

    coordinates_5 = Point(self.x - side, self.y - side, self.z  + side)
    self.list.append(coordinates_5)

    coordinates_6 = Point(self.x - side, self.y + side, self.z  + side)
    self.list.append(coordinates_6)

    coordinates_7 = Point(self.x + side, self.y - side, self.z  - side)
    self.list.append(coordinates_7)

    coordinates_8 = Point(self.x + side, self.y + side, self.z  - side)
    self.list.append(coordinates_8)

    return self.list
  
  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    calc_area = (self.side ** 2) * 6
    return calc_area

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    calc_volume = self.side ** 3
    return calc_volume

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def get_maxes(self):
      max_values_list = []
      half_side = self.side / 2
      max_values_list.append(self.center.x + half_side)
      max_values_list.append(self.center.y + half_side)
      max_values_list.append(self.center.z + half_side)

      return max_values_list

  # gets minimum x,y, and z values for the cube
  def get_mins(self):
      min_values_list = []
      half_side = self.side / 2
      min_values_list.append(self.center.x - half_side)
      min_values_list.append(self.center.y - half_side)
      min_values_list.append(self.center.z - half_side)

      return min_values_list

  def is_inside_point (self, p):
    min_x = self.center.x - self.side/2
    max_x = self.center.x + self.side/2
    min_y = self.center.y - self.side/2
    max_y = self.center.y + self.side/2
    min_z  =self.center.z - self.side/2
    max_z = self.center.z +self.side/2
    return (min_x < p.x < max_x) and (min_z < p.z < max_z) and (min_y < p.y < max_y)

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    sphere_mins = a_sphere.get_mins()
    sphere_maxes = a_sphere.get_maxes()
    cube_mins = self.get_mins()
    cube_maxes = self.get_maxes()

    if cube_mins[0] < sphere_mins[0] < sphere_maxes[0] < cube_maxes[0] and \
        cube_mins[1] < sphere_mins[1] < sphere_maxes[1] < cube_maxes[1] and \
        cube_mins[2] < sphere_mins[2] < sphere_maxes[2] < cube_maxes[2]:
        is_inside = True
    else:
        is_inside = False
    return is_inside

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    another_cube = other.verticies()
    for x in another_cube:
      if(self.is_inside_point(x) == False):
        return False
    return True

  def is_inside_cylinder (self, a_cyl):
      other_maxes = a_cyl.get_maxes()
      other_mins = a_cyl.get_mins()
      self_maxes = self.get_maxes()
      self_mins = self.get_mins()

      if self_mins[0] < other_mins[0] < other_maxes[0] < self_maxes[0] and \
              self_mins[1] < other_mins[1] < other_maxes[1] < self_maxes[1] and \
              self_mins[2] < other_mins[2] < other_maxes[2] < self_maxes[2]:
          is_inside = True
      else:
          is_inside = False

      return is_inside

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    if self.is_inside_cube(other) == False and other.is_inside_cube(self) == False and Cylinder.is_outside(self, other) == False:
      return True
    else:
      return False

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    ans = abs((self.x - other.x) * (self.y - other.y) * (self.z - other.z))
    return float(ans)

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    radius = self.side/2
    sphere = Sphere(self.center.x, self.center.y, self.center.z, radius)
    return sphere

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.radius = float(radius)
    self.height = float(height)
    self.center = Point(x,y,z)

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    str_Cylinder =  "Center: (" + str(self.x) +", " + str(self.y)+", "  +str(self.z) + ")," + " Radius: " + str(self.radius) + ", " + "Height: " + str(self.height)
    return str_Cylinder
  
  def get_maxes(self):
    max_list = []
    max_list.append(self.center.x + self.radius)
    max_list.append(self.center.y + self.radius)
    max_list.append(self.center.z + (self.height/2))

    return max_list

  def get_mins(self):
    min_list = []
    min_list.append(self.center.x - self.radius)
    min_list.append(self.center.y - self.radius)
    min_list.append(self.center.z - (self.height / 2))

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    calculate_area = (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2))
    return calculate_area
  
  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    calculate_volum = math.pi * (self.radius ** 2) * self.height
    return calculate_volum

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    center = Point(self.x, self.y, self.z)
    return center.distance(p) < self.radius and center.distance(p) < self.height

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    centers_distance = self.center.distance(a_sphere.center)
    return ((centers_distance + a_sphere.radius) < self.radius) and ((centers_distance + a_sphere.radius) < self.height)

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      cube_side = a_cube.side / 2
      vertex1 = Point(a_cube.x + cube_side, a_cube.y + cube_side, a_cube.z + cube_side)
      vertex2 = Point(a_cube.x - cube_side, a_cube.y + cube_side, a_cube.z + cube_side)
      vertex3 = Point(a_cube.x - cube_side, a_cube.y - cube_side, a_cube.z + cube_side)
      vertex4 = Point(a_cube.x - cube_side, a_cube.y - cube_side, a_cube.z - cube_side)
      vertex5 = Point(a_cube.x + cube_side, a_cube.y - cube_side, a_cube.z + cube_side)
      vertex6 = Point(a_cube.x + cube_side, a_cube.y - cube_side, a_cube.z - cube_side)
      vertex7 = Point(a_cube.x + cube_side, a_cube.y + cube_side, a_cube.z - cube_side)
      vertex8 = Point(a_cube.x - cube_side, a_cube.y + cube_side, a_cube.z - cube_side)
      return (self.center.distance(vertex1) < self.radius) and (self.center.distance(vertex2) < self.radius)\
            and (self.center.distance(vertex3) < self.radius) and (self.center.distance(vertex4) < self.radius) and \
              (self.center.distance(vertex5) < self.radius) and (self.center.distance(vertex6) < self.radius) and \
                (self.center.distance(vertex7) < self.radius) and (self.center.distance(vertex8) < self.radius) and \
                  (self.center.distance(vertex1) < self.height) and (self.center.distance(vertex2) < self.height) and \
                    (self.center.distance(vertex3) < self.height) and (self.center.distance(vertex4) < self.height) and \
                      (self.center.distance(vertex5) < self.height) and (self.center.distance(vertex6) < self.height) and \
                        (self.center.distance(vertex7) < self.height) and (self.center.distance(vertex8) < self.height)
  
  def is_outside(shape1, shape2):
    maxes1 = shape1.get_maxes()
    mins1 = shape1.get_mins()

    maxes2 = shape2.get_maxes()
    mins2 = shape2.get_mins()
    check_list = []

    if maxes1[0] < mins2[0]:
        check_list.append(True)
    if maxes2[0] < mins1[0]:
        check_list.append(True)
    if maxes1[1] < mins2[1]:
        check_list.append(True)
    if maxes2[1] < mins1[1]:
        check_list.append(True)
    if maxes1[2] < mins2[2]:
        check_list.append(True)
    if maxes2[2] < mins1[2]:
        check_list.append(True)
    if True in check_list:
        out = True
    else:
        out = False

    return out

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    distance = self.center.distance(other.center)
    return (distance+other.radius < self.radius) and (distance+other.radius < self.height) and (distance+other.height < self.radius) and (distance+other.height < self.height)
    
    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
  def does_intersect_cylinder (self, other):
    centers_distance = self.center.distance(other.center)
    return (centers_distance < (self.radius + other.radius) and (centers_distance < (self.height + other.height)) and not(self.is_inside_cylinder(other)))

def main():
  #Part 1
  # read data from standard input
  coordinates_of_p = sys.stdin.readline()
  coordinates_of_p = coordinates_of_p.split()
  
  coordinates_of_q = sys.stdin.readline()
  coordinates_of_q = coordinates_of_q.split()
  # read the coordinates of the first Point p
  #point_p = (coordinates_of_p[0], coordinates_of_p[1], coordinates_of_p[2])
  #print(coordinates_of_p)
  #print(point_p)

  # create a Point object 
  point_object_p = Point(coordinates_of_p[0], coordinates_of_p[1], coordinates_of_p[2])
  #print(point_object_p)

  # read the coordinates of the second Point q
  #point_q = (coordinates_of_q[0],coordinates_of_q[1], coordinates_of_q[2])
  #print(coordinates_of_q)
  #print(point_q)

  # create a Point object 
  point_object_q = Point(coordinates_of_q[0],coordinates_of_q[1], coordinates_of_q[2])
  #print(point_object_q)

  #Part 2
  coordinates_sphereA = sys.stdin.readline()
  coordinates_sphereA = coordinates_sphereA.split()

  # create a Sphere object
  sphere_object_A = Sphere(coordinates_sphereA[0], coordinates_sphereA[1], coordinates_sphereA[2], coordinates_sphereA[3])

  # read the coordinates of the center and radius of sphereB
  coordinates_sphereB = sys.stdin.readline()
  coordinates_sphereB = coordinates_sphereB.split()

  # create a Sphere object
  sphere_object_B = Sphere(coordinates_sphereB[0], coordinates_sphereB[1], coordinates_sphereB[2], coordinates_sphereB[3])

  #Part 3
  # read the coordinates of the center and side of cubeA
  coordinates_cubeA = sys.stdin.readline()
  coordinates_cubeA = coordinates_cubeA.split()

  # create a Cube object 
  cube_object_A = Cube(coordinates_cubeA[0], coordinates_cubeA[1], coordinates_cubeA[2], coordinates_cubeA[3])

  # read the coordinates of the center and side of cubeB
  coordinates_cubeB = sys.stdin.readline()
  coordinates_cubeB = coordinates_cubeB.split()

  # create a Cube object 
  cube_object_B = Cube(coordinates_cubeB[0], coordinates_cubeB[1], coordinates_cubeB[2], coordinates_cubeB[3])

  #Part 4
  # read the coordinates of the center, radius and height of cylA
  coordinates_of_cylA = sys.stdin.readline()
  coordinates_of_cylA = coordinates_of_cylA.split()

  # create a Cylinder object 
  cylinder_object_A = Cylinder(coordinates_of_cylA[0], coordinates_of_cylA[1], coordinates_of_cylA[2], coordinates_of_cylA[3], coordinates_of_cylA[4])
  #print(cylinder_object_A)

  # read the coordinates of the center, radius and height of cylB
  coordinates_of_cylB = sys.stdin.readline()
  coordinates_of_cylB = coordinates_of_cylB.split()

  # create a Cylinder object
  cylinder_object_B = Cylinder(coordinates_of_cylB[0], coordinates_of_cylB[1], coordinates_of_cylB[2], coordinates_of_cylB[3], coordinates_of_cylB[4])
  #print(cylinder_object_B)

  #Part 1
  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
  origin = Point(0, 0, 0)
  distance_1 = Point.distance(point_object_p, origin)
  distance_2 = Point.distance(point_object_q, origin)

#1 - Distance of Point p from the origin is not greater than the distance of Point q from the origin

  if distance_1 > distance_2:
    print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
  else:
    print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')

  #print()

#2 - Point p is not inside sphereA
  # print if Point p is inside sphereA
  if Sphere.is_inside_point(sphere_object_A, point_object_p) == True:
    print('Point p is inside sphereA')
  else:
    print('Point p is not inside sphereA')

#3 -sphereB is not inside sphereA
  # print if sphereB is inside sphereA
  if Sphere.is_inside_sphere(sphere_object_A, sphere_object_B) == True:
    print('sphereB is inside sphereA')
  else:
    print('sphereB is not inside sphereA')

#4 - cubeA is not inside sphereA
  # print if cubeA is inside sphereA
  if Sphere.is_inside_cube(sphere_object_A, cube_object_A) == True:
      print('cubeA is inside sphereA')
  else:
    print('cubeA is not inside sphereA')

#5 - sphereA does intersect sphereB
  # print if sphereA intersects with sphereB
  if Sphere.does_intersect_sphere(sphere_object_A, sphere_object_B) == True:
    print('sphereA does intersect sphereB')
  else:
    print('sphereA does not intersect sphereB')

#6 - cubeB does intersect sphereB
  # print if cubeB intersects with sphereB
  if Sphere.does_intersect_cube(sphere_object_B, cube_object_B) == True:
    print('cubeB does intersect sphereB')
  else:
    print('cubeB does not intersect sphereB')
  
  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
  circumscribed_cube = sphere_object_A.circumscribe_cube()
  circumscribed_cube_volume = circumscribed_cube.volume()
  cylinder_A_volume = cylinder_object_A.volume()

#7 - Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA
  if circumscribed_cube_volume > cylinder_A_volume:
    print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
  else:
    print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')

  #print()
  #Part 3
  #8 - Point p is not inside cubeA
  # print if Point p is inside cubeA
  if cube_object_A.is_inside_point(point_object_p) == True:
    print('Point p is inside cubeA')
  else:
    print('Point p is not inside cubeA')

#9 - sphereA is not inside cubeA
  # print if sphereA is inside cubeA
  if cube_object_A.is_inside_sphere(sphere_object_A) == True:
    print('sphereA is inside cubeA')
  else:
    print('sphereA is not inside cubeA')

#10 - cubeB is not inside cubeA
  # print if cubeB is inside cubeA
  if cube_object_A.is_inside_cube(cube_object_B) == True:
    print('cubeB is inside cubeA')
  else:
    print('cubeB is not inside cubeA')

#11- cubeA does intersect cubeB
  # print if cubeA intersects with cubeB
  if Cube.does_intersect_cube(cube_object_A, cube_object_B) == True:
    print("cubeA does intersect cubeB")
  else:
    print("cubeA does not intersect cubeB")

#12 - Intersection volume of cubeA and cubeB is not greater than the volume of sphereA
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  intersection_volume = cube_object_A.intersection_volume(cube_object_B)

  if intersection_volume > sphere_object_A.volume():
    print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
  else:
    print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')

#13 - Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA 
  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
  sphere = cube_object_A.inscribe_sphere()

  if sphere.volume() > cylinder_object_A.area():
    print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
  else:
    print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')

  #print()

  #Part 4
#14 - Point p is not inside cylA
  # print if Point p is inside cylA
  if cylinder_object_A.is_inside_point(point_object_p) == True:
    print('Point p is inside cylA')
  else:
    print('Point p is not inside cylA')

#15 - sphereA is not inside cylA
   #print if sphereA is inside cylA
  if cylinder_object_A.is_inside_sphere(sphere_object_A) == True:
    print('sphereA is inside cylA')
  else:
    print('sphereA is not inside cylA')

#16 - cubeA is not inside cylA
  # print if cubeA is inside cylA
  if cylinder_object_A.is_inside_cube(cube_object_A) == True:
    print('cubeA is inside cylA')
  else:
    print('cubeA is not inside cylA')

if __name__ == "__main__":
  main()
