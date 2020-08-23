from __future__ import print_function
from bisect import bisect_right,bisect_left,insort
from collections import deque, defaultdict
import functools
from heapq import *
import itertools
from math import *
import operator
from random import random, randint, randrange, shuffle
import sys
#
magic=1234567
true,false=True,False
null=none=None
reduce=functools.reduce
slow=SLOW=__debug__
sys.setrecursionlimit(11111111)
def testrec(n=1111111):
 if n==0: return 0
 return testrec(n-1)
def getitem(lst,i0,default=None):
 if i0<len(lst) and i0>-1:
  return lst[i0]
 return default
try:
 range=xrange
except:
 pass
def fast():
 global SLOW
 global slow
 slow=SLOW=False
def ceil(a,b):
 c,d=divmod(a,b)
 return c+int(d!=0)
def coal(*args):
 for vv in args:
  if vv is not None:
   return vv
def div(a,b): return float(a)/b
def rrange(*args): return reversed(range(*args))
def seq(lo,hi,step=1): 
 return range(lo,hi+1,step)
def rev(lo,hi,step=1):
 return rrange(lo,hi+1,step)
def sround(val,nd):
 return '{0:.{1}f}'.format(val,nd)
def e1e(d,e): return d*(10**e)
mod=e1e(1,9)+7
try:
 memoiz=functools.lru_cache(None)
except:
 class _memoiz(dict):
  def __init__(self,f):
   self.f=f
  def __call__(self,*args):
   return self[args]
  def __missing__(self,key):
   ans=self[key]=self.f(*key)
   return ans
 memoiz=_memoiz
class _arrays(list):
 def __init__(self,defval,sizes):
  self.sizes=sizes
  self.dimension=len(sizes)
  self.pm=pm=list(sizes)
  pm.append(1)
  for ii in reversed(range(self.dimension)): pm[ii]*=pm[ii+1]
  list.__init__(self,[defval]*pm[0])
 def ___i1d___(self,ixs):
  if SLOW:
   assert len(ixs)==self.dimension, ('Dimension must be {}.'.format(self.dimension))
  ans=0
  for ii in range(self.dimension):
   ix=ixs[ii]
   if SLOW:
    assert ix<self.sizes[ii], ('Index[{}]={} >= Len[{}]={}.'.format(ii,ix,ii,self.sizes[ii]))
   ans+=ix*self.pm[ii+1]
  return ans
 def __getitem__(self,ixs):
  ixs=self.___i1d___(ixs)
  return list.__getitem__(self,ixs)
 def __setitem__(self,ixs,val):
  ixs=self.___i1d___(ixs)
  list.__setitem__(self,ixs,val)
 def _str_(self,dim0=0,ofs=0):
  lft="  "*dim0
  if dim0+1==self.dimension: return lft+str(list.__getitem__(self,slice(ofs,ofs+self.sizes[dim0])))
  ans=[]
  for ii in range(self.sizes[dim0]):
   ans.append(self._str_(dim0+1,ofs))
   ofs+=self.pm[dim0+1]
  ans="{0}[\n{1}\n{0}]".format(lft,",\n".join(ans))
  return ans
 def __str__(self):
  return self._str_()
def arrays(defval,*sizes):
 if len(sizes)==1: return [defval]*sizes[0]
 return _arrays(defval,sizes)
def perr(*args,**kwargs): 
 if SLOW:
  print(*args,file=sys.stderr,**kwargs)
def line():
 ln=sys.stdin.readline().strip()
 #perr(ln)
 if ln=='': sys.exit()
 return ln
def flush(): sys.stdout.flush()
def lines(n): return [line() for i in range(n)]
def split(ln=None): return (ln or line()).split()
def num(str=None):
 str=str or line()
 return float(str) if '.' in str else int(str)
def nums(o=None): return list(map(num, o or split()))
def bfs(fchildren,*root,**kwargs):
  p=deque()
  c=deque()
  q=deque()
  q.append(root)
  while len(q)>0:
   pp=q.popleft()
   if isinstance(pp,tuple):
    dd=fchildren(*pp)
   else:
    dd=fchildren(pp)
   for cc in dd:
    if cc is not None:
     p.append(pp)
     c.append(cc)
     q.append(cc)
  ctop=kwargs.get("ctop")
  if ctop is not None:
   for _ in range(len(p)):
    ctop(c.pop(),p.pop())   
def summod(*args):
 sums=0
 for vv in args:
  if vv is not None:
   sums=(sums+vv)%mod
 return sums
def multmod(*args):
 ans=1
 for vv in args:
  if vv is not None:
   ans=(ans*vv)%mod
 return ans
def subsmod(a,b): return (a+mod-b)%mod
def matmultmod(a,b):
 if a is None:
  return b
 if b is None:
  return a
 ra=len(a)
 ca=len(a[0])
 rb=len(b)
 cb=len(b[0])
 if SLOW:
  assert ca==rb, "matrix incompatible size"
 return [[summod(*map(lambda ii:a[rr][ii]*b[ii][cc],range(ca))) for cc in range(cb)] for rr in range(ra)]
def yesno(b): return "YES" if b else "NO"
class _reverse():
 def __init__(self,vv):
  self.vv=vv
 def __lt__(self,other):
  return self.vv>=other.vv
 def __cmp__(self,other):
  return -cmp(self.vv,other.vv)
def reverse(vv):
 if isinstance(vv,int): return -vv
 return _reverse(vv)
def maxheappush(heap,vv):
 heappush(heap,(reverse(vv),vv))
def maxheappop(heap):
 return heappop(heap)[1]
def reduce(ff,*args,**kwargs):
 ans=kwargs.get("default")
 for bb in args:
  if bb is not None:
   if ans is None: ans=bb
   else: ans=ff(ans,bb,**kwargs)
 return ans
_max,_min=max,min
def max(*args,**kwargs): return reduce(_max,*args,**kwargs)
def min(*args,**kwargs): return reduce(_min,*args,**kwargs)
abcdef="abcdefghijklmnopqrstuvwxyz"
def fastpow(a,n,op,init=None):
 ans=init
 while n>0:
  if n%2==1: ans=op(ans,a)
  n=n//2
  a=op(a,a)
 return ans
class factmod():
 def __init__(self,n):
  self.fac=fac=arrays(1,n)
  for ii in range(2,n):
   fac[ii]=multmod(ii,fac[ii-1])
  self.inv=inv=arrays(
   fastpow(fac[-1],mod-2,multmod,1),
   n)
  for ii in rrange(n-1):
   inv[ii]=multmod(ii+1,inv[ii+1])
 def nck(self,n,k):
  return multmod(self.fac[n],self.inv[k],self.inv[n-k])
def primes(xx):
 aa=[1]*xx
 aa[0]=aa[1]=0
 for ii in range(2,int(sqrt(xx+1))+1):
  if aa[ii]:
   for jj in range(ii*ii,xx,ii):
    aa[jj]=0
 return (ii for ii in range(2,xx) if aa[ii])
def bit(a,i0): return 1&a>>i0
def bitlen(a):
 ans=0
 while a>0:
  ans+=1
  a=a>>1
 return ans
"""
bit(a,i0) bitlen bitcnt
getitem(list,i0,default?)
factmod=nck
fastpow(a,n,op,init_zero?):
 a op a = a^2 .. a^n
maxheappush maxheappop magic
matmultmod yesno abcdef
summod* multmod* subsmod primes
testrec bfs(fchilds:?,root*,ctop=)
coal* e1e(d,e) mod arrays(defv,*sz)
@memoiz=del|scope
div sround(val,nd) true false none null
num(s?) nums(s..?) split(s?) lines(n) line flush
perr(print) seq/rev rrange fast ceil
"""
tcmax=0 #

for tcid in seq(1,tcmax or 9999999): #
 ignore=1 #
