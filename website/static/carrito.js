//Declaro objeto item1 
var item1 = {
	precio : document.getElementById("price1").textContent,
	cantidad: document.getElementById("cantidad1")}
//Declaro item 2
var item2 = {
	precio : document.getElementById("price2").textContent,
	cantidad: document.getElementById("cantidad2")}
	
var price1 = parseFloat(item1.precio).toFixed(2)
//Evento para recibir si la cantidad cambia
item1.cantidad.addEventListener("change", function(){
	var cantity1 = document.getElementById("cantidad1").value;
	var totalItem1 = price1 * cantity1;
	document.getElementById("totalItem1").innerHTML = totalItem1 + "$";
	//Da total
	var cantity2 = document.getElementById("cantidad2").value;
	var totalItem2 = price2 * cantity2;
	var total = totalItem1 + totalItem2;
	document.getElementById("total").innerHTML = total;
	document.getElementById("totalConIva").innerHTML = total + (total * 0.21) + "$"
})

var price2 = parseFloat(item2.precio).toFixed(2)
//Evento para recibir si la cantidad cambia
item2.cantidad.addEventListener("change", function(){
	var cantity2 = document.getElementById("cantidad2").value;
	var totalItem2 = price2 * cantity2;
	document.getElementById("totalItem2").innerHTML = totalItem2 + "$";
	//da total---- Resuelvo lo mismo en ambas, para que escuche ambos y de la suma
	var cantity1 = document.getElementById("cantidad1").value;
	var totalItem1 = price1 * cantity1;	
	var totalItem2 = price2 * cantity2;
	var total = totalItem1 + totalItem2;
	document.getElementById("total").innerHTML = total;
	document.getElementById("totalConIva").innerHTML = total + (total * 0.21) + "$"
	})

