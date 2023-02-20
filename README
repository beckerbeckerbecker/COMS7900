# Ecological Models of Enchanted Kingdoms

## Abstract

We have created a detailed ecological model of Enchanted Kingdoms using both system dynamics and agent-based modeling methodologies.  We have simulated the Prince-Frog and the Princess-Sleeping Beauty co-linked ecological cycles.  We compare the results from the two modeling approaches for this problem, including the regulation mechanisms of kiss effectiveness and witch density.  Using our models, we can make predictions about population dynamics adn the regulation mechanisms needed for a quasi-stable system.  *Dr. Bob Panoff (Shodor Foundation)*

## 1 Introduction

1. Snow white and the seven dwarves 1937
2. Cinderella 1950
3. Sleeping Beauty 1959
4. The princess and the from 2009

The stories of Enchanted Kingdoms have existed for generations [1, 2, 3.].  Although little direct data exists for these systems, the available literature suggests that several key cycles developed in these uniques ecological environments.  One of the key ecological cycles found in the literature is the regulated transformations between princes and frogs.  Based on published works, these transformations are regulated by two factors.  Witches living in the enchanteed kingdom would transform princes into frogs [4].  Once this transformation happens, princesses have been able to reverse the process creating princes from frogs.  The prince-frog cycle (hereafter, PF-cycle) is clearly a fascinating example of a reversible ecological transformation.

The exact factors regulating the PF-cycle are somewhat mysterious.  It is clear that witches and princesses act effectively as types of ecological enzymes regulating the transofrmation rates without entering into the reactions themselves.  Like other reactions regulated by enzymes, it is possible that these transformations might happen spontaneously, but at an extrememly low rate unless an enzyme is present.  Current studies of modern princes and frogs suggest that the spontaneous transformation of princes into frogs and vice versa has not significantly affected the frog or the prince populations.  We also know that the regulation mechanism of the PF-cycle seem to be dependent on certain quantifiable factors.  Literature sources suggest, for example that there is a unique paring between princes and frogs in order to induce a transformation back into a princely state.  Other literature sources suggest that not all prince + witch interations inevitably lead to the emergence of the frog state.

The second critical cycle to consider when evaluating the ecology of the Enchanted Kingdom is the transformations between princesses and the so-called sleeping beauties [3,1].  Although these two states are superficially the same, there are critical differences between the metabolism rates, mobility, and levels of consciousness between these forms.  The princess-sleeping beauty cycle( hereafter PSB-cycle) bears a remarkable similarity to the PF-cycle.  Specifically, the regullation mechanism of witches and princes in the  PSB-cycle plays the same role as the witches and princesses in the PF-cycle.

Although the PF-cycle and the PSB-cycle have capture the imagination of scientists and no-scientists of all ages, there have been no detailed studies of the ecological systems as a whole.  Although the co-regulation mechanisms seem to be unique, there have been no direct observations of the long-term stability of this cycle.  In fact, all accounts have focused on individual transformations.  Although these stories are helpful and entertaining, they cannot provide a complete picture of how these well-documented cycles may interact with each other.  Because the system of interest was only observed long, long ago and in a land far, far away the prospects for direct field study seem remote.


## 2 Method

The interlocking PF/PSB cycles can be examined numerical using two different simulation methods.  In the subsections below, we will examine this ecological cycle.  In the subsections below, we will examine this ecological cycle can be examined using either system dynamics and agent-based modeling software.

### 2.1 System Dynamics Models

At a simple level, the PF/PSB cycles can be considered as a set of coupled differential equations

${dN_{princes}}/{dt} = -c_{PF}N_{witches}N_{Princes} + k_{FP}N_{frogs}N_{princesses}$
${dN_{princesses}}/{dt} = -c_{PSB}N_{witches}N_{princesses} + k_{SBP}N_{sleeping beauties}N_{princesses}$

Where $N_{princes}$ is the number of princes, $N_{princesses}$ is the number of princesses, $N_{frogs}$ is the number of frogs, and $N_{sleeping beauties}$ is the number of sleeping beauties.  We have also introduced four constants:

$c_{PF} =$ the Prince to Frog cursing factor
$c_{PSB} =$ the Prince to Princess cursing factor
$k_{FP} =$ the Frog to Prince kissing factor
$k_{SBP} =$ the Sleeping Beauty to Frog kissing factor

For this preliminary investigation, we will set $k_{FP} = k_{SBP} = k$ and $c_{PF} = c_{PBS} = c$ since there is no evidence that witches preferentially curse princes more or less than princesses or that the kiss from princes is more or less magical than that from princesses.  Although these constaants could certainly be altered, it seems like such assumptions arenot justified by the available literature.

We have made some simplifications in our system in order to derive these equations.  We are considering the PF/PSB cycles as closed loops, with no external mechanisms to generate additional elements in any of hte four regulated populations.  We also have no net loss in these populations, except through the transformation mechanisms.  Further, we are assuming that the $c$ and $k$ factors remain constant over time.  The number of witches is assumed to be driven by external factors, an dheld as a free parameter in the system.

Figure 1 : The PF/PSB Cycle

In fact, this last assumption is not directly supported by the literature.  There are several acounts suggesting that decreases in the overall witch population can occur, and the typical cause of these decreases is a prince.

To simplifythe solution to this problem, we further deviate from the original equations and substitute density measurements for cardinal numbers.  The use of density for our populations may seem a bit strange, but it allows us to use standard numerical techniques to model the system.  Even so, it does make it inevitable to have fractional numbers of witches, princes, princesses, frogs, and sleeping beauties.  We feel this error is acceptable in the context of these simulations.

### 2.2 Agent Based Modeling

The second approach for modeling the PF/PSB cycle is agent modeling.  The idea of this type of simulation is to set up a two dimenstional grid representing the geography of the Enchanted Kingdom.  Within this grid, there are three types of Agents that each follow a set of rules.

#### Witches

* Witches can move freely across the grid in a random direction one square per timestep
* When a witch is next to a prince or a princess, the prince or princess will change form with a probability of $C_f$, the cursing factor.

#### Princes/Frogs

* Princes and frogs can move freely across the grid in a random direction one square per timestep
* Princes turn into frogs as described under the witches agent.
* Frogs can turn back into princes as described under the Princesses/Sleeping Beauty agent
* When a prince is next to a sleeping beauty, it can transform the sleeping beauty back into a princess with a probability of $K_f$, the kissing factor.
* Frogs cannot transform a sleeping beauty into a princess, because that would be cheating.

#### Princesses/Sleeping Beauties

* Princesses can move freely across the grid in a random direction one square per timestep.
* Sleeping beauties don't move
* Princesses transform into sleeping beauties as described under the witch agent.
* When a princess is next to a frog, it can transform the frog back into a prince with a probability of $K_f$, the kissing factor.

The agent-based modeling is likely to be more realistic than the dynamical systems approach since the number of agents is represented by cardinal numbers.  The population of princes and princesses can crash to zero, thus preventing any future transformations.

# 3 Analysis

A systainable ecological system must have quasistable populations.  Although some fluctuations can occur, crashes in the population of princes and princess would ultimately be irreversable and lead to catastrophic losses [5 Disney Corporation www.disney.com/corporate/about.html].  To ensure a stable population, the number of princess and princes needs to be high enough to resist over-preditation by witches.

Using odeint in python, create a dynamical simulation of the PF/PSB system.  It should return a graph of hte population of princes, princesses, frogs, and sleeping beauties over time.  Explore the parameter space to find typical behaviors of such systems

Using python, create an agent based model of the PF/PSB system.  I would suggest starting with a modest grid size, perhaps 50x50. Iif possible, animate the interactions between the agents to show their movement and transformations across the grid). The simulation should return the same graph as the dynamical systems approach.  Explore the paramenter space to find the typical behaviors in this system.

Compare the dynamical systems approach to the agent based modeling approach.  Can you find any way to translate the coefficients of one system to the coefficients of the other?  What are the similaritites and differences between two approaches?

# Rubric Criterion Score

## ODE code simulates the system

Code works perfectly and is well documented.

1 to 3 minor issues in the code - some documentation missing

Major issues with the code.

Code is doesn't work

## Agent code simulates the system

Code works perfectly and is well documented.

1 to 3 minor issues in the code - some documentation missing

Major issues with the code.

Code is doesn't work

## Runs were done to explore parameter space.

The project fully explores parameter space.  Connections are made between both simulation method.

There are numerous runs of both codes, but there aren't enough to fully understand the space.

One code seems to have enough runs to explore the space, but the other is inadequite.

Only simple runs were done with the codes,   There was not enough data to draw conclusions.

## Results and discussion

Excellent discussion - good graphs and writeup.   

Discussion is good, but perhaps a bit short or missing some minor points.  Either the graphs or analysis may have some minor issues.

Discussion is weak and perhaps a bit short.   More graphs may be needed along with associated analysis. 

Discussion is missing.

## Conclusions

Conclusions are drawn based on the runs and data.  There is a good understanding of the project.

The project conclusions are ok, but perhaps missing some elements.  

The project conclusions are weak.   

There are no conclusions.  
