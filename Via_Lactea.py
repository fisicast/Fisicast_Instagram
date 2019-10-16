import matplotlib.pyplot as plt
import numpy as np
import math

def spiral(R0,psi,theta):
	aux=(180.0*(theta+math.pi)*math.tan(psi))/math.pi
	return [R0*math.exp(aux)*math.cos(theta),R0*math.exp(aux)*math.sin(theta)]
	

names=['Scutum','Perseus','Sagittarius','Norma'];

# as curvas vem desse artigo: https://arxiv.org/pdf/1011.4576.pdf

xtab=np.linspace(-0.13*math.pi,2.37*math.pi,100) 
tabScutum=[spiral(2.0,0.003665,theta) for theta in xtab]

xtab=np.linspace(0.85*math.pi,2.85537*math.pi,100)
tabPerseus=[spiral(0.97, 0.217*math.pi/180.0,theta) for theta in xtab]

xtab=np.linspace(1.35*math.pi,3.8*math.pi,100)
tabSagittarius=[spiral(0.9,0.192*math.pi/180.0,theta) for theta in xtab]

xtab=np.linspace(0.3*math.pi,2.75*math.pi,100)
tabNorma=[spiral(1.3,0.22*math.pi/180.0,theta) for theta in xtab]

#olho nu
xtab=np.linspace(0.0*math.pi,2.0*math.pi,100)
naked=[[-0.3+1.2*math.cos(theta),7.94+1.2*math.sin(theta)] for theta in xtab]



fig = plt.figure();
plt.suptitle(r'Via Láctea', fontsize=14,y=0.98)
ax=[]
ax.append(plt.subplot(1,1,1));
ax[0].plot([x[0] for x in tabScutum],[x[1] for x in tabScutum],color='gray', alpha=0.5)

ax[0].plot([x[0] for x in tabPerseus],[x[1] for x in tabPerseus],color='gray', alpha=0.5)

ax[0].plot([x[0] for x in tabSagittarius],[x[1] for x in tabSagittarius],color='gray', alpha=0.5)

ax[0].plot([x[0] for x in tabNorma],[x[1] for x in tabNorma],color='gray', alpha=0.5)


ax[0].plot([x[0] for x in naked],[x[1] for x in naked], linestyle='--', color='red')


ax[0].plot([-1.74,1.846],[-3.2,2.7],color='gray', alpha=0.5)
ax[0].scatter([-0.3],[7.94],s=6,color='red')

ax[0].text(11,15,names[0], rotation=-47,color='gray', alpha=1)
ax[0].text(-10,10.5,names[1], rotation=20,color='gray', alpha=1)
ax[0].text(10,-12,names[2], rotation=20,color='gray', alpha=1)
ax[0].text(-10,15.5,names[3], rotation=15,color='gray', alpha=1)

ax[0].set_xlabel(r'$x$ [kpc]', fontsize=16);
ax[0].set_ylabel(r'$y$ [kpc]', fontsize=16);
ax[0].set_xlim([-17,19]);
ax[0].set_ylim([-16,20]);

fig.tight_layout(pad=2, w_pad=-.3, h_pad=0.1);
fig.savefig('milkyway_plot.png');
plt.close(fig)

