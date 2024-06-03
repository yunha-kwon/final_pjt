<template>
    <div>
       <p>저축 금리 유형명 : {{ option.intr_rate_type_nm}}</p>       
       <p>저축 금리 : {{ option.intr_rate }}</p>
       <p>최고 우대 금리 : {{ option.intr_rate2 }}</p>
       <p>저축 기간 : {{ option.save_trm }}</p>       
    </div>
    <hr>
</template>

<script setup>

defineProps({
option: Object
})
</script>

<style  scoped>

</style>