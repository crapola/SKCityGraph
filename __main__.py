import sk
import graphviz
from graph import citygraph_node

sk.check_path()

graph_attr={'rankdir':'LR','bgcolor':'#444444'}
node_attr={'style':'filled','fillcolor':'#220000','color':'#FFCC00','shape':'rectangle',
	'fontname':'Verdana','fontsize':'12.0','fontcolor':'#FFFFFF'}
edge_attr={'color':'#FFCC00'}

g=graphviz.Digraph('City Graph','A visualization...','tree',None,'svg',None,None,
	graph_attr,node_attr,edge_attr)

longtext="""Lorem ipsum dolor sit amet, consectetur adipiscing elit,<br/>
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.<br/>
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut<br/>
aliquip ex ea commodo consequat.<br/>
"""

nodes=(
citygraph_node('A','test.png','Display Name!',longtext,112212),
citygraph_node('B','test.png','Display Name!22','blah...',212),
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