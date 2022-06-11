<template>
  <router-view/>
</template>
<script>
export default {
  name: 'App',
  mounted() {
    this.$router.push({
      query: {
        name: 'Felita',
      },
    });
  },
  data() {
    return {
      BASE_URL: 'https://62530581c534af46cb92aea3.mockapi.io/',
    };
  },
};
</script>
