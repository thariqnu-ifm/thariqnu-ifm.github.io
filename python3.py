import sys
import collections
import math
import functools
import itertools
import bisect
import operator
import heapq
import random
true=True
false=False
null=None
SLOW=True
memoi=functools.lru_cache(None)
tcid=0
tcmax=99999999
def fast(): SLOW=False
def compute(val, func): return func(val)
def seq(lo,hi,step=1): 
 return range(lo,hi+1,step)
def sround(val,nd):
 return f'{val:.{nd}f}'
def ceil(a,b):
 ans=a//b
 if a%b!=0: ans+=1
 return ans
def perr(*args,**kwargs): 
 if SLOW:
  print(*args,file=sys.stderr,**kwargs)
def line():
 ln=sys.stdin.readline().strip()
 #perr(ln)
 if ln=='': sys.exit()
 return ln
def lines(n): return [line() for i in range(n)]
def split(ln=None): return (ln or line()).split()
def num(str=None):
 str=str or line()
 return float(str) if '.' in str else int(str)
def nums(o=None):
 if o is not None:
  if isinstance(o, int): o=lines(o)
  elif isinstance(o, str): o=split(o)
 return list(map(num, o or split()))
"""
ceil(a,b) sround(val,nd) true false null @memoi
num(?) nums(?) split(?) lines(n) line()
perr(print) tcmax seq() compute(v,f) tcid fast()
"""
#{#

#}#
def mainloop(tcid=1):
# {{{
 
# }}}
while tcid<tcmax:
 tcid+=1
 mainloop(tcid)
"""

"""
