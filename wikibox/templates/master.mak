<html>
<head>
  <%block name="header"/>
  <link href="https://fonts.googleapis.com/css?family=Roboto:300,500,700" rel="stylesheet">
  <link rel="stylesheet" href="/static/master.css" />
  <link rel="stylesheet" href="/static/syntax-vim.css" />
</head>
<body>
  <header>
    <h1>WIKI.CARRENE.COM</h1>
    <div class="breadcrumbs">
        <div class="path">
            <a href="/"></a>
        </div>
        %for p in parents:
        <div class="path">
	        <a href="/${p.path}">${p.name}</a>
        </div>
        %endfor
        %if filename:
  	    <div class="path file">
  	        <p>${filename}</p>
  	    </div>
  	    %endif
    </div>
    %if filename:
    <div class="actions">
        <div>
            <img src="./../../static/images/print.svg" alt="Print">
        </div>
        <div>
            <img src="./../../static/images/pdf.svg" alt="Export as PDF">
        </div>
    </div>
    %endif
  </header>
  <nav>
    <ul>
    %for node in nodes:
	  <li>
	    <a href="/${node.path}" title="${node.name}">${node.name}</a>
	    %if node.name[-1] == '/':
	    <img src="./../static/images/chevron-right.svg" />
	    %endif
	  </li>
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

