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



