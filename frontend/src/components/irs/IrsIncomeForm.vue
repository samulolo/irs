<template>
  <section class="bg-white rounded-2xl p-6 shadow-sm">
    <h2 class="font-semibold mb-6 flex items-center gap-2">
      <span class="material-symbols-outlined text-blue-500">
        business_center
      </span> Rendimentos e Despesas
    </h2>

    <div class="flex flex-col md:grid-cols-2 gap-4">
        <BaseSelect :income-type="incomeType"
        v-model="useFormData.incomeType"
        label="Categoria de rendimentos"
        :required="true"/>
      <div class="flex gap-2">
          <Input label="Salário Bruto Anual (€)" v-model.number="form.gross_income" :required="true"/>
          <Input label="Ordem Profissional (€)" v-model.number="form.profissional_order"/>
      </div>
      <div class="flex flex-col gap-2 items-center md:flex-row">
          <Input v-for="item in inputContent" 
          :key="item.id"
          :label="item.label" 
          v-model.number="useFormData.deductions[item.field]"/>
      </div>
    </div>
  </section>
</template>

<script setup>
import Input from "@/components/ui/BaseInput.vue"
import BaseSelect from "../ui/BaseSelect.vue";
import { useFormData } from "@/composable/useFormData";
import { reactive } from "vue";

const form = useFormData

const inputContent = reactive([
  {id: 1, label: "Saúde (€)", field: "health"},
  {id: 2, label: "Educação (€)", field : "education"},
  {id: 3, label: "Gastos de famailia (€)", field : "family"},
])

const incomeType = reactive([
    {id: 1, value: "", label : "Escolha uma opção..."},
    {id: 2, value: "cat-A", label: "Trabalho dependente (Categoria - A)"},
    {id: 3, value: "cat-B", label: "Trabalho independente (Categoria - B)"},
])

</script>