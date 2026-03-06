<template>
    <div>
        <h6>{{ label }}</h6>
        <span>{{ value }}</span>
    </div>
</template>

<script setup>

const props = defineProps({label: String, value: String})

</script>

