import matplotlib.pyplot as plt
import numpy as np
import random
a=random.uniform(-3,3)#random產生一個fixed constant number
x=np.arange(-10,10,0.0001)

def f(x):
    return 1/(1+np.exp(-x))  

y=f(a+x)*f(a-x)
dy=(np.exp(-x-a)-np.exp(x-a))/(pow((np.exp(x-a)+1),2)*pow((np.exp(-x-a)+1),2))
ans=np.argmax(y)
probability=np.exp(f(x[ans]))/(1+np.exp(f(x[ans])))
logoddsratio=np.log(probability/(1-probability))

plt.subplot(2, 1, 1) 
plt.plot(x,y,label='f(a)')
plt.grid()
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(x,dy,label='df(a)/da')
plt.grid()
plt.legend()
print(ans)#在第ans個 有dy=0的極端值
print(x[ans])#最大值在x[ans]的地方 約=0 => 要set b to zero
print(probability)#0.6224593312004854
print(logoddsratio)#0.49999999999417366
plt.show()
