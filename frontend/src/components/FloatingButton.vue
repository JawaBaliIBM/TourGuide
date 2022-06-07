<template>
  <div class="pt-6 px-4 fixed w-full h-24 bottom-0">
    <button class="btn btn-wide btn-primary w-full text-white">{{ text }}</button>
  </div>
</template>

<script>
export default {
  name: 'Floating Button',
  props: {
    text: String,
  },
};
</script>
