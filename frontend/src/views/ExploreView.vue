<template>
  <div class="min-h-screen">
    <SearchNavbar
      :name="name"
      :show-search-bar="true"
      @enter="redirectToSearchResult"
    />
    <CurrentLocation
      :location="selectedCity"
      class="pt-12"
    />
    <div v-if="isLoading" class="flex btn btn-lg btn-ghost loading"></div>
    <div v-else>
      <MyPlan v-if="myPackages" class= "pt-6 mb-4" :packages="myPackages"/>
      <Categories class="pt-6"/>
    </div>
  </div>
</template>
<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import CurrentLocation from '@/components/CurrentLocation.vue';
import Categories from '@/components/Categories.vue';
import MyPlan from '@/components/MyPlan.vue';
import FloatingButton from '@/components/FloatingButton.vue';
import axios from 'axios';

export default {
  name: 'ExploreView',
  components: {
    SearchNavbar,
    CurrentLocation,
    Categories,
    MyPlan,
    FloatingButton,
  },
  mounted() {
    this.selectedCity = this.$route.query.city;
    this.name = this.$route.query.name;
    this.getOnGoingPlan();
  },
  data() {
    return {
      selectedCity: null,
      name: '',
      myPackages: [],
      isLoading: false,
    };
  },
  methods: {
    redirectToSearchResult(keyword) {
      this.$router.push({
        name: 'result',
        query: {
          keyword,
          name: this.name,
          city: this.selectedCity,
        },
      });
    },
    getOnGoingPlan() {
      this.isLoading = true;
      axios
        .get(`${this.$root.BASE_URL}/on-going-plans/`)
        .then((response) => {
          this.myPackages = response.data.plan_items;
          this.isLoading = false;
        });
    },
  },
};
</script>
