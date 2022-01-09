w1 = 0.5; w2 = 0.5; b = -0.5    # AND
w1 = 0.5; w2 = 0.5; b = 0       # OR

def perceptron(x1, x2):
    y = w1 * x1 + w2 * x2 + b
    if y > 0:
        return 1
    else:
        return 0
    
for x1, x2 in [(0,0), (0,1), (1,0), (1,1)]:
    print(f'입력: {x1} {x2}', f'출력: {perceptron(x1, x2)}')
    
    