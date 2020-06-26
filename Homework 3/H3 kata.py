# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#
# The output should be two capital letters with a dot separating them.
#
# It should look like this:
#
# Sam Harris => S.H
#
# Patrick Feeney => P.F


def abbrevName(name):

    return(f'{name[0].upper()}.{name[name.index(" ") + 1].upper()}')

print(abbrevName('Patrick Feenan'))