import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline


# Assignment 1
x=np.arange(1,8) # Days of d week
y=[160,150,140,145,175,165,180]
plt.plot(x,y)

# Assignment 2
days=np.arange(1,8) # Days of d week
sales_1=[160,150,140,145,175,165,180]
sales_2=[70,90,160,150,140,145,175]
plt.plot(days,sales_1)
plt.plot(days,sales_2)