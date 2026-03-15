function validarFormulario(){

let titulo = document.getElementById("titulo").value;
let ano = document.getElementById("ano_publicacao").value;
let paginas = document.getElementById("numero_paginas").value;

if(titulo == ""){
alert("O campo título é obrigatório!");
return false;
}

if(ano == "" || isNaN(ano)){
alert("O ano de publicação deve ser um número!");
return false;
}

if(paginas <= 0 || paginas == ""){
alert("O número de páginas deve ser maior que 0!");
return false;
}

return true;

}
