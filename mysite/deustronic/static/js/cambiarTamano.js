const ajustes = document.getElementById('cambiarTamano');



// TAMAÑO DE FUENTE
const getFontSize = () =>
  parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--font-size'))

const aumentarTamano = element => {
  element.addEventListener('click', () => {
    let fontSize = getFontSize()
    document.documentElement.style.setProperty('--font-size', `${fontSize * 1.1}`)
    localStorage.setItem("fuente", fontSize)
  })
}

const bajarTamano = element => {
  element.addEventListener('click', () => {
    let fontSize = getFontSize()
    document.documentElement.style.setProperty('--font-size', `${fontSize * 0.9}`)
    localStorage.setItem("fuente", fontSize)
  })
}

addEventListener('keyup', e => {
  if (e.key === 'ArrowUp') document.getElementById('aumentarTamaño').click()
  if (e.key === 'ArrowDown') document.getElementById('bajarTamaño').click()
})

aumentarTamano(document.getElementById('aumentarTamaño'))
bajarTamano(document.getElementById('bajarTamaño'))
