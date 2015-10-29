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


	$('body').on('click','#agregarCampoItemComandos',function(e){
		$('.itemsComandosTabla').append('<tr><td><input id="id_instruccion" maxlength="500" name="instruccion[]" type="text"></td><td><textarea cols="40" id="id_descripcion" name="descripcion[]" rows="1"></textarea></td></tr>');
		e.preventDefault();
	})

$('.editarItemComando').click(function(){
	$.ajax({
		url: '/comandoItem/editar/4/11/',
		success: function(datos){
			$('#modalAdministracion').html(datos);

		}
	});
});


	$('.eliminarComandoItem').click(function(e){
		var r = confirm("Realmente desea elimarlo ? ");
		if(r== true){
			return true;
		}else{
			e.preventDefault();
		}
	})




	$('#itemCollection').masonry({
		columnWidth: 200,
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
