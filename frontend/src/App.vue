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
      BASE_URL: `${process.env.VUE_APP_BASE_URL}/api`,
    };
  },
};
</script>
