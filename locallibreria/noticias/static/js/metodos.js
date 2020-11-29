/* funcion 1 Nota de los juegos*/
function CircleBar(e) 
{
    $(e)
      .circleProgress({ fill: { color: "#00EAFF" } })
      
      .on("circle-animation-progress", function(_event, _progress, stepValue) {
        $(this)
          .find("strong")
          .text(String(parseInt(100 * stepValue)));
      });
}
CircleBar(".round");

/* funcion 2 */
/*                  Formulario                 */
function validar(){
    
  var todo_correcto = true;
  if(document.getElementById('nombre').value.length < 2 ){
    alert('Necesitas llenar el nombre correctamente');
    document.getElementById('nombre').value="";
    document.getElementById('nombre').focus();
      return todo_correcto==false;
  }
  
  if(document.getElementById('password').value.length < 2 ){
    alert('Necesitas llenar la password correctamente');
    document.getElementById('password').value="";
    document.getElementById('password').focus();
      return todo_correcto==false;
  }

  var expresion = /^[a-z][\w.-]+@\w[\w.-]+\.[\w.-]*[a-z][a-z]$/i;
  var email = document.formulario2.email.value;
  if (!expresion.test(email)){
    alert('Necesitas llenar el email correctamente');
    document.getElementById('email').value="";
    document.getElementById('email').focus();
      return todo_correcto==false;
  }
  
  var a = document.formulario2.telefono.value;
  if(isNaN(a) || a.length < 2){
    alert('Necesitas ingresar numeros');
    document.getElementById('telefono').value="";
    document.getElementById('telefono').focus();
      return todo_correcto==false;
  }

  var ano = document.getElementById("Nacimiento").value;
  var mes = document.getElementById("Nacimiento").value;
  var dia = document.getElementById("Nacimiento").value;
  valor = new Date(ano, mes, dia);

  if( !isNaN(valor) ) {
    alert('Necesitas ingresar fecha de nacimiento');
    document.getElementById('Nacimiento').focus();
    return todo_correcto==false;
  }
  
  if(document.getElementById('direccion').value.length < 2 ){
    alert('Necesitas llenar la direccion correctamente');
    document.getElementById('direccion').value="";
    document.getElementById('direccion').focus();
      return todo_correcto==false;
  }
  
  if(todo_correcto==true)
  {
    alert('Creacion de usuario exitosa :D');
    document.getElementById('direccion').value="";
    document.getElementById('telefono').value="";
    document.getElementById('email').value="";
    document.getElementById('password').value="";
    document.getElementById('nombre').value="";
  }
  else
  {
  return todo_correcto
  }
  
}

  /* funcion 3 */
  /*                 FUNCION DE INICIO DE SESION                 */
function iniciar()
{
    
    var todo_bien = true;

    if(document.getElementById('usuario').value.length < 2 ){
      alert('El usuario no puede quedar en blanco');
      document.getElementById('usuario').value="";
      document.getElementById('usuario').focus();
        return todo_bien ==false;
    }

    if(document.getElementById('contraseña').value.length < 2 ){
      alert('La contraseña no puede quedar en blanco');
      document.getElementById('contraseña').value="";
      document.getElementById('contraseña').focus();
        return todo_bien ==false;
    }
    
    if(todo_bien ==true)
    {
    alert('Inicio de sesion correcto');
    document.getElementById('nombre').value="";
    document.getElementById('password').value="";    
    }
    else
    {
    return todo_bien
    }
}

/*                  Pagina Juegos              */
/* funcion 4  like*/
function myFunction(x) {
    x.classList.toggle("fa-thumbs-down");
}

/* funcion 5 limbia cuadro de comentario*/
function Limpiar(){
  document.getElementById('comentario').value="";
}