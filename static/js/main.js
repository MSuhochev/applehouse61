/* jshint jquery:true */
(function() {
    "use strict";

    // Кнопка прокрутки
    var btn = $('#button');

    // Добавляем/удаляем класс при прокрутке
    $(window).scroll(function() {
        if ($(window).scrollTop() > 300) {
            btn.addClass('show');
        } else {
            btn.removeClass('show');
        }
    });

    // Обработчик клика по кнопке
    btn.on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({scrollTop: 0}, 300);
    });

    // Функция для тумблера навигации
    function myFunction(x) {
        x.classList.toggle("change");
    }

    // Скрываем прелоадер
    $(document).ready(function() {
    // После загрузки страницы скрыть прелоадер
    $(window).on('load', function() {
        $('#hellopreloader_preload').fadeOut(1000); // скрывает прелоадер за 2 сек
    });
});


})();
