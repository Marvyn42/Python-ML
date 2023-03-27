from sys import exit as sys_exit


class Vector:
    """Create a Vector that's contains his values and shape."""

    value = None
    shape = None

    def __init__(self, arg=None):
        self.check_arg(arg, type(arg))
        list_value = []
        if isinstance(arg, int):
            for elem in range(0, arg):
                list_value.append([float(elem)])
            self.value = list_value
            self.shape = (arg, 1)
        elif isinstance(arg, tuple):
            for elem in range(arg[0], arg[1]):
                list_value.append([float(elem)])
            self.value = list_value
            self.shape = (arg[1] - arg[0], 1)
        elif isinstance(arg, list):
            self.value = arg
            if (len(arg) > 1):
                self.shape = (len(arg), 1)
            else:
                self.shape = (1, len(arg[0]))

    def __str__(self):
        return (f"Vector({self.value})")

    def __repr__(self):
        return (f"Vector({self.value})")

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError("addition with Vector only")
        if other.shape != self.shape:
            raise ValueError("Vectors doesn't have the same shape.")
        list_value = []
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                list_value.append(self.value[0][i] + other.value[0][i])
            return Vector([list_value])
        else:
            for i in range(self.shape[0]):
                list_value.append([self.value[i][0] + other.value[i][0]])
            return Vector(list_value)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError("substraction with Vector only")
        if other.shape != self.shape:
            raise ValueError("Vectors doesn't have the same shape.")
        list_value = []
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                list_value.append(self.value[0][i] - other.value[0][i])
            return Vector([list_value])
        else:
            for i in range(self.shape[0]):
                list_value.append([self.value[i][0] - other.value[i][0]])
            return Vector(list_value)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, div):
        if not isinstance(div, (int, float)):
            raise NotImplementedError("division with scalar only")
        if div == 0:
            raise ZeroDivisionError("division by 0")
        list_value = []
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                list_value.append(self.value[0][i] / div)
            return Vector([list_value])
        else:
            for i in range(self.shape[0]):
                list_value.append([self.value[i][0] / div])
            return Vector(list_value)

    def __rtruediv__(self, _):
        raise NotImplementedError(
            "Division of a scalar by a Vector is not defined here.")

    def __mul__(self, mul):
        if not isinstance(mul, int):
            raise NotImplementedError("multiplication with scalar only")
        list_value = []
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                list_value.append(self.value[0][i] * mul)
            return Vector([list_value])
        else:
            for i in range(self.shape[0]):
                list_value.append([self.value[i][0] * mul])
            return (Vector(list_value))

    def __rmul__(self, other):
        return self.__mul__(other)

    @staticmethod
    def check_arg(arg, arg_type):
        """Parse the argument to initialize value and shape."""
        if arg is None:
            raise ValueError("No Value given to the Vector class.")
        elif arg_type is int:
            if (arg < 0):
                raise ValueError("The integer must be positif.")
        elif arg_type is tuple:
            if (len(arg) > 2 or not isinstance(arg[0], int)
               or not isinstance(arg[1], int)):
                raise ValueError("Range must contains 2 int.")
            elif (arg[0] > arg[1]):
                raise ValueError("The range must be increasing.")
        elif arg_type is list:
            if len(arg) > 1:
                for elem in arg:
                    if not isinstance(elem[0], float):
                        raise ValueError("Only floats.")
            else:
                if not isinstance(arg[0], list):
                    raise ValueError("It must be a list of list.")
                for elem in arg[0]:
                    if not isinstance(elem, float):
                        raise ValueError("Only floats.")
        else:
            sys_exit("Non valid argument.")

    def dot(self, other):
        """Produce a dot product between two vectors of same shape"""
        if not isinstance(other, Vector):
            raise ValueError("The argument must be a vector")
        if other.shape != self.shape:
            raise ValueError("Vectors doesn't have the same shape.")
        dot_product = 0
        if self.shape[0] == 1:
            for i in range(self.shape[1]):
                dot_product += self.value[0][i] * other.value[0][i]
        else:
            for i in range(self.shape[0]):
                dot_product += self.value[i][0] * other.value[i][0]
        return (dot_product)

    def T(self):
        """Transpose columns into row and row into columns"""
        list_value = []
        if self.shape[0] == 1:
            for elem in self.value[0]:
                list_value.append([float(elem)])
            return Vector(list_value)
        else:
            for elem in self.value:
                list_value.append(float(elem[0]))
            return Vector([list_value])
