<template>
  <div>
    <div
      v-for="item in prices"
      :key="item.id"
      class="flex justify-between items-center border border-base-200 py-1 px-4"
    >
      <div>
        <p class="font-medium py-4">{{item.name}}</p>
      </div>
      <div class="w-40">
          <p class="text-md font-medium text-right">Rp {{item.price}}</p>
      </div>
    </div>
    <div
      class="flex justify-between items-center py-1 px-4 mt-8"
    >
      <div>
        <p class="font-bold text-lg">Total</p>
      </div>
      <div>
          <p class="text-lg font-medium ">Rp {{total}}</p>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  name: 'Pricelist',
  props: {
    prices: Array,
    total: Number,
  },
};
</script>
