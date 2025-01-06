# Author : Ole Magnus Bukholm 
# Modifided by : Emil Keserovic
# Date Created : 6 December 2024 - 14:00 GMT+1
# Programming Name: Simulering ved varierende akselerasjon

# Vi importerer hele "pylab" biblioteket
from pylab import *

# Start betingelser
v = 0
s = 0
t = 0

# Konstanter
k=0.32
m=79
g=9.81
G=m*g

# Lager en funksjon for akselerasjon
def a(v):
    return (G-k*v**2)/m # Dobbelt gangetegn betyr å opphøye

# Tidssteg
dt=0.01

# Lister vi lagrer verdiene i underveis:
sliste=[s] 
vliste=[v]
tliste=[t]
aliste=[a(v)]

# Simulasjonen
while t<10: # Simulasjonen kjører til t blir 10 sekunder
    v=v+a(v)*dt # Vi regner ut den nye farten med formel A fra OneNote
    s=s+v*dt # Vi regner ut den nye farten med formel B fra Onenote
    t=t+dt
    
    sliste.append(s) # Den nye s-verdien legges til i sliste
    vliste.append(v) # Den nye v-verdien legges til i vliste
    tliste.append(t) # Den nye t-verdien leges til i tliste
    aliste.append(a(v)) # Funksjonen a(v) finner den nye akselerasjonen, og vi legger den inn i alista

# Tegning av graf    
plot(tliste, sliste) # Posisjon som funksjon av tiden
title("Posisjonen som funksjon av tiden")
xlabel("$Tid$ / s")
ylabel("$Posisjon$ / m")
grid() # Legger på et rutenett
show() # Sørger for at neste graf tegnes i et nytt vindu

# Tegning av graf    
plot(tliste, vliste) # Posisjon som funksjon av tiden
title("Farten som funksjon av tiden")
xlabel("$Tid$ / s")
ylabel("$Fart$ / m/s")
grid() # Legger på et rutenett
show() # Sørger for at neste graf tegnes i et nytt vindu