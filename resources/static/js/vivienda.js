// Funcionalidad de búsqueda
document.addEventListener("DOMContentLoaded", () => {
  const searchInput = document.getElementById("searchInput")

  if (searchInput) {
    searchInput.addEventListener("input", function () {
      const searchTerm = this.value.toLowerCase()
      const table = document.getElementById("viviendasTable")

      if (table) {
        const rows = table.getElementsByTagName("tbody")[0].getElementsByTagName("tr")

        for (let i = 0; i < rows.length; i++) {
          const row = rows[i]
          const cells = row.getElementsByTagName("td")
          let found = false

          for (let j = 0; j < cells.length; j++) {
            if (cells[j].textContent.toLowerCase().includes(searchTerm)) {
              found = true
              break
            }
          }

          row.style.display = found ? "" : "none"
        }
      }
    })
  }

  // Efecto de carga
  const loading = document.getElementById("loading")
  const tableWrapper = document.querySelector(".table-wrapper")

  if (loading && tableWrapper) {
    loading.style.display = "block"
    tableWrapper.style.display = "none"

    setTimeout(() => {
      loading.style.display = "none"
      tableWrapper.style.display = "block"
      tableWrapper.classList.add("fade-in")
    }, 800)
  }

  // Efecto de hover mejorado para filas
  const rows = document.querySelectorAll("tbody tr")
  rows.forEach((row) => {
    row.addEventListener("mouseenter", function () {
      this.style.transform = "translateY(-2px)"
    })

    row.addEventListener("mouseleave", function () {
      this.style.transform = "translateY(0)"
    })
  })

  // Contador animado
  animateCounter()
})

// Función para animar el contador
function animateCounter() {
  const counter = document.querySelector(".stats-item h3")
  if (counter) {
    const target = Number.parseInt(counter.textContent)
    let current = 0
    const increment = target / 50

    const timer = setInterval(() => {
      current += increment
      if (current >= target) {
        counter.textContent = target
        clearInterval(timer)
      } else {
        counter.textContent = Math.floor(current)
      }
    }, 20)
  }
}

// Función para exportar datos (funcionalidad adicional)
function exportToCSV() {
  const table = document.getElementById("viviendasTable")
  if (!table) return

  const csv = []
  const rows = table.querySelectorAll("tr")

  for (let i = 0; i < rows.length; i++) {
    const row = [],
      cols = rows[i].querySelectorAll("td, th")

    for (let j = 0; j < cols.length; j++) {
      row.push(cols[j].innerText)
    }

    csv.push(row.join(","))
  }

  downloadCSV(csv.join("\n"), "viviendas.csv")
}

function downloadCSV(csv, filename) {
  const csvFile = new Blob([csv], { type: "text/csv" })
  const downloadLink = document.createElement("a")

  downloadLink.download = filename
  downloadLink.href = window.URL.createObjectURL(csvFile)
  downloadLink.style.display = "none"

  document.body.appendChild(downloadLink)
  downloadLink.click()
  document.body.removeChild(downloadLink)
}
