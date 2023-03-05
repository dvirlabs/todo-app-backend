function onLoad() {
  var isDarkmode = localStorage.getItem("darkmode") === "true"
  if (isDarkmode){
    toggleDarkMode()
  }
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
  var isDarkMode = body.classList.contains('dark-mode');
  localStorage.setItem('darkmode', String(isDarkMode))

}


function addInput() {
  var input = document.createElement("input");
  input.setAttribute("type", "json");
  document.getElementById("input-container").appendChild(input);
}


function clearTable() {
  $.ajax({
    type: 'delete',
    url: '/clear_table'
  })
  location.reload();
}


