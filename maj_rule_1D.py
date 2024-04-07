import matplotlib.pyplot as plt
import numpy as np

N, T = 39, 10

Field = []
for i in range(N):
    if not N % 2:
        Field.append([1, 0] * (N // 2))
    else:
        Field.append([1, 0] * (N // 2) + [1])

for i in range(N // 3):
    for j in range(len(Field)):    
        Field[j][(3*i + 1) % len(Field)] = 0

print(*Field, sep = "\n")

def SumF (Field):
    s = 0
    for i in range(len(Field)):
        for j in range(len(Field)):
            s += Field[i][j]
    return s
            
def Sum (Field, i, j):
    h = [-1, 0, 1]
    s = 0 
    for k in h:
        for l in h:
            s += Field[(i + k) % len(Field)][(j + l) % len(Field)] 
    return s

print(SumF(Field) / N**2)
print('\n')

fig, ax = plt.subplots()
plt.imshow(Field)
# fig.savefig("defect1_path_" + "step_" + "init" +".png", format = 'png', dpi = 300)

Value = [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]

dim = len(Field)

for k in range(T):
    tmp_Field = []
    for i in range(dim):
        tmp_row = []
        for j in range(dim):
            tmp_row.append(Value[Sum(Field, i, j)])
        tmp_Field.append(tmp_row)
    Field = list(tmp_Field)
    
    fig, ax = plt.subplots()
    plt.imshow(Field)
    # fig.savefig("defect1_path_" + "step_" + str(k) +".png", format = 'png', dpi = 300)
    
    print(SumF(Field) / N**2)