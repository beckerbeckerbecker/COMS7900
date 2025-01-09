# Three Body Problem Notes

## 1. Introduction
The Three Body Problem is a classic problem in physics that involves predicting the motion of three celestial bodies interacting under mutual gravitational forces. Unlike the Two Body Problem, it cannot be solved analytically, showcasing the inherent chaos and sensitivity in dynamical systems. This project explores the problem to understand nonlinear dynamics, stability, and the impact of small perturbations on system behavior.

---

## 2. Mathematical Background

### Governing Equations
The equations of motion for three bodies are derived from Newton's law of gravitation:
\[
\frac{d^2 \mathbf{r}_i}{dt^2} = \sum_{j \neq i} G \frac{m_j (\mathbf{r}_j - \mathbf{r}_i)}{||\mathbf{r}_j - \mathbf{r}_i||^3}, \quad i = 1, 2, 3
\]
Where:
- \( \mathbf{r}_i \): Position vector of the \( i \)-th body.
- \( m_j \): Mass of the \( j \)-th body.
- \( G \): Gravitational constant.

### Initial Conditions
- Positions: \((3, 4), (-3, -4), (0, 0)\) (example).
- Masses: 3, 4, and 5 units.
- Velocities: Assigned to maintain bounded dynamics.

---

## 3. Simulation Approach

### Numerical Method
To solve the equations of motion, we employ the **4th-order Runge-Kutta (RK4)** method for numerical integration. This method provides a balance between accuracy and computational efficiency.

### Simulation Steps
1. Define initial conditions (masses, positions, and velocities).
2. Calculate gravitational forces acting on each body.
3. Use RK4 to update the positions and velocities over small time steps.
4. Store the results for visualization.

#### Pseudocode
```plaintext
Initialize positions, velocities, and masses
For each time step:
    Compute pairwise gravitational forces
    Update positions and velocities using RK4
    Store results for analysis
