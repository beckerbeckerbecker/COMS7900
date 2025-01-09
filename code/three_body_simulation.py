import numpy as np
from scipy.integrate import odeint

def grav_orbit(y, t, m1, m2, G):
    x1, y1, vx1, vy1, x2, y2, vx2, vy2 = y
    r = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    dvx1dt = G * m2 * (x2-x1) / r**3
    dvy1dt = G * m2 * (y2-y1) / r**3
    dvx2dt = G * m1 * (x1-x2) / r**3
    dvy2dt = G * m1 * (y1-y2) / r**3
    return [vx1, vy1, dvx1dt, dvy1dt, vx2, vy2, dvx2dt, dvy2dt]

# Initial conditions and parameters
x1, y1, vx1, vy1 = 1, 0, 0, 0.5
x2, y2, vx2, vy2 = -1, 0, 0, -0.5
y0 = [x1, y1, vx1, vy1, x2, y2, vx2, vy2]
m1, m2 = 1, 1
G = 1

# Time range for integration
t = np.arange(0, 10, 0.01)
sol = odeint(grav_orbit, y0, t, args=(m1, m2, G))

# Extract positions for visualization
x1, y1, x2, y2 = sol[:, 0], sol[:, 1], sol[:, 4], sol[:, 5]
print("Simulation Complete: Trajectories Calculated")
