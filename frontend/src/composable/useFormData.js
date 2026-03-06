import { reactive } from "vue"

const curretYear = new Date().getFullYear() - 1

export const useFormData = reactive(
    {
  income_year: `${curretYear}`,
  incomeType: "",
  gross_income: null,
  deductions: {
    dependents: {
      total: 0,
      dependents_upto_3: 0,
      dependents_upto_6: 0
    },
    health: 0.00,
    family: 0.00,
    education: 0.00
  },
  profissional_order: 0.00
}
)
