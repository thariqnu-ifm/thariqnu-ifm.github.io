import sys
import collections
true=True
false=False
null=None
def perr(*args,**kwargs): print(*args,file=sys.stderr,**kwargs)
def line():
	ln=sys.stdin.readline().strip()
#	perr(ln)
	if ln=='': sys.exit()
	return ln
def split(ln=None): return (ln or line()).split()
def parse(*parsers): return list(map((lambda p,w:p(w)),parsers,split()))
def nums(o=None):
	if o is not None and isinstance(o, str): o=split(o)
	return list(map(int, o or split()))
def num(): return int(line())
"""
perr(print) true false null
num() nums(?) parse(..) split(?) line()
"""
# 
# 11799 
# 
for tc in range(num()):
	aa=nums()
	aa.pop(0)
	print(max(aa))
#
#
#
#
#
#
