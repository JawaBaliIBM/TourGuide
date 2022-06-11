<template>
  <div class="min-h-screen">
    <SearchNavbar
      :name="name"
      :keyword="keyword"
      :show-search-bar="true"
      @enter="(keyword) => getDestinations(keyword)"
    />
    <CurrentLocation :location="city" class="pt-12"/>
    <SearchResult
      :destinations="destinations"
      class="pt-6"
      :category="category"
      @addPackage="addBasket"
      @removePackage="removeFromBasket"
      @closeCategory="handleRemoveCategory"
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
import axios from 'axios';
import AddPackageButton from '../components/AddPackageButton.vue';

export default {
  name: 'SearchResultView',
  components: {
    SearchNavbar,
    CurrentLocation,
    SearchResult,
    AddPackageButton,
  },
  async mounted() {
    this.city = this.$route.query.city;
    this.name = this.$route.query.name;
    this.keyword = this.$route.query.keyword;
    this.category = this.$route.query.category;

    await this.getCities();
    this.getDestinations();
  },
  data() {
    return {
      name: '',
      city: '',
      keyword: '',
      category: '',
      basket: [],
      cities: {},
      destinations: [],
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
    async getCities() {
      const response = await axios.get(`${this.$root.BASE_URL}/cities`);
      response.data.forEach((data) => {
        this.cities[data.name] = data.id;
      });
    },
    getDestinations(keyword = this.keyword) {
      axios
        .get(`${this.$root.BASE_URL}/point-of-interests`, {
          params: {
            keyword,
            category: this.category,
            city_id: this.cities[this.city],
          },
        })
        .then((response) => {
          this.destinations = response.data;
        });
    },
    handleRemoveCategory() {
      this.category = undefined;
      this.$route.query.category = this.category;
      this.getDestinations();
    },
  },
};
</script>
