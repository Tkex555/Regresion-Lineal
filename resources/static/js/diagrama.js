document.addEventListener("DOMContentLoaded", () => {
  // Elementos
  const chartImage = document.getElementById("chartImage")
  const modal = document.getElementById("imageModal")
  const modalImg = document.getElementById("modalImage")
  const closeModal = document.querySelector(".close")
  const downloadBtn = document.getElementById("downloadBtn")
  const fullscreenBtn = document.getElementById("fullscreenBtn")
  const loading = document.getElementById("loading")
  const content = document.querySelector(".content")

  // Efecto de carga
  if (loading && content) {
    loading.style.display = "block"
    content.style.display = "none"

    setTimeout(() => {
      loading.style.display = "none"
      content.style.display = "block"
      content.classList.add("fade-in")
    }, 1000)
  }

  // Zoom en modal
  if (chartImage && modal && modalImg) {
    chartImage.addEventListener("click", () => {
      modal.style.display = "block"
      modalImg.src = chartImage.src
    })

    closeModal.addEventListener("click", () => {
      modal.style.display = "none"
    })

    modal.addEventListener("click", (e) => {
      if (e.target === modal) {
        modal.style.display = "none"
      }
    })
  }

  // Descargar imagen
  if (downloadBtn && chartImage) {
    downloadBtn.addEventListener("click", () => {
      const link = document.createElement("a")
      link.download = "diagrama_dispersion.png"
      link.href = chartImage.src
      link.click()
    })
  }

  // Pantalla completa
  if (fullscreenBtn) {
    fullscreenBtn.addEventListener("click", () => {
      if (document.fullscreenElement) {
        document.exitFullscreen()
      } else {
        document.documentElement.requestFullscreen()
      }
    })
  }

  // Animaciones al hacer scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("fade-in")
      }
    })
  }, observerOptions)

  // Observar elementos para animaciones
  document.querySelectorAll(".chart-container, .info-panel").forEach((el) => {
    observer.observe(el)
  })

  // Efecto de hover mejorado para botones
  document.querySelectorAll(".btn").forEach((btn) => {
    btn.addEventListener("mouseenter", function () {
      this.style.transform = "translateY(-3px)"
    })

    btn.addEventListener("mouseleave", function () {
      this.style.transform = "translateY(0)"
    })
  })
})

// Función para actualizar estadísticas (si tienes datos dinámicos)
function updateStats(data) {
  const statElements = document.querySelectorAll(".stat-number")
  if (statElements.length > 0 && data) {
    statElements[0].textContent = data.totalPoints || "N/A"
    statElements[1].textContent = data.correlation || "N/A"
    statElements[2].textContent = data.trend || "N/A"
  }
}

// Función para mostrar notificaciones
function showNotification(message, type = "info") {
  const notification = document.createElement("div")
  notification.className = `notification ${type}`
  notification.textContent = message
  notification.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    padding: 15px 20px;
    background: ${type === "success" ? "#d4edda" : "#f8d7da"};
    color: ${type === "success" ? "#155724" : "#721c24"};
    border-radius: 5px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    z-index: 1001;
    animation: slideIn 0.3s ease;
  `

  document.body.appendChild(notification)

  setTimeout(() => {
    notification.remove()
  }, 3000)
}
