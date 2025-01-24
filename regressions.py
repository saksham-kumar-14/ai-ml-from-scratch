import numpy as np
import sys
import math

def linear_regression(x, y):
	m, n = x.shape  # m -> elements, also length of y, n -> features provided
	w = np.zeros(n)
	b = 0

	all_x_means = []
	x_mean = 0
	y_mean = 0

	for i in range(n):
		y_mean = 0
		x_mean = 0
		for j in range(m):
			x_mean += x[j][i]
			y_mean += y[j]
		x_mean = x_mean/m
		y_mean = y_mean/m

		num = 0
		den = 0
		for j in range(m):
			num += (x[j][i] - x_mean)*(y[j] - y_mean)
			den += (x[j][i] - x_mean)**2

		if den!=0:
			w[i] = num/den
		else:
			w[i] = 2**31

		all_x_means.append(x_mean)

	b = y_mean - float(np.dot(w, all_x_means))

	return [w, b]


def gradient_descent(x, y):
	m, n = x.shape  # m -> elements, also length of y, n -> features provided
	w = np.zeros(n)
	b = 0

	learning_rate = 0.01
	iterations = 100000

	while iterations:
		db = 0
		for j in range(m):
			db += float(np.dot(w,x[j])) + b - y[j]
		db *= (learning_rate/m)

		for i in range(n):
			dw = 0
			for j in range(m):
				dw += (x[j][i]*w[i] + b - y[j])*x[j][i]
			dw *= (learning_rate/m)

			w[i] -= dw

		b -= db

		iterations -= 1

	return [w, b]


def sigmoid(x):
	return 1/(1+math.e**(-x))


def logistic_regression(x, y, w, b):
	m, n = x.shape  # m -> elements, also length of y, n -> features provided
	total_cost = np.zeros(n)

	for i in range(n):
		t = 0
		for j in range(m):
			t += -1*y[j]*math.log(sigmoid(w[i]*x[j][i] + b)) - (1-y[j])*math.log(sigmoid(1 - ( w[i]*x[j][i] + b ) ))
		t/=m
		total_cost[i] = t


	return total_cost


def k_nearest_nbd():
	pass


if __name__ == '__main__':
	x = np.array([[0.2],[0.1],[0.05], [0.025]])
	y = np.array([44.95, 29.25, 15.9, 6.5])

	print(linear_regression(x, y))
	print(gradient_descent(x, y))

	#[w,b] = gradient_descent(x, y)
	#print(logistic_regression(x, y, w, b))
