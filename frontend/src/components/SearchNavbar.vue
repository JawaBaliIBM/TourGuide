<template>
  <nav>
    <div class="bg-primary px-6 pt-6" :class="showSearchBar?'h-24':'h-20'">
      <h3 v-if="name" class="text-lg font-norml text-base-100">Hello, {{ name }}!</h3>
    </div>
    <div class="mx-4 m-[-25px]">
      <div v-if="showSearchBar" class="input-group drop-shadow-md">
        <button class="btn btn-square btn-disabled bg-base-100 border-base-200">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
        </button>
        <input
          v-model="keyword"
          type="text"
          placeholder="Search museums or galleries"
          class="input input-bordered w-full"
          @keyup.enter="$emit('enter', keyword)"
        />
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'SearchNavbar',
  props: {
    name: String,
    showSearchBar: Boolean,
    keyword: String,
  },
};
</script>
