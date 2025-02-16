# bieu dien do thi bang danh sach ke voi dictionary
graph = {
        'A':{'Z': 75, 'S': 140, 'T':118},
        'Z':{'O': 71, 'A': 75},
        'T':{'L':111, 'A': 118},
        'O':{'S': 151, 'Z': 71},
        'S':{'A':140, 'O': 151, 'F': 99, 'R': 80},
        'L':{'T': 111, 'M':70},
        'D':{'M': 75, 'C':120} ,
        'M':{'L': 70, 'D': 75},
        'R':{'S': 80, 'P':97, 'C':146},
        'F':{'S': 99, 'B':211},
        'C':{'D':120, 'R':146, 'P':138},
        'P':{'R': 97, 'C': 138, 'B':110},
        'G':{'B': 90},
        'B':{'G': 90, 'B':110, 'F':211, 'U':85},
        'U':{'B':85, 'V':142, 'H':98},
        'N':{'I':87},
        'H':{'U': 98, 'E':86},
        'E':{'H':98},
        'I':{'N': 87, 'V':92},
        'V':{'I': 92, 'U':142}
        }

CUTOFF = 'cutoff'
FAILURE = 'failure'

# moves:luu qua trinh di chuyen
def RecursiveDepthLimitedSearch(graph:dict, dest:str, node:str, moves:list, limit:int):
    moves.append(node)
    if(node == dest):
        return moves
    cutoff_occurred = False
    if(limit == 0):
        return CUTOFF
    
    for childNode in graph[node].keys():
        if(childNode in moves):
            continue
        result = RecursiveDepthLimitedSearch(graph, dest, childNode, moves.copy(), limit-1)
        if(result == CUTOFF):
            cutoff_occurred = True
        elif(result != FAILURE):
            return result

    if(cutoff_occurred):
        return CUTOFF
    else:
        return FAILURE
    
    

def DepthLimitedSearch(graph:dict, start:str, dest:str, limit:int):
    moves = []
    return RecursiveDepthLimitedSearch(graph=graph, dest=dest, node=start, moves=moves, limit=limit)

def InteractiveDeepeningSearch(graph:dict, start:str, dest:str, display_illustrate:bool):
    # dat infinity = 1.000.000.000 de tranh TH bai toan ko co loi giai
    depth = 0
    infinity = 10**9
    if(display_illustrate):
        print("InteractiveDeepeningSearch(graph, start=%s, dest=%s)"%(start, dest))

    for depth in range(0, infinity):
        result = DepthLimitedSearch(graph, start, dest, depth)
        if(display_illustrate):
            print("depth = %d, result = "%(depth), result)
        if(result != CUTOFF and result != FAILURE):
            return result
    return FAILURE




start = input("start point: ")
dest = input("destination: ")
# limit = int(input("limit: "))

# print("=>", DepthLimitedSearch(graph=graph, start=start, dest=dest, limit=limit))

print("=>", InteractiveDeepeningSearch(graph=graph, start=start, dest=dest, display_illustrate=True))

