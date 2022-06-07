<template>
  <div class="px-6">
    <div class="prose mb-2">
      <h3>Ongoing Plan</h3>
    </div>
    <div class="flex flex-wrap">
      <div v-for="category in categories" :key="category.name" class="mx-2">
        <div class="card lg:card-side bg-base-100 shadow-xl">
          <figure><img :src="category.imagesUrl" :alt="category.name" ></figure>
          <div class="card-body">
            <h2 class="card-title">{{category.name}}</h2>
            <div class="card-actions justify-end">
              <button class="btn btn-accent w-full">Detail</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'MyPlan',
  data() {
    return {
      categories: [
        {
          name: 'Jalan jalan santai',
          imagesUrl: 'https://api.lorem.space/image/album?w=400&h=100',
        },
      ],
    };
  },
};
</script>
