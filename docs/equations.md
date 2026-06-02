# Key Equations and Theoretical Framework

## Overview

This document summarizes the principal equations used in the computational analysis of gravitational lensing signatures in Schwarzschild Black Holes, Kalb-Ramond Black Holes, and Morris-Thorne Wormholes.

The primary observables investigated are:

* Photon Sphere Radius
* Shadow Radius
* Weak Deflection Angle
* Wormhole Geometry
* Effective Potential

---

# 1. Einstein Deflection Angle

For a point mass lens, the weak gravitational deflection angle is given by

```math
\alpha = \frac{4GM}{c^2 b}
```

where:

* (G) = Gravitational Constant
* (M) = Mass of the lens
* (c) = Speed of Light
* (b) = Impact Parameter

---

# 2. Schwarzschild Black Hole

## Schwarzschild Metric

The Schwarzschild spacetime describing a static and spherically symmetric black hole is

```math
ds^2 =
-\left(1-\frac{2GM}{rc^2}\right)c^2dt^2
+
\left(1-\frac{2GM}{rc^2}\right)^{-1}dr^2
+
r^2 d\Omega^2
```

where

```math
d\Omega^2=d\theta^2+\sin^2\theta\,d\phi^2
```

---

## Schwarzschild Radius

The event horizon occurs at

```math
r_s=\frac{2GM}{c^2}
```

---

## Conserved Quantities

Energy:

```math
E=
\left(1-\frac{2GM}{r}\right)
\frac{dt}{d\lambda}
```

Angular Momentum:

```math
L=
r^2
\frac{d\phi}{d\lambda}
```

Impact Parameter:

```math
b=\frac{L}{E}
```

---

## Null Geodesic Orbit Equation

Using

```math
u=\frac{1}{r}
```

the photon orbit equation becomes

```math
\left(\frac{du}{d\phi}\right)^2
=
\frac{1}{b^2}
-u^2
+2GMu^3
```

---

## Weak Field Deflection Angle

```math
\alpha=\frac{4GM}{b}
```

---

# 3. Kalb-Ramond Black Hole

Kalb-Ramond gravity modifies the Schwarzschild spacetime through deformation parameters (\Gamma) and (\lambda).

---

## Modified Metric

```math
ds^2
=
-\left(
1-\frac{2GM}{r}
+\frac{\Gamma}{r^{2\lambda}}
\right)dt^2
+
\left(
1-\frac{2GM}{r}
+\frac{\Gamma}{r^{2\lambda}}
\right)^{-1}dr^2
+
r^2d\Omega^2
```

where:

* (\Gamma) = Kalb-Ramond deformation parameter
* (\lambda) = coupling parameter

---

## Modified Orbit Equation

```math
\left(
\frac{du}{d\phi}
\right)^2
=
\frac{1}{b^2}
-
u^2
\left(
1
-
2GMu
+
\Gamma u^{2/\lambda}
\right)
```

---

## Kalb-Ramond Deflection Angle

```math
\alpha
=
\frac{4GM}{b}
-
\frac{\pi\Gamma}
{2b^{1-\frac{2}{\lambda}}}
```

For

```math
\Gamma = 0
```

the Schwarzschild result is recovered.

---

# 4. Photon Sphere

The photon sphere corresponds to unstable circular photon orbits around compact objects.

The radius is obtained from

```math
\frac{d}{dr}
\left(
\frac{r^2}{f(r)}
\right)
=
0
```

where

```math
f(r)
=
1
-
\frac{2GM}{r}
+
\frac{\Gamma}{r^{2\lambda}}
```

---

## Schwarzschild Photon Sphere

```math
r_{ph}=3GM
```

---

# 5. Shadow Radius

The shadow radius is related to the photon sphere radius through

```math
R_{sh}
=
\frac{R_{ph}}
{\sqrt{
1-\frac{R_s}{R_{ph}}
}}
```

For a Schwarzschild black hole

```math
R_{sh}
=
\frac{3\sqrt{3}}{2}
\,r_s
```

---

# 6. Morris-Thorne Wormhole

## Wormhole Metric

The Morris-Thorne traversable wormhole metric is

```math
ds^2
=
e^{2\Phi(r)}dt^2
-
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
```

where:

* (\Phi(r)) = Redshift Function
* (b(r)) = Shape Function

---

## Wormhole Throat

The throat radius is defined by

```math
b(r_0)=r_0
```

---

## Flaring-Out Condition

For a traversable wormhole

```math
b'(r_0)<1
```

must hold.

---

## Shape Function Used

The simplified Morris-Thorne shape function adopted in this project is

```math
b(r)
=
\frac{r_0^2}{r}
```

---

# 7. Wormhole Embedding Geometry

The embedding surface is described by

```math
\frac{dz}{dr}
=
\left(
\frac{r}{b(r)}
-
1
\right)^{-1/2}
```

For

```math
b(r)=\frac{r_0^2}{r}
```

the embedding function becomes

```math
z(r)
=
r_0
\cosh^{-1}
\left(
\frac{r}{r_0}
\right)
```

---

# 8. Effective Potential

The effective potential governing photon motion around the wormhole is

```math
V_{eff}
=
\frac{L^2}{r^2}
\left(
1-\frac{b(r)}{r}
\right)
```

This potential determines possible photon trajectories and lensing behavior near the wormhole throat.

---

# 9. Primary Observables

The computational analysis performed in this project focuses on:

1. Photon Sphere Radius

```math
r_{ph}
```

2. Shadow Radius

```math
R_{sh}
```

3. Weak Deflection Angle

```math
\alpha
```

4. Effective Potential

```math
V_{eff}
```

5. Wormhole Embedding Surface

```math
z(r)
```

These observables provide theoretical signatures that may be used to distinguish black holes from traversable wormholes through gravitational lensing observations.
