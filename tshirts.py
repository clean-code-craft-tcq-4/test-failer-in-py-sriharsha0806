class tshirts:    
    @staticmethod
    def size(cms):
        if cms < 38:
            return 'S'
        elif cms in range(38,43):
            return 'M'
        elif cms in range(43,50):
            return 'L'
        else:
            return 'Custom Design is required'


assert(tshirts.size(37) == 'S')
assert(tshirts.size(40) == 'M')
assert(tshirts.size(43) == 'L')
print("All is well (maybe!)\n")
