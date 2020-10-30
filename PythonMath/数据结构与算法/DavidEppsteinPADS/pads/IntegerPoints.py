"""IntegerPoints.py

Space-efficient streaming algorithms to generate all integer points (x,y)
of the Euclidean plane, in order by distance from the origin,
as described at http://11011110.livejournal.com/332116.html

D. Eppstein, July 2016.
"""

import unittest
from BucketQueue import BucketQueue
from Sequence import Sequence

def IntegerPointsByDistance():
    """All integer points in order by distance, regardless of sign.
    The space needed to generate the first N points is O(N^{1/3}).
    Each point is generated in constant amortized time."""

    # Start out by generating the two initial points of the hull
    yield (0,0)
    yield (0,1)

    # Data structures: hull, a sequence of edges, and queue, a bucket queue
    # Each point is represented as a tuple (x,y) of integer coordinates
    # Each edge is an object with instance attributes
    #    corner -- the point at its counterclockwise end
    #    unit -- the difference between the corner and the
    #            next grid point that lies on the same edge
    #            (which is not necessarily the other endpoint)
    #    beyond -- the next point beyond the edge, in its rectangle
    class edge:
        def __init__(self,corner,unit,beyond):
            self.corner = corner
            self.unit = unit
            self.beyond = beyond

    e = edge((0,0),(0,1),(-1,0))
    f = edge((0,1),(0,-1),(1,0))
    hull = Sequence([e,f])

    def dist2(p):
        """Squared Euclidean distance of a point from the origin"""
        return p[0]**2 + p[1]**2

    def prioritize(e):
        """Include edge e in the priority queue with its correct priority"""
        queue[e] = dist2(e.beyond)

    queue = BucketQueue()
    prioritize(e)
    prioritize(f)

    def box(p,u,b):
        """Given an edge with corner p and unit u, find a boxed translate of b."""
        dot = (b[0]-p[0])*u[0]+(b[1]-p[1])*u[1]
        shift = dot//dist2(u)
        b = (b[0]-shift*u[0],b[1]-shift*u[1])
        if abs(u[0]) + abs(u[1]) == 1:  # Unit square has 2 boxed xlates, pick best
            c = (b[0]+u[0],b[1]+u[1])
            if dist2(c) < dist2(b):
                return c
        return b

    def nonconvex(e):
        """Are e and its successor not strictly convex?"""
        u = e.unit
        v = hull.successor(e).unit
        return u[1]*v[0]-u[0]*v[1] <= 0

    def pop(e):
        """Merge e into its successor (removing the successor from the hull)"""
        f = hull.successor(e)
        if e.unit == f.unit:    # Special case flat vertex
            if dist2(f.beyond) < dist2(e.beyond):
                e.beyond = f.beyond
        else:                   # Concave vertex, use opp vertex of parallelogram
            p = e.corner
            q = f.corner
            r = hull.successor(f).corner
            e.unit = (r[0]-p[0],r[1]-p[1])
            e.beyond = (p[0]-q[0]+r[0],p[1]-q[1]+r[1])
        hull.remove(f)
        del queue[f]
        prioritize(e)
    
    def split(e):
        """Update the hull after adding e's beyond point"""
        p = e.corner
        q = hull.successor(e).corner
        u = e.unit
        b = e.beyond
        e.unit = (b[0]-p[0],b[1]-p[1])
        e.beyond = box(p,e.unit,(b[0]-u[0],b[1]-u[1]))
        fu = (q[0]-b[0],q[1]-b[1])
        fb = box(b,fu,(q[0]+u[0],q[1]+u[1]))
        f = edge(b,fu,fb)
        hull.insertAfter(e,f)
        prioritize(e)
        prioritize(f)
        while nonconvex(hull.predecessor(e)):
            pop(hull.predecessor(e))
            e = hull.predecessor(f)
        while nonconvex(f):
            pop(f)

    for e in queue:
        yield e.beyond
        split(e)

# ============================================================
#     If run from command line, perform unit tests
# ============================================================

class IntegerPointsByDistanceTest(unittest.TestCase):
    radius = 100
    threshold = radius**2
    trange = range(-radius,radius+1)

    def testOrdered(self):
        """Test whether point ordering is by distance."""
        oldDistance = 0
        for x,y in IntegerPointsByDistance():
            newDistance = x**2 + y**2
            self.assertTrue(newDistance >= oldDistance)
            oldDistance = newDistance
            if newDistance > IntegerPointsByDistanceTest.threshold:
                break

    def testCircle(self):
        """Test whether each point in a disk is listed exactly once."""
        points = []
        for x,y in IntegerPointsByDistance():
            if x**2 + y**2 > IntegerPointsByDistanceTest.threshold:
                break
            points.append((x,y))
        self.assertEqual(len(points),len(set(points)))
        self.assertEqual(len(points),len(
            [None for x in IntegerPointsByDistanceTest.trange
             for y in IntegerPointsByDistanceTest.trange
             if x**2 + y**2 <= IntegerPointsByDistanceTest.threshold]))

if __name__ == "__main__":
    unittest.main()   
