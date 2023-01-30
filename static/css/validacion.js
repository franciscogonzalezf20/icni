function validateForm() {
  var number = document.getElementById("search").value;
  if (number.length !== 13 && number.length !== 8) {
    alert("Debe ingresar 13 o 8 números");
    return false;
  }
  return true;
}
