import sys
from collections import deque
from bisect import bisect_left,bisect_right
true,false=True,False
null=none=None
slow=__debug__
def arrays(v,sz): return [v]*sz
def perr(*args,**kwargs):
 if slow: print(*args,file=sys.stderr,**kwargs)
def ceil(a,b): return a//b+int(a%b!=0)
def yesno(o): return "YES" if o else "NO"
def strip(): return input().strip()
def split(): return strip().split()
def num(o=None):
 if o is None: o=strip()
 return (float if "." in o else int)(o)
def nums(o=None): 
 return [num(s) for s in (o or split())]
"""
ceil yesno arrays
num nums strip split
"""
def mloop(tcid): #
 def solve(): #
  pass
 pass
tcmax=1
for tcid in range(tcmax): #
 mloop(tcid+1) #
