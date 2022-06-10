<template>
  <div>
    <div
      v-for="destination in destinations"
      :key="destination.id"
      class="flex justify-between items-center border border-base-200 py-1 px-4"
    >
      <div>
        <p class="font-medium">{{destination.name}}</p>
        <p class="text-sm">{{destination.location}}</p>
      </div>
      <div>
          <p class="text-md font-medium ">Rp {{destination.price}}</p>
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
    destinations: Array,
    total: Number,
  },
};
</script>
