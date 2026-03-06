<template>
  <div class="bg-gray-50 rounded-xl p-4 text-center">
    <p class="text-xs text-gray-500 mb-2">{{ label }}</p>
    <div class="flex justify-center items-center gap-4">
      <button type="button" class="w-8 h-8 rounded-full bg-white shadow" @click="decrement">−</button>
      <span class="font-semibold text-lg">{{ modelValue }}</span>
      <button type="button" class="w-8 h-8 rounded-full bg-white shadow" @click="increment">+</button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps(
    { label: String, modelValue : Number }
)
const emits = defineEmits(["update:modelValue"])

const increment = () => emits("update:modelValue", props.modelValue + 1)
const decrement = () => emits("update:modelValue", Math.max(0, props.modelValue - 1))

</script>