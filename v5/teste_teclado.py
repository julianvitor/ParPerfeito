a = 2
for b in range(1000000):
    c = b**2
    print(c)
    with open('readme.txt', 'a') as f:
        f.write('\n'.join(str(c)))
    if c > 1000000000000000000000000000000000000000000000000000000000000000:
        break
    else:
        pass