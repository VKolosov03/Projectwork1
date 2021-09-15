import sys as console
#importing module sys for using sys.argv and using key word as for explaining using of module
switch = {'add':'+','sub':'-','div':'/','mul':'*','pow':'**'}
#using dictionary for turning phrazes into symbols
console.argv[1],console.argv[2]=console.argv[2],switch[console.argv[1]]
#swap elements
print(eval(''.join(console.argv[1::])))
#join turns list into string, eval calculate string examples