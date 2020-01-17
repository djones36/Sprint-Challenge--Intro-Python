# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:  # Base Class
    pass

# Group A from base class


class GroundVehicle(Vehicle):  # Child 1
    pass


class Car(GroundVehicle):  # Grandchild 1
    pass


class Motorcycle(GroundVehicle):  # Grandchild 2
    pass

# Group B from base class


class FlightVehicle(Vehicle):  # Child 2
    pass


class Starship(FlightVehicle):  # Grandchild 1
    pass


class Airplane(FlightVehicle):  # Grandchild 2
    pass
