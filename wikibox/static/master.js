
let pdfButton = document.getElementById('pdf')
let printButton = document.getElementById('print')

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
