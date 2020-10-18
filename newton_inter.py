import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# input x and y to calculate the coefficients
# return the function f(x)
def coeff(x,y):

	# test if their lengths are equal
	assert len(x)==len(y)
	# number of x N, then the degree is N-1
	N = len(x)
	# initialise the coefficient list
	coeff = []
	coeff.append(y[0])
	# initialise iterate Y values
	iter_y = y
	depth = 1

	# Then iterate to calculate other coefficients
	while depth < N:
		# initialise iterate data
		iterdata = []
		# for each new comming y, renew iterdata
		for j in range(len(iter_y)-1):
			delta_y = iter_y[j+1]-iter_y[j]
			delta_x = x[depth+j]-x[j]
			itercoeff = delta_y/delta_x
			iterdata.append(itercoeff)
			
			# Add the first of the tree to coeff
			if j==0: coeff.append(itercoeff)
			
		# renew iter_y
		iter_y = iterdata
		depth += 1
		
	return coeff
 
 

def predict_y(x,y,x_test):
    c = coeff(x,y)
    y_predict = []
    # Create a function to express newton interpolating
    def f(i):
        preval = 0
        for j in range(len(c)):
            iterval = c[j]
            iterx = x[:j]
            for k in iterx: iterval*=(i-k)
            preval += iterval
        return preval
    for i in x_test:
        y_pre = f(i)
        y_predict.append(y_pre)
    return y_predict

x = [-2,1,3]
y = np.sin(x)
x_test = np.linspace(-2.5,4,500)
y_test = np.sin(x_test)
# Get the coefficients and return a list of predicted y_value
y_predict = predict_y(x,y,x_test)

# plot the original function

fig,ax = plt.subplots()
ax.plot(x_test,y_test,label='Actual fuction')
ax.plot(x_test,y_predict,label='Newton interpolating')
ax.scatter(x,y)
ax.set_title('Newton interpolating')
#ax.legend()
fig.show()

# To keep the image stay on the screen
plt.pause(200)







