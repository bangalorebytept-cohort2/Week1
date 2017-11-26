#!/usr/bin/env python3

# def function_name(arguments):
#	function_statements


# Function arguments can be multiple arguments, 
# Function returning multiple arguments
def printmessage(str, str1, str2):
	return(str, str1, str2)


#Function handling variable number of arguments
def vararguments(*args, **kwargs):
	
	print(type(args), type(kwargs))


	print("Length of the arguments ", len(args))
	for i in range(0,len(args)):
		print(args[i])
	

	for i in range(0,len(kwargs)):
		print(kwargs.items())
		print(kwargs.keys(), kwargs.values())


def posarguments(x,y):
	print(x,y)

def defarguments(x=0):
	print(x)


def returnfunction(f):
	return(f)
	
#s, s1, s2 = printmessage("hello world\n","string 1\n", "string 2\n")
#print(s,s1,s2)

#d = {'name':'Byte Academy', 'address':'Domlur'}

#vararguments(1,3,4,5,d)
#vararguments(100,200)

#posarguments(1,2)
#posarguments(y=2,x=1)


#defarguments()
#defarguments(10)

f = defarguments
f1 = returnfunction(f)
f1(100)


