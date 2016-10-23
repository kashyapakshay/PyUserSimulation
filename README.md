# Union College User Simulation Framework

Statistical User Simulation framework for developing and evaluating Dialogue Systems.

1. The library has two models to build USer SImulations:

```python
# Bigram-based Model [1]
from models import BigramModel

# Cluster-based Model [2]
from models import ClusterModel
```

2. How to use:

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
