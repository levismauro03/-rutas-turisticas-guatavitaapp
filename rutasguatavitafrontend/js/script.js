
const url = "https://tourist--destinations.herokuapp.com/searches";
const select = document.querySelector("#select");
const btn = document.getElementById("submit");


fetch(url, {
    method: 'GET',
  })
  .then(res => res.json())
  .then(datos => {

    for (let data of datos) {
      let newOption = document.createElement("option");
      newOption.value = data.id;
      newOption.text = data.place;
      select.add(newOption);
    }

    function searchDestination() {
        let numberDestination = document.getElementById("select").value;
        let placeDestination = datos[numberDestination - 1]["place"];
        let ubicationDestination = datos[numberDestination - 1]["ubication"];
        let descriptionDestination = datos[numberDestination - 1]["description"];
        
        document.getElementById("container").innerHTML = `<p class="fs-3"><b>${placeDestination}</b></p>
                                                          <p><b>Direccion: </b>${ubicationDestination}</p>
                                                          <p>${descriptionDestination}</p>`
    }
    
    btn.addEventListener("click", searchDestination);
  })
  .catch(function(error) {
    console.error("¡Error!", error);
  });





