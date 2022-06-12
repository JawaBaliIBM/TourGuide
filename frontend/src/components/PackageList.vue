<template>
  <div>
    <Package
    v-for="pack in packages"
    :key="pack.id"
    :destination="pack"
    @removePackage="id => $emit('removePackage', id)"
    />
  </div>
</template>
<script>
import Package from '@/components/Package.vue';

export default {
  name: 'PackageList',
  components: {
    Package,
  },
  props: {
    packages: Array,
  },
};
</script>
