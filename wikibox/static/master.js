let headers = document.querySelectorAll(
  'main h1, main h2, main h3, main h4, main h5, main h6'
)

if (headers.length) {
  for (header of headers) {
    let headerId = header.id
    let textNode = document.createTextNode(header.innerText)

    // Creating the link icon

    let linkIconElement = document.createElement('a')
    linkIconElement.setAttribute('href', `#${headerId}`)
    linkIconElement.setAttribute('class', `link-icon`)
    let linkIcon = document.createElement('img')
    linkIcon.setAttribute(
      'src',
      `${window.location.origin}/static/images/link.svg`
    )
    linkIconElement.appendChild(linkIcon)
    linkIconElement.addEventListener('click', () => {
      navigator.clipboard.writeText(
        `${window.location.href.split('#')[0]}#${headerId}`
      )
    })

    // Adding link to header text

    let headerLink = document.createElement('a')
    header.innerText = ''
    headerLink.appendChild(textNode)
    headerLink.setAttribute('href', `#${headerId}`)

    header.appendChild(linkIconElement)
    header.appendChild(headerLink)

    // Adding the legend icon

    if (textNode.substringData(0, 4) === 'LIST') {
      let legendLinkElement = document.createElement('a')
      legendLinkElement.setAttribute(
        'href',
        `LEGEND-restfulpy--v*.md?nonav=true`
      )
      legendLinkElement.setAttribute('target', '_blank')
      legendLinkElement.setAttribute('class', 'legend-icon')
      let helpIcon = document.createElement('img')
      helpIcon.setAttribute(
        'src',
        `${window.location.origin}/static/images/help.svg`
      )
      legendLinkElement.appendChild(helpIcon)
      header.appendChild(legendLinkElement)
    }
  }
}

let printButton = document.getElementById('print')

if (printButton) {
  printButton.addEventListener('click', () => {
    window.print()
  })
}
