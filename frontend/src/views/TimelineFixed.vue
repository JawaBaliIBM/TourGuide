<template>
  <div class="min-h-screen">
    <SearchNavbar :name="name" :show-search-bar="false" :handleBackClicked="redirectToHome"/>
    <CurrentLocation
      :disable-edit="true"
      :location="city"
      class="pt-12"
    />
    <div v-if="isLoading" class="flex btn btn-lg btn-ghost loading"></div>
    <div v-else>
      <h1 class="pros flex justify-center font-bold text-lg">Enjoy your day</h1>
      <div class="flex justify-center items-center py-2 font-medium text-secondary">
        <h2 class="text-lg">{{myPackages.name}}</h2>
      </div>
      <Timeline :packages="myPackages.plan_items" class="mb-24" fixed />
    </div>
  </div>
</template>
<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import CurrentLocation from '@/components/CurrentLocation.vue';
import Timeline from '@/components/Timeline.vue';
import axios from 'axios';

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
    this.getOnGoingPlan();
  },
  data() {
    return {
      name: '',
      city: '',
      myPackages: [],
      isLoading: false,
    };
  },
  methods: {
    redirectToHome() {
      this.$router.push({
        name: 'explore',
        query: {
          ...this.$route.query,
        },
      });
    },
    getOnGoingPlan() {
      this.isLoading = true;
      axios
        .get(`${this.$root.BASE_URL}/on-going-plans/`)
        .then((response) => {
          this.myPackages = response.data;
          this.isLoading = false;
        });
    },
  },
};
</script>
