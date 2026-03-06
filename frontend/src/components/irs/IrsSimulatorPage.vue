<template>
  <div class="bg-gray-50 min-h-screen">
    <AppNavbar />
    <main class="max-w-7xl mx-auto px-6 py-10">
      <h1 class="text-3xl font-bold mb-2 mt-20">
        Simulador de IRS 2024
      </h1>
      <p class="text-gray-600 mb-4">
        Estime o seu imposto anual e deduções de forma simples e precisa.
      </p>

      <div class="flex flex-col gap-5 md:flex-row">
        <form @submit.prevent="submitForm" class="w-full">
            <div class="space-y-6">
              <IrsIncomeForm />
              <IrsFamilyForm />
              <button type="submit" class="border p-2 w-full rounded-xl bg-blue-500 text-white font-bold">Calcular</button>
            </div>
        </form>
         <div class="space-y-6">
          <IrsResultCard :result="result" />
           <IrsTipCard />
        </div>
      </div>
    </main>

    <AppFooter />
  </div>
</template>

<script setup>
import AppNavbar from "@/components/layout/AppNavbar.vue"
import AppFooter from "@/components/layout/AppFooter.vue"
import IrsIncomeForm from "./IrsIncomeForm.vue"
import IrsFamilyForm from "./IrsFamilyForm.vue"
import IrsResultCard from "./IrsResultCard.vue"
import IrsTipCard from "./IrsTipCard.vue"
import { useFormData } from "@/composable/useFormData"
import { useIrs } from "@/composable/UseIrsService"
import { ref } from "vue"

let result = ref({})

const {calculate} = useIrs()

const submitForm = async function(){

    try{
        const response = await calculate(useFormData.income_year, useFormData)
        result.value = response
        console.log(response)
    } catch(err){
        console.log("ALGO DE ERRADO NÃO DEU CERTO.", err)
    }
}
</script>