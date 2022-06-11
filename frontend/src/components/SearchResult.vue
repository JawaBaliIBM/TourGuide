<template>
  <div class="px-6">
    <button v-if="category" class="badge badge-accent gap-2 mb-4" @click="$emit('closeCategory')">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-4 h-4 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      {{category}}
    </button>
    <div class="grid gap-4 grid-cols-2 grid-rows-2">
      <Card
        v-for="destination in destinations"
        :key="destination.id"
        :destination="destination"
        @addPackage="des => $emit('addPackage', des)"
        @removePackage="desId => $emit('removePackage', desId)"
      />
    </div>
  </div>
</template>
<script>
import Card from '@/components/Card.vue';

export default {
  name: 'Categories',
  components: {
    Card,
  },
  props: {
    destinations: Array,
    category: String,
  },
};
</script>
