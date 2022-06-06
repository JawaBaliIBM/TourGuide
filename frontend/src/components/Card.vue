<template>
  <div class="card border border-base-200">
    <figure>
      <img class="w-full" :src="destination.imagesUrl" :alt="destination.name"/>
    </figure>
    <div class="card-body p-2">
      <p class="font-medium">{{destination.name}}</p>
      <div class="flex items-center">
        <LocationMarkerIcon class="h-3 w-3 mr-1"/>
        <p class="text-xs">{{destination.location}}</p>
      </div>
      <div class="flex items-center">
        <ClockIcon class="h-3 w-3 mr-1"/>
        <p class="text-xs">{{destination.time}}</p>
      </div>
      <p class="text-xs text-gray-400 pt-2">{{destination.description}}</p>
      <p class="text-md flex justify-end font-medium text-accent">Rp{{destination.price}}</p>
      <div class="card-actions justify-end">
        <button class="btn btn-primary btn-sm mt-2 w-full text-base-100 normal-case">
          Add To Package
        </button>
      </div>
      <div>
      </div>
    </div>
  </div>
</template>
<script>
import { LocationMarkerIcon, ClockIcon } from '@heroicons/vue/solid';

export default {
  name: 'Card',
  props: {
    destination: Object,
  },
  components: {
    LocationMarkerIcon,
    ClockIcon,
  },
};
</script>
