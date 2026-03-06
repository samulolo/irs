<template>
    <div class="bg-white p-4 rounded-xl border border-gray-200">
        <div class="flex items-center">
            <Euro size="20" class="text-blue-500"/>
            <h3 class="p-2 font-bold">Rendimentos</h3>
        </div>

        <div class="my-2">
            <select name="year" id="year" v-model="useFormData.income_year" class="border border-gray-300 rounded-xl p-2">
                <option value="">Escolha o ano dos rendimentos...</option>
                <option value="2025">2025</option>
            </select>
        </div>
        <div class="p-3 rounded-xl">
           <!-- Origem dos rendimentos -->
                <div class="flex flex-col gap-3">
                    <div class="flex flex-col gap-2">
                        <label for="income" class="text-gray-500">Categoria de rendimentos</label>
                        <select name="income" id="income" class="text-gray-500 border border-gray-300 p-2 rounded-xl"
                        v-model="useFormData.incomeType">
                            <option
                            v-for="rendimento in income_origin" :key="rendimento.id" :value="rendimento.value">{{ rendimento.label }}</option>
                        </select>
                    </div>
                    <div class="flex gap-2">
                        <div class="flex flex-col gap-1 w-full text-gray-500">
                            <label for="gross-income">Rendimento bruto</label>
                            <div class="flex items-center border rounded-xl border-gray-300 px-2 focus-within:border-blue-500 focus-within:ring-1">
                                <input type="text" name="gross-income" id="gross-income" required
                                min="1"
                                class="p-2 rounded-xl outline-none  w-full"
                                v-model="useFormData.gross_income">
                                 <Euro/>
                            </div>
                        </div>
                        <div class="flex flex-col gap-1 w-full text-gray-500">
                            <label for="profissional-order">Ordem profissional</label>
                            <input type="number" name="profissional-order" id="profissional-order"
                            min="0"
                            class="p-2 rounded-xl border border-gray-300"
                             v-model="useFormData.profissional_order">
                        </div>
                    </div>
                </div>
        </div>
        <DeductionsForm/>
    </div>
</template>

<script setup>
import { useFormData } from '@/composable/useFormData';
import { reactive } from 'vue';
import { Euro } from 'lucide-vue-next';
import DeductionsForm from './DeductionsForm.vue';


const income_origin = reactive([
    {id: 1, label:"Esolha uma opção", value : ""},
    {id: 2, label:"Rendimento da categoria A (Tabalho por conta de outrem)", value : "catA"},
    {id: 3, label:"Rendimento de trabalho independente (Recibos verdes)", value : "catB"},
])

</script>

<style lang="scss" scoped>

</style>