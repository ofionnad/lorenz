"""
Lets create a chaotic attractor. Beginning with Lorenz.
"""
import numpy as np
import matplotlib.pyplot as plt

def lorenz(x, y, z, sigma=10, rho=28, beta=2.667):

    xdot = sigma*(y - x)
    ydot = x*(rho - z) -y
    zdot = x*y - beta*z

    return [xdot, ydot, zdot]

def make_attractor(x1, y1, z1, nt=1000, dt=0.01, sigma=10, rho=28, beta=2.667):

    r = np.empty((3,nt+1))
    r[0][0], r[1][0], r[2][0] = x1, y1, z1

    for i in range(nt):
        xdot, ydot, zdot = lorenz(r[0][i], r[1][i], r[2][i], sigma=sigma, rho=rho, beta=beta)
        r[0][i+1] = r[0][i] + (xdot * dt)
        r[1][i+1] = r[1][i] + (ydot * dt)
        r[2][i+1] = r[2][i] + (zdot * dt)

    return r


def logistic(r, x):
    return r*x*(1-x)


def bifurcation(n, r, iterations, last, x):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 9),
                               sharex=True)
    for i in range(iterations):
        x = logistic(r, x)

        lyapunov += np.log(abs(r - 2 * r * x))

        if i >= (iterations - last):
            ax1.plot(r, x, ',k', alpha=.25)
    ax1.set_xlim(2.5, 4)
    ax1.set_title("Bifurcation diagram")

    ax2.axhline(0, color='k', lw=.5, alpha=.5)

    ax2.plot(r[lyapunov < 0],
             lyapunov[lyapunov < 0] / iterations,
             '.k', alpha=.5, ms=.5)

    ax2.plot(r[lyapunov >= 0],
             lyapunov[lyapunov >= 0] / iterations,
             '.r', alpha=.5, ms=.5)
    ax2.set_xlim(2.5, 4)
    ax2.set_ylim(-2, 1)
    ax2.set_title("Lyapunov exponent")
    plt.tight_layout()


if __name__=="__main__":
    x1, y1, z1 = 1.0, 0.0, 0.0
    r = make_attractor(x1, y1, z1)

    ax = plt.axes(projection='3d')
    ax.plot3D(r, 'gray')


    n = 10000
    r = np.linspace(2.5,4.0,n)
    iterations=1000
    last = 100
    x = 1e-4*np.ones(n)
    bifurcation(n, r, iterations, last, x)


