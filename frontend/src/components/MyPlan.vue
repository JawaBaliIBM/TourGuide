<template>
  <div class="px-6">
    <div class="prose mb-2">
      <h3>Ongoing Plan</h3>
    </div>
    <FixedPackageList :packages="myPackages" class="max-h-48 overflow-auto" fixed />
  </div>
</template>
<script>
import FixedPackageList from '@/components/FixedPackageList.vue';

export default {
  name: 'MyPlan',
  components: {
    FixedPackageList,
  },
  data() {
    return {
      categories: [
        {
          name: 'Jalan jalan santai',
          imagesUrl: 'https://api.lorem.space/image/album?w=400&h=100',
        },
      ],
      myPackages: [
        {
          id: 1,
          name: 'Aare',
          imagesUrl: 'https://api.lorem.space/image?w=400&h=400',
          location: 'Bern, Swiss',
          time: '09.00 - 10.00',
          description: 'Lorem ipsum dolor sit amet syalalala syalalhi',
          price: 10000,
        },
        {
          id: 2,
          name: 'Culinary',
          imagesUrl: 'https://api.lorem.space/image?w=400&h=400',
          location: 'Bandung, Jawa Barat',
          time: '09.00 - 10.00',
          description: 'Lorem ipsum dolor sit amet syalalala syalalhi',
          price: 10000,
        },
        {
          id: 3,
          name: 'Leisure',
          imagesUrl: 'https://api.lorem.space/image?w=400&h=400',
          location: 'Bandung, Jawa Barat',
          time: '09.00 - 10.00',
          description: 'Lorem ipsum dolor sit amet syalalala syalalhi',
          price: 10000,
        },
        {
          id: 4,
          name: 'Wellness',
          imagesUrl: 'https://api.lorem.space/image?w=400&h=400',
          location: 'Bandung, Jawa Barat',
          time: '09.00 - 10.00',
          description: 'Lorem ipsum dolor sit amet syalalala syalalhi',
          price: 10000,
        },
      ],
    };
  },
};
</script>
