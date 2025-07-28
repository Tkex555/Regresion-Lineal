document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("predictionForm")
  const submitBtn = document.getElementById("submitBtn")
  const loading = document.getElementById("loading")
  const inputs = document.querySelectorAll(".form-input")

  // Validación en tiempo real
  inputs.forEach((input) => {
    input.addEventListener("input", validateInput)
    input.addEventListener("blur", validateInput)
  })

  function validateInput(e) {
    const input = e.target
    const formGroup = input.closest(".form-group")
    const value = Number.parseFloat(input.value)

    // Remover clases previas
    formGroup.classList.remove("error", "success")

    if (input.value === "") {
      return
    }

    let isValid = true
    let errorMessage = ""

    // Validaciones específicas
    switch (input.name) {
      case "area":
        if (value <= 0 || value > 1000) {
          isValid = false
          errorMessage = "El área debe estar entre 1 y 1000 m²"
        }
        break
      case "habitaciones":
        if (value < 1 || value > 20 || !Number.isInteger(value)) {
          isValid = false
          errorMessage = "Las habitaciones deben ser entre 1 y 20"
        }
        break
      case "antiguedad":
        if (value < 0 || value > 100) {
          isValid = false
          errorMessage = "La antigüedad debe estar entre 0 y 100 años"
        }
        break
    }

    // Aplicar clases y mensajes
    if (isValid) {
      formGroup.classList.add("success")
    } else {
      formGroup.classList.add("error")
      let errorEl = formGroup.querySelector(".error-message")
      if (!errorEl) {
        errorEl = document.createElement("div")
        errorEl.className = "error-message"
        formGroup.appendChild(errorEl)
      }
      errorEl.textContent = errorMessage
    }

    updateSubmitButton()
  }

  function updateSubmitButton() {
    const allValid = Array.from(inputs).every((input) => {
      const formGroup = input.closest(".form-group")
      return input.value !== "" && !formGroup.classList.contains("error")
    })

    submitBtn.disabled = !allValid
  }

  // Manejo del formulario
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault()

      // Mostrar loading
      if (loading) {
        loading.style.display = "block"
        submitBtn.disabled = true
        submitBtn.innerHTML =
          '<span class="spinner" style="width: 20px; height: 20px; margin-right: 10px;"></span>Calculando...'
      }

      // Simular delay para mejor UX
      setTimeout(() => {
        form.submit()
      }, 1000)
    })
  }

  // Animaciones
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
  document.querySelectorAll(".form-container, .info-cards, .result-container").forEach((el) => {
    observer.observe(el)
  })

  // Efectos de hover para botones
  document.querySelectorAll(".btn").forEach((btn) => {
    btn.addEventListener("mouseenter", function () {
      if (!this.disabled) {
        this.style.transform = "translateY(-3px)"
      }
    })

    btn.addEventListener("mouseleave", function () {
      if (!this.disabled) {
        this.style.transform = "translateY(0)"
      }
    })
  })

  // Auto-focus en el primer input
  const firstInput = document.querySelector(".form-input")
  if (firstInput) {
    firstInput.focus()
  }
})

// Función para formatear números
function formatNumber(num) {
  return new Intl.NumberFormat("es-ES", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(num)
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
    background: ${type === "success" ? "#d4edda" : type === "error" ? "#f8d7da" : "#d1ecf1"};
    color: ${type === "success" ? "#155724" : type === "error" ? "#721c24" : "#0c5460"};
    border-radius: 5px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    z-index: 1001;
    animation: slideIn 0.3s ease;
  `

  document.body.appendChild(notification)

  setTimeout(() => {
    notification.remove()
  }, 4000)
}
