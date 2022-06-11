<template>
  <div class="min-h-screen">
    <SearchNavbar :name="name" :show-search-bar="false"/>
    <CurrentLocation
      :disable-edit="true"
      :location="city"
      class="pt-12"
    />
    <h1 class="pros flex justify-center font-bold text-lg">Here is our recommendation</h1>
    <div class="flex justify-center items-center py-4 font-medium text-secondary">
      <h2 class="text-lg">Package name</h2>
    </div>
    <Timeline
      :packages="myPackages"
      class="mb-24"
      @close="id => handleClose(id)"
      @arrowUp="index => handleArrowUp(index)"
      @arrowDown="index => handleArrowDown(index)"
    />
    <FloatingButton
      text="Confirm Package"
      :fixed="true"
      class="z-40"
      @click="redirectToCheckout"
    />
  </div>
</template>
<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import CurrentLocation from '@/components/CurrentLocation.vue';
import Timeline from '@/components/Timeline.vue';
import FloatingButton from '@/components/FloatingButton.vue';
import { PencilIcon } from '@heroicons/vue/solid';

export default {
  name: 'TimelineList',
  components: {
    SearchNavbar,
    CurrentLocation,
    Timeline,
    FloatingButton,
    PencilIcon,
  },
  mounted() {
    this.city = this.$route.query.city;
    this.name = this.$route.query.name;
  },
  data() {
    return {
      name: '',
      city: '',
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
    redirectToCheckout() {
      this.$router.push({
        name: 'checkout',
        query: {
          ...this.$route.query,
        },
      });
    },
    handleClose(id) {
      this.myPackages = this.myPackages.filter((dest) => dest.id !== id);
    },
    handleArrowUp(index) {
      this.swapPackages(index, index - 1);
    },
    handleArrowDown(index) {
      this.swapPackages(index, index + 1);
    },
    swapPackages(i, j) {
      const temp = this.myPackages[i];
      this.myPackages[i] = this.myPackages[j];
      this.myPackages[j] = temp;
    },
  },
};
</script>
