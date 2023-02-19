function onLoad() {
  $.ajax({
    type: 'GET',
    url: '/table',
    dataType: 'json',
    success: function(data) {
      var table = $('#pg_table');
      $.each(data.results, function(index, row) {
        table.append(
          $('<tr>').append(
            $('<td>').text(row.id),
            $('<td>').text(row.task),
            $('<td>').text(row.status)
          )
        );
      });
    }
  });
}



function toggleDarkMode() {
  var body = document.getElementsByTagName('body')[0];
  body.classList.toggle('dark-mode');
}
