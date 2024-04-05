import numpy as np

# First atom starts at 0
indices = [100, 101]


indices = sorted(indices)

indices = (np.array(indices) + 1)*6

indices2 = []
for i in indices:
    indices2.append(np.arange(i-5, i+1))

indices2 = np.concatenate(indices2)
indices2 = [str(i).zfill(3) for i in indices2]
print(' '.join(indices2))

