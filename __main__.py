import sk
import graphviz
import graph

sk.check_path()

elist=sk.extract_improvements(sk.load_improvements())

g=graph.citygraph()

longtext="""Lorem ipsum dolor sit amet, consectetur adipiscing elit,<br/>
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.<br/>
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut<br/>
aliquip ex ea commodo consequat.<br/>
"""

nodes=(
graph.citygraph_node('A','test.png','Display Name!',longtext,112212),
graph.citygraph_node('B','test.png','Display Name!22','blah...',212),
('Z',{}),
('Unit12435',{})
)
edges=(('A','B'),('B','Z'))

for x in nodes:
	g.node(x[0],**x[1])

g.edges(edges)

try:
	f=g.render()
except RuntimeError as r:
	print("Rendering failed:",r)