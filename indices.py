import numpy as np

score = np.array([103, 1502, 6230, 3, 1682, 5241, 4532])

scoreSorted = score.copy();
scoreSorted.sort();

for i in range(score.size):
	print("index of value ", score[i], " in sorted array: ", np.where(scoreSorted == score[i])[0]);