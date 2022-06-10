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
    </div>
    <Pricelist :destinations="myPackages" :total="40000" class="mb-4"/>
    <FloatingButton text="Pay" :fixed="true" @click="redirectToTimeline"/>
  </div>
</template>
<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import CurrentLocation from '@/components/CurrentLocation.vue';
import Pricelist from '@/components/Pricelist.vue';
import FloatingButton from '@/components/FloatingButton.vue';
import { PencilIcon } from '@heroicons/vue/solid';

export default {
  name: 'SearchResultView',
  components: {
    SearchNavbar,
    CurrentLocation,
    Pricelist,
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
  methods: {
    redirectToTimeline() {
      this.$router.push({ name: 'timeline' });
    },
  },
};
</script>
