"""readUndirectedGraph.py

Parse various undirected graph formats

readUndirectedGraph(arg) takes an argument which may be a file object,
string, or list of strings, and returns a parsed undirected graph.

Various input formats are supported and automatically detected:

 - MALF, edge list, and node edge list format documentation is at
   http://loki.cs.brown.edu:8081/graphserver/gds/formats.shtml

 - GraphML format doc is at http://graphml.graphdrawing.org/

 - graph6 and sparse6 doc is at http://cs.anu.edu.au/~bdm/data/formats.txt

 - LEDA.GRAPH documentation is at
   http://www.algorithmic-solutions.info/leda_guide/graphs/leda_native_graph_fileformat.html

The output is a dict mapping vertices to adjacency lists (also dicts).
Each vertex is either a unique integer or a string.
Each adjacency list maps neighbors to edge ids, either unique integers or strings.
Each edge is represented twice, once for each endpoint.

Only the graph structure itself is returned; any additional information may be lost.

D. Eppstein, UC Irvine, August 12, 2003.
"""

class GraphFormatError(Exception):
	pass

def graphNum(s):
	"""Parse s as an integer, complain appropriately if it fails."""
	try:
		return int(s)
	except:
		raise GraphFormatError, 'Number expected: "%s"' % s

def graph():
	"""Create a new empty graph."""
	return {}
	
def vertex(G, v):
	"""Add new vertex v to graph G."""
	if v in G:
		raise GraphFormatError, 'Duplicate vertex %s', str(v)
	G[v] = {}

def edge(G,u,v,e):
	"""Add edge e connecting vertices u and v in graph G.  Vertices must already be in G."""
	if u == v:
		raise GraphFormatError, 'Self-loop at %s' % str(u)
	if u not in G:
		raise GraphFormatError, 'Unexpected vertex %s in edge to %s' % (str(u),str(v))
	if v not in G:
		raise GraphFormatError, 'Unexpected vertex %s in edge from %s' % (str(v),str(u))
	G[u][v] = G[v][u] = e


# ==========================================================================
#		MALF format
# ==========================================================================

def readMALF(lines):
	"""Read undirected graph in MALF format."""
	G = graph()
	lines = iter(filter(None,lines))
	for line in lines:
		if line == '#':
			break
		n = graphNum(line.split()[0])
		if n != len(G)+1:
			raise GraphFormatError, 'Nonconsecutive vertices in MALF'
		vertex(G,n)

	m = 0
	for line in lines:
		nums = [graphNum(x) for x in line.split()]
		m += 1
		if len(nums) != 4:
			raise GraphFormatError, "Other than four numbers per line in MALF edge list"
		elif nums[0] != m:
			raise GraphFormatError, 'Nonconsecutive edges in MALF'
		elif nums[1] != 0:
			raise GraphFormatError, "Unrecognized edge type in MALF edge list"
		edge(G,nums[2],nums[3],m)

	return G


# ==========================================================================
#		Edge list format
# ==========================================================================
	
def readEdgeList(lines):
	"""Read undirected graph in edge list format."""
	G = graph()
	m = 0
	for line in filter(None,lines):
		words = line.split()
		if len(words) < 2 or len(words) > 3:
			raise GraphFormatError, 'Wrong number of words in edge list: "%s"' % line
		if len(words) == 3 and words[1] != '-':
			raise GraphFormatError, 'Unrecognized edge type "%s" in edge list' % words[1]
		u, v = words[0], words[-1]
		if u not in G:
			vertex(G, u)
		if v not in G:
			vertex(G, v)
		m = m + 1
		edge(G, u, v, m)

	return G


# ==========================================================================
#		Node edge list format
# ==========================================================================
	
def readNodeEdgeList(lines):
	"""Read undirected graph in node edge list format."""
	G = graph()
	EdgeNames = {}
	lines = iter(filter(None,lines))
	numEdges = [0]

	def addVertex(line):
		vertex(G, line)

	def addEdge(line, id):
		u = line
		v = next(lines)
		if v.startswith('//'):
			raise GraphFormatError, 'Missing edge endpoint in node edge list'
		edge(G, u, v, id)
		numEdges[0] += 1

	def anonEdge(line):
		return addEdge(line, numEdges[0]+1)
		
	def namedEdge(line):
		id = line
		if id in EdgeNames:
			raise GraphFormatError, 'Edge name "%s" used twice in node edge list' % id
		addEdge(next(lines), id)
		EdgeNames[id] = id
		
	def noActionYet(line):
		raise GraphFormatError, 'No section yet in node edge list'
		
	actions = {
		'nodes': addVertex,
		'edges': anonEdge,
		'named edges': namedEdge,
	}
	action = noActionYet
	
	for line in lines:
		if line.startswith('// '):
			try:
				action = actions[line[3:]]
			except KeyError:
				raise GraphFormatError, 'Unrecognized section "%s" in node edge list' % line[3:]
		else:
			action(line)

	return G


# ==========================================================================
#		GraphML format
# ==========================================================================
	
def readGraphML(lines):
	"""Read undirected graph in GraphML format."""
	context = []
	G = graph()
	edgecounter = [0]
	defaultDirectedness = ['true']
	
	def start_element(name,attrs):
		context.append(name)
		if len(context) == 1:
			if name != 'graphml':
				raise GraphFormatError, 'Unrecognized outer tag "%s" in GraphML' % name
		elif len(context) == 2 and name == 'graph':
			if 'edgedefault' not in attrs:
				raise GraphFormatError, 'Required attribute edgedefault missing in GraphML'
			if attrs['edgedefault'] == 'undirected':
				defaultDirectedness[0] = 'false'
		elif len(context) == 3 and context[1] == 'graph' and name == 'node':
			if 'id' not in attrs:
				raise GraphFormatError, 'Anonymous node in GraphML'
			vertex(G, attrs['id'])
		elif len(context) == 3 and context[1] == 'graph' and name == 'edge':
			if 'source' not in attrs:
				raise GraphFormatError, 'Edge without source in GraphML'
			if 'target' not in attrs:
				raise GraphFormatError, 'Edge without target in GraphML'
			if attrs.get('directed', defaultDirectedness[0]) != 'false':
				raise GraphFormatError, 'Directed edge in GraphML'
			edge(G, attrs['source'], attrs['target'], edgecounter[0])
			edgecounter[0] += 1			
		
	def end_element(name):
		context.pop()
	
	import xml.parsers.expat
	p = xml.parsers.expat.ParserCreate()
	p.StartElementHandler = start_element
	p.EndElementHandler = end_element
	for line in lines:
		p.Parse(line)
	p.Parse("", 1)
	return G


# ==========================================================================
#		Graph6 and Sparse6 format
# ==========================================================================
	
def graph6data(str):
	"""Convert graph6 character sequence to 6-bit integers."""
	v = [ord(c)-63 for c in str]
	if min(v) < 0 or max(v) > 63:
		return None
	return v
	
def graph6n(data):
	"""Read initial one or four-unit value from graph6 sequence.  Return value, rest of seq."""
	if data[0] <= 62:
		return data[0], data[1:]
	return (data[1]<<12) + (data[2]<<6) + data[3], data[4:]

def readGraph6(str):
	"""Read undirected graph in graph6 format."""
	if str.startswith('>>graph6<<'):
		str = str[10:]
	data = graph6data(str)
	n, data = graph6n(data)
	nd = (n*(n-1)//2 + 5) // 6
	if len(data) != nd:
		raise GraphFormatError, 'Expected %d bits but got %d in graph6' % (n*(n-1)//2, len(data)*6)

	def bits():
		"""Return sequence of individual bits from 6-bit-per-value list of data values."""
		for d in data:
			for i in [5,4,3,2,1,0]:
				yield (d>>i)&1
				
	nEdges = 0
	G = graph()
	for i in range(n):
		vertex(G, i)

	for (i,j),b in zip([(i,j) for j in range(1,n) for i in range(j)], bits()):
		if b:
			edge(G, i, j, nEdges)
			nEdges += 1

	return G
					
def readSparse6(str):
	"""Read undirected graph in sparse6 format."""
	if str.startswith('>>sparse6<<'):
		str = str[10:]
	if not str.startswith(':'):
		raise GraphFormatError, 'Expected colon in sparse6'
	n, data = graph6n(graph6data(str[1:]))
	k = 1
	while 1<<k < n:
		k += 1
	
	def parseData():
		"""Return stream of pairs b[i], x[i] for sparse6 format."""
		chunks = iter(data)
		d = None	# partial data word
		dLen = 0	# how many unparsed bits are left in d

		while 1:
			if dLen < 1:
				d = next(chunks)
				dLen = 6
			dLen -= 1
			b = (d>>dLen) & 1	# grab top remaining bit
			
			x = d & ((1<<dLen)-1) 	# partially built up value of x
			xLen = dLen				# how many bits included so far in x
			while xLen < k:			# now grab full chunks until we have enough
				d = next(chunks)
				dLen = 6
				x = (x<<6) + d
				xLen += 6
			x = (x >> (xLen - k))	# shift back the extra bits
			dLen = xLen - k
			yield b,x
	
	v = 0
	G = graph()
	nEdges = 0
	for i in range(n):
		vertex(G, i)

	for b,x in parseData():
		if b: v += 1
		if x >= n: break			# padding with ones can cause overlarge number here
		elif x > v: v = x
		else:
			edge(G, x, v, nEdges)
			nEdges += 1

	return G


# ==========================================================================
#		LEDA.GRAPH format
# ==========================================================================
	
def ledaLines(lines):
	"""Filter sequence of lines to keep only the relevant ones for LEDA.GRAPH"""
	def relevant(line):
		return line and not line.startswith('#')
	return filter(relevant, lines)
	
def readLeda(lines):
	"""Parse filtered LEDA.GRAPH format file."""
	lines = iter(lines)
	for i in range(3):
		next(lines)			    # skip header lines
	G = graph()

	n = graphNum(next(lines))	# number of vertices
	for i in range(n):
		vertex(G, i+1)
		next(lines)			    # skip LEDA data
	
	m = graphNum(next(lines))	# number of edges
	for i in range(m):
		words = next(lines).split()
		if len(words) < 4:
			raise GraphFormatError, 'Too few fields in LEDA.GRAPH edge %d' % (i+1)
		source = graphNum(words[0])
		target = graphNum(words[1])
		reversal = graphNum(words[2])
		if not reversal:
			raise GraphFormatError, 'Edge %d is directed in LEDA.GRAPH' % (i+1)
		if source < target:
			edge(G, source, target, i+1)
	
	return G


# ==========================================================================
#		Main entry
# ==========================================================================

def readUndirectedGraph(arg):
	"""Parse graph and return in modified GvR format.
	Argument may be a file object, a single string, or a sequence of lines.
	"""
	if isinstance(arg,file):
		lines = [L.strip() for L in arg]
	elif isinstance(arg,str) or isinstance(arg,unicode):
		lines = [arg]
	else:
		lines = list(arg)

	# Test out different possible formats,
	# ordered from more distinctive to more ambiguous.
	
	# Graph6 and Sparse6
	if len(lines) == 1:
		line = lines[0]
		if line.startswith('>>graph6<<') or graph6data(line):
			return readGraph6(line)
		elif line.startswith('>>sparse6<<') or \
				(line.startswith(':') and graph6data(line[1:])):
			return readSparse6(line)
			
	# LEDA.GRAPH
	leda = ledaLines(lines)
	if leda and leda[0] == 'LEDA.GRAPH':
		return readLeda(leda)

	# GraphML
	if lines[0].startswith("<"):
		return readGraphML(lines)
		
	# Node edge list
	if lines[0].startswith("//"):
		return readNodeEdgeList(lines)
		
	# MALF
	if '#' in lines:
		return readMALF(lines)

	# Edge list
	return readEdgeList(lines)
