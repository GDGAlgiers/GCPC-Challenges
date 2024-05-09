def sol(net):
    def serie(*args):
        return sum(args)
    def parallel(*args):
        return 1 / sum((0 if (cur == 0) else (1/cur)) for cur in args)
    def burned(*args):
        return 0

    return eval(net.replace('(', 'serie(').replace('[', 'parallel(').replace('{', 'burned(').replace(']', ')').replace('}', ')'))

# result
resistances = input("")
print("{:.2f}".format(sol(resistances)))