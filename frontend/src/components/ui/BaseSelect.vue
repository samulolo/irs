<template>
    <div class="bg-white rounded-xl text-sm text-xs text-gray-500">
        <div class="mb-2"><label for="">{{ label }}</label></div>
        <select name="" id="" @change="update" class="border border-gray-300 p-2 rounded-xl w-full" :required="required">
            <option v-for="income in incomeType"
            :key="income.id"
            :value="income.value">{{ income.label }}</option>
        </select>
    </div>
</template>

<script setup>

const props = defineProps({incomeType: Array, label: String,
    required : {
        type: Boolean,
        default: () => true
    }
})
const emits = defineEmits(["update:modelValue"])

const update = (e) => emits("update:modelValue", e.target.value)



</script>

