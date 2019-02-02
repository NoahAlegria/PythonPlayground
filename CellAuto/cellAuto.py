import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.collections as coll
import numpy as np
from matplotlib import colors 

data = np.zeros((40,40))
data[0,20] = 1
ax = plt.subplot(1,1,1, aspect = 'equal')

#Rule 57
def makeRules():
	for i in range(1,40):
		for j in range(0,39):
			if data[i-1, j-1] == 1 and data[i-1, j] == 1 and data[i-1, j+1] == 1:
				data[i,j] = 0
			if data[i-1, j-1] == 1 and data[i-1, j] == 1 and data[i-1, j+1] == 0:
				data[i,j] = 0
			if data[i-1, j-1] == 1 and data[i-1, j] == 0 and data[i-1, j+1] == 1:
				data[i,j] = 1
			if data[i-1, j-1] == 1 and data[i-1, j] == 0 and data[i-1, j+1] == 0:
				data[i,j] = 1
			if data[i-1, j-1] == 0 and data[i-1, j] == 1 and data[i-1, j+1] == 1:
				data[i,j] = 1
			if data[i-1, j-1] == 0 and data[i-1, j] == 1 and data[i-1, j+1] == 0:
				data[i,j] = 0
			if data[i-1, j-1] == 0 and data[i-1, j] == 0 and data[i-1, j+1] == 1:
				data[i,j] = 0
			if data[i-1, j-1] == 0 and data[i-1, j] == 0 and data[i-1, j+1] == 0:
				data[i,j] = 1

def addPatches():
	for i in range(1,40):
		for j in range(0,39):
			if data[i,j] == 0:
				patch = patches.Rectangle((j,i), 1, 1, fill = False)
				ax.add_patch(patch)
			if data[i,j] == 1:
				patch = patches.Rectangle((j,i), 1, 1, fill = True)
				ax.add_patch(patch)
			
def main():
	ruleNum = input("What rule would you like to generate? (1-256)\n")
	makeRules()
	addPatches()
	plt.axis([40,0,40,0])
	plt.show()


if __name__ == "__main__":
	main()
