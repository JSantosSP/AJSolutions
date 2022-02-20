<template>
  <div id="header">
    <div class="div1">
      <div class="logo">
        <img alt="logo" src="../assets/AJ.png">
      </div>
      <div id="derecha">
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
      <div id="izquierda">
        <div class="box">
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
        
        <div class="cesta">
          <span class="material-icons icon"> shopping_cart </span>
        </div>
      </div>
      
      
    </div>
  </div>
</template>

<script>
export default {
  name: 'HeaderInit'
}
</script>

<style scoped>
#header{
  background: grey;
  margin: 0%;
  color: white;
}
.box input[type=text]{
    width:150px;
    height: 25px;
    border-radius:25px;
    border: none;
    outline: none;
    padding-left: 10px;
}
      

      
.box button{
    background-color: transparent;
    color: #f2f2f2;
    padding-left: 5px;
    padding-top: 4px;
    font-size: 12px;
    border: none;
    cursor: pointer;
} 
.logo img{
  margin-left: 10%;
  margin-top: 25%;
  width: 40px;
}
.div1{
  display: flex;
  justify-content: space-between;
}
.option{
  margin: 2%;

}
.cesta{
  align-items: center;
  padding: 2%;
}
#derecha{
display: flex;
justify-content: space-around;
align-items: center;
width:40%;
}
#izquierda{
display: flex;
justify-content: space-around;
align-items: center;
width: 30%;
}
.box{
  display:flex;
  align-items: center;
  background: white;
  border-radius: 25px;
  height: 29px;
  width: 200px;
}
.icon{
  color: black;
}
</style>
