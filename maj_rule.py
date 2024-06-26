import matplotlib.pyplot as plt
import numpy as np

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

N, D, T = 256, 16, 100


Field = []

# Random filling
# for i in range(N):
    # Field.append(np.random.randint(2, size = N))

# Chess coloring
Field = []
for i in range(N):
    if (i % 2):
        Field.append([0, 1] * (N//2))
    else:
        Field.append([1, 0] * (N//2))

# Adding defect
for i in range(D):
    for j in range(D):
        if i != 0 and j != 0:
            Field[D * i][D * j] = 0
            Field[D*i - 1][D * j] = 0
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