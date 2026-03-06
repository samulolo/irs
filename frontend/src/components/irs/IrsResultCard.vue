<template>
  <section class="flex flex-col text-xs w-full">
    <div
      class="max-w-md mx-auto bg-gradient-to-br from-blue-500 to-blue-600 text-white rounded-2xl shadow-2xl p-8"
    >
      <div class="flex items-center gap-3 mb-8">
        <h2 class="text-xl font-semibold">
          Resultado Estimado
        </h2>
      </div>

      <div class="space-y-6 text-sm">
        <div class="flex justify-between items-center">
          <span class="text-white/80">Rendimento Coletável</span>
          <span class="text-lg font-semibold">
            {{ formatCurrency(result?.taxable_income) }}
          </span>
        </div>

        <div class="flex justify-between items-center">
          <span class="text-white/80">Deduções à Coleta</span>
          <span class="text-lg font-semibold">
            {{ formatCurrency(result?.deductions?.total) }}
          </span>
        </div>

        <div class="flex justify-between items-center">
          <span class="text-white/80">Taxa Aplicada</span>
          <span class="text-lg font-semibold">
            {{ formatPercent(result?.tax_rates?.marginal) }}
          </span>
        </div>
      </div>

      <div class="border-t border-white/30 my-8"></div>

      <div>
        <p class="text-white/80 text-sm mb-2">
          Imposto Total a Pagar
        </p>
        <h1 class="text-4xl font-bold">
          {{ formatCurrency(result?.net_tax) }}
        </h1>
      </div>

      <div class="mt-8 bg-white/15 backdrop-blur-sm rounded-xl p-4 text-sm text-white/90">
        Este valor é uma estimativa baseada nos dados introduzidos.
        Os valores finais podem variar consoante a declaração oficial da AT.
      </div>

      <button
        type="button"
        @click.stop="downloadPdf"
        class="mt-8 w-full bg-white text-blue-700 font-semibold py-3 rounded-xl hover:bg-blue-50 transition duration-200"
      >
        ⬇️ Descarregar PDF
      </button>
    </div>
  </section>
</template>

<script setup>
const props = defineProps({
  result: {
    type: Object,
    default: () => null
  }
})

const normalizeNumber = (value) => {
  if (value === null || value === undefined || value === "") {
    return 0
  }

  if (typeof value === "number") {
    return Number.isFinite(value) ? value : 0
  }

  if (typeof value === "string") {
    const normalized = value.replace(",", ".").trim()
    const parsed = Number(normalized)
    return Number.isFinite(parsed) ? parsed : 0
  }

  return 0
}

const formatCurrency = (value) => {
  const number = normalizeNumber(value)

  return new Intl.NumberFormat("pt-PT", {
    style: "currency",
    currency: "EUR"
  }).format(number)
}

const formatPercent = (value) => {
  return `${normalizeNumber(value)}%`
}

const downloadPdf = () => {
  console.log("Iniciando o download")
  alert("Clique do PDF funcionando")
}
</script>