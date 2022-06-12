<template>
  <div class="card border border-base-200">
    <figure>
      <img class="w-full h-24" :src="destination.photo" :alt="destination.title"/>
    </figure>
    <div class="card-body p-2">
      <p class="font-medium">{{destination.title}}</p>
      <div class="flex items-center">
        <LocationMarkerIcon class="h-3 w-3 mr-1"/>
        <p class="text-xs">{{destination.address}}</p>
      </div>
      <div class="flex items-center">
        <ClockIcon class="h-3 w-3 mr-1"/>
        <p class="text-xs">{{destination.open_time}}</p>
      </div>
      <div class="pt-2 overflow-hidden w-full">
        <p class="text-xs h-24 text-gray-400 text-ellipsis ...">
          {{destination.description}}
        </p>
      </div>
      <p class="text-md flex justify-end items-end font-medium text-accent">
        Rp{{destination.price}}
      </p>
      <div class="card-actions justify-end">
        <button
          v-if="isShowAddButton"
          class="btn btn-primary btn-sm mt-2 w-full text-base-100 normal-case"
          @click="handleAddPackage"
        >
          Add To Package
        </button>
        <button
          v-else
          class="btn btn-accent btn-sm mt-2 w-full text-base-100 normal-case"
          @click="handleRemovePackage"
        >
          Remove package
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
  data() {
    return {
      isShowAddButton: true,
    };
  },
  methods: {
    handleAddPackage() {
      this.isShowAddButton = false;
      this.$emit('addPackage', this.destination);
    },
    handleRemovePackage() {
      this.isShowAddButton = true;
      this.$emit('removePackage', this.destination.id);
    },
  },
};
</script>
