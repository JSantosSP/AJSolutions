<template>
  <div>
    <p>{{pieza.nombre}}</p>
    <p>{{pieza.descripcion}}</p>
    <p>{{pieza.precio}}</p>
  </div>
</template>

<script>
export default {
  name: 'ViewPieza',
  data(){
    return {
      pieza: JSON.parse(this.$route.params.obj)
    }
  }
}
</script>


<style scoped>

</style>
