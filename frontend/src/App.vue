<template>
  <div id="app">
    <NaamVinder/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import NaamVinder from './components/NaamVinder.vue';

@Component({
  components: {
    NaamVinder,
  },
})
export default class App extends Vue {}
</script>

<style>
body {
  width: 100%;
  height: 100%;
}

#app {

  width: 100%;
  height: 100%;

  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
