
---

### **Populating the Python Script**

Below is a basic implementation for `three_body_model.py`:

```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Gravitational constant
G = 1.0

def three_body_equations(t, state, m1, m2, m3):
    x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3 = state

    def compute_acceleration(xi, yi, xj, yj, mj):
        r = np.sqrt((xj - xi)**2 + (yj - yi)**2)
        ax = G * mj * (xj - xi) / r**3
        ay = G * mj * (yj - yi) / r**3
        return ax, ay

    # Accelerations due to gravity
    ax1, ay1 = compute_acceleration(x1, y1, x2, y2, m2)
    ax2, ay2 = compute_acceleration(x2, y2, x1, y1, m1)
    ax3, ay3 = compute_acceleration(x3, y3, x1, y1, m1)

    ax1 += compute_acceleration(x1, y1, x3, y3, m3)[0]
    ay1 += compute_acceleration(x1, y1, x3, y3, m3)[1]
    ax2 += compute_acceleration(x2, y2, x3, y3, m3)[0]
    ay2 += compute_acceleration(x2, y2, x3, y3, m3)[1]

    ax3 += compute_acceleration(x3, y3, x2, y2, m2)[0]
    ay3 += compute_acceleration(x3, y3, x2, y2, m2)[1]

    return [vx1, vy1, ax1, ay1, vx2, vy2, ax2, ay2, vx3, vy3, ax3, ay3]

# Initial conditions
m1, m2, m3 = 1.0, 1.0, 1.0
state0 = [3, 4, 0, 0, -3, -4, 0, 0, 0, 0, 0, 0]  # [x1, y1, vx1, vy1, ...]

# Time span for simulation
t_span = (0, 10)
t_eval = np.linspace(0, 10, 1000)

# Solve the equations
solution = solve_ivp(three_body_equations, t_span, state0, t_eval=t_eval, args=(m1, m2, m3))

# Extract results
x1, y1 = solution.y[0], solution.y[1]
x2, y2 = solution.y[4], solution.y[5]
x3, y3 = solution.y[8], solution.y[9]

# Visualization
plt.plot(x1, y1, label="Body 1")
plt.plot(x2, y2, label="Body 2")
plt.plot(x3, y3, label="Body 3")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Three Body Problem")
plt.show()
