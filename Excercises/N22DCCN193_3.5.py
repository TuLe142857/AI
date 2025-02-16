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

# khoang cach uoc luong tu diem bat ky den diem B
heuristic = {
        'A':366,
        'B':0,
        'C':160,
        'D':242,
        'E':161,
        'F':178,
        'G':77,
        'H':151,
        'I':226,
        'L':244,
        'M':241,
        'N':234,
        'O':380,
        'P':98,
        'R':193,
        'S':253,
        'T':329,
        'U':80,
        'V':199,
        'Z':374
        }

FAILURE = 'failure'

def GreedyBestFirstSearch(graph:dict, start:str, dest:str):
    pass
