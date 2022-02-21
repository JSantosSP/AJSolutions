<template>
  <div id="header">
    <div class="div1">
      <div class="logo">
        <img alt="logo" src="../assets/AJ.png">
      </div>
      <div id="derecha">
        <div class="option">
          <label>PIEZAS</label>
        </div>
        <div class="option">
          <label>DISEÑO 3D</label>
        </div>
        <div class="option">
          <label>ANIMACIONES</label>
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
  background: #E0E0E0;
  margin: 0%;
  color: white;
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  box-shadow:.2rem .2rem .2rem #7B1111;
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
    transition: all 400ms ease;
}

.box button .icon:hover{
   transform: translate(-3%);
   color:#B91919;
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
  padding: 4%;
  transition: all 400ms ease;
}
.option:hover{
   box-shadow: 0px 1px 10px rgba(0,0,0,0.2);
   transform: translate(-1%);
   color:#B91919;
}

.cesta{
  align-items: center;
  padding-left:0%;
  padding-right:0%;
  padding-top: 4px;
  cursor: pointer;
  transition: all 400ms ease;
}
.cesta .icon:hover{
   transform: translate(-3%);
   color:#B91919;
}
#derecha{
display: flex;
justify-content: space-around;
align-items: center;
width:45%;
margin-right: 20%;
margin-left: 3%;
}
#izquierda{
display: flex;
justify-content: space-around;
align-items: center;
width: 30%;
margin-left: 15%;
margin-right: 0%;
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
  color: #7B1111;
}
@media screen and (max-width: 750px) {
  
}
  

</style>
