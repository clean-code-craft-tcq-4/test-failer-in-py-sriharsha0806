class tshirts:
    def size(self, cms):
        if cms < 38:
            return 'S'
        elif cms in range(38,43):
            return 'M'
        elif cms in range(43,50):
            return 'L'
        else:
            return 'Custom Design is required'


assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
print("All is well (maybe!)\n")
