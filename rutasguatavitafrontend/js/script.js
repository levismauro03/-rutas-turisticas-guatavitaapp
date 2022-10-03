
const url = "https://tourist--destinations.herokuapp.com/searches/";
// const url = "http://localhost:8000/searches/";
const select = document.querySelector("#select");
const btn = document.getElementById("submit");


const getTouristDestinations = async() => {
    const res = await fetch(url);
    const datos = await res.json();
    
    for (let data of datos) {
        let newOption = document.createElement("option");
        newOption.value = data.id;
        newOption.text = data.place;
        select.add(newOption);
    }

    return datos
};

const searchDestination = async() => {
    let datos = await getTouristDestinations();
    let numberDestination = document.getElementById("select").value;
    let placeDestination = datos[numberDestination - 1]["place"];
    let ubicationDestination = datos[numberDestination - 1]["ubication"];
    let descriptionDestination = datos[numberDestination - 1]["description"];
    
    document.getElementById("container").innerHTML = `<p class="fs-3"><b>${placeDestination}</b></p>
                                                      <p><b>Direccion: </b>${ubicationDestination}</p>
                                                      <p>${descriptionDestination}</p>`
}

window.addEventListener("load", function (){
  getTouristDestinations();
});

btn.addEventListener("click", function (){
  searchDestination();
});





