//<!--   @rangeField  -->
$('#duracao').change(function(){
    var duracao = $('#duracao').val()
    label_duracao = $('#label_duracao')
    switch(duracao) {
    case '0':
        label_duracao.text('30 Minutos');
        break;
    case '1':
        label_duracao.text('1 Hora');
        break;
    case '2':
        label_duracao.text('1 Hora e 30 Minutos');
        break;
    case '3':
        label_duracao.text("2 Horas");
        break;
    }   
})