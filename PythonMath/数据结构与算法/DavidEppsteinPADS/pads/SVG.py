"""SVG.py

Simple generation of SVG-format vector graphics files

D. Eppstein, November 2011.
"""

def _coord(x):
    """String representation for coordinate"""
    return ("%.4f" % x).rstrip("0").rstrip(".")

class SVG:
    def __init__(self, bbox, stream,
               standalone=True, prefix=None, indentation=0):
        """Create a new SVG object, to be written to the given stream.
        If standalone is True or omitted, the SVG object becomes a whole
        XML file; otherwise, it becomes an XML object within a larger XML
        file. If the prefix is nonempty, it is used to distinguish svg tags
        from other tags; a reasonable choice for the prefix value would be
        "s" or "svg". If the indentation is nonzero, it gives a number of
        spaces by which every line of the file is indented.
        
        The bbox argument should be a complex number, the farthest visible
        point from the origin in the positive quadrant. The bounding box
        will become the rectangle between the origin and that point.
        All other methods that specify points should do so using
        complex number coordinates."""
        self.stream = stream
        if prefix:
            self.prefix = prefix + ":"
        else:
            self.prefix = ""
        if standalone:
            self.stream.write('''<?xml version="1.0"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
''')
        self.indentation = indentation
        self.nesting = 0
        br = _coord(bbox.real)
        bi = _coord(bbox.imag)
        self.element('''svg width="%s" height="%s" viewBox="0 0 %s %s"
     xmlns="http://www.w3.org/2000/svg" version="1.1"''' % (br,bi,br,bi),+1)

    def close(self):
        """Output the end of an SVG file."""
        self.element("svg", -1)
        if self.nesting:
            raise Exception("SVG: Unclosed tags")

    def element(self, e, delta=0, unspaced=False, style={}, **morestyle):
        """Output an SVG element.
        The delta argument distinguishes between XML tags that
        open a nested section of the XML file (delta=+1), XML tags
        that close the same section (delta=-1), and XML tags that
        stand alone without anything nested inside them (delta=0).
        Every call with delta=+1 must be matched by a call with delta=-1.
        If the style argument is nonempty, it should be a dictionary
        of style parameters, included within the object; these
        may also be passed as keyword arguments to element.
        If the same keyword is present both in style and as a keyword
        argument, the keyword argument takes priority."""
        if delta < 0:
            self.nesting += delta
        if delta >= 0 or not unspaced:
            output = [" " * (self.indentation + 2*self.nesting), "<"]
        else:
            output = ["<"]
        if delta < 0:
            output.append("/")
        output += [self.prefix, e]
        style = dict(style)
        style.update(morestyle)
        if style:
            output.append(' style="')
            second = False
            for keyword in style:
                if second:
                    output.append("; ")
                second = True
                output += [keyword, ":", style[keyword]]
            output.append('"')
        if delta > 0:
            self.nesting += delta
        elif delta == 0:
            output.append("/")
        output.append(">")
        if delta <= 0 or not unspaced:
            output.append("\n")
        self.stream.write("".join(output))

    def group(self,style={},**morestyle):
        """Start a group of objects, all with the same style"""
        self.element("g", +1, style=style, **morestyle)

    def ungroup(self):
        """End a group of objects"""
        self.element("g", -1)

    def circle(self, center, radius, style={}, **morestyle):
        """Circle with given center and radius"""
        self.element('circle cx="%s" cy="%s" r="%s"' %
                (_coord(center.real), _coord(center.imag), _coord(radius)),
            style=style, **morestyle)

    def rectangle(self, p, q, style={}, **morestyle):
        """Rectangle with corners at points p and q"""
        x = min(p.real,q.real)
        y = min(p.imag,q.imag)
        width = abs((p-q).real)
        height = abs((p-q).imag)
        self.element('rect x="%s" y="%s" width="%s" height="%s"' %
                (_coord(x), _coord(x), _coord(width), _coord(height)),
            style=style, **morestyle)

    def polygon(self, points, style={}, **morestyle):
        """Polygon with corners at the given set of points"""
        pointlist = " ".join(_coord(p.real)+","+_coord(p.imag) for p in points)
        self.element('polygon points="%s"' % pointlist,
                     style=style, **morestyle)

    def segment(self, p, q, style={}, **morestyle):
        """Line segment from p to q"""
        self.element('line x1="%s" y1="%s" x2="%s" y2="%s"' % 
                     (_coord(p.real), _coord(p.imag),
                      _coord(q.real), _coord(q.imag)), style=style, **morestyle)

    def arc(self, p, q, r, large=False, style={}, **morestyle):
        """Circular arc from p to q with radius r.
        If the large flag is set true, the arc will cover more than
        half of a circle. The SVG "sweep-flag" is not provided;
        instead, to achieve the same effect, swap p and q."""
        if large:
            large = "1"
        else:
            large = "0"
        r = _coord(abs(r))
        self.element('path d="M %s,%s A %s,%s 0 %s 0 %s,%s"' %
                     (_coord(p.real),_coord(p.imag),r,r,large,
                      _coord(q.real),_coord(q.imag)), style=style, **morestyle)

    def text(self, label, location, style={}, **morestyle):
        """Text label at the given location.
        Caller is responsible for making the label xml-safe."""
        self.element('text x="%s" y="%s"' %
            (_coord(location.real),_coord(location.imag)),
            delta=1, unspaced=True, style=style, **morestyle)
        self.stream.write(label)
        self.element('text', delta=-1, unspaced=True)

# A small color palette chosen to have high contrast
# even when viewed by color-blind readers
class colors:
    none = "none"
    white = "#FFFFFF"
    black = "#000000"
    red = "#BC1E46"
    blue = "#0081CD"
    green = "#009246"
    yellow = "#FEC200"
    magenta = "#CC33CC"
