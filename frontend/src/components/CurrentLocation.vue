<template>
  <div class="px-6 prose">
    <p class="mb-2">Your Current Location <span class="font-bold">{{location}}</span></p>
    <a href="" class="flex items-center text-secondary no-underline text-sm">
      <LocationMarkerIcon class="h-5 w-5 mr-2"/>
      Explore Other Places
    </a>
  </div>
</template>

<script>
import { LocationMarkerIcon } from '@heroicons/vue/solid';

export default {
  name: 'Current Location',
  components: {
    LocationMarkerIcon,
  },
  props: {
    location: String,
  },
};
</script>
