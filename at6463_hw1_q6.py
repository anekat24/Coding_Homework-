class Vector:
    def __init__(self, d):
        if type(d) == int:
            self.coords = [0] * d
        elif type(d) == list:
            self.coords = d
        else:
            raise TypeError("Input must be an integer or a list")

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __mul__(self, other):
        if type(other) == Vector:  # Dot product
            if len(self) != len(other):
                raise ValueError("Dimensions must agree")
            return sum(self[i] * other[i] for i in range(len(self)))
        elif type(other) == int or type(other) == float:  
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
            return result
        else:
            raise TypeError("Unsupported multiplication")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '<' + ', '.join(map(str, self.coords)) + '>'

    def __repr__(self):
        return str(self)
