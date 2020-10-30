"""CirclePack.py
Compute circle packings according to the Koebe-Thurston-Andreev theory,
Following a numerical algorithm by C. R. Collins and K. Stephenson,
"A Circle Packing Algorithm", Comp. Geom. Theory and Appl. 2003.
"""

from math import pi,acos,asin,sin,e

tolerance = 1+10e-12    # how accurately to approximate things

# ======================================================
#   The main circle packing algorithm
# ======================================================

def CirclePack(internal,external):
    """Find a circle packing for the given data.
    The two arguments should be dictionaries with disjoint keys; the
    keys of the two arguments are identifiers for circles in the packing.
    The internal argument maps each internal circle to its cycle of
    surrounding circles; the external argument maps each external circle
    to its desired radius. The return function is a mapping from circle
    keys to pairs (center,radius) where center is a complex number."""
    
    # Some sanity checks and preprocessing
    if min(external.values()) <= 0:
        raise ValueError("CirclePack: external radii must be positive")
    radii = dict(external)
    for k in internal:
        if k in external:
            raise ValueError("CirclePack: keys are not disjoint")
        radii[k] = 1

    # The main iteration for finding the correct set of radii
    lastChange = 2
    while lastChange > tolerance:
        lastChange = 1
        for k in internal:
            theta = flower(radii,k,internal[k])
            hat = radii[k]/(1/sin(theta/(2*len(internal[k])))-1)
            newrad = hat * (1/(sin(pi/len(internal[k]))) - 1)
            kc = max(newrad/radii[k],radii[k]/newrad)
            lastChange = max(lastChange,kc)
            radii[k] = newrad

    # Recursively place all the circles
    placements = {}
    k1 = next(iter(internal))   # pick one internal circle
    placements[k1] = 0j         # place it at the origin
    k2 = internal[k1][0]        # pick one of its neighbors
    placements[k2] = radii[k1]+radii[k2] # place it on the real axis
    place(placements,radii,internal,k1)  # recursively place the rest
    place(placements,radii,internal,k2)

    return dict((k,(placements[k],radii[k])) for k in radii)

# ======================================================
#   Invert a collection of circles
# ======================================================

def InvertPacking(packing,center):
    """Invert with specified center"""
    result = {}
    for k in packing:
        z,r = packing[k]
        z -= center
        if z == 0:
            offset = 1j
        else:
            offset = z/abs(z)
        p,q = z-offset*r,z+offset*r
        p,q = 1/p,1/q
        z = (p+q)/2
        r = abs((p-q)/2)
        result[k] = z,r
    return result

def NormalizePacking(packing,k=None,target=1.0):
    """Make the given circle have radius one (or the target if given).
    If no circle is given, the minimum radius circle is chosen instead."""
    if k is None:
        r = min(r for z,r in packing.values())
    else:
        z,r = packing[k]
    s = target/r
    return dict((kk,(zz*s,rr*s)) for kk,(zz,rr) in packing.iteritems())

def InvertAround(packing,k,smallCircles=None):
    """Invert so that the specified circle surrounds all the others.
    Searches for the inversion center that maximizes the minimum radius.
    
    This can be expressed as a quasiconvex program, but in a related
    hyperbolic space, so rather than applying QCP methods it seems
    simpler to use a numerical hill-climbing approach, relying on the
    theory of QCP to tell us there are no local maxima to get stuck in.
    
    If the smallCircles argument is given, the optimization
    for the minimum radius circle will look only at these circles"""
    z,r = packing[k]
    if smallCircles:
        optpack = {k:packing[k] for k in smallCircles}
    else:
        optpack = packing
    q,g = z,r*0.4
    oldrad,ratio = None,2
    while abs(g) > r*(tolerance-1) or ratio > tolerance:
        rr,ignore1,ignore2,q = max(list(testgrid(optpack,k,z,r,q,g)))
        if oldrad:
            ratio = rr/oldrad
        oldrad = rr
        g *= 0.53+0.1j  # rotate so not always axis-aligned
    return InvertPacking(packing,q)  


# ======================================================
#   Utility routines, not for outside callers
# ======================================================

def acxyz(x,y,z):
    """Angle at a circle of radius x given by two circles of radii y and z"""
    try:
        return acos(((x+y)**2 + (x+z)**2 - (y+z)**2)/(2.0*(x+y)*(x+z)))
    except ValueError:
        return pi/3
    except ZeroDivisionError:
        return pi

def flower(radius,center,cycle):
    """Compute the angle sum around a given internal circle"""
    return sum(acxyz(radius[center],radius[cycle[i-1]],radius[cycle[i]])
               for i in range(len(cycle)))

def place(placements,radii,internal,center):
    """Recursively find centers of all circles surrounding k"""
    if center not in internal:
        return
    cycle = internal[center]
    for i in range(-len(cycle),len(cycle)-1):
        if cycle[i] in placements and cycle[i+1] not in placements:
            s,t = cycle[i],cycle[i+1]
            theta = acxyz(radii[center],radii[s],radii[t])
            offset = (placements[s]-placements[center])/(radii[s]+radii[center])
            offset *= e**(-1j*theta)
            placements[t] = placements[center] + offset*(radii[t]+radii[center])
            place(placements,radii,internal,t)

def testgrid(packing,k,z,r,q,g):
    """Build grid of test points around q with grid size g"""
    for i in (-2,-1,0,1,2):
        for j in (-2,-1,0,1,2):
            center = q + i*g + j*1j*g
            if abs(center-z) < r:
                newpack = InvertPacking(packing,center)
                newpack = NormalizePacking(newpack,k)
                minrad = min(r for z,r in newpack.values())
                yield minrad,i,j,center
