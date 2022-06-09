<template>
  <div class="min-h-screen">
    <SearchNavbar name="Fellita" :show-search-bar="false"/>
    <CurrentLocation
      :disable-edit="true"
      location="Cimahi"
      class="pt-12"
    />
    <div class="flex justify-center items-center py-4 font-medium text-secondary">
      <h2 class="prosa text-lg">Package name</h2>
      <PencilIcon class="h-4 w-4 ml-2"/>
    </div>
    <PackageList :packages="myPackages" class="mb-4"/>
    <div class="px-4 mb-8">
      <select class="select select-bordered w-full mb-4">
        <option disabled selected>Choose Starting Point</option>
        <option>Depok</option>
        <option>Bandung</option>
      </select>
      <label class="label cursor-pointer float-left" for="include-transport-checkbox">
        <input
          type="checkbox"
          class="checkbox checkbox-primary mr-4"
          id="include-transport-checkbox"
        />
        <span class="label-text">Include Transportation</span>
      </label>
    </div>
    <FloatingButton text="Next" :fixed="true"/>
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
  data() {
    return {
      basket: [],
      myPackages: [
        {
          id: 1,
          name: 'Aare',
          imagesUrl: 'https://api.lorem.space/image?w=400&h=400',
          location: 'Bern, Swiss',
          time: '09.00 - 10.00',
          description: 'Lorem ipsum dolor sit amet syalalala syalalhi',
          price: 10000,
        },
        {
          id: 2,
          name: 'Culinary',
          imagesUrl: 'https://api.lorem.space/image?w=400&h=400',
          location: 'Bandung, Jawa Barat',
          time: '09.00 - 10.00',
          description: 'Lorem ipsum dolor sit amet syalalala syalalhi',
          price: 10000,
        },
        {
          id: 3,
          name: 'Leisure',
          imagesUrl: 'https://api.lorem.space/image?w=400&h=400',
          location: 'Bandung, Jawa Barat',
          time: '09.00 - 10.00',
          description: 'Lorem ipsum dolor sit amet syalalala syalalhi',
          price: 10000,
        },
        {
          id: 4,
          name: 'Wellness',
          imagesUrl: 'https://api.lorem.space/image?w=400&h=400',
          location: 'Bandung, Jawa Barat',
          time: '09.00 - 10.00',
          description: 'Lorem ipsum dolor sit amet syalalala syalalhi',
          price: 10000,
        },
      ],
    };
  },
};
</script>
