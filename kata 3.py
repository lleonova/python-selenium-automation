def abbrevName(name):
    #code away!

    return(f'{name[0].upper()}.{name[name.index(" ") + 1].upper()}')

print(abbrevName('Patrick Feenan'))