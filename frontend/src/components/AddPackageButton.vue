<template>
  <div class="pt-6 px-4 sticky w-full h-24 bottom-0 bg-base-100">
    <button class="btn btn-wide btn-primary w-full text-white">
      Basket • {{ count }} Item
    </button>
  </div>
</template>

<script>
export default {
  name: 'Plan Button',
  props: {
    text: String,
    count: Number,
  },
};
</script>
