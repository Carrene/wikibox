<html>
<head>
    <title>WikiBox</title>
</head>
<body>
    <h1>WSGI environ</h1>
    <ul>
    %for key, value in environ.items():
      <li><b>${key}:</b> ${value}</li>
    %endfor
    </ul>
</body>
</html>

