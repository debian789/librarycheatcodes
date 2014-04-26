$(document).ready(function(){
	$(".mostrar").click(function(){
		$(".menuMovil").toggleClass('ocultar');
	});

	$(".menuMobilPrincipal").click(function(){
		if($(".principalMenu").is(":visible")){
			$(".principalMenu").hide();
		}else{
			$(".principalMenu").show("fast");
			$(".principalMenuBuscador").hide();
		}       
	});

	$(".activarBuscador").click(function(){
		if($(".principalMenuBuscador").is(":visible")){
			$(".principalMenuBuscador").hide();
		}else{
			$(".principalMenuBuscador").show("fast");
			$(".principalMenu").hide();
		} 
	});

	$(".activarCrar").click(function(){
		if($(".ocultoCrar").is(":visible")){
			$(".ocultoCrar").hide();
		}else{
			$(".ocultoCrar").show("fast");
		} 
	});
	
	$(".masInformacionDetallada").click(function(){
		if($(".descripcionExtra").is(":visible")){
			$(".descripcionExtra").hide();
		}else{
			$(".descripcionExtra").show("fast");
		} 
	});
	$(".masOpciones").click(function(){
		if($(".filtros").is(":visible")){
			$(".filtros").hide();
			//$(".opcionBuscar2").show();
			//$(".opcionBuscar").hide();			
		}else{
			$(".filtros").show("fast");
			//$(".opcionBuscar2").hide();
			//$(".opcionBuscar").show();


		} 
	});

	$(".itemIngresar").click(function(){
		if($(".itemSesion").is(":visible")){
			$(".itemSesion").hide();
			//$(".opcionBuscar2").show();
			//$(".opcionBuscar").hide();			
		}else{
			$(".itemSesion").show("fast");
			//$(".opcionBuscar2").hide();
			//$(".opcionBuscar").show();

		} 
	});

	





	$('#itemCollection').masonry({
		columnWidth: 100,
		itemSelector: '.itemIngresadosCodigos',
		position: 'absolute',
		containerStyle: null,
	});


	$(document).on('click','.contenido', function(){ 

		$(".itemSesion").hide();
		$(".principalMenu").hide();
		

	});



// $.post( $('h4 > a').attr('href'), function( data ) {
// 	alert(data);
//   //$( ".result" ).html( data );
// });


$('.opcionEditar').on('click',function(){

	$.ajax({
		url: $(this).attr('href'),
		success: function(datos){
			$('#modalAdministracion').html(datos);

		}
	});
});



$('.opcionNuevo').on('click',function(){

	$.ajax({
		url: $(this).attr('href'),
		success: function(datos){
			$('#modalAdministracion').html(datos);

		}
	});
});



});
