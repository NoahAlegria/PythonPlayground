import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.collections as coll
import numpy as np
from matplotlib import colors 

data = np.zeros((40,40))
data[0,20] = 1
ax = plt.subplot(1,1,1, aspect = 'equal')

def applyRules(modNum):
	for i in range(1,39):
		for j in range(0,39):
			temp = (abs(data[i-1,j-1] + data[i-1,j] + data[i-1,j+1])) % modNum
			data[i,j] = temp	

def addPatches(colorNum):
	for i in range(1,39):
		for j in range(0,39):
			if data[i,j] < colorNum:
				if data[i,j] == 0:
					patch = patches.Rectangle((j,i), 1, 1, color = 'black')
					ax.add_patch(patch)
				if data[i,j] == 1:
					patch = patches.Rectangle((j,i), 1, 1, color = '#39FF14')
					ax.add_patch(patch)
				if data[i,j] == 2:
					patch = patches.Rectangle((j,i), 1, 1, color = 'cyan')
					ax.add_patch(patch)
				if data[i,j] == 3:
					patch = patches.Rectangle((j,i), 1, 1, color = 'magenta')
					ax.add_patch(patch)
				if data[i,j] == 4:
					patch = patches.Rectangle((j,i), 1, 1, color = 'gold')
					ax.add_patch(patch)
				if data[i,j] == 5:
					patch = patches.Rectangle((j,i), 1, 1, color = 'blue')
					ax.add_patch(patch)
				if data[i,j] == 6:
					patch = patches.Rectangle((j,i), 1, 1, color = 'yellow')
					ax.add_patch(patch)
#plt.axis([39,0,33,1])

def main():
	colorNum = input("Enter Amount of Colors to Build With: (1-7)\n")
	modNum = input("Enter Number to be Applied to Rule Set: (Any)\n")
	applyRules(modNum)
	addPatches(colorNum)
	plt.axis([39,0,32,1])
	plt.show()


if __name__ == "__main__":
	main()
	
