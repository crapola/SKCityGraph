import graphviz

graph_attr={'rankdir':'LR','bgcolor':'#444444'}
node_attr={'style':'filled','fillcolor':'#002244','color':'#FF0000','shape':'rectangle',
	'fontname':'Verdana','fontsize':'11.0','fontcolor':'#FFFFFF'}
edge_attr={'color':'#FFAA00'}

g=graphviz.Digraph('City tree','Comment','tree',None,'svg',None,None,
	graph_attr,node_attr,edge_attr)

longtext="""Lorem ipsum dolor sit amet, consectetur adipiscing elit,<br/>
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.<br/>
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut<br/>
aliquip ex ea commodo consequat.<br align="left"/>
"""
# First char must be < not a newline

label="""<
<TABLE border="0" cellpadding="0" cellspacing="0">
<TR>
	<TD width="64" height="64" fixedsize="true" >
		<IMG SRC="test.png"/>
	</TD>
	<TD>
		<TABLE border="0" cellborder="1" cellspacing="0" cellpadding="2">
			<TR><TD align="left">Name</TD></TR>
			<TR><TD align="left" balign="left" valign="top" height="80%">"""+longtext+"""</TD></TR>
			<TR><TD align="left">9001</TD></TR>
		</TABLE>
	</TD>
</TR>
</TABLE>
>"""

nodes=(
('A',{'label':label,
	'margin':'0.04',
	'imagescale':'true'}),
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