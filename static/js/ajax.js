$( document ).ready(function() {
    $("#btn").click(
		function(){
			sendAjaxForm('result_form', 'ajax_form', 'action_ajax_form.php');
			return false;
		}
	);
});

function sendAjaxForm(result_form, ajax_form, url) {
    $.ajax({
        url:     "https://web.crooteam.com:9000/feedback", //url страницы (action_ajax_form.php)
        type:     "POST", //метод отправки
        dataType: "html", //формат данных
        data: $("#"+ajax_form).serialize(),  // Сеарилизуем объект
        success: function(response) { //Данные отправлены успешно
        	result = $.parseJSON(response);
        	$('#result_form').html('Заявка успешно отправлена! Имя: '+result.name+'<br>Телефон: '+result.phonenumber);
      	},
      	error: function(response) { // Данные не отправлены
              $('#result_form').html('Ошибка. Данные не отправлены.');
      	}
 	});
}



// $( document ).ready(function() {
//   $("body").on("click","#btn",function(){
//     $.ajax({
//         url:     "https://web.crooteam.com:9000/feedback", //url страницы (action_ajax_form.php)
//         type:     "POST", //метод отправки
//         dataType: "html", //формат данных
//         data: $("#"+ajax_form).serialize(),  // Сеарилизуем объект
//         success: function(response) { //Данные отправлены успешно
//           result = $.parseJSON(response);
//           $('#result_form').html('Заявка успешно отправлена! Имя: '+result.name+'<br>Телефон: '+result.phonenumber);
//         },
//         error: function(response) { // Данные не отправлены
//               $('#result_form').html('Ошибка. Данные не отправлены.');
//         }
//   });
// })
