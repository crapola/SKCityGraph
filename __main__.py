import graphviz

graph_attr={'rankdir':'LR'}
node_attr={'style':'filled','fillcolor':'#FFFFFF','color':'#000000','shape':'rectangle'}
edge_attr={'color':'#FFAA00'}

g=graphviz.Digraph('City tree','Comment','tree',None,'svg',None,None,
	graph_attr,node_attr,edge_attr)


# First char must be < not a newline

longtext="""Lorem ipsum dolor sit amet, consectetur adipiscing elit,<br align="left"/>
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.<br align="left"/>
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut<br align="left"/>
aliquip ex ea commodo consequat.<br align="left"/>
"""

label="""<
<TABLE border="0" cellpadding="1" cellspacing="0">
<TR>
	<TD>
		<IMG SRC="test.png"/>
	</TD>
	<TD>
		<TABLE border="0" cellborder="1" cellspacing="0" cellpadding="2">
			<TR><TD align="left">Name</TD></TR>
			<TR><TD align="left" height="80%">"""+longtext+"""</TD></TR>
			<TR><TD align="left">9000</TD></TR>
		</TABLE>
	</TD>
</TR>
</TABLE>
>"""

nodes=(
('A',{'label':label}),
('B',{}),
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