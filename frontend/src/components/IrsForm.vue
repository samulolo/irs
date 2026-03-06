<template>
    <div class="flex gap-5  justify-center min-h-screen items-center p-4 text-xs">
        <form @submit.prevent="submitForm" class="p-3 flex flex-col gap-3 ">
             <h2>Simulador de IRS</h2>
            <IncomeForm/>
            <FamiliarAgregateForm/>
            <button type="submit" class="border rounded-xl p-2 bg-blue-500 font-bold text-white">Calcular</button>
        </form>
        <IrsResultCard :result="irsResponse"/>
    </div>
</template>

<script setup>

import IncomeForm from './IncomeForm.vue';
import FamiliarAgregateForm from './FamiliarAgregateForm.vue';
import { useFormData } from '@/composable/useFormData';
import { useIrs } from '@/composable/UseIrsService';
import IrsResultCard from './IrsResultCard.vue';
import { reactive, ref } from 'vue';

let irsResponse = ref({})

const {calculate} = useIrs()

const submitForm = async function(){

    console.log("DADOS DO FORMULÁRIO: ", useFormData)
    const data = useFormData
    const response = await calculate(useFormData.income_year, useFormData)
    irsResponse.value = response
    console.log("Resposta: ", response)
}

</script>

<style scoped>

</style>