<template>
  <div class="main">
    <div class="cont">
      <div id="anima">
        <video autoplay loop> 
        <source src="../assets/Animacion.mp4" type="video/mp4"> 
        </video>
      </div>
      <div id="texto">
        <h1 class="titulo">ANIMACIONES</h1>
        <p class="par">Este servicio enfocado al ámbito industrial y de ingeniería, te permitirá enviar una idea de mecanismo en cualquier tipo de formato, para que nosotros podamos realizar una animación de este, que se devolverá en formato .mp4. 
          <br><br>Ejemplo de mecanismo: Pistón de un motor, una serie de engranajes, estructuras articulables…
        </p>
      </div>
      <div id="correo">
        <form action="futuro_php.php" method="post" enctype="multipart/form-data">
          <div class="ventana">
            <div class = "contenedor">
              <div id="desc">
                <textarea name="Desc" placeholder="Descripcion"/>
              </div>
              <div class="arch">
                <input type="file" name="archivo" accept=".pdf" required/>
              </div>
            </div>
            <div id="btn_env">
              <input type="submit"/>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AnimacionesView',
}
</script>


<style scoped>
.titulo {
  font-weight: bolder;
}
.par {
  font-size: 20px;
}
.main{
  padding: 1%;
}
.cont{
}
#anima video{
  background: transparent;
  width: 70%;
  
}
#texto{
  margin: 0 5% 0 5%;
  text-align: justify;
  font-family: 'Fredoka';
  margin-bottom: 40px;
}
#correo{
}
.ventana{
}
.contenedor{
  display: flex;
  justify-content: left;
}
#desc{
  margin-left: 5%;
  width: 40%;
  height: 150px;
}
#desc textarea{
  height: 100%;
  width: 100%;
  outline: none;
  resize: none;
  box-shadow: 0px 0px 11px rgba(102,16,15,.64);
}
#desc textarea:hover{
  box-shadow: 0px 0px 21px rgba(102,16,15,.64);
}

.arch {
  margin-left: 5%;
}
.arch input[type = file]{
  top: 0;
  left: 0;
  text-align: right;
  background: none repeat scroll 0 0 transparent;
}

#btn_env{
  padding: 2%;
}
#btn_env  input {
  font-size:13px;
  font-family:Verdana;
  width:80px;
  height:35px;
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

#btn_env input:hover {
  background: linear-gradient(rgba(102, 16, 15, 1), rgba(20, 21, 22, 1));
}
</style>
