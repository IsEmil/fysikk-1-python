# Author : Emil Keserovic
# Date Created : 6 December 2024 - 14:00 GMT+1
# Programming Name: Simulering ved varierende akselerasjon

# Vi importerer hele "pylab" biblioteket
from pylab import *

# Start betingelser
v = 8.0
s = 0
t = 0

# Tidssteg
dt = 0.01 # Forteller hvor langt inn i framtiden programmet regner om gangen

#Tyngdeakselerasjonen: 9.81 m/s^2
# Funksjonen for akselerasjonen konstant
def a(v):
    return -9.81

# Lister vi lagrer verdiene i underveis
sliste = [s] # Nå settes starverdiene inn i lister
vliste = [v]
tliste = [t]
aliste = [a(v)] # Vi bruker a(v) til å finne startverdien for

# Simulasjonen
while t<2:
    v=v+a(v)*dt # Vi regner ut den nye farten med formel A
    s=s+v*dt # Vi regner ut den nye farten med formel B
    t=t+dt
    
    sliste.append(s) # Den nye s-verdien legges til i sliste
    vliste.append(v) # Den nye v-verdien legges til i vliste
    tliste.append(t) # Den nye t-verdien leges til i tliste
    aliste.append(a(v)) # Funksjonen a(v) finner den nye akselerasjonen, og 

# Tegning av graf    
print("Posisjon: ", s)
#plot(tliste, sliste) # Posisjon som funksjon av tiden
#title("Stein posisjonen som funksjon av tiden")
#xlabel("$Tid$ / s")
#ylabel("$Posisjon$ / m")
#grid() # Legger på et rutenett
#show() # Sørger for at neste graf tegnes i et nytt vindu

#plot(tliste, vliste) # Fart som funksjon av tiden
#title("Fart som funksjon av tiden")
#xlabel("$Tid$ / s")
#ylabel("$Fart$ / (m/s)")
#grid() # Legger på et rutenett
#show() # Sørger for at neste graf tegnes i et nytt vindu