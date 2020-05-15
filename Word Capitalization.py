name = input()
if (len(name) > 0 and name[0].islower()):
    print(name[0].upper() + name[1:])
else:
    print(name)