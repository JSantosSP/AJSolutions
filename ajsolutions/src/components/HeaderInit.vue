<template>
  <div id="header">
    <div class="div1">
      <div id="logo">
        <img alt="logo" src="">
      </div>
      <div id="buscador">
        <input type="text" name="navegador">
      </div>
      <div class="option">
        <label>op1</label>
      </div>
      <div class="option">
        <label>op2</label>
      </div>
      <div class="option">
        <label>op3</label>
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
  background: black;
  margin: 0%;
  color: white;
}
#buscador{
  margin: 20px;
}
#logo{
  margin-left: 0%;
}
.div1{
  display: flex;
  justify-content: flex-start;
}
.option{
  margin: 20px;

}

</style>
