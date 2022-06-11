<template>
  <div class="min-h-screen">
    <SearchNavbar :name="name" :keyword="keyword" :show-search-bar="true"/>
    <CurrentLocation :location="city" class="pt-12"/>
    <SearchResult
      :destinations="destinations"
      class="pt-6"
      @addPackage="addBasket"
      @removePackage="removeFromBasket"
    />
    <AddPackageButton
      v-if="basket.length > 0"
      :count="basket.length"
      @click="redirectToPackagePage"
    />
  </div>
</template>
<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import CurrentLocation from '@/components/CurrentLocation.vue';
import SearchResult from '@/components/SearchResult.vue';
import AddPackageButton from '../components/AddPackageButton.vue';

export default {
  name: 'SearchResultView',
  components: {
    SearchNavbar,
    CurrentLocation,
    SearchResult,
    AddPackageButton,
  },
  mounted() {
    this.city = this.$route.query.city;
    this.name = this.$route.query.name;
    this.keyword = this.$route.query.keyword;
  },
  data() {
    return {
      name: '',
      city: '',
      keyword: '',
      basket: [],
      destinations: [
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
    addBasket(destination) {
      this.basket.push(destination);
    },
    removeFromBasket(destinationId) {
      this.basket = this.basket.filter((des) => des.id !== destinationId);
    },
    redirectToPackagePage() {
      this.$router.push({
        name: 'myPackages',
        query: {
          ...this.$route.query,
          basket: JSON.stringify(this.basket),
        },
      });
    },
  },
};
</script>
