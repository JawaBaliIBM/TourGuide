<template>
  <div class="min-h-screen">
    <SearchNavbar name="Fellita" :show-search-bar="true"/>
    <CurrentLocation :location="selectedCity" class="pt-12"/>
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
  },
  data() {
    return {
      selectedCity: null,
    };
  },
};
</script>
