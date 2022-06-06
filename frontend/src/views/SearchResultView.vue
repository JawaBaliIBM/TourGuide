<template>
  <div class="min-h-screen">
    <SearchNavbar name="Fellita" :show-search-bar="true"/>
    <CurrentLocation location="Cimahi" class="pt-12"/>
    <SearchResult class="pt-6"/>
  </div>
</template>
<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import CurrentLocation from '@/components/CurrentLocation.vue';
import SearchResult from '@/components/SearchResult.vue';

export default {
  name: 'ExploreView',
  components: {
    SearchNavbar,
    CurrentLocation,
    SearchResult,
  },
};
</script>
