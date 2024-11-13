var sale = 0;
$('#model').click(function(){
  if ($('#model').val() != 0) {
    $('#memory-container').removeClass("d-none");
    $('#memory-container').addClass("d-block");
  }
  else {
    $('#memory-container').removeClass("d-block");
    $('#memory-container').addClass("d-none");
  }
});

$('#memory').click(function(){
  if ($('#memory').val() != 0) {
    $('#sale').removeClass("d-none");
    $('#sale').addClass("d-block");
  }
  else {
    $('#sale').removeClass("d-block");
    $('#sale').addClass("d-none");
  }
});
