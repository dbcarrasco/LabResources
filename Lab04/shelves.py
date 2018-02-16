"""
Utility function for plotting a PMF as a histogram-like shelf plot.

2018-02-16 by Tom Loredo for BDA
"""


from matplotlib.pyplot import *


def shelves(hts, lo=0, hi=1, fmt='b-', ends=False, dy=False):
    """
    Plot piecewise-constant "shelves" with ordinates in `hts`, evenly spaced
    from `lo` to `hi`.  Plot the lines with the specified format.
    
    If ends==True, plot end segments to 0.
    
    If dy != False, shift all heights by dy (e.g., to offset the
    curve to make it more visible in a multi-curve plot).
    """
    n = len(hts)
    if dy:
        hts = hts + dy
    step = 1./n
    left = lo
    xvals = []
    yvals = []
    if ends:
        xvals.append(left)
        yvals.append(0.)
    for i in range(n):
        xvals.append(left)
        yvals.append(hts[i])
        xvals.append(left+step)
        yvals.append(hts[i])
        left += step
    if ends:
        xvals.append(left)
        yvals.append(0.)
    plot(xvals, yvals)
