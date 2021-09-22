def check_initial_symbols(string_main,list_index):
#check_initial_symbols()-check string existence and checks string for sign existence before digits

	if not string_main:
		return (False,None)
	if list(string_main)[list_index].isdigit() and len(string_main)>1 :
#isdigit()-check elements for digits
#len()-return string length

		if '+' in list(string_main)[:list_index:] or '-' in list(string_main)[:list_index:]:
			return (False,None)
		else:
			return check_list(list(string_main),0,0,len(string_main)-1,0)
	else:
		return check_initial_symbols(string_main,
		list_index+1) if list_index!=len(string_main)-1 else check_list(list(string_main),0,0,len(string_main)-1,0)
#it searching initial digit and start next function if there're no digits
#then it searching '+' nad '-' before this digit
#ternary operator checking why the searching was over 

def check_list(list_main,list_index,repeat_sign,max_length,space_index):
#check_list()-check list for all SPACE elements and non arithmetic symbols and for signs after equation

	if list_main[list_index]==' ' or list_main[list_index]=='	':
		space_index=space_index+1
	if list_main[list_index] not in" 1234567890+-	"or list_index==max_length or check_repeated_signs(list_main,
	list_index,repeat_sign):
		return print_result(list_index,max_length,list_main,space_index)
	else:
		return check_list(list_main,list_index+1,list_main[list_index],max_length,space_index)

def check_repeated_signs(list_main,list_index,repeat_sign):
#check_repeated_signs()-check list for repeating '+' and '-'

	if list_main[list_index]==' ' or list_main[list_index]=='	':
		return check_repeated_signs(list_main,list_index+1,repeat_sign)
	return True if list_main[list_index] in "+-" and repeat_sign in "+-" else False

def print_result(list_index,max_length,list_main,space_index):
#print_result()-return result for output

	if list_index!=max_length or space_index==list_index+1 or list_main[list_index] not in " 1234567890	":
		return (False,None)
	else:
		return (True,eval(''.join(list_main[0::])))
#eval()-evaluate the expression
#join()-connect list's elements into string

string_main = input("User input: ")
print("Result: ",check_initial_symbols(string_main,0))