<template>
  <div class="w-full">
    <label class="text-xs text-gray-500">{{ label }}</label>
    <input :value="modelValue"
    @input="update"
      type="number"
      :required="required"
      placeholder="Insira o valor"
      class="mt-1 w-full border text-xs border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring"
    />
  </div>
</template>

<script setup>
const props = defineProps({ label: String, modelValue : Number ,
  required : {
    type: Boolean,
    default: false
  },
})
const emits = defineEmits(["update:modelValue"])

const update = (e) => emits("update:modelValue", e.target.value)



</script>