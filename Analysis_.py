import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft



X=[]
Y=[]

with open("DS00011.csv") as f:
    lines=f.readlines()
    for line in lines:
        a=line.split(',')
        X.append(a[0])
        Y.append(a[1])




print(len(X))

t=[float(X[i]) for i in range(16,15303)]
x=[100*float(Y[i]) for i in range(16,15303)]

#print(x[0:10])

#file=open("Mytext.txt","w")
#for i in range(len(x)):
    #file.writelines(str(x[i])+"\n")



f_0=10**5

def coscoef(x,a,N,t):   #Function for cosinus coeffiecients
    A=[]
    Total=0
    delta=t[2]-t[1]
    Time=t[len(t)-1]-t[0]
    for i in range(len(t)):
        Total+=x[i]*delta
    A.append(Total/Time)
    Total=0
    for j in range(1,N+1):
        for i in range(len(t)):
            Total+=x[i]*delta*np.cos(2*np.pi*j*a*t[i])
        A.append(Total*2/Time)
        Total=0
    return A   

def sincoef(x,a,N,t):          #Function for sinus coeffiecients
    A=[]
    Total=0
    delta=t[2]-t[1]
    Time=t[len(t)-1]-t[0]
   
    for j in range(1,N+1):
        Total=0
        for i in range(len(t)):
            Total+=x[i]*delta*np.sin(2*np.pi*j*a*t[i])
        A.append(Total*2/Time)
        
    return A

N=10
COS=coscoef(x,f_0,N,t) 
SIN=sincoef(x,f_0,N,t)

#print(COS)
#print(SIN)
Wave=[COS[0] for i in range(len(t))]
Draw_wave=[]
Draw_wave.append(Wave)



for j in range(1,N+1): 
    for i in range(len(t)):
        Wave[i]+=COS[j]*np.cos(2*np.pi*j*f_0*t[i])+SIN[j-1]*np.sin(2*np.pi*j*f_0*t[i])
        
        
print("DC Voltaj"+str(COS[0]))

#print(max(Wave)-COS[0])
#print(min(Wave)-COS[0])

#for i in range(len(SIN)):
 #   print(SIN[i])


plt.plot(t,x)
plt.plot(t,Wave)
plt.title("N="+str(N)+" Çözümü")
plt.legend(['orjinal','fourier_seri hali'])
plt.xlabel('Zaman (s)')
plt.ylabel('Voltaj (mV)')
plt.show()   

print("Cos values"+str(COS))
print("Sin values"+str(SIN))
file=open("Mytext.txt","w")

Cos_wave=[COS[5]*np.cos(2*np.pi*5*f_0*t[i]) for i in range(len(t))]
Sin_wave=[SIN[4]*np.sin(2*np.pi*5*f_0*t[i]) for i in range(len(t))]

#plt.plot(t,Cos_wave)
#plt.title("N="+str(5)+" Cosinus Dalgası")
#plt.xlabel('Zaman (s)')
#plt.ylabel('Voltaj (mV)')

#plt.show()

#plt.plot(t,Sin_wave)
#plt.title("N="+str(5)+" Sinus Dalgası")
#plt.xlabel('Zaman (s)')
#plt.ylabel('Voltaj (mV)')

#plt.show()

#Extra content for fast fourrier transform. There is more work to be done. 
p=fft(x)
n=len(x)
mag=np.sqrt(p.real**2+p.imag**2)
mag = mag * 2 / n


plt.plot(mag)
plt.show()





