<html>
<head>
  <%block name="header"/>
  <link href="https://fonts.googleapis.com/css?family=Roboto:300,500,700" rel="stylesheet">
  <link rel="stylesheet" href="/static/master.css" />
  <link rel="stylesheet" href="/static/syntax-vim.css" />
  <script src="https://html2canvas.hertzen.com/dist/html2canvas.js"></script>
  <script src="https://unpkg.com/jspdf@latest/dist/jspdf.min.js"></script>
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
            <img src="./../../static/images/print.svg" alt="Print" id="print">
        </div>
        <div>
            <img src="./../../static/images/pdf.svg" alt="Export as PDF" id="pdf">
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
  <main id="main">
  	${self.body()}
  </main>

  <footer>
    <%block name="footer">
    </%block>
  </footer>

  <script src="/static/master.js" type="text/javascript"></script>
</body>
</html>

