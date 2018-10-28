<html>
<head>
  <%block name="header"/>
  <link href="https://fonts.googleapis.com/css?family=Roboto:300,500,700" rel="stylesheet">
  <link rel="stylesheet" href="/static/master.css" />
  <link rel="stylesheet" href="/static/syntax-vim.css" />
</head>
<body class="${'no-nav' if hide_navigation else 'with-nav'}">
  <header>
    <h1>WIKI.CARRENE.COM</h1>
    <div class="breadcrumbs">
        <div class="path">
            <a href="/"></a>
        </div>
        %for p in parents:
        <div class="path">
	        <a href="/${p.path}">${p.title}</a>
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
    </div>
    %endif
  </header>
  %if not hide_navigation:
  <nav>
    <ul>
    %for node in nodes:
	  <li>
	    <a href="/${node.path}" title="${node.realname}">
	        %if filename == node.realname:
                <span class="verb selected">${node.verb}</span>
                <span class="subject selected">${node.subject}</span>
                <span class="selected">${node.title}</span>
	        %else:
                %if not node.isdirectory:
                    <span class="verb">${node.verb}</span>
                    <span class="subject">${node.subject}</span>
                %endif
                <span>${node.title}</span>
	        %endif
	    </a>
	    %if node.isdirectory:
	    <img src="./../static/images/chevron-right.svg" />
	    %endif
	  </li>
    %endfor
	</ul>
  </nav>
  %endif
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

