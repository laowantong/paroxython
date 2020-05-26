parents, babies = (1, 1)
while babies < 100:
    print("This generation has {} babies".format(babies))
    parents, babies = (babies, parents + babies)
