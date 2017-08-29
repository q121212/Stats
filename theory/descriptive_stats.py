#!/usr/bin/python3

# Descriptive statistics
class descriptive:
	def mean(*args):
		return sum(args)/len(args)
	def median(*args):
		if type(args)== (int or float):
			return args
		return args[int(len(args)/2)] if len(args)%2!=0 else (args[int(len(args)/2)-1]+args[int(len(args)/2)])/2
	def diffusion(*args):
		if type(args)== (int or float):
			return 0
		return max(args)-min(args)
	def deviation(*args):
		return [i-descriptive.mean(*args) for i in args]
	def dispersion(*args):
		return descriptive.mean(*[i*i for i in descriptive.deviation(*args)])

if __name__ == '__main__':
	x0=0
	x1=-1
	x2=1,2,3,4,5
	x3=1,2,3,4,5,6

	print(x0, descriptive.mean(x0))
	print(x1, descriptive.mean(x1))
	print(x2, descriptive.mean(*x2))
	print(x0, descriptive.median(x0))
	print(x1, descriptive.median(x1))
	print(x2, descriptive.median(*x2))
	print(x3, descriptive.median(*x3))
	print(x0, descriptive.diffusion(x0))
	print(x1, descriptive.diffusion(x1))
	print(x2, descriptive.diffusion(*x2))
	print(x3, descriptive.diffusion(*x3))
	print(x0, descriptive.deviation(x0))
	print(x1, descriptive.deviation(x1))
	print(x2, descriptive.deviation(*x2))
	print(x3, descriptive.deviation(*x3))
	print(x0, descriptive.dispersion(x0))
	print(x1, descriptive.dispersion(x1))
	print(x2, descriptive.dispersion(*x2))
	print(x3, descriptive.dispersion(*x3))
