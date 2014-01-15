$(document).ready(function(){
	$(".mostrar").click(function(){
		//$(this).parent().css('padding-bottom','1em')
		//$(".oculto").css('display','inline');
       $(".menuMovil").toggleClass('ocultar');
	});

	$(".menuMobilPrincipal").click(function(){
		//$(this).parent().css('padding','0')
       $(".principalMenu").toggleClass('ocultarMenu');

		//$(".ocultarMenu").css('display','inline');
       //$(".menuMovil").toggleClass('ocultar');
	});

// 	//alert("hola");

// //$('#myTab a:last').tab('show'); 
// $.each($("select[multiple]"), function () {  
// 	//alert("da");
//  // "Locations" can be any label you want   /static/admin/img/selector-search.gif

//  SelectFilter.init(this.id, "S.O", 0, "/static/");  
// });
 });
