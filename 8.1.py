class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return (f'{Color.START};{self.red};{self.green};{self.blue}{Color.MOD}'
                f'●'
                f'{Color.END}{Color.MOD}')

    def __eq__(self, other):
        if type(other) != Color:
            return False
        return all(self.__dict__[col] == other.__dict__[col]
                   for col in self.__dict__)

    def __add__(self, other):
        return Color(min(255, self.red + other.red),
                     min(255, self.green + other.green),
                     min(255, self.blue + other.blue))

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __mul__(self, other):

        if not 0 <= other <= 1:
            raise ValueError('c не от 0 до 1')

        def new_col(col, c):
            cl = 256 * (c - 1)
            F = (259 * (cl + 255)) / (255 * (259 - cl))
            return int(F * (col - 128) + 128)

        return Color(new_col(self.red, other),
                     new_col(self.green, other),
                     new_col(self.blue, other))

    def __rmul__(self, other):
        return self.__mul__(other)
