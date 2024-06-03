<template>
    <div>
       <p>저축 금리 유형명 : {{ saveoption.intr_rate_type_nm}}</p>       
       <p>적립 유형 명 : {{ saveoption.rsrv_type_nm }}</p>
       <p>저축 금리 : {{ saveoption.intr_rate }}</p>
       <p>최고 우대 금리 : {{ saveoption.intr_rate2 }}</p>
       <p>저축 기간 : {{ saveoption.save_trm }}</p>       
    </div>
    <hr>
</template>

<script setup>

defineProps({
  saveoption: Object
})
</script>

<style  scoped>

</style>