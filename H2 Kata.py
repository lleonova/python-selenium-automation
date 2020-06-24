# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make 'Past' function which returns time converted to milliseconds.

def past(h, m, s):
     return( (h * 60 * 60 + m * 60 + s ) * 1000)