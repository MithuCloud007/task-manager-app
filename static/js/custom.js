//modal code start
$('DOCUMENT').ready(function(){
    $(document).on('click','#softDelete',function(){
    var deleteID=$(this).data('id');
    $('.modal_body #modalID').val(deleteID)
    
    });
    
    });
  
  
  //datatable code start
  $('#allTableInfo').dataTable( {
    "ordering": false,
    "searching": true,
  } );
  //message auto hide
  $(document).ready(function(){
    $('.alert_primary').fadeOut(5000);
  });
  