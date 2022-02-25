<template>
  <div id="general">
    <div class="container">
      <div class="foto">
        <img alt="piezas" src="../assets/Piezas.png">
      </div>
      <div class="titulo"> 
        <p>PIEZAS</p>
      </div>
      <div class="texto">
          <p>Accede a una amplia gama de piezas diseñadas para la impresión 3D.</p>
      </div>
    </div>
    <div class="container">
      <div class="foto">
        <img alt="3D" src="../assets/Diseno_3D.png">
      </div>
      <div class="titulo"> 
        <p>DISEÑO 3D</p>
      </div>
      <div class="texto">
          <p>Envíanos una pieza y consigue el croquis de esta con el archivo para imprimirlo en tu maquina 3D.</p>
      </div>
    </div>
      <div class="container">
        <div class="foto">
          <img alt="3D" src="../assets/Animaciones.png">
        </div>
        <div class="titulo"> 
          <p>ANIMACIONES</p>
        </div>
        <div class="texto">
          <p>Envíanos una idea de un mecanismo y consigue tu animación personalizada.</p>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'HomeView',
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
.titulo{
  text-align: center;
  font-size: 30px;
  font-weight: bolder;
  color: black;
}
#general .container{
  width: 30%;
  height: 80px%;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  margin: 1%;
  text-align: center;
  transition: all 0.25s;
  cursor: pointer;
  align-items: center;
}
#general .container:hover{
  transform: translateY(-15px);
  box-shadow: 0 10px 14px rgba(0, 0, 0, 0.2);
}
.foto img{
 width: 30%;
 height: 30%;
}
.texto{
  font-size: 20px;
  color: black;
}
</style>
