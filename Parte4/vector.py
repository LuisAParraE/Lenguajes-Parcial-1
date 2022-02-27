class vector:

    def __init__(self, x, y ,z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return ((self.x == other.x) and (self.y == other.y) and (self.z == other.z))

    def __add__(self, other):
        suma = vector(0,0,0)
        if isinstance(other, int) or isinstance(other, float):
            suma.x = self.x + other
            suma.y = self.y + other
            suma.z = self.z + other
        elif isinstance(self, vector) and isinstance(other, vector):
            
            suma.x = self.x + other.x
            suma.y = self.y + other.y
            suma.z = self.z + other.z
        else:
            pass
        return suma

    def __sub__(self, other):
        resta = vector(0,0,0)
        if isinstance(other, int) or isinstance(other, float):
            resta.x = self.x - other
            resta.y = self.y - other
            resta.z = self.z - other
        elif isinstance(self, vector) and isinstance(other, vector):
            
            resta.x = self.x - other.x
            resta.y = self.y - other.y
            resta.z = self.z - other.z
        else:
            pass
        return resta

    def __mul__(self, other):
        mult = vector(0,0,0)
        if isinstance(other, int) or isinstance(other, float):
            mult.x = self.x * other
            mult.y = self.y * other
            mult.z = self.z * other
        elif isinstance(self, vector) and isinstance(other, vector):
            
            mult.x = self.y * other.z - (self.z * other.y)
            mult.y = -( self.x * other.z - (self.z * other.x) )
            mult.z = self.x * other.y - (self.y * other.x)
        else:
            pass
        return mult

    def __mod__(self, other):
        modul = vector(0,0,0)
        if isinstance(other, int) or isinstance(other, float):
            if other == 0:
                raise ValueError("Can not divide by Zero")

            modul.x = self.x % other
            modul.y = self.y % other
            modul.z = self.z % other

            return modul
        elif isinstance(self, vector) and isinstance(other, vector):
            
            return(self.x * other.x + self.y * other.y + self.z * other.z)

        else:
            pass
        

    def print(self):
        print(self.x)
        print(self.y)
        print(self.z)
