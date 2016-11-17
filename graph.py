import graphviz

def citygraph_node(internal_name,icon,display_name,description,cost):
	"""
	Create a node stylized for our graph.

	Parameters
	----------
	icon,name,description,cost : str
		icon must be full path to picture.
		description may have <BR/> newlines.

	Returns
	-------
	(str,dict)
		The node identified by internal_name and its params.
	"""
	html="""<
	<TABLE border="0" cellpadding="0" cellspacing="0" color="#880000">
	<TR>
		<TD width="64" height="64" fixedsize="true" >
			<IMG SRC="{0}"/>
		</TD>
		<TD>
			<TABLE border="0" cellborder="1" cellspacing="0" cellpadding="2">
				<TR><TD align="left">{1}</TD></TR>
				<TR><TD align="left" balign="left" valign="top"><FONT color="#AAAAAA" point-size="10">{2}</FONT></TD></TR>
				<TR><TD align="left"><FONT color="#AA8800">{3}</FONT></TD></TR>
			</TABLE>
		</TD>
	</TR>
	</TABLE>
	>"""
	label=html.format(icon,display_name,description,str(cost))
	return (internal_name,{'label':label,'margin':'0.04'})