<template>
    <div class="bg-white border border-gray-200 p-4 rounded-xl">
        <div class="flex items-center gap-3 mb-2">
            <span class="material-symbols-outlined text-blue-500">
                family_group
            </span>
            <h3 class="font-bold">Agregado familiar</h3>
        </div>
        <div class="p-4 border border-gray-300 flex gap-3 w-full rounded-xl text-center text-xs text-gray-500">
            <div class="w-full flex flex-col gap-1 bg-gray-50 p-2 rounded shadow">
                <label for="education" class="uppercase">Total dependentes</label>
                <div class="flex items-center justify-center gap-2">
                     <button type="button"  @click="useFormData.deductions.dependents.total--" class="cursor-pointer border border-gray-200 bg-white rounded-full p-2">
                        <Minus size="20" class="text-blue-500"/></button>
                    <span class="text-xl font-bold text-blue-500">{{ useFormData.deductions.dependents.total }}</span>
                    <button type="button" @click="useFormData.deductions.dependents.total++" class="cursor-pointer border border-gray-200 bg-white rounded-full p-2">
                        <Plus size="20" class="text-blue-500"/></button>
                </div>
            </div>
            <div class="w-full flex flex-col gap-1 text-center text-xs text-gray-500 bg-gray-50 p-2 rounded shadow">
                <label for="health" class="uppercase">Até 3 anos</label>
                <div class="flex items-center justify-center gap-2">
                     <button  type="button" @click="useFormData.deductions.dependents.dependents_upto_3--" class="cursor-pointer border border-gray-200 bg-white rounded-full p-2">
                        <Minus size="20" class="text-blue-500"/></button>
                    <span class="text-xl font-bold">{{ useFormData.deductions.dependents.dependents_upto_3 }}</span>
                    <button type="button" @click="useFormData.deductions.dependents.dependents_upto_3++" class="cursor-pointer border border-gray-200 bg-white rounded-full p-2">
                        <Plus size="20" class="text-blue-500"/></button>
                </div>
            </div>
            <div class="w-full flex flex-col gap-1 text-center text-xs text-gray-500 bg-gray-50 p-2 rounded shadow">
                <label for="family" class="uppercase">Entre 3 e 6 anos</label>
                <div class="flex items-center justify-center gap-2">
                     <button  type="button" @click="useFormData.deductions.dependents.dependents_upto_6--" class="cursor-pointer border border-gray-200 bg-white rounded-full p-2">
                        <Minus size="20" class="text-blue-500"/></button>
                    <span class="text-xl font-bold">{{ useFormData.deductions.dependents.dependents_upto_6 }}</span>
                    <button  type="button"@click="useFormData.deductions.dependents.dependents_upto_6++"  class="cursor-pointer border border-gray-200 bg-white rounded-full p-2">
                        <Plus size="20" class="text-blue-500"/></button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useFormData } from '@/composable/useFormData';
import { Minus,Plus } from 'lucide-vue-next';

</script>

<style scoped>

</style>