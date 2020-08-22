//#include<bits/stdc++.h>
#include<algorithm>
#include<assert.h>
#include<bitset>
#include<deque>
#include<iomanip>
#include<iostream>
#include<list>
#include<map>
#include<math.h>
#include<random>
#include<set>
#include<sstream>
#include<string>
#include<unordered_map>
#include<unordered_set>
#include<vector>
using namespace std;
typedef long long llong;
#define perr(begin,end) for(auto x=begin; x!=end; ++x) cerr<<*x<<" "; cerr<<endl
#define seq(i,lo,hi) for(llong i=lo;i<=hi;++i)
#define rev(i,lo,hi) for(llong i=hi;i>=lo;--i)
void fast() { ios_base::sync_with_stdio(false); cin.tie(NULL); }
void precision(int n) { cout.precision(n); cout.setf(ios_base::fixed, ios_base::floatfield); }
/*
 fast() precision(n)
 seq(i64,lo,hi) rev(i64,lo,hi)
 llong perr(begin,end)
*/
llong tcid=1, tcmax=1, mtc=0;
int mloop(llong tcid) {
 
}
int main(){
 // mtc=1;
 if(mtc) cin >> tcmax;
 while(tcid<=tcmax) {
  mloop(tcid);
  tcid++;
 }
}
