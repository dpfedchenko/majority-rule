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

N = 25

Field = []
for i in range(N):
    Field.append(np.random.randint(2, size = N))

print(SumF(Field)/N**2)
print('\n')

fig, ax = plt.subplots()
plt.imshow(Field)

Value = [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]

T = 100

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
    print(SumF(Field) / N**2)