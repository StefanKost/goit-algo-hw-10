# goit-algo-hw-10
Linear Programming and Randomized Algorithms

## Task 1 (Production optimization)
Using PuLP library to maximize fresh drinks production by given constraints.


### Run
Create virtual env and install packages:
```bash
# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
pip install -r requirements.txt
```
```bash
python task1_production_optimization.py
```

### Results
![Task1](https://github.com/user-attachments/assets/6f76b3bb-439e-4163-886b-e4a80f153bc5)

## Task 2 (Monte Carlo Integration)
Computing the definite integral of **f(x) = sin(x) + x²** on the interval **[0, 3]** by Monte Carlo method.

### Run
```bash
python task2_monte_carlo_integral.py
```

### Analytical Solution:
```
F(x) = -cos(x) + x³/3
∫₀³ (sin(x) + x²) dx = F(3) - F(0)
                     = (-cos(3) + 27/3) - (-cos(0) + 0)
                     = (-cos(3) + 9) - (-1 + 0)
                     = (-cos(3) + 9) + 1
                     = 10 - cos(3)
                     ≈ 10 - (-0.98999)
                     ≈ 10.990
```

### Results
| Method                   | Result   |
|--------------------------|----------|
| Analytical               | 10.990   |
| SciPy                    | 10.98999 |
| Monte Carlo (N=100)      | ~11.24   |
| Monte Carlo (N=1000)     | ~11.10   |
| Monte Carlo (N=10000)    | ~11.02   |
| Monte Carlo (N=100000)   | ~10.95   |
| Monte Carlo (N=1000000)  | ~11.01   |
| Monte Carlo (N=10000000) | ~10.99   |

### Visualization
![Monte Carlo](https://github.com/user-attachments/assets/5f569886-b86f-4f8a-87dd-8d099597e6ca)

### Conclusions
1. The Monte Carlo method provides a reasonable approximation of the integral. Increasing the number of sample points improves accuracy, and roughly 100 times more points are needed to reduce the error by a factor of 10.
2. The Monte Carlo estimate fluctuates more with a small number of points but stabilizes as the sample size increases. This demonstrates the stochastic nature of the method.
3. For straightforward functions, numerical integration using `SciPy` quad is more precise and efficient.
4. Analytical solutions give exact results when available. Monte Carlo is particularly useful for functions that are complicated, high-dimensional, or difficult to integrate analytically.