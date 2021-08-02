import sys
a = sys.argv[1]
a_int = int(sys.argv[1])
b_list = sys.argv[2:]
b_str = sys.argv[2]
b_eval = eval(sys.argv[2])
print a, type(a)
print a_int, type(a_int)
print b_list, type(b_list)
print b_str, type(b_str)
print b_eval, type(b_eval)
print b_list[0], type(b_list[0])