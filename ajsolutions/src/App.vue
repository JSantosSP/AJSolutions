<template>
  <div id="header">
    <div class="div1">
      <router-link to = "/">
        <div class="logo">
          <img alt="logo" src="./assets/AJ.png">
        </div>
      </router-link>
      <div id="derecha" class="container-fluid">
        <div class="row">
          <router-link to = "/piezas">
            <div class="option col-md-12 col-sm-12 col-xs-12">
              <label class="cLabel">PIEZAS</label>
            </div>
          </router-link>
          <router-link to = "/3d">
            <div class="option col-md-12 col-sm-12 col-xs-12">
              <label class="cLabel">DISEÑO 3D</label>
            </div>
          </router-link>
          <router-link to = "/animaciones">
            <div class="option col-md-12 col-sm-12 col-xs-12">
              <label class="cLabel">ANIMACIONES</label>
            </div>
          </router-link>
        </div>
      </div>
      <div id="izquierda" class="container-fluid">
        <div class="row">
          <div class="box col-lg-10 col-md-12 col-sm-12 col-xs-12">
            <form action="#">
              <input type="text"
                    placeholder="Search"
                    name="search">
            </form>
            <button>
                  <span class="material-icons icon">
                    search
                  </span>
            </button>
          </div>
          <router-link to = "/iniciar_sesion">
            <div class="cesta col-lg-2 col-md-12 col-sm-12 col-xs-12">
              <span class="material-icons icon"> shopping_cart </span>
            </div>
          </router-link>
        </div>
      </div>
      <router-link to = "/user">
        <div class="user">
            <span class="material-symbols-outlined icon"> account_circle</span>
        </div>
      </router-link>
    </div>
  </div>
  <div id="contenedor">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data(){
    return{
    }
  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#header{
  background: #E0E0E0;
  margin: 0%;
  color: white;
  position: fixed;
  z-index: 6;
  left: 0;
  top: 0;
  width: 100%;
  box-shadow:.2rem .2rem .2rem #7B1111;
}
#contenedor {
  margin-top: 120px;
  width: 100%;
}
.box{
  display:flex;
  align-items: center;
  background: white;
  border-radius: 25px;
  height: 29px;
  width: 200px;
}

.box input[type=text]{
    width: 127px;
    height: 25px;
    border-radius:25px;
    border: none;
    outline: none;
    margin-right: 10px;
}    
.box button{
    background-color: transparent;
    color: #f2f2f2;
    margin-left: 0px;
    padding-right: 0px;
    padding-top: 4px;
    font-size: 12px;
    border: none;
    transition: all 400ms ease;
}

.box button .icon:hover{
   transform: translate(-3%);
   color:#B91919;
   cursor: pointer;
}
.logo img{
  margin-left: 45%;
  margin-top: 25%;
  margin-right:0%;
  width: 60px;
  cursor: pointer;
  transition: all 400ms ease;
}
.logo img:hover{
  transform: translate(-5%);
}
.div1{
  display: flex;
  justify-content: space-around;
}
.option{
  cursor: pointer;
  display:inline-block;
  color: #7B1111;
  font-weight: bolder;
  font-family:"Arial";
  width: 110%;
  transition: all 400ms ease;
}
.option label{
  cursor: pointer;
  width: max-content;
  margin: 10px;
}
.option:hover{
   box-shadow: 0px 1px 10px rgba(0,0,0,0.2);
   transform: translate(-1%);
   color:#B91919;
}

.cesta{
  align-items: center;
  padding-left: 75%;
  padding-right:0%;
  padding-top: 4px;
  transition: all 400ms ease;
}
.cesta .icon:hover{
   transform: translate(-3%);
   color:#B91919;
   cursor: pointer;
}
.user{
  align-items: center;
  padding-top: 16px;
  transition: all 400ms ease;
  margin-left: -25%;
  margin-right: 1%;
}
.user .icon:hover{
   transform: translate(-3%);
   color:#B91919;
   cursor: pointer;
}
.user span{
  font-size: 60px;
}
#derecha{
display: flex;
justify-content: space-around;
align-items: center;
width:45%;
margin-right: 10%;
margin-left: 3%;
}
#izquierda{
display: flex;
justify-content: space-around;
align-items: center;
width: 30%;
margin-left: 10%;
margin-right: 0%;
}
.icon{
  color: #7B1111;
}

</style>
