<template>
    <div class="bg-white p-4 rounded-xl">
        <div class="flex items-center gap-2">
            <BadgeEuro class="text-blue-500"/>
            <h3 class="py-2 font-bold text-sm">Deduções</h3>
        </div>
        <div class="p-4 border rounded-xl border-gray-300 flex gap-3 w-full text-gray-500">
            <div class="w-full flex flex-col gap-1">
                <label for="education">Educação</label>
                <input type="number" name="education" id="education" v-model="useFormData.deductions.education"
                class="border border-gray-300 p-2 rounded-xl">
            </div>
            <div class="w-full flex flex-col gap-1">
                <label for="health">Saúde</label>
                <input type="number" name="health" id="health" v-model="useFormData.deductions.health"
                class="border border-gray-300 p-2 rounded-xl">
            </div>
            <div class="w-full flex flex-col gap-1">
                <label for="family">Gastos gerais de familia</label>
                <input type="number" name="family" id="family" v-model="useFormData.deductions.family"
                class="border border-gray-300 p-2 rounded-xl">
            </div>
        </div>
    </div>
</template>


<script setup>
import { useFormData } from '@/composable/useFormData';
import { BadgeEuro } from 'lucide-vue-next';

</script>

<style scoped>

</style>