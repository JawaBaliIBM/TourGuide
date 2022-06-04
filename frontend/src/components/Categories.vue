<template>
  <div class="px-6">
    <div class="prose mb-2">
      <h2>Explore Categories</h2>
    </div>
    <div class="flex flex-wrap">
      <div v-for="category in categories" :key="category.name" class="mx-2">
        <img :src="category.imagesUrl" :alt="category.name" class="w-16">
        <p class="text-center text-sm">{{category.name}}</p>
      </div>
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
          name: 'All',
          imagesUrl: 'https://i.postimg.cc/pXY01TxV/Screen-Shot-2022-06-05-at-00-54-53.png',
        },
        {
          name: 'Nature',
          imagesUrl: 'https://i.postimg.cc/pXY01TxV/Screen-Shot-2022-06-05-at-00-54-53.png',
        },
        {
          name: 'Jalan aja',
          imagesUrl: 'https://i.postimg.cc/pXY01TxV/Screen-Shot-2022-06-05-at-00-54-53.png',
        },
        {
          name: 'Gatau Apa',
          imagesUrl: 'https://i.postimg.cc/pXY01TxV/Screen-Shot-2022-06-05-at-00-54-53.png',
        },
        {
          name: 'Shopping',
          imagesUrl: 'https://i.postimg.cc/pXY01TxV/Screen-Shot-2022-06-05-at-00-54-53.png',
        },
      ],
    };
  },
};
</script>
