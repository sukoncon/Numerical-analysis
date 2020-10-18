import numpy as np
import matplotlib.pyplot as plt


# Calucluate AtA(Coeff1) ans Atb(Coeff2)
A = np.mat('1,1;1,-1;1,1')
b = np.mat('2,1,3').T


Coeff1 = np.dot(A.T,A)
Coeff2 = np.dot(A.T,b)


# Compute the result C
C = np.dot(np.linalg.inv(Coeff1),Coeff2)

print(C)
# Visualise the Points and the line

# Visualize the points
x = [1,-1,1]
y = [2,1,3]

fig,ax = plt.subplots()
ax.scatter(x,y)



# Visualise the line 
X = [-2,1,2,3]
Y = [-2,1,2,3]

for i in range(0,len(X)):

    Y[i] = X[i]*C[1,0]+C[0,0]

ax.plot(X,Y)
ax.set_title('Least squares 1')
fig.show()
# To keep the image stay on the screen
plt.pause(200)




