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
      <h2 class="text-lg">{{packageName}}</h2>
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
      @click="createPlan"
    />
  </div>
</template>
<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import CurrentLocation from '@/components/CurrentLocation.vue';
import Timeline from '@/components/Timeline.vue';
import FloatingButton from '@/components/FloatingButton.vue';
import { PencilIcon } from '@heroicons/vue/solid';
import axios from 'axios';

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
    this.packageName = this.$route.query.packageName;
    this.getRecommendations();
  },
  data() {
    return {
      name: '',
      city: '',
      myPackages: [],
      packageName: '',
    };
  },
  methods: {
    redirectToCheckout(responseId) {
      this.$router.push({
        name: 'checkout',
        query: {
          ...this.$route.query,
          checkoutId: responseId,
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
    getRecommendations() {
      axios
        .post(`${this.$root.BASE_URL}/recommendation`, {
          params: {
            package_name: this.$route.query.packageName,
            starting_point: this.$route.query.selectedStartPoint,
            is_include_ride: this.$route.query.isIncludeTransportation,
            destinations: this.$route.query.basket,
          },
        })
        .then((response) => {
          this.myPackages = response.data;
        });
    },
    async createPlan() {
      const response = await axios.post(`${this.$root.BASE_URL}/plan`, {
        params: {
          package_name: this.$route.query.packageName,
          starting_point: this.$route.query.selectedStartPoint,
          is_include_ride: this.$route.query.isIncludeTransportation,
          destinations: this.$route.query.basket,
        },
      });
      if (response) {
        this.redirectToCheckout(response.id);
      }
    },
  },
};
</script>
