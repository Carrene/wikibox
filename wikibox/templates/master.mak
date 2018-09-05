<html>
<head>
  <%block name="header"/>
  <link rel="stylesheet" href="/static/master.css" />
</head>
<body>
  <nav>
    <ul>
	  <li>aaaa</li>
	</ul>
  </nav>
  <main>
  	${self.body()}
  </main>

  <footer>
    <%block name="footer">
      this is the footer
    </%block>
  </footer>
</body>
</html>

