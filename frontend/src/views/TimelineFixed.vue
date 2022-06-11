<template>
  <div class="min-h-screen">
    <SearchNavbar :name="name" :show-search-bar="false" :handleBackClicked="redirectToHome"/>
    <CurrentLocation
      :disable-edit="true"
      :location="city"
      class="pt-12"
    />
    <h1 class="pros flex justify-center font-bold text-lg">Enjoy your day</h1>
    <div class="flex justify-center items-center py-4 font-medium text-secondary">
      <h2 class="text-lg">Package name</h2>
    </div>
    <Timeline :packages="myPackages" class="mb-24" fixed />
  </div>
</template>
<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import CurrentLocation from '@/components/CurrentLocation.vue';
import Timeline from '@/components/Timeline.vue';

export default {
  name: 'TimelineFixed',
  components: {
    SearchNavbar,
    CurrentLocation,
    Timeline,
  },
  mounted() {
    this.name = this.$route.query.name;
    this.city = this.$route.query.city;
  },
  data() {
    return {
      basket: [],
      name: '',
      city: '',
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
    redirectToHome() {
      this.$router.push({
        name: 'explore',
      });
    },
  },
};
</script>
