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
    <MyPlan class= "pt-6 mb-4"/>
    <Categories class="pt-6"/>
  </div>
</template>
<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import CurrentLocation from '@/components/CurrentLocation.vue';
import Categories from '@/components/Categories.vue';
import MyPlan from '@/components/MyPlan.vue';
import FloatingButton from '@/components/FloatingButton.vue';

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
  },
  data() {
    return {
      selectedCity: null,
      name: '',
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
  },
};
</script>
