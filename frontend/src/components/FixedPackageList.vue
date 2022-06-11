<template>
  <div>
    <div
      v-for="pack in packages"
      :key="pack.id"
    >
      <div class="flex border border-base-200 rounded-md m-4 w-[80vw] indicator">
        <span
          class="indicator-item indicator-bottom indicator-center flex"
        >
          <button class="btn btn-primary btn-xs text-white cursor-pointer ">
            {{ pack.type === 'POI' ? 'Show Ticket' : 'Book Now' }}
          </button>
        </span>
        <img :src="pack.photo" :alt="pack.title" class="w-24" />
        <div class="ml-4">
          <p class="text-left font-medium pb-2"> {{ pack.title }}</p>
          <div class="flex items-center">
            <LocationMarkerIcon class="h-3 w-3 mr-1"/>
            <p class="text-xs">{{pack.address}}</p>
          </div>
          <div class="flex items-center">
            <ClockIcon class="h-3 w-3 mr-1"/>
            <p class="text-xs">{{pack.open_time}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import {
  LocationMarkerIcon,
  ClockIcon,
} from '@heroicons/vue/solid';

export default {
  name: 'Timeline',
  props: {
    packages: Array,
  },
  components: {
    LocationMarkerIcon,
    ClockIcon,
  },
};
</script>
