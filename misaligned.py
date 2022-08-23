# Rather than functions improve it using decorators

class colors:
    def __init__(self):
        self.major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
        self.minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
        self.formatted_string = []
        
    def print_color_map(self):
        for i, major in enumerate(major_colors):
            for j, minor in enumerate(minor_colors):
                temp = i*5+j
                self.formatted_string.append(self.formatter(temp, major, minor))
        return len(major_colors) * len(minor_colors), self.formatted_string
    
    def formatter(self, idx, Major, Minor):
        formatted_string = f'{idx}|{Major}|{Minor}'
        return formatted_string
    
    def print_on_console(self, formatted_text_arr):

#result = print_color_map()
#assert(result == 25)
#print("All is well (maybe!)\n")
