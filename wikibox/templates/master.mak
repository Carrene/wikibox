<html>
<head>
  <%block name="header"/>
  <link rel="stylesheet" href="/static/master.css" />
</head>
<body>
  <header><h4>${virtual_path}</h4></header>
  <nav>
    <ul>
    %for node in nodes:
	<li><a href="${node.path}">
	  ${node.name}${'/' if node.isdirectory else ''}
	</a></li>
    %endfor
	</ul>
  </nav>
  <main>
  	${self.body()}
  </main>

  <footer>
    <%block name="footer">
    </%block>
  </footer>
</body>
</html>

