<html>
<head>
  <%block name="header"/>
  <link rel="stylesheet" href="/static/master.css" />
</head>
<body>
  <header><h4>
	<a href="/">Home/</a>
  %for p in parents:
	<a href="/${p.path}">${p.name}</a>
  %endfor
  	${filename}
  </h4></header>
  <nav>
    <ul>
    %for node in nodes:
	  <li><a href="/${node.path}">${node.name}</a></li>
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

