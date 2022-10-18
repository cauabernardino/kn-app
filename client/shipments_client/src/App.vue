<template>
  <div id="app">
    <ShipmentsList />
  </div>
</template>

<script>
import ShipmentsList from './components/ShipmentsList.vue'


export default {
  name: 'App',
  components: {
    ShipmentsList,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  justify-content: center;
  align-items: center;
  display: flex;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
}
</style>
