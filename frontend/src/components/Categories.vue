<template>
  <div class="px-6">
    <div class="prose mb-2">
      <h3>What kind of tour suits you today?</h3>
    </div>
    <div class="flex flex-wrap">
      <button
        v-for="category in CATEGORY_LIST"
        :key="category.name"
        class="mt-2 btn btn-ghost flex flex-col h-full p-2 w-1/3 md:w-24"
        @click="redirectToSearchPage(category.name, category.key)"
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
      CATEGORY_LIST: [
        {
          key: undefined,
          name: 'All Categories',
          imagesUrl: 'https://i.postimg.cc/xd5G44hF/all-categories-1-1.png',
        },
        {
          key: 'MG',
          name: 'Museums & Galleries',
          imagesUrl: 'https://i.postimg.cc/bv4Dzvt3/image-3.png',
        },
        {
          key: 'LA',
          name: 'Landmark',
          imagesUrl: 'https://i.postimg.cc/yx1VBqvL/image-4.png',
        },
        {
          key: 'WE',
          name: 'Wellness',
          imagesUrl: 'https://i.postimg.cc/SKbbkFKc/image-5.png',
        },
        {
          key: 'NA',
          name: 'Nature',
          imagesUrl: 'https://i.postimg.cc/5t81C9rP/image-6.png',
        },
      ],
    };
  },
  methods: {
    redirectToSearchPage(categoryName, categoryKey) {
      this.$router.push({
        name: 'result',
        query: {
          category: categoryName,
          categoryKey,
          ...this.$route.query,
        },
      });
    },
  },
};
</script>
