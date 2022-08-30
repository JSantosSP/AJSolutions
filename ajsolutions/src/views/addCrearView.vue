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
              Precio
            </h3>
          </div>
          <div class="text">
            <h3>
              Descripcion
            </h3>
          </div>
        </div>
        <div class="cajas">
          <div class="bx">
            <input type="text" name = "nombre" >
          </div>
          <div class="bx">
            <input type="text" name = "precio" >
          </div>
          <div class="bx">
            <textarea name = "desc" />
          </div>
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

.bx textarea{
  width: 200px;
  border: none;
  outline: none;
  resize: none;
}
.arch {
  margin-left: 5%;
  border: 5px dashed #273e4e;
  width: 400px;
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
  margin-top: 5%;
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
