from typing import List, Dict

def solve(m: int, n: int, clients: List[Dict[str, int]]) -> List[Dict[str, str]]:
    horses_next_free_time = [0] * m #all horses are free
    horses_current_client_priority = [None] * m #no horse is taken
    res = []
    for client in clients:
        if horses_current_client_priority[client['horse']] is None:
            start = max(horses_next_free_time[client["horse"]], client["arrival"])
        #check if threre is a client that has a higher priority 
        end = start + client["duration"]
        res.append({
            "number": client["number"],
            "start": start,
            "end": end
        })

        horses_next_free_time[client["horse"]] = end
    
    res.sort(key=lambda x: x["start"])
    return res

m = int(input())
n = int(input())

clients: List[Dict[str, int]] = []

for i in range(n):
    temp = input().split(' ')
    clients.append({
        'number': int(temp[0]),
        'priority': int(temp[1]),
        'horse': int(temp[2]),
        'arrival': int(temp[3]),
        'duration': int(temp[4])
    })

res = solve(m, n, clients)
for r in res:
    print(r["number"], r["start"], r["end"])
