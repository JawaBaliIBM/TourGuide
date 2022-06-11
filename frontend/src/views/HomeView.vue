<template>
  <div>
    <SearchNavbar name="Felita"/>
    <main class="container mx-auto px-8 min-h-screen flex flex-column justify-center items-center
    mt-[-100px]">
      <section class="prose">
        <h1 class="mb-8"> Where do you want to go? </h1>
        <select
          v-model="selectedCity"
          class="select select-bordered w-full"
          :class="isError? 'select-error': ''"
          @change="isError = false"
        >
          <option disabled selected>Choose City</option>
          <option
            v-for="city in cities"
            :key="city.id"
          >
            {{city.name}}
          </option>
        </select>
      </section>
    </main>
    <FloatingButton text="next" @click="redirectToExplore"/>
  </div>
</template>

<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import FloatingButton from '@/components/FloatingButton.vue';
import axios from 'axios';

export default {
  name: 'HomeView',
  components: {
    SearchNavbar,
    FloatingButton,
  },
  mounted() {
    this.getCity();
  },
  data() {
    return {
      cities: [],
      selectedCity: 'Choose City',
      isError: false,
    };
  },
  methods: {
    redirectToExplore() {
      if (this.selectedCity !== 'Choose City') {
        this.$router.push({
          name: 'explore',
          query: {
            city: this.selectedCity,
          },
        });
      } else {
        this.isError = true;
      }
    },
    getCity() {
      axios
        .get('https://62530581c534af46cb92aea3.mockapi.io/cities')
        .then((response) => {
          this.cities = response.data;
        });
    },
  },
};
</script>
