
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
number_observation=5000

x1=np.random.multivariate_normal([1],[[1]],number_observation)
x0=np.random.multivariate_normal([-1],[[1]],number_observation)

#將其兩個從原本的shape都為(number_observation,1) 轉變成(2*number_observation,1) 疊加的概念
features=np.vstack((x0,x1)).astype(np.float32)
labels=np.hstack((np.zeros(number_observation),np.ones(number_observation)))
y=np.zeros(number_observation)

plt.subplot(3,1,1)
plt.scatter(x1,y,c='g')
plt.scatter(x0,y,c='b')

def sigmoid(x):
    return 1/(1+np.exp(-x))

def logistic_regression(features,target,num_steps,learning_rate,add_intercept=False):

    if add_intercept:
        intercept=np.ones((features.shape[0],1))
        features=np.hstack((intercept,features))
    weights=np.zeros(features.shape[1])

    #開始進行迴圈跑最出最佳參數
    for step in range(num_steps):
        scores=np.dot(features,weights)
        #function套入sigmoid function得1機率值
        predictions=sigmoid(scores)
        #觀看誤差
        output_error_singal=target-predictions
        #gradient
        gradient=np.dot(features.T,output_error_singal)
        weights+=learning_rate*gradient
    return weights

weights=logistic_regression(features,labels,num_steps=3000,learning_rate=5e-5,add_intercept=True)
print('權重:',weights)

def softmaxx0(x,weight):
    return np.exp(weight[0]*x)/(np.exp(weight[0]*x)+np.exp(weight[1]*x))
def softmaxx1(x,weight):
    return np.exp(weight[1]*x)/(np.exp(weight[0]*x)+np.exp(weight[1]*x))

def sigmoidx1(x,weight):
    return 1/(1+np.exp(-(weight[1])*x))
def sigmoidx0(x,weight):
    return 1/(1+np.exp(-(weight[0])*x))
    
sigma = 1
sampleNo = 2000

s = np.random.normal(1, sigma, sampleNo)
b = np.random.normal(-1, sigma, sampleNo)
x = np.linspace(-5,5,2000)

plt.subplot(3,1,2)
plt.hist(s, bins=100)
plt.hist(b, bins=100)

plt.subplot(3,1,3)
plt.plot(x,softmaxx1(x,weights),label='softmax_x1')
plt.plot(x,softmaxx0(x,weights),label='softmax_x0')
plt.legend()
print('sigmoid c1:',sigmoidx1(1,weights))
print('sigmoid c0:',sigmoidx0(1,weights))
print('softmax c1:',softmaxx1(1,weights))
print('softmax c0:',softmaxx0(1,weights))
plt.show()


