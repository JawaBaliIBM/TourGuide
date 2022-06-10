<template>
  <div class="pt-6 px-4 w-full h-24 bottom-0" :class="fixed? 'fixed':'sticky'">
    <button class="btn btn-wide btn-primary w-full text-white">{{ text }}</button>
  </div>
</template>

<script>
export default {
  name: 'Floating Button',
  props: {
    text: String,
    fixed: Boolean,
  },
};
</script>
