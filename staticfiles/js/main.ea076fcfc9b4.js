$(document).ready(function(){
	$(".mostrar").click(function(){
		$(".menuMovil").toggleClass('ocultar');
	});

	$(".menuMobilPrincipal").click(function(){
		if($(".principalMenu").is(":visible")){
			$(".principalMenu").hide();
		}else{
			$(".principalMenu").show();
			$(".principalMenuBuscador").hide();
		}       
	});

	$(".activarBuscador").click(function(){
		if($(".principalMenuBuscador").is(":visible")){
			$(".principalMenuBuscador").hide();
		}else{
			$(".principalMenuBuscador").show();
			$(".principalMenu").hide();
		} 
	});

	$(".activarCrar").click(function(){
		if($(".ocultoCrar").is(":visible")){
			$(".ocultoCrar").hide();
		}else{
			$(".ocultoCrar").show();
		} 
	});
	
	$(".masInformacionDetallada").click(function(){
		if($(".descripcionExtra").is(":visible")){
			$(".descripcionExtra").hide();
		}else{
			$(".descripcionExtra").show();
		} 
	});
	$(".masOpciones").click(function(){
		if($(".filtros").is(":visible")){
			$(".filtros").hide();
			//$(".opcionBuscar2").show();
			//$(".opcionBuscar").hide();

			
		}else{
			$(".filtros").show();
			//$(".opcionBuscar2").hide();
			//$(".opcionBuscar").show();


		} 
	});

});
