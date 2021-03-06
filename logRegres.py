#logistic回归梯度上升优化算法

from numpy import *
def loadDataSet():
	dataMat = []
	labelMat = []
	fr = open('./data/testSet.txt')
	for line in fr.readlines():
		lineArr = line.strip().split()
		dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat,labelMat

def sigmoid(inX):
	return 1.0/(1+exp(-inX))


def gradAscent(dataMatIn,classLabels):
	#print("dataMatIn",dataMatIn)
	dataMatrix = mat(dataMatIn)
	#print("dataMatrix",dataMatrix)
	print("classLabels",classLabels)
	labelMat = mat(classLabels).transpose()
	print("mat(classLabels)",mat(classLabels))
	print("labelMat",labelMat)
	m,n = shape(dataMatrix)
	alphpa = 0.001
	maxCycles = 500
	weights = ones((n,1))
	for k in range(maxCycles):
		h = sigmoid(dataMatrix*weights)
		error = (labelMat-h)
		weights = weights+alphpa*dataMatrix.transpose()*error
	return weights

def stocGradAscent(dataMatrix,classLabels,numIter=150):
	m,n = shape(dataMatrix)
	weights = ones(n)
	for j in range(numIter):
		dataIndex = list(range(m))
		for i in range(m):
			alpha = 4/(1.0+i+j)+0.01
			randIndex = int(random.uniform(0,len(dataIndex)))
			h = sigmoid(sum(dataMatrix[randIndex]*weights))
			error = classLabels[randIndex]-h
			weights = weights + alpha*error*dataMatrix[randIndex]
			del(dataIndex[randIndex])
	return weights

def plotBestFit(weights):
	import matplotlib.pyplot as plt
	plt.switch_backend('agg')
	dataMat,labelMat = loadDataSet()
	dataArr = array(dataMat)
	n = shape(dataArr)[0]
	xcord1 = []
	ycord1 = []
	xcord2 = []
	ycord2 = []
	for i in range(n):
		if int(labelMat[i])==1:
			xcord1.append(dataArr[i,1])
			ycord1.append(dataArr[i,2])
		else:
			xcord2.append(dataArr[i,1])
			ycord2.append(dataArr[i,2])
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
	ax.scatter(xcord2,ycord2,s=30,c='green')
	x = arange(-3.0,3.0,0.1)
	y = (-weights[0]-weights[1]*x)/weights[2]
	print(x)
	print("==================")
	print(y)
	ax.plot(x,y)
	plt.xlabel('X1')
	plt.ylabel('X2')
	plt.savefig('test.jpg')
if __name__=='__main__':
	dataArr,labelMat = loadDataSet()
	#weights = gradAscent(dataArr,labelMat)
	weights = stocGradAscent(array(dataArr),labelMat)
	#print(weights.getA())
	#plotBestFit(weights.getA())
	plotBestFit(weights)
