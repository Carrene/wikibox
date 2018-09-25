
let pdfButton = document.getElementById('pdf')
let printButton = document.getElementById('print')
let headers = document.querySelectorAll('main h1, main h2, main h3, main h4')
for (header of headers) {
  let textNode = document.createTextNode(header.innerText)
  let headerId = header.id
  let link = document.createElement('a')
  header.innerText = ''
  link.appendChild(textNode)
  link.setAttribute('href', `#${headerId}`)
  header.appendChild(link)
}

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

if (printButton) {
  printButton.addEventListener('click', () => {
    window.print()
  })
}
