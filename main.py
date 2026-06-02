import numpy as np
import matplotlib.pyplot as plt
from src.photon_sphere import photon_sphere_radius
from src.shadow_radius import shadow_radius
from src.deflection_angle import weak_deflection

gamma = np.linspace(0,1,100)

# Photon Sphere 
plt.figure(figsize=(8,5))
for lam in [1,2,3]:
    rph = [
        photon_sphere_radius(g,lam)
        for g in gamma
    ]
    plt.plot(
        gamma,
        rph,
        label=f"λ={lam}"
    )
plt.title("Photon Sphere vs Gamma")
plt.xlabel("Gamma")
plt.ylabel("Photon Sphere Radius")
plt.grid()
plt.legend()

plt.savefig(
    "outputs/photon_sphere/photon_vs_gamma.png",
    dpi=300
)

plt.close()

# Shadow Radius Plot
plt.figure(figsize=(8,5))
for lam in [1,2,3]:
    rph = [
        photon_sphere_radius(g,lam)
        for g in gamma
    ]
    rsh = [
        shadow_radius(x)
        for x in rph
    ]
    plt.plot(
        gamma,
        rsh,
        label=f"λ={lam}"
    )
plt.title("Shadow Radius vs Gamma")
plt.xlabel("Gamma")
plt.ylabel("Shadow Radius")
plt.grid()
plt.legend()
plt.savefig(
    "outputs/shadow_radius/shadow_vs_gamma.png",
    dpi=300
)
plt.close()

# Deflection Angle
plt.figure(figsize=(8,5))
for lam in [1,2,3]:
    alpha = [
        weak_deflection(g,lam)
        for g in gamma
    ]
    plt.plot(
        gamma,
        alpha,
        label=f"λ={lam}"
    )
plt.title("Weak Deflection Angle vs Gamma")
plt.xlabel("Gamma")
plt.ylabel("Deflection Angle")
plt.grid()
plt.legend()
plt.savefig(
    "outputs/deflection_angle/deflection_vs_gamma.png",
    dpi=300
)
plt.close()

#Wormhole shape function
r0 = 1
r = np.linspace(1,10,500)
b = r0**2 / r
plt.figure(figsize=(8,5))
plt.plot(r,b)
plt.xlabel("r")
plt.ylabel("b(r)")
plt.title("Morris-Thorne Shape Function")
plt.grid()
plt.savefig(
    "outputs/wormhole/shape_function.png",
    dpi=300
)
plt.show()
plt.close()

#Embedded diagram
r0 = 1
r = np.linspace(1.01,10,1000)
z = r0*np.arccosh(r/r0)

plt.figure(figsize=(8,6))
plt.plot(r,z)
plt.plot(r,-z)
plt.xlabel("r")
plt.ylabel("z")

plt.title(
    "Morris-Thorne Wormhole Embedding Diagram"
)
plt.grid()
plt.savefig(
    "outputs/wormhole/embedding_diagram.png",
    dpi=300
)
plt.show()
plt.close()

#Effective potential
r0 = 1
L = 1
r = np.linspace(1.05,10,1000)
b = r0**2/r
V = (
    L**2/r**2
)*(
    1-b/r
)
plt.figure(figsize=(8,5))
plt.plot(r,V)
plt.xlabel("r")
plt.ylabel("Veff")

plt.title(
    "Photon Effective Potential in Wormhole"
)
plt.grid()
plt.savefig(
    "outputs/wormhole/effective_potential.png",
    dpi=300
)
plt.show()
plt.close()

#Wormhole deflection angle
b = np.linspace(1.1,10,500)
alpha = 2/b
plt.figure(figsize=(8,5))
plt.plot(b,alpha)
plt.xlabel("Impact Parameter")
plt.ylabel("Deflection Angle")
plt.title(
    "Wormhole Deflection Angle"
)
plt.grid()
plt.savefig(
    "outputs/wormhole/wormhole_deflection.png",
    dpi=300
)
plt.show()
plt.close()

#BH vs Wormhole Deflection
b = np.linspace(1.2,10,500)
alpha_bh = 4/b
alpha_wh = 2/b
plt.figure(figsize=(8,5))
plt.plot(
    b,
    alpha_bh,
    label="Schwarzschild BH"
)
plt.plot(
    b,
    alpha_wh,
    label="Morris-Thorne WH"
)
plt.xlabel("Impact Parameter")
plt.ylabel("Deflection Angle")
plt.title(
    "Black Hole vs Wormhole Lensing"
)
plt.legend()
plt.grid()
plt.savefig(
    "outputs/wormhole/bh_vs_wh_deflection.png",
    dpi=300
)
plt.show()
plt.close()

#Light ray bending
x = np.linspace(-10,10,1000)
y1 = 1/(1+0.05*x**2)
y2 = -1/(1+0.05*x**2)
plt.figure(figsize=(8,8))
plt.plot(x,y1)
plt.plot(x,y2)
circle = plt.Circle(
    (0,0),
    1,
    fill=False
)
plt.gca().add_patch(circle)
plt.axis('equal')
plt.title(
    "Simulated Wormhole Gravitational Lensing"
)
plt.savefig(
    "outputs/wormhole/wormhole_lensing.png",
    dpi=300
)
plt.show()