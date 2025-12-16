import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

LOWER_BOUND = 0
UPPER_BOUND = 3


def f(x):
    return np.sin(x) + x**2


def monte_carlo_integrate(func, a, b, num_samples=10000):
    """
    Monte Carlo integration using the "hit or miss" method.
    """
    x_test = np.linspace(a, b, 1000)
    max_y = np.max(func(x_test))

    x_rand = np.random.uniform(a, b, num_samples)
    y_rand = np.random.uniform(0, max_y, num_samples)

    under_curve = y_rand <= func(x_rand)
    area_ratio = np.mean(under_curve)
    return (b - a) * max_y * area_ratio


def visualize(func, a, b, num_points=5000, quad_result=None, func_label=None):
    """
    Visualize Monte Carlo integration.
    """
    func_label = func_label or "f(x)"
    x_test = np.linspace(a, b, 1000)
    max_y = np.max(func(x_test))

    fig, ax = plt.subplots(figsize=(10, 6))
    x_plot = np.linspace(a - 0.5, b + 0.5, 400)
    ax.plot(x_plot, func(x_plot), 'b', linewidth=2, label=func_label)

    ix = np.linspace(a, b, 100)
    ax.fill_between(ix, func(ix), color='gray', alpha=0.3, label='Integration area')

    x_rand = np.random.uniform(a, b, num_points)
    y_rand = np.random.uniform(0, max_y, num_points)
    under_curve = y_rand <= func(x_rand)
    mc_estimate = (b - a) * max_y * np.mean(under_curve)

    ax.scatter(x_rand[under_curve], y_rand[under_curve], c='green', s=1, alpha=0.5,
               label=f'Under curve: {np.sum(under_curve)}')
    ax.scatter(x_rand[~under_curve], y_rand[~under_curve], c='red', s=1, alpha=0.5,
               label=f'Above curve: {num_points - np.sum(under_curve)}')

    ax.axvline(x=a, color='gray', linestyle='--', label=f'a = {a}')
    ax.axvline(x=b, color='gray', linestyle='--', label=f'b = {b}')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(f'Monte Carlo Integration of {func_label} from {a} to {b}')
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)

    # Add text box with results
    textstr = f'Points: {num_points}\nMonte Carlo: {mc_estimate:.4f}'
    if quad_result is not None:
        textstr += f'\nSciPy quad: {quad_result:.4f}'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    ax.text(0.98, 0.02, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='bottom', horizontalalignment='right', bbox=props)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    a, b = LOWER_BOUND, UPPER_BOUND

    print(f"Function: f(x) = sin(x) + x^2")
    print(f"Bounds: [{a}, {b}]\n")

    # Exact integral
    quad_result, _ = spi.quad(f, a, b)
    print(f"SciPy quad result: {quad_result:.6f}\n")

    # Monte Carlo for different sample sizes
    print("Monte Carlo results:")
    for n in [100, 1000, 10000, 100000, 1000000, 10000000]:
        mc = monte_carlo_integrate(f, a, b, n)
        print(f" -> N={n:<8} | {mc:.6f}")

    func_label = r'$f(x) = \sin(x) + x^2$'
    visualize(f, a, b, num_points=10000, quad_result=quad_result, func_label=func_label)
