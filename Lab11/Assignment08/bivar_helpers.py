"""
Helper objects for inference of a straight-line regression function.

Created Apr 21, 2015 by Tom Loredo
"""

import numpy as np
import scipy
from scipy import *
from scipy import stats
from matplotlib.pyplot import *


class MargCondJoint2D:

    def __init__(self, x_marg, y_cond_x):
        """
        Define a joint dist'n for (x,y) by specifying a marginal for x and
        a conditional for y given x.

        Parameters
        ----------

        x_marg : distribution instance
            An object defining the marginal, p(x); it should have a pdf(xvals)
            method evaluating the marginal PDF, and an rvs(n) method that
            returns n samples

        y_cond_x : conditional distribution provider
            An function returning the conditional, p(y|x), as a function of x;
            y_cond_x(x) should return a distribution instance with the same
            required methods as x_marg
        """
        self.x_marg = x_marg
        self.y_cond_x = y_cond_x

    def pdf(self, xy):
        """
        Return the joint PDF, p(x,y), for an (x,y) point:
            xy[0] = x
            xy[1] = y
        """
        y_cond = self.y_cond_x(xy[0])
        return self.x_marg.pdf(xy[0]) * y_cond.pdf(xy[1])

    def sample(self, n=1):
        """
        Return `n` samples from the joint distribution as two
        arrays, of x and y coordinates.
        """
        if n==1:
            xvals = array( [self.x_marg.rvs()] )
        else:
            xvals = self.x_marg.rvs(n)
        yvals = empty_like(xvals)
        for i, x in enumerate(xvals):
            y_cond = self.y_cond_x(x)
            yvals[i] = y_cond.rvs()
        return xvals, yvals



def traceplots(fit):
    """
    Make a set of traceplots for StanFitResults instance `fit`.
    """
    f=figure(figsize=(10,9))
    ax=f.add_subplot(3,1,1)
    fit.beta_0.trace(axes=ax,alpha=.6)  # without `axes`, this will make its own fig
    ax.set_xlabel('')

    ax=f.add_subplot(3,1,2)
    fit.beta_1.trace(axes=ax,alpha=.6)
    ax.set_xlabel('')

    ax=f.add_subplot(3,1,3)
    fit.log_p.trace(axes=ax,alpha=.6)


def betas_plot(fit, beta_0, beta_1):
    """
    Make a scatterplot of the beta samples from StanFitResults instance `fit`.

    Draw a crosshair showing true values `beta_0` and `beta_1`.
    """
    # Thin samples using smallest ESS.
    nsc = fit.chains.shape[0]  # number of samples kept per chain
    thin_by = nsc / min(fit.beta_0.ess, fit.beta_1.ess)
    thin_by = int(ceil(thin_by))
    print('Thinning chains by', thin_by)

    figure()
    xlabel(r'$\beta_0$')
    ylabel(r'$\beta_1$')

    # Go through chains.
    nc = fit.chains.shape[1]
    for c in range(nc):
        b0 = fit.beta_0.chains[::thin_by,c]
        b1 = fit.beta_1.chains[::thin_by,c]
        scatter(b0, b1, s=15, c='b', linewidths=0, alpha=.2)

    # Thin-lined crosshair showing true values:
    xhair = dict(c='k', ls=':', lw=1.5, alpha=.5)
    axvline(beta_0, **xhair)
    axhline(beta_1, **xhair)

