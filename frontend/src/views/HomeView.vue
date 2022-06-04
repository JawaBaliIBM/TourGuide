<template>
  <div class="bg-primary">
    <main class="container mx-auto px-8 flex flex-column min-h-screen justify-center items-center">
      <div class="callout mask mask-squircle"/>
      <section class="prose z-10">
        <h1 class="mb-8"> Where do you want to go? </h1>
        <div class="form-control">
          <div class="input-group drop-shadow-md">
            <input
              id="search"
              type="text"
              placeholder="Search City"
              class="input input-bordered w-full"
            />
            <button class="btn btn-square">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
            </button>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
};
</script>
<style scoped>
.callout {
  width: 100vw;
  height: 80vh;
  position: absolute;
  background: white;
  z-index: 0;
}
</style>
