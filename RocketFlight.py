import matplotlib.pyplot as plt

'''
LoisLab

Acceleration data from model rocket flight,
September 15, 2019. South Berwick, Maine.
'''
#converts what sensor says to meters per seccond ^2
def to_mss(x,limit):
	return limit*(float(x)/2**15)*9.8

f = open('new_accel.txt','r')

_t,_a=[],[]
t=0
v=0
d=0
_d=[]
_v=[]
for n in range(2000):
  vals = f.readline().split('|')  
  dt=float(vals[0])
  t+=dt
  d+=v*dt
  r=float(vals[1])
  a=to_mss(r,200)
  print (t,a)
  _t.append(t)
  v+=a*dt
  _v.append(v)
  _a.append(a)
  _d.append(d)
plt.scatter(_t,_a,marker='+')    
plt.savefig('accel')
plt.clf()
plt.scatter(_t,_d)
plt.savefig('distance')
plt.clf()
plt.scatter(_t,_v)
plt.savefig('velocity')

