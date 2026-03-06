<template>
  <section class="bg-white rounded-2xl p-6 shadow-sm">
    <h2 class="font-semibold mb-6 flex items-center gap-2">
        <span class="material-symbols-outlined text-blue-500">
          family_group
        </span>
        Agregado familiar
    </h2>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <Counter v-for="item in deductions"
       :key="item.id"
       :label="item.label" 
       v-model.number="useFormData.deductions.dependents[item.field]"/>
    </div>
  </section>
</template>

<script setup>
import Counter from "@/components/ui/BaseCounter.vue"
import { useFormData } from "@/composable/useFormData";
import { reactive } from "vue";


const deductions = reactive([
  { id: 1, label: "Total Dependentes", field: "total" },
  { id: 2, label: "Até 3 anos", field: "dependents_upto_3" },
  { id: 3, label: "Entre 3 e 6 anos", field: "dependents_upto_6" }
])
</script>