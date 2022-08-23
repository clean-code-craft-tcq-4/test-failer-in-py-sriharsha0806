# Open-closed principle
class tshirtsize:
    @staticmethod
    def size(cms):
        pass

class Small(tshirtsize):
    @staticmethod
    def size(cms):
        if cms < 38:
            return 'S'
        
        
class Medium(tshirtsize):
    @staticmethod
    def size(cms):
        if cms in range(38,43):
            return 'M'
        
class Large(tshirtsize):
    @staticmethod
    def size(cms):
        if cms >= 43:
            return 'L'
     
sizes = [Small, Medium, Large]

class tshirts:    
    @staticmethod
    def categorize(cms):
        for size in sizes:
            if size.size(cms):
                return size.size(cms)
