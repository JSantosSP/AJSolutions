<template>
  <div id="general">
    <div id="contenido">
      <div class="imagenes">
        <div class="fotosP">
          <div class="fotoP" @click="chageImgG('Animaciones')">
            <img alt="piezas" src="../assets/Animaciones.png">
          </div>
          <div class="fotoP" @click="chageImgG('Piezas')">
            <img alt="piezas" src="../assets/Piezas.png">
          </div>
          <div class="fotoP" @click="chageImgG('Animaciones')">
            <img alt="piezas" src="../assets/Piezas.png">
          </div>
          <div class="fotoP" @click="chageImgG('Animaciones')">
            <img alt="piezas" src="../assets/Piezas.png">
          </div>
        </div>
        <div class="fotoG">
          <img id="fg" alt="pieza" :src="require('@/assets/'+fotoG+'.png')">
        </div>
      </div>
      <div class="textos">
        <p id="titulo">{{pieza.nombre}}</p>
        <p id="descr">{{pieza.descripcion}}</p>
        <p id="precio">{{pieza.precio}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ViewPieza',
  data(){
    return {
      pieza: JSON.parse(this.$route.params.obj),
      fotoG: "Piezas"
    }
  },
  methods: {
    chageImgG(nombre) {
      this.fotoG = nombre;
    }
  }
}
</script>


<style scoped>
#general{
  width: 100%;
  height: 60%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin: auto;
  padding-top: 8%;
  padding-bottom: 8%;
}
#contenido{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin: 10px;
  border-style: groove;
  border-color: black;
}
.imagenes{
  margin: 5px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  border-style: groove;
  border-color: black;
}
.fotosP{
  border-style: groove;
  border-color: black;
}
.fotoP{
  margin: 1px;
  border-style: groove;
  border-color: black;
}
.fotoG{
  border-style: groove;
  border-color: black;
  padding: 128px;
}
.textos{
  margin: 5px;
  border-style: groove;
  border-color: black;
}
#titulo{

}
#descr{

}
#precio{

}
</style>
