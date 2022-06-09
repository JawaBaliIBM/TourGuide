<template>
  <div class="flex justify-between items-center border border-base-200 py-1 px-4">
    <div>
      <p class="font-bold">{{destination.name}}</p>
      <p class="text-sm">{{destination.location}}</p>
      <p class="text-sm ">Rp {{destination.price}}</p>
    </div>
    <XIcon class="w-4"/>
  </div>
</template>
<script>
import { XIcon } from '@heroicons/vue/solid';

export default {
  name: 'Package',
  props: {
    destination: Object,
  },
  components: {
    XIcon,
  },
};
</script>
