<template>
  <div id="general">
    <div class="todo">
      <div class="cont">
        <div class="texts">
          <div class="text">
            <h3>
              Nombre
            </h3>
          </div>
          <div class="text">
            <h3>
              Apellidos
            </h3>
          </div>
          <div class="text">
            <h3>
              Tel.
            </h3>
          </div>
          <div class="text">
            <h3>
              Correo electrónico
            </h3>
          </div>
          <div class="text">
            <h3>
              Dirección postal
            </h3>
          </div>
          <div class="text">
            <h3>
              Codigo postal
            </h3>
          </div>
          <div class="text">
            <h3>
              Nombre de Usuario
            </h3>
          </div>
          <div class="text">
            <h3>
              Contraseña
            </h3>
          </div>
          <div class="text">
            <h3>
              Repetir Contraseña
            </h3>
          </div>
        </div>
        <div class="cajas">
          <div class="bx">
            <input type="text" name = "nombre" >
          </div>
          <div class="bx">
            <input type="text" name = "apellidos" >
          </div>
          <div class="bx">
            <input type="text" name = "Telefono" >
          </div>
          <div class="bx">
            <input type="text" name = "correo_electronico" >
          </div>
          <div class="bx">
            <input type="text" name = "direción_postal" >
          </div>
          <div class="bx">
            <input type="text" name = "codigo_postal" >
          </div>
          <div class="bx">
            <input type="text" name = "nombre_de_usuario" >
          </div>
          <div class="bx">
            <input type="password" name = "contraseña" >
          </div>
          <div class="bx">
            <input type="password" name = "repetir_contraseña" >
          </div>
        </div>
      </div>
    <div id="btn_env">
      <a href="#">Registrar</a>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ViewCrear',
  data(){
    return {
      files: new Array(),
      visible: true,
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
.todo{
  display: flex;
  flex-direction: column;
}
.cont{
  display: flex;
  justify-content: space-between;
}
.texts{
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  margin-right: 5%;
}
.text{
  display: flex;
  justify-content: start;
  width: 250px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.cajas{
  display: flex;
  justify-content: space-around;
  flex-direction: column;
  margin-left: 10px;
}
.bx input{
  width: 200px;
  height: 25px;
  border: none;
  outline: none;
}   
#btn_env{
  padding: 2%;
  margin-top: 5%;
}
#btn_env  a {
  font-size:13px;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
  padding: 15px 30px;
  border-width:1px;
  color:#fff;
  border-color:rgba(52, 55, 56, 1);
  border-top-left-radius:8px;
  border-top-right-radius:8px;
  border-bottom-left-radius:8px;
  border-bottom-right-radius:8px;
  box-shadow: 0px 10px 14px -7px rgba(102, 16, 15, 1);
  text-shadow: 0px 1px 0px rgba(102, 16, 15, 1);
  background:linear-gradient(rgba(20, 21, 22, 1), rgba(102, 16, 15, 1));
  }

#btn_env a:hover {
  background: linear-gradient(rgba(102, 16, 15, 1), rgba(20, 21, 22, 1));
}
</style>
