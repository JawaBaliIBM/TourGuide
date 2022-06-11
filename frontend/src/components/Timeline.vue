<template>
  <div>
    <ul class="steps steps-vertical w-[97vw]">
      <li
        v-for="(pack, index) in packages"
        :key="pack.id"
        class="step step-accent mr-10"
        data-content=""
      >
        <div class="flex border border-base-200 rounded-md m-4 mr-6 w-full indicator">
          <button v-if="!fixed" class="indicator-item" @click="$emit('close', pack.id)">
            <div class="badge badge-lg badge-ghost cursor-pointer">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-4 h-4 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </div>
          </button>
            <span
              class="indicator-item indicator-bottom indicator-center flex"
            >
              <button v-if="fixed" class="btn btn-primary btn-xs text-white cursor-pointer ">
                Book Now
              </button>
              <div v-else class="flex">
                <button
                  class="badge badge-primary text-white cursor-pointer"
                  :class="index === 0 ? 'badge-ghost': ''"
                  @click="$emit('arrowUp', index)"
                >
                  <ArrowUpIcon class="w-4" />
                </button>
                <button
                  class="badge badge-primary text-white cursor-pointer"
                  :class="index === packages.length-1 ? 'badge-ghost' : ''"
                  @click="$emit('arrowDown', index)"
                >
                  <ArrowDownIcon class="w-4"/>
                </button>
              </div>
            </span>
          <img :src="pack.imagesUrl" :alt="pack.name" class="w-24" />
          <div class="ml-4">
            <p class="text-left font-medium pb-2"> {{ pack.name }}</p>
            <div class="flex items-center">
              <LocationMarkerIcon class="h-3 w-3 mr-1"/>
              <p class="text-xs">{{pack.location}}</p>
            </div>
            <div class="flex items-center">
              <ClockIcon class="h-3 w-3 mr-1"/>
              <p class="text-xs">{{pack.time}}</p>
            </div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>
<script>
import {
  XIcon,
  LocationMarkerIcon,
  ClockIcon,
  ArrowUpIcon,
  ArrowDownIcon,
} from '@heroicons/vue/solid';

export default {
  name: 'Timeline',
  props: {
    packages: Array,
    fixed: Boolean,
  },
  components: {
    XIcon,
    LocationMarkerIcon,
    ClockIcon,
    ArrowUpIcon,
    ArrowDownIcon,
  },
};
</script>
