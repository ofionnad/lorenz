import matplotlib.pyplot as plt

def logistic(r, x):
    return r*x*(1-x)

def make_plot(xn, yn):
    plt.plot(xn, yn)
    plt.plot(xn, xn, c='gray', lw=0.4, alpha=0.7)
    return plt.gca()

def poincare(xn, r, x0, iterations):

    yn = logistic(r, xn)
    ax = make_plot(xn, yn)

    for i in range(iterations):
        y = logistic(r, x0)
        ax.plot(x0, y, 'ko', ms=8, alpha=(i+1)/iterations)
        ax.plot([x0,x0],[x0,y], color='gray', lw=0.5, ls='-', alpha=0.7)
        ax.plot([x0,y],[y,y], color='gray', lw=0.5, ls='-', alpha=0.7)
        plt.savefig('poincare_map/r3p5_image_{}.png'.format(i))
        x0 = y

