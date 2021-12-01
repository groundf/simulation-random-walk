import random
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy import optimize
from tqdm import tqdm
import time

TRIALS = 500   # cca 500
REPEATS = 1000  # cca 100
RESTRICTION = True

directions = np.array([complex(0, 1), complex(1, 0), complex(0, -1), complex(-1, 0)])

# Calculate probabilites for 5 discrete values
x = np.arange(-2, 3)
prob = stats.norm.cdf(x + 0.5, scale=1.58) - stats.norm.cdf(x - 0.5 , scale=1.58)
prob = prob / prob.sum()

results = [] 

t0 = time.time()

for N in tqdm(range(1, TRIALS + 1), desc='Calculating trials...'):
    dst = []
    if RESTRICTION:
        for n in range(REPEATS):
            # choose random numbers from [-2, -1, 0, 1, 2]
            nums = np.random.choice(x, size=N, p=prob)
            # swap +/- 2 with +/- 3
            nums[nums == -2] = -3
            nums[nums == 2] = 3
            # cumulative sum to calculate steps with restriction. (+/- 2 steps are restricted)
            steps = np.mod(np.cumsum(nums), 4)
            walk = directions[steps].cumsum()
            dst.append(abs(walk[-1]))
    else:
        for n in range(REPEATS):
            steps = np.random.randint(0, 4, N)
            walk = directions[steps].cumsum()
            dst.append(abs(walk[-1]))
    
    results.append((N, np.mean(dst), np.std(dst)))

t1 = time.time()
soltime = t1 - t0

if RESTRICTION:
    print(f"2D example with restrictions: from 1 to {TRIALS} steps and {REPEATS} repeats per step.")
else:
    print(f"2D example without restrictions: from 1 to {TRIALS} steps and {REPEATS} repeats per step.")
print(f"Total time of execution: {soltime:.2g} seconds.")

# visualization
steps, distance, error = np.array(results).T

# fit curve
fun = lambda x, a, b: a + b*np.sqrt(x)
fit, _ = optimize.curve_fit(fun, steps,  distance)

# plot with 2 sigma and 1 sigma fills, points with mean values and curve for fit
plt.fill_between(steps, distance - 2*error, distance + 2*error, color='gray', alpha=0.2)
plt.fill_between(steps, distance - error, distance + error, color='gray', alpha=0.4)
plt.plot(steps, distance, 'k.')
plt.plot(steps, fun(steps, *fit), 'r', lw=3)
plt.title(r'$y=%.3f + %.3f\sqrt{x})$' % (fit[0], fit[1]))
plt.show()

