import sys

switch = {'add':'+','sub':'-','div':'/','mul':'*','pow':'**'}
try:
	sys.argv[1],sys.argv[2]=sys.argv[2],switch[sys.argv[1]]
	print(eval(''.join(sys.argv[1::])))
#eval()-evaluate the expression
#join()-connect list's elements into string

except SyntaxError:
    print("Programme can't run it")
except NameError:
    print("Programme can't run it")
except ZeroDivisionError:
    print("Programme can't run it")
except KeyError:
    print("Programme can't run it")
except IndexError:
    print("Programme can't run it")