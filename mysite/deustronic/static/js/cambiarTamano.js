const ajustes = document.getElementById('cambiarTamano');


// RESTAURAR ESTILOS ANTERIORES
obtenerEstilosAnteriores();

function obtenerEstilosAnteriores() {
  let fuente = localStorage.getItem("fuente");
  document.documentElement.style.setProperty('--font-size', fuente);
}


// CONTROL DE TAMAÑO DE FUENTE
const getFontSize = () =>
  parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--font-size'))

const subirFuente = element => {
  element.addEventListener('click', () => {
    let fontSize = getFontSize()
    document.documentElement.style.setProperty('--font-size', `${fontSize * 1.1}`)
    localStorage.setItem("fuente", fontSize)
  })
}

const bajarFuente = element => {
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

subirFuente(document.getElementById('aumentarTamaño'))
bajarFuente(document.getElementById('bajarTamaño'))
