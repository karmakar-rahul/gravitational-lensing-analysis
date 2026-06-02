# Key Equations and Theoretical Framework

## Introduction

This document summarizes the principal equations used throughout the project for analyzing gravitational lensing signatures in Schwarzschild Black Holes, Kalb-Ramond Black Holes, and Morris-Thorne Wormholes.

The focus is placed on the spacetime metrics, photon trajectories, photon sphere radius, shadow radius, and gravitational deflection angle.

---

# 1. Gravitational Lensing

Gravitational lensing occurs due to the curvature of spacetime produced by massive objects.

## Lens Equation

[
\vec{\beta}
===========

## \vec{\theta}

\frac{D_{ds}}{D_s}
\vec{\alpha}
]

where

* (\beta) = angular position of source
* (\theta) = angular position of image
* (D_{ds}) = lens-source distance
* (D_s) = observer-source distance
* (\alpha) = deflection angle

---

# 2. Einstein Deflection Angle

For a point mass lens,

[
\alpha
======

\frac{4GM}{c^2 b}
]

where

* (M) = lens mass
* (b) = impact parameter

---

# 3. Einstein Radius

The Einstein radius defines the angular scale of a lensing system.

[
\theta_E
========

\sqrt{
\frac{4GM}{c^2}
\frac{D_{LS}}
{D_{OL}D_{OS}}
}
]

---

# 4. Schwarzschild Black Hole

## Schwarzschild Metric

[
ds^2
====

-\left(
1-\frac{2GM}{rc^2}
\right)c^2dt^2
+
\left(
1-\frac{2GM}{rc^2}
\right)^{-1}dr^2
+
r^2 d\Omega^2
]

where

[
d\Omega^2
=========

d\theta^2
+
\sin^2\theta , d\phi^2
]

---

## Schwarzschild Radius

[
r_s
===

\frac{2GM}{c^2}
]

---

## Conserved Energy

[
E
=

\left(
1-\frac{2GM}{r}
\right)
\frac{dt}{d\lambda}
]

---

## Conserved Angular Momentum

[
L
=

r^2
\frac{d\phi}{d\lambda}
]

---

## Impact Parameter

[
b
=

\frac{L}{E}
]

---

## Orbit Equation for Null Geodesics

Using

[
u=\frac{1}{r}
]

the photon orbit equation becomes

[
\left(
\frac{du}{d\phi}
\right)^2
=========

## \frac{1}{b^2}

u^2
+
2GMu^3
]

---

## Weak Field Deflection Angle

[
\alpha
======

\frac{4GM}{b}
]

This represents the classical Einstein light-bending result.

---

# 5. Kalb-Ramond Black Hole

Kalb-Ramond gravity introduces modifications to General Relativity through an antisymmetric tensor field.

---

## Modified Metric

[
ds^2
====

*

\left(
1
-

\frac{2GM}{r}
+
\frac{\Gamma}{r^{2\lambda}}
\right)dt^2
+
\left(
1
-

\frac{2GM}{r}
+
\frac{\Gamma}{r^{2\lambda}}
\right)^{-1}dr^2
+
r^2 d\Omega^2
]

where

* (\Gamma) = deformation parameter
* (\lambda) = coupling parameter

---

## Modified Orbit Equation

[
\left(
\frac{du}{d\phi}
\right)^2
=========

## \frac{1}{b^2}

u^2
\left(
1
-

2GMu
+
\Gamma u^{2/\lambda}
\right)
]

---

## Weak Deflection Angle in Kalb-Ramond Gravity

[
\alpha
======

## \frac{4GM}{b}

\frac{\pi\Gamma}
{2b^{,1-\frac{2}{\lambda}}}
]

This equation reduces to the Schwarzschild result when

[
\Gamma = 0
]

---

# 6. Photon Sphere

The photon sphere represents unstable circular photon orbits around compact objects.

The radius is obtained from

[
\frac{d}{dr}
\left(
\frac{r^2}{f(r)}
\right)
=======

0
]

where

[
f(r)
====

## 1

\frac{2GM}{r}
+
\frac{\Gamma}{r^{2\lambda}}
]

---

## Schwarzschild Photon Sphere

[
r_{ph}
======

3GM
]

---

# 7. Black Hole Shadow Radius

The shadow radius is determined from the photon sphere radius.

[
R_{sh}
======

\frac{R_{ph}}
{\sqrt{
1-\frac{R_s}{R_{ph}}
}}
]

For a Schwarzschild Black Hole,

[
R_{sh}
======

\frac{3\sqrt{3}}{2}
r_s
]

---

# 8. Morris-Thorne Wormhole

## Morris-Thorne Metric

[
ds^2
====

e^{2\Phi(r)}
dt^2
----

\frac{dr^2}
{
1-\frac{b(r)}{r}
}
-

r^2
\left(
d\theta^2
+
\sin^2\theta d\phi^2
\right)
]

where

* (\Phi(r)) = redshift function
* (b(r)) = shape function

---

## Wormhole Throat Condition

The throat occurs at

[
b(r_0)
======

r_0
]

where

[
r_0
]

is the throat radius.

---

## Flaring-Out Condition

For a traversable wormhole,

[
b'(r_0)
<
1
]

must be satisfied.

---

## Shape Function Used

The simplified shape function adopted in this project is

[
b(r)
====

\frac{r_0^2}{r}
]

---

# 9. Wormhole Embedding Equation

The embedding geometry is described by

[
\frac{dz}{dr}
=============

\left(
\frac{r}{b(r)}
--------------

1
\right)^{-1/2}
]

For

[
b(r)
====

\frac{r_0^2}{r}
]

the embedding surface becomes

[
z(r)
====

r_0
\cosh^{-1}
\left(
\frac{r}{r_0}
\right)
]

---

# 10. Wormhole Effective Potential

For photon trajectories,

[
V_{eff}
=======

\frac{L^2}{r^2}
\left(
1-\frac{b(r)}{r}
\right)
]

This effective potential determines possible photon orbits around the wormhole throat.

---

# 11. Comparative Optical Observables

The principal observables analyzed throughout this project are:

1. Photon Sphere Radius

[
r_{ph}
]

2. Shadow Radius

[
R_{sh}
]

3. Weak Deflection Angle

[
\alpha
]

4. Effective Potential

[
V_{eff}
]

5. Wormhole Embedding Geometry

[
z(r)
]

These quantities provide observational signatures capable of distinguishing black holes from wormholes and testing extensions of General Relativity.

---

