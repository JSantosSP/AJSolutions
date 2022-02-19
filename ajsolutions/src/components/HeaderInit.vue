<template>
  <div id="header">
    <div class="div1">
      <div class="logo">
        <img alt="logo" src="../assets/AJ.png">
      </div>
      <div id="buscador">
        <input type="text" name="navegador">
      </div>
      <div class="option">
        <label>Piezas</label>
      </div>
      <div class="option">
        <label>Diseño 3D</label>
      </div>
      <div class="option">
        <label>Animaciones</label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HeaderInit'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#header{
  background: grey;
  margin: 0%;
  color: white;
}
#buscador{
  margin: 20px;
}
.logo img{
  margin-left: 0%;
  width: 40px;
}
.div1{
  display: flex;
  justify-content: flex-start;
}
.option{
  margin: 20px;

}
template label{
padding: 100px;
}

</style>
