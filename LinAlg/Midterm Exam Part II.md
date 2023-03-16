Part II – Numerical stability and chaos

In your previous homework, you created a code to integrate the Pythagorean three-body problem.   Goal of this homework was to show that you have converged to the correct answer using convergence, numerical cross validation, and verification.

The goal of this problem is to text the numerical sensitivity of the project to initial perturbations in the position of the particles.  The number next to the particle indicates their masses.  The distance between them is given by a 3-4-5 triangle.  Assume the x-axis is horizontal and the y-axis is vertical such that the particle with mass 3 is at (3, 4).





				





Since there is no final state of the system, we are going to sample the position at some time T which is after the system goes into its final dynamical configuration.  Basically, there is a pair of two particles in orbit around each other that escaping away from the third particle.  This is an example of a possible final T.  

 
Using this as the base configuration, change the location of the particle with mass 3 from (3, 4) to (3, 4 – delta) where delta is a small number.  Analyze how the final positions of the three particles varies as you alter delta while keeping Tfinal fixed.

The minimum summary of this section should be:

1)	Validity of the results - A recap how you know your system is giving stable and correct results based on the results of homework.  Basically, rediscuss the process you used for numerical validation and verification.  This can use the results from the group project.   
2)	A description of the initial conditions used for the analysis - Create a set of initial delta to explore the behavior of the system.
3)	A summary of the results of the displacements of the particles compared to their unperturbed positions.   Run the system to and find the final positions of all the particles.
4)	A discussion of what the results mean.  
a.	Does the system have a linear or non-linear behavior to these perturbations?  Explain how you can draw this conclusion based on your data.  
b.	Are there regions which produce similar outputs?  Does a tiny shift suddenly change everything?  Are there regions (say a displacement + a tiny tiny delta) where the response seems linear? What is tiny tiny?  Is it really tiny tiny tiny?
c.	Are there critical points when this happens?
