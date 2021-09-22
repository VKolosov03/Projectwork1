import sys

try:
    print(eval(''.join(sys.argv[1::])))
#eval()-evaluate the expression
#join()-connect list's elements into string

except SyntaxError:
    print("Programme can't run it")
except NameError:
    print("Programme can't run it")
except ZeroDivisionError:
    print("Programme can't run it")