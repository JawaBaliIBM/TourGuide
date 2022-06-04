<template>
  <div class="min-h-screen">
    <SearchNavbar name="Fellita"/>
    <CurrentLocation location="Cimahi" class="pt-12"/>
    <Categories class="pt-6"/>
    <MyPlan class="pt-6"/>
    <AddPackages/>
  </div>
</template>
<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import CurrentLocation from '@/components/CurrentLocation.vue';
import Categories from '@/components/Categories.vue';
import MyPlan from '@/components/MyPlan.vue';
import AddPackages from '@/components/AddPackages.vue';

export default {
  name: 'ExploreView',
  components: {
    SearchNavbar,
    CurrentLocation,
    Categories,
    MyPlan,
    AddPackages,
  },
};
</script>
