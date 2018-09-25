
let headers = document.querySelectorAll('main h1, main h2, main h3, main h4')

if (headers.length) {
  for (header of headers) {
    let textNode = document.createTextNode(header.innerText)
    let headerId = header.id
    let link = document.createElement('a')
    header.innerText = ''
    link.appendChild(textNode)
    link.setAttribute('href', `#${headerId}`)
    header.appendChild(link)

    // Adding the legend icon

    if (textNode.substringData(0, 4) === 'LIST') {
      let legendLinkElement = document.createElement('a')
      legendLinkElement.setAttribute('href', `LEGEND-restfulpy--v*.md?nonav=true`)
      legendLinkElement.setAttribute('target', '_blank')
      let helpIcon = document.createElement('img')
      helpIcon.setAttribute('src', `${window.location.origin}/static/images/help.svg`)
      legendLinkElement.appendChild(helpIcon)
      header.appendChild(legendLinkElement)
    }
  }
}

let pdfButton = document.getElementById('pdf')

if (pdfButton) {
  pdfButton.addEventListener('click', () => {
    let title = document.querySelector('#main title').text
    let filename = title.split('/')[title.split('/').length - 1]

    var doc = new jsPDF()
    var source = document.getElementById("main")
    doc.fromHTML(
      source,
      15,
      15,
      {
        width: 180
      })
    doc.save(`${filename}.pdf`)
  })
}

let printButton = document.getElementById('print')

if (printButton) {
  printButton.addEventListener('click', () => {
    window.print()
  })
}
