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
      BASE_URL: 'https://3b50-2001-448a-50e0-6aa7-b16e-fec3-497e-bb2c.ngrok.io/api',
    };
  },
};
</script>
