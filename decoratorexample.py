

def myfancydecorator(function):
	def mywrapper(a):
		return function(a + "!!") 
		
	return mywrapper


@myfancydecorator
def inner_function(a):
	print(a)

#inner_function = myfancydecorator(inner_function)

inner_function("Hello decorators")

