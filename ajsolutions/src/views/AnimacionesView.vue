<template>
  <div class="main">
    <div class="cont">
      <div id="anima">
        <h1>Lorem Ipsum</h1>
      </div>
      <div id="texto">
        <pre>
            "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
          "There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain..."
        </pre>
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
.main{
  padding: 1%;
}
.cont{
}
#anima{
}
#texto{
  margin: 0 5% 0 5%;
}
#correo{
}
.ventana{
}
.contenedor{
  display: flex;
  justify-content: center;
}
#desc{
  margin-left: 15%;
  width: 40%;
  height: 150px;
}
#desc textarea{
  height: 95%;
  width: 95%;
  outline: none;
  resize: none;
  box-shadow: 0px 0px 11px rgba(102,16,15,.64);
}
#desc textarea:hover{
  box-shadow: 0px 0px 21px rgba(102,16,15,.64);
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
