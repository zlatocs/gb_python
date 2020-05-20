def my_fun(a,b,c):
    seq = [a,b,c]
    total = []
    i = 0
    for i in seq:
        i += 1
        maxN = max(seq)
        total.append(maxN)
        seq.remove(maxN)
    print(sum(total))
my_fun(780, 1000, 3400167)