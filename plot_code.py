import numpy as np
import matplotlib.pyplot as plt

# load the columns

bestand = open("oef6_solution.txt", 'r')
bestand.readline()
parameters =  bestand.readline()
parameters = parameters.rstrip('\n')
reduced_m , time_step = parameters.split(' ')
bestand.close()
(t, rx, ry ,vx,vy,e,e_error) = np.loadtxt("oef6_solution.txt", unpack=True,skiprows=3)
# create and save the plot
#plt.figure(figsize=(6,4))
plt.plot(rx, ry)
plt.title(r"Orbit with $\mu$ = {} and h = {}".format(reduced_m,time_step))
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.savefig(r"oef6mu{}h{}orbit2.pdf".format(reduced_m,time_step))
#plt.show()
plt.close()
plt.plot(t,e_error)
plt.title(r"energy error of orbit with $\mu$ = {} and h = {}".format(reduced_m,time_step))
plt.xlabel("t")
plt.ylabel(r"$\frac{\Delta E}{E}$")
plt.yscale("log")
plt.savefig(r"oef6mu{}h{}error2.pdf".format(reduced_m,time_step))
plt.close()
