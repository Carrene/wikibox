<html>
  <body>
    <div class="header">
      <%block name="header"/>
    </div>

    ${self.body()}

    <div class="footer">
      <%block name="footer">
        this is the footer
      </%block>
    </div>
  </body>
</html>

