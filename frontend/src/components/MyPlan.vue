<template>
  <div class="px-6">
    <div class="prose mb-2">
      <h3>Ongoing Plan</h3>
    </div>
    <FixedPackageList :packages="packages" class="max-h-48 overflow-auto" fixed />
  </div>
</template>
<script>
import FixedPackageList from '@/components/FixedPackageList.vue';

export default {
  name: 'MyPlan',
  components: {
    FixedPackageList,
  },
  props: {
    packages: Array,
  },
};
</script>
