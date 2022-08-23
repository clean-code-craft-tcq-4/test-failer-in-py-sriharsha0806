class tshirts:    
    @staticmethod
    def size(cms):
        if cms < 38:
            return 'S'
        elif cms in range(38,43):
            return 'M'
        else:
            return 'L'
        
