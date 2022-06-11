<template>
  <div class="min-h-screen">
    <SearchNavbar :name="name" :show-search-bar="false"/>
    <CurrentLocation
      :disable-edit="true"
      :location="city"
      class="pt-12"
    />
    <div class="flex justify-center items-center py-4 font-medium text-secondary">
      <input type="text" :value="packageName" class="input input-ghost w-full max-w-xs" />
      <PencilIcon class="h-4 w-4 ml-2"/>
    </div>
    <PackageList :packages="myPackages" class="mb-4" @removePackage="id => filterPackage(id)"/>
    <div class="px-4 mb-8">
      <select
        v-model="selectedStartPoint"
        class="select select-bordered w-full mb-4"
        :class="isError ? 'select-error': ''"
        @change="isError = false"
      >
        <option disabled selected>Choose Starting Point</option>
        <option v-for="startPoint in myPackages" :key="startPoint.id">{{startPoint.name}}</option>
      </select>
      <label class="label cursor-pointer float-left" for="include-transport-checkbox">
        <input
          v-model="isIncludeTransportation"
          type="checkbox"
          class="checkbox checkbox-primary mr-4"
          id="include-transport-checkbox"
        />
        <span class="label-text">Include Transportation</span>
      </label>
    </div>
    <FloatingButton text="Next" :fixed="true" @click="redirectToTimeline"/>
  </div>
</template>
<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import CurrentLocation from '@/components/CurrentLocation.vue';
import PackageList from '@/components/PackageList.vue';
import FloatingButton from '@/components/FloatingButton.vue';
import { PencilIcon } from '@heroicons/vue/solid';

export default {
  name: 'SearchResultView',
  components: {
    SearchNavbar,
    CurrentLocation,
    PackageList,
    FloatingButton,
    PencilIcon,
  },
  mounted() {
    this.myPackages = JSON.parse(this.$route.query.basket);
    this.name = this.$route.query.name;
    this.city = this.$route.query.city;
  },
  data() {
    return {
      myPackages: [],
      selectedStartPoint: 'Choose Starting Point',
      city: '',
      name: '',
      isError: false,
      isIncludeTransportation: false,
      packageName: 'Package Name',
    };
  },
  methods: {
    redirectToTimeline() {
      if (this.selectedStartPoint !== 'Choose Starting Point') {
        this.$router.push({
          name: 'timeline',
          query: {
            ...this.$route.query,
          },
        });
      } else {
        this.isError = true;
      }
    },
    filterPackage(id) {
      this.myPackages = this.myPackages.filter((des) => des.id !== id);
    },
  },
};
</script>
