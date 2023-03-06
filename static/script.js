var theam = "light";
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
                $('<td class="task_id">').text("#"+row.id.toString()),
                $('<td class="task_data">').text(row.task),
                $('<td class="task_status">').text(row.status)
            )
          );
        });
      }
    });
  }
  
  
  
  
  function toggleDarkMode() {
    const body = document.body;
    const theam_but_text = document.getElementById("theam_but_text");
    const theam_but_image = document.getElementById("theme-btn-img");
    console.log(theam_but_image);
    
    if(theam == "light"){
      body.classList.toggle("dark_mode");
      theam_but_text.innerHTML = "Dark";
      theam_but_image.src = "./static/images/moon.svg"
      theam = "dark";
    }
    else if(theam == "dark"){
      body.classList.toggle("dark_mode");
      theam_but_text.innerHTML = "Light";
      theam_but_image.src = "./static/images/light.svg"
      theam = "light";
    }
  }
  
  
  function addInput() {
    var input = document.createElement("input");
    input.setAttribute("type", "json");
    document.getElementById("input-container").appendChild(input);
  }

  function updateDatabase() {
    
  }
  
  
  function clearTable() {
    $.ajax({
      type: 'delete',
      url: '/clear_table'
    })
    location.reload();
  }
  
  