<template>
  <div>
    <ul class="steps steps-vertical w-[97vw]">
      <li
        v-for="pack in packages"
        :key="pack.id"
        class="step step-accent mr-10"
        data-content=""
      >
        <div class="flex border border-base-200 rounded-md m-4 mr-6 w-full indicator">
          <div class="indicator-item">
            <div class="badge badge-lg badge-ghost cursor-pointer">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-4 h-4 stroke-current"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </div>
          </div>
            <span
              class="indicator-item indicator-bottom indicator-center flex"
            >
              <span class="badge badge-primary text-white cursor-pointer">
                <ArrowUpIcon class="w-4" />
              </span>
              <span class="badge badge-primary text-white cursor-pointer">
                <ArrowDownIcon class="w-4"/>
              </span>
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
