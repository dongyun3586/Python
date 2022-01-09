def p0(x1, x2):
    w1 = 1; w2 = 1; b = -0.5
    y = w1 * x1 + w2 * x2 + b
    return 1 if y>0 else 0

def p1(x1, x2):
    w1 = 1; w2 = 1; b = -1.5
    y = w1 * x1 + w2 * x2 + b
    return 1 if y>0 else 0
    
def p2(x1, x2):
    w1 = 1; w2 = -1; b = -0.5
    y = w1 * x1 + w2 * x2 + b
    return 1 if y>0 else 0
    
for x1, x2 in [(0,0), (0,1), (1,0), (1,1)]:
    print(f'입력: {x1} {x2}', f'출력: {p2(p0(x1, x2), p1(x1, x2))}')