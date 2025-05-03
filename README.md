# Dice Roll Simulation (Task_07)

## Summary

This simulation estimates the probabilities of sums when rolling two six-sided dice using the Monte Carlo method. The results from the simulation are compared with the theoretical probabilities derived from combinatorial analysis.

### Simulation Results (Number of rolls = 100_000)

| Сума | Імовірність (Симуляція) |
| ---- | ----------------------- |
| 2    | 2.77%                   |
| 3    | 5.58%                   |
| 4    | 8.30%                   |
| 5    | 11.03%                  |
| 6    | 13.83%                  |
| 7    | 16.62%                  |
| 8    | 13.81%                  |
| 9    | 11.34%                  |
| 10   | 8.24%                   |
| 11   | 5.65%                   |
| 12   | 2.84%                   |

### Expected Results

Based on theoretical probabilities, the expected distributions for sums when rolling two dice are as follows:

| Сума | Імовірність (Теоретична) |
| ---- | ------------------------ |
| 2    | 2.78%                    |
| 3    | 5.56%                    |
| 4    | 8.33%                    |
| 5    | 11.11%                   |
| 6    | 13.89%                   |
| 7    | 16.67%                   |
| 8    | 13.89%                   |
| 9    | 11.11%                   |
| 10   | 8.33%                    |
| 11   | 5.56%                    |
| 12   | 2.78%                    |

### Comparison

The simulated probabilities closely match the theoretical probabilities, demonstrating the effectiveness of the Monte Carlo simulation method. Minor discrepancies appear due to the simulations randomness, but overall, the results confirm the expected distribution of sums when rolling two dice.
