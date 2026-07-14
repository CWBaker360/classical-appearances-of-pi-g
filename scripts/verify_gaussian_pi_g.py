import math


def next_chord_by_doubling(c):
    """
    Given c_N = chord length of a regular N-gon in the unit circle,
    compute c_{2N} using only square roots.

    Stable form:
        c_{2N} = c_N / sqrt(2 + 2 sqrt(1 - c_N^2/4))
    """
    return c / math.sqrt(2.0 + 2.0 * math.sqrt(1.0 - 0.25 * c * c))


def geometric_Q_values(start_doublings, extra_values):
    """
    Start from the regular hexagon:
        N = 6, c_6 = 1.

    After start_doublings, return Q_N, Q_{2N}, Q_{4N}, ...
    where
        Q_N = N c_N / 2.
    """
    N = 6
    c = 1.0

    for _ in range(start_doublings):
        c = next_chord_by_doubling(c)
        N *= 2

    values = []

    for _ in range(extra_values):
        Q = 0.5 * N * c
        values.append((N, Q))

        c = next_chord_by_doubling(c)
        N *= 2

    return values


def n_series_acceleration(Q_values, order):
    """
    Even-power Richardson/N-series acceleration.

    order = 0:
        Q_N

    order = 1:
        (4 Q_{2N} - Q_N) / 3

    order = 2:
        applies the next correction level as well.
    """
    current = list(Q_values)

    for r in range(1, order + 1):
        factor = 4.0 ** r
        current = [
            (factor * current[i + 1] - current[i]) / (factor - 1.0)
            for i in range(len(current) - 1)
        ]

    return current[0]


def compute_pi_g(start_doublings=12, order=2):
    """
    Compute pi_g from the geometric polygon/N-series expression.

    start_doublings=12 gives N = 6 * 2^12 = 24576.
    order=2 uses Q_N, Q_{2N}, Q_{4N}.
    """
    values = geometric_Q_values(
        start_doublings=start_doublings,
        extra_values=order + 1
    )

    Q_values = [Q for _, Q in values]
    pi_g = n_series_acceleration(Q_values, order=order)

    return pi_g, values


def simpson(f, a, b, n):
    """
    64-bit Simpson integration.
    """
    if n % 2:
        n += 1

    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        s += (4.0 if i % 2 else 2.0) * f(x)

    return s * h / 3.0


pi_g, source_values = compute_pi_g(start_doublings=12, order=2)

L = 6.0
n_steps = 10_000

integral_approximation = simpson(
    lambda x: math.exp(-x * x),
    -L,
    L,
    n_steps
)

sqrt_pi_g = math.sqrt(pi_g)
difference = integral_approximation - sqrt_pi_g
normalized_area = integral_approximation / sqrt_pi_g

print("Geometric/N-series source values:")
for N, Q in source_values:
    print(f"N = {N:8d}, Q_N = {Q:.17f}")

print()
print("pi_g from geometry/N-series:", format(pi_g, ".17f"))
print("sqrt(pi_g):", format(sqrt_pi_g, ".17f"))
print("Integral approximation:", format(integral_approximation, ".17f"))
print("difference:", difference)
print("normalized area:", format(normalized_area, ".17f"))
