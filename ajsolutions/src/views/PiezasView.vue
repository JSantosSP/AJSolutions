<template>
  <div id="general">
    <div class="container" v-for="(pieza,index) in piezas.piezas" :key="index">
      <div @click="routeGo(pieza)">
        <div class="foto">
          <img alt="piezas" src="../assets/Piezas.png">
        </div>
        <div class="pie_foto">
          <div class="titulo"> 
            <p>{{pieza.nombre}}</p>
          </div>
          <div class="precio"> 
            <p>{{pieza.precio}}€</p>
          </div>
        </div>
      </div>
    </div>
    <div>
      <router-link to = "/introducir_pieza">
        <div class="plus">
          <div class="fot">
            <img alt="piezas" src="../assets/plus.png">
          </div>
        </div>
      </router-link>
    </div> 
  </div>
</template>

<script>
export default {
  name: 'PiezasView',
   data() {
    return {
      piezas: {},
    }
  },
  methods: {
    leerBaseDatos(){
      this.piezas = 
      {
        piezas:
        [
          {
            id_Pieza: 1,
            nombre: 'ejemplo1',
            precio: 23.30,
            descripcion: 'ejemplo 1 kjnvskjd kjsdc',
            n_com: 0,
            n_vis: 0
          },
          {
            id_Pieza: 2,
            nombre: 'ejemplo2',
            precio: 25.45,
            descripcion: 'ejemplo 2 kjnvskjd kjsdc',
            n_com: 0,
            n_vis: 0
          },
          {
            id_Pieza: 3,
            nombre: 'ejemplo3',
            precio: 80.27,
            descripcion: 'ejemplo 3 kjnvskjd kjsdc',
            n_com: 0,
            n_vis: 0
          }
        ]
      }
    },
    routeGo(pieza){
      this.$router.push({
        name: "viewPieza",
        params:{
          nombre: pieza.nombre,
          obj: JSON.stringify(pieza)
        }
      });
    }
  },
  beforeMount() {
    this.leerBaseDatos();
    console.log(this.piezas);
  }
}
</script>


<style scoped>
a{
  text-decoration: none;
}
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
#general .container{
  width: 30%;
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
.plus{
  margin-top: 8%;

}
.foto img{
 width: 30%;
 height: 30%;
}
.fot img{
 width: 30%;
 height: 30%;
 box-shadow: 0 2px 2px rgba(0, 0, 0, 0.2);
 overflow: hidden;
 margin: 1%;
 text-align: center;
 transition: all 0.25s;
 cursor: pointer;
 align-items: center;
 border-radius: 76px;
}
.fot img:hover{
  transform: translateY(-15px);
  box-shadow: 0 10px 14px rgba(0, 0, 0, 0.2);
}
.pie_foto{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: auto;
}
.titulo{
  text-align: center;
  font-size: 15px;
  color: black;
  padding: 5px;
}
.precio{
  text-align: center;
  font-size: 15px;
  color: grey;
  padding: 5px;
}
</style>
