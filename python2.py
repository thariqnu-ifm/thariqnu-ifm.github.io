from __future__ import print_function
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
def fast(): SLOW=False
def compute(val, func): return func(val)
def seq(lo,hi,step=1): 
 return range(lo,hi+1,step)
def sround(val,nd):
 return '{0:.{1}f}'.format(val,nd)
def ceil(a,b):
 ans=a//b
 if a%b!=0: ans+=1
 return ans
def e1e(d,e): return d*(10**e)
mod=e1e(1,9)+7
class memoi(dict):
 def __init__(self,f):
  self.f=f
 def __call__(self,*args):
  return self[args]
 def __missing__(self,key):
  ans=self[key]=self.f(*key)
  return ans
class arrays(list):
 def __init__(self,defval,*sizes):
  self.sizes=sizes
  self.dimension=len(sizes)
  self.pm=pm=list(sizes)
  pm.append(1)
  for ii in reversed(range(self.dimension)): pm[ii]*=pm[ii+1]
  list.__init__(self,itertools.repeat(defval,pm[0]))
 def ___i1d___(self,ixs):
  if not isinstance(ixs,tuple): return ixs
  if len(ixs)!=self.dimension: raise LookupError('Dimension must be {}.'.format(self.dimension))
  ans=0
  for ii in range(self.dimension):
   ix=ixs[ii]
   if ix>=self.sizes[ii]:
    raise IndexError('Index[{}]={} >= Len[{}]={}.'.format(ii,ix,ii,self.sizes[ii]))
   ans+=ix*self.pm[ii+1]
  return ans
 def __getitem__(self,ixs):
  ixs=self.___i1d___(ixs)
  return list.__getitem__(self,ixs)
 def __setitem__(self,ixs,val):
  ixs=self.___i1d___(ixs)
  list.__setitem__(self,ixs,val)
 def jagged(self,dim0,ofs):
  if dim0+1==self.dimension: return self[ofs:ofs+self.sizes[dim0]]
  ans=[]
  for ii in range(self.sizes[dim0]):
   ans.append(self.jagged(dim0+1,ofs))
   ofs+=self.pm[dim0+1]
  return ans
 def __str__(self):
  return str(self.jagged(0,0))
def perr(*args,**kwargs): 
 if SLOW:
  print(*args,file=sys.stderr,**kwargs)
"""
e1e(d,e) mod arrays(defv,*sz)
ceil(a,b) sround(val,nd) true false null @memoi
perr(print) seq() compute(v,f) fast()
"""
