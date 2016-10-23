# Union College User Simulation Framework

Statistical User Simulation framework for developing and evaluating Dialogue Systems.

Statistical User Simulation models are useful for building simulations of users for testing spoken
and adaptive dialogue systems when it is too expensive to run experiments with real users.

The basic principle of a User Simulation is that given a system action (such as generating an
instruction, providing suggestions, etc. by the dialogue system) at time *t*, *u<sub>s,t</sub>*, it
predicts the action the next action a real user would perform in response at time *t + 1*,
*u<sub>a,t+1</sub>* (such as following the instruction, accepting or rejecting the suggestions, etc.)

The models assume Markov Property holds, i.e, the next user action depends only on the corresponding
system action and not the past action/dialogue history.

The models accept *(u<sub>s,t</sub>, u<sub>a,t+1</sub>)* pairs as training data.

The library has two models to build User Simulations:

```python
# Bigram-based Model [1]
from models import BigramModel

# Cluster-based Model [2]
from models import ClusterModel
```

**How to use:**

```python
userSimulation = BigramModel()
# OR
# userSimulation = ClusterModel()

userSimulation.recordAction(userAction1, systemAction1)
userSimulation.recordAction(userAction2, systemAction1)
userSimulation.recordAction(userAction1, systemAction2)
# ...

# Get predicted user action (at next time step t) after performing
# systemAction (at time t - 1)
userSimulation.getPredictedUserAction(systemAction1)

```

**References:**

[1] Rieser, V. and Lemon, O. *[Reinforcement Learning for Adaptive Dialogue Systems](http://link.springer.com/book/10.1007%2F978-3-642-24942-6)*. Springer, New York, 2011, 133-134.

[2] Rieser, V. and Lemon, O. [Cluster-based User Simulations for Learning Dialogue Strategies](https://pdfs.semanticscholar.org/92c4/08960e3a9cbb433a719f280e0b29b62c1edd.pdf). *INTERSPEECH*, 2006.
