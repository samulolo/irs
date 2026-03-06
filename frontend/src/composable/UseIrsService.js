import { irsService } from "@/services/IrsService"

const url = import.meta.env.VITE_API_ADDRESS

export const useIrs = function () {

  const calculate = async function (year, data) {
    try {
      return await irsService.calculate(
        `${url}/${year}/v1/calculate/${data.incomeType}`,
        data
      )
    } catch (err) {
      console.error("Não foi possível efetuar o cálculo:", err.message)
      throw err // importante
    }
  }

  return {
    calculate
  }
}