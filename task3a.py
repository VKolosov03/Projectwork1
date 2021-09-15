def task1(list1,index,repeater,maxlen):
#list1-string turned into list,repeater index for repeating non numbers,maxlen-string's length
	str2 = "1234567890+-"
	return task3(index,maxlen,list1) if list1[index] not in str2 or index==maxlen or task2(list1[index],repeater)==1 else task1(list1,index+1,list1[index],maxlen)
#task1 function was created for searching repeating non numbers and alphavite symbols into list.It uses ternary recursion
def task2(curnumb,repeater):
#curnumb-current list's element
	str3 = "+-"
	return 1 if curnumb in str3 and repeater in str3 else 0
#task2 function was made for checking repeating of '+' and '-'.It uses ternary operator
def task3(index,maxlen,list1):
	return task4('True',eval(''.join(list1[0::]))) if index==maxlen else task4('False',None)
#task3 function collects results and due to ternary operator chooses the answer
def task4(boolf,numbf):
#boolf-result from task3:is it true or faulse, numbf-final digit after all opertions
	print('Result: (',boolf,',',numbf,')')
	pass
#task4 print the final result and stops by function pass
strmain = input("User input: ")
#user inputs main string for our programme
task1(list(strmain),0,0,len(strmain)-1)
#list()-turns string into list, len()-outputs string's length