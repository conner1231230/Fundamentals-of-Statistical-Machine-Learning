import math
import numpy as np
from scipy.stats import norm
import random
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
sigma1= 2
sigma2= 1
rho= 0.5
siq1= sigma1**2;
siq2= sigma2**2;
lamba1= siq1
lamba2= siq2

if ( rho!= 0 ) :
  lamba1= 0.5*(  siq1 + siq2 + math.sqrt( (siq1+siq2)**2 - 4*siq1*siq2*(1-rho**2) )  )
  lamba2= 0.5*(  siq1 + siq2 - math.sqrt( (siq1+siq2)**2 - 4*siq1*siq2*(1-rho**2) )  )



ellipseMajor=  2 * math.log(2) * math.sqrt(lamba1)
ellipseMinor=  2 * math.log(2) * math.sqrt(lamba2)
ellipseAngleRad= math.atan(  sigma1 * sigma2 * rho / lamba1   )
ellipseAngle= ellipseAngleRad  * 180 / math.pi

#計算傾斜橢圓的座標
c=math.sqrt(math.pow(ellipseMajor,2)-math.pow(ellipseMinor,2))
c1=(c*math.cos(ellipseAngleRad),c*math.sin(ellipseAngleRad))
c2=(-c*math.cos(ellipseAngleRad),-c*math.sin(ellipseAngleRad))

n= 10000
X=np.arange(n,dtype='f')
Y=np.arange(n,dtype='f')
count=0

for i in range(n):
    z1 = random.gauss(mu=0,sigma=1)
    z2 = random.gauss(mu=0,sigma=1)
    xraw= sigma1*z1
    yraw= sigma2*(rho*z1 + z2*math.sqrt( 1 - rho*rho))
    X[i]= xraw
    Y[i]= yraw
    #判斷(X[i],Y[i])此點是否在橢圓內
    point=(xraw,yraw)
    if math.dist(c1,point)+math.dist(c2,point)<2*ellipseMajor:
        count+=1
print(count/n)#在橢圓內的dot個數/dot總數=在橢圓內的dot個數百分比


#set size ratio -1;

# Note: gnuplot ellipse size takes values 2a,2b.   for ellipse  x�/a� + y�/b� < 1
#set object 1 ellipse center 0,0  size 2*ellipseMajor,2*ellipseMinor  angle ellipseAngle  front fillstyle empty border -1 lw 2

#plot [-5:5][-5:5] X using (X[$1]):(Y[$1]) with dots notitle
fig = plt.figure(0)
ax = fig.add_subplot(111, aspect='equal')
plt.scatter(X,Y,s=0.5,marker="o")
e = Ellipse(xy = (0,0), width = ellipseMajor * 2, height = ellipseMinor * 2, angle = ellipseAngle)
ax.add_artist(e)
e.set_edgecolor("black")
e.set_facecolor("none")
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.show()
