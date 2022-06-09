<template>
  <div class="px-6 prose">
    <p class="mb-2">Your Current Location <span class="font-bold">{{location}}</span></p>
    <button
      v-if="!disableEdit"
      class="flex items-center text-secondary no-underline text-sm"
      @click="redirectToHomeView"
    >
      <LocationMarkerIcon class="h-5 w-5 mr-2"/>
      Explore Other Places
    </button>
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
    disableEdit: {
      type: Boolean,
    },
  },
  methods: {
    redirectToHomeView() {
      this.$router.push({
        name: 'home',
      });
    },
  },
};
</script>
