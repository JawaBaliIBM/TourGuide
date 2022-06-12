<template>
  <div class="min-h-screen">
    <SearchNavbar :name="name" :show-search-bar="false"/>
    <CurrentLocation
      :disable-edit="true"
      :location="city"
      class="pt-12"
    />
    <div class="flex justify-center items-center py-4 font-medium text-secondary">
      <h2 class="prosa text-lg">{{priceList.name}}</h2>
    </div>
    <Pricelist :prices="priceList.plan_items" :total="priceList.total" class="mb-4"/>
    <FloatingButton text="Pay" :fixed="true" @click="redirectToTimeline"/>
  </div>
</template>
<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import CurrentLocation from '@/components/CurrentLocation.vue';
import Pricelist from '@/components/Pricelist.vue';
import FloatingButton from '@/components/FloatingButton.vue';
import { PencilIcon } from '@heroicons/vue/solid';
import axios from 'axios';

export default {
  name: 'SearchResultView',
  components: {
    SearchNavbar,
    CurrentLocation,
    Pricelist,
    FloatingButton,
    PencilIcon,
  },
  mounted() {
    this.name = this.$route.query.name;
    this.city = this.$route.query.city;
    this.getPrice();
  },
  data() {
    return {
      name: '',
      city: '',
      priceList: [],
    };
  },
  methods: {
    redirectToTimeline() {
      const res = this.createOnGoingPlan();
      if (res) {
        this.$router.push({
          name: 'timeline-fixed',
          query: {
            ...this.$route.query,
            checkout: undefined,
          },
        });
      }
    },
    getPrice() {
      this.priceList = JSON.parse(this.$route.query.checkout);
    },
    async createOnGoingPlan() {
      const response = await axios
        .post(`${this.$root.BASE_URL}/on-going-plans/`, {
          name: this.priceList.name,
          plan_items: this.priceList.plan_items,
        });

      return response;
    },
  },
};
</script>
