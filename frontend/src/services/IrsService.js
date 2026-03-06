

export const irsService = {
  calculate: async (url, data) => {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })

    const result = await response.json()

    if (!response.ok) {
        console.log("ERRO NA RESPOSTA: ",response)
      throw new Error(result.message || "Erro no cálculo do IRS")
    }

    return result
  }
}