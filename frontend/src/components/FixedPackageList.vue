<template>
  <div>
    <div
      v-for="pack in packages"
      :key="pack.id"
    >
      <div class="flex border border-base-200 rounded-md m-4 w-[80vw] indicator">
        <div class="flex items-center justify-center">
          <img :src="pack.photo" :alt="pack.name" class="w-24 h-24" />
        </div>
        <div class="ml-4">
          <p class="text-left font-medium pb-2"> {{ pack.name }}</p>
          <div class="flex items-center" v-if="pack.type === 'POI'">
            <LocationMarkerIcon class="h-3 w-3 mr-1"/>
            <p class="text-xs">{{pack.address}}</p>
          </div>
          <div class="flex items-center" v-if="pack.type === 'POI'">
            <ClockIcon class="h-3 w-3 mr-1"/>
            <p class="text-xs">{{pack.open_time}}</p>
          </div>
          <button class="btn btn-primary btn-xs text-white w-full my-4">
            {{ pack.type === 'POI' ? 'Show Ticket' : 'Book Now' }}
          </button>
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
