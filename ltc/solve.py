import ast 

def findL(horses, l, budget):
    res = []
    if not horses : 
        return res
    temp_budget = budget // l
    
    if temp_budget < horses[0] or temp_budget > horses[-1]: return res
    
    if l == 2 : 
        return findTwo(horses, budget)
    
    for i in range(len(horses)):
        if i == 0 or horses[i-1] != horses[i]:
            for sres in findL(horses[i+1:], l-1,budget-horses[i]):
                res.append([horses[i]]+sres)
    return res
    
def findTwo(horses, budget):
    res = []
    l = len(horses)-1
    bi, bs = 0, l
    while bi<bs:
        curr = horses[bi]+horses[bs]
        if curr < budget or bi>0 and horses[bi]==horses[bi-1]  : 
            bi+=1
        elif curr > budget or bs<l and horses[bs]==horses[bs+1]:
            bs-=1
        else:
            res.append([horses[bi],horses[bs]])
            bi+=1
            bs-=1
    return res

if __name__ == "__main__":
    with open("input.text") as f :
        lines = f.readlines()

    results = open("solutions.txt", "w")

    for line in lines:
        horses, budget, l = map(ast.literal_eval,line.replace(", ",",").split())
        horses.sort()
        result = findL(horses, l, budget)
        print(result, file=results)