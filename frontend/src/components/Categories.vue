<template>
  <div class="px-6">
    <div class="prose mb-2">
      <h3>What kind of tour suits you today?</h3>
    </div>
    <div class="flex flex-wrap">
      <button
        v-for="category in categories"
        :key="category.name"
        class="mt-2 btn btn-ghost flex flex-col h-full p-2 w-1/3 md:w-24"
        @click="redirectToSearchPage(category.name)"
      >
        <img :src="category.imagesUrl" :alt="category.name" class="w-full mask mask-squircle">
        <p class="text-center text-sm pt-2 normal-case">{{category.name}}</p>
      </button>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Categories',
  data() {
    return {
      categories: [
        {
          name: 'All Categories',
          imagesUrl: 'https://i.postimg.cc/xd5G44hF/all-categories-1-1.png',
        },
        {
          name: 'Culinary',
          imagesUrl: 'https://i.postimg.cc/hGNTJQzc/culinary-1.png',
        },
        {
          name: 'Leisure',
          imagesUrl: 'https://i.postimg.cc/qv5CY6Gy/Leisure-1.png',
        },
        {
          name: 'Wellness',
          imagesUrl: 'https://i.postimg.cc/NFByT6gq/wellness-1.png',
        },
        {
          name: 'Nature',
          imagesUrl: 'https://i.postimg.cc/W1ChSL27/nature-1.png',
        },
        {
          name: 'Shopping',
          imagesUrl: 'https://i.postimg.cc/0Qdj8z7t/shopping-1.png',
        },
      ],
    };
  },
  methods: {
    redirectToSearchPage(categoryName) {
      this.$router.push({
        name: 'result',
        query: {
          category: categoryName,
          ...this.$route.query,
        },
      });
    },
  },
};
</script>
