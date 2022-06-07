<template>
  <div>
    <SearchNavbar name="Felita"/>
    <main class="container mx-auto px-8 min-h-screen flex flex-column justify-center items-center
    mt-[-100px]">
      <section class="prose">
        <h1 class="mb-8"> Where do you want to go? </h1>
        <select class="select select-bordered w-full">
          <option disabled selected>Choose City</option>
          <option>Depok</option>
          <option>Bandung</option>
        </select>
      </section>
    </main>
    <FloatingButton text="next" @click="redirectToExplore"/>
  </div>
</template>

<script>
import SearchNavbar from '@/components/SearchNavbar.vue';
import FloatingButton from '@/components/FloatingButton.vue';

export default {
  name: 'HomeView',
  components: {
    SearchNavbar,
    FloatingButton,
  },
  methods: {
    redirectToExplore() {
      this.$router.push({
        name: 'explore',
      });
    },
  },
};
</script>
