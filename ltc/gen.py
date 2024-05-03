import random 
from config import *
from solve import findL


f = open("input.text", "w")
cnt = 0

while cnt < NB_TESTS:
    budget = random.randint(MIN_BUDGET, MAX_BUDGET)
    k = random.randint(MIN_K, MAX_K)
    n = random.randint(MIN_HORSES, MAX_HORSES)
    horses = [ random.randint(MIN_PRICE, MAX_PRICE) for i in range(n)]

    if findL(sorted(horses), k, budget):

        print(horses, budget, k, file=f)
        MAX_HORSES += INCREMENT
        cnt += 1 
        print(cnt, "/ 200")
        print(MAX_HORSES)

