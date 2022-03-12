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
        <!--<form action="Futuro_PHP.php" method="post" enctype="multipart/form-data">-->
          <div class="ventana">
            <div class = "contenedor">
              <div id="desc">
                <textarea name="Desc" placeholder="Descripcion"/>
              </div>
              <div @dragover.prevent="dragOver()" @dragleave.prevent="dragLeave()" @drop.prevent="dropPDF($event)" class="arch" id="arch">
                <h1 v-show="visible" id="dragText">Arrastra tu archivo</h1>
                <div class="ic">
                  <div v-for="(file,index) in files" :key="index">
                    <img src="../assets/PDF.png" v-if="file.type == 'application/pdf'">
                    <img src="../assets/PNG.png" v-else>
                    <span v-for="(letra, id) in file.name" :key="id"><span v-show="id < 5">{{letra}}</span></span>
                    ...<span class="material-icons trash" @click="deleteFile(index)">delete_outline</span>
                  </div>
                </div>
                <button @click="clickPDF()">Selecciona tus archivos</button>
                <input type="file" name="archivo" id="inputFile" @change="inputChange($event)" hidden multiple>
              </div>
            </div>
            <div id="btn_env">
              <input type="submit" id="save"/>
            </div>
          </div>
        <!--</form>-->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AnimacionesView',
  data() {
    return {
      files: new Array(),
      visible: true,
    }
  },
  methods: {
    dragOver(){
      const dropArea = document.getElementById("arch");
      const dragText = document.getElementById("dragText");
      dropArea.classList.add("active");
      dragText.textContent = "Sulta para subir los archivos";
    },
    dragLeave(){
      const dropArea = document.getElementById("arch");
      const dragText = document.getElementById("dragText");
      dropArea.classList.remove("active");
      dragText.textContent = "Arrastra tu archivo";
    },   
    dropPDF(event) {
      this.addFile(event.dataTransfer.files);
      const dropArea = document.getElementById("arch");
      const dragText = document.getElementById("dragText");
      dropArea.classList.remove("active");
      dragText.textContent = "Arrastra tu archivo";
    },
    clickPDF() {
      const input = document.getElementById("inputFile");
      input.click();
    },
    showFiles(){
      var files = document.getElementById("inputFile").files;
      var ok = true;
      if(files.length != undefined){
        for(const file of files){
          ok = this.processFile(file);
          if(!ok){
            break;
          }
        }
      }
      if(!ok){
        alert("Solo png/jpg/pdf");
        const input = document.getElementById("inputFile");
        input.value = "";
      }
    },
    processFile(file){
      const docType = file.type;
      const validExtensons = ['image/png', 'image/jpg','image/jpeg', 'application/pdf']
      if(!validExtensons.includes(docType)){
        return false;
      }
      return true;
    },
    inputChange(){
      const dropArea = document.getElementById("arch");
      dropArea.classList.add("active");
      this.showFiles();
      dropArea.classList.remove("active");
      this.addFile(document.getElementById("inputFile").files);
    },
    addFile(files){
      for(var i = 0; i < files.length; ++i){
        var ok = true;
        this.files.forEach(file => {
          if(file.name == files[i].name){
            ok = false;
          }
        });
        if(ok){
          this.files.push(files[i]);
        }
      }
      this.visible = false;
    },
    deleteFile(id){
      this.files = this.borrar(this.files,id);
      if(this.files.length == 0){
        this.visible = true;
      }
    },
    borrar(lista,id){
      var aux = new Array();
      for(var i = 0; i < lista.length; ++i){
        aux.push(lista[i]);
      }
      aux.splice(id,1);
      return aux;
    }
  }
}
</script>

<style scoped>
.main{
  padding: 1%;
}
.cont{
}
#anima video{
  width: 70%;
}
#texto{
  margin: 0 5% 0 5%;
  text-align: justify;
  font-family: 'Fredoka';
  margin-bottom: 40px;
}
.titulo {
  font-weight: bolder;
}
.par {
  font-size: 20px;
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
  height: 180px;
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
  border: 5px dashed #273e4e;
  width: 40%;
  height: 180px;
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.arch input[type = file]{
  top: 0;
  left: 0;
  text-align: right;
  background: none repeat scroll 0 0 transparent;
}
.arch.active{
  background-color: #b8d4fe;
  color: black;
  border: 2px dashed #618ac9;
}
.arch h1{
  font-weight: bolder;
  font-family: 'Fredoka';
  font-size: 30px;
}
.ic {
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: default;
}
.ic img{
  display: flex;
  width: 60px;
  flex-direction:column;
  font-family: 'Fredoka';
}
.trash{
  cursor: pointer;
}

.arch button{
  padding: 10px 25px;
  font-size: 15px;
  border: 0;
  outline: none;
  background-color: #4A7491;
  color: white;
  border-radius: 8px;
  margin-top: 5px;
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
