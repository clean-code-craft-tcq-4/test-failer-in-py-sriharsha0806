from misaligned import colors
Colors = colors()
res, final = Colors.print_color_map()
assert(res==25)
Colors.print_on_console(final)
