order_data = {"type" : null}
var places = []
function MoveToAnotherSection(button){
    console.log(places)
    var sections = ['type_section' , 'goods_section' , 'name_section', 'final_section']
    var current_section = document.querySelector(".opened");
    var index;

    for (let i = 0; i < sections.length; i++) {
        if (current_section.id == sections[i]) {
            index = i;
            break;
        }
    }

    if(button.classList.contains('prev')){
        if (index != 0) {
            current_section.classList.add("d-none");
            current_section.classList.remove("opened");
            document.getElementById("" + sections[index - 1]).classList.remove("d-none");
            document.getElementById("" + sections[index - 1]).classList.add("opened");
        }
    }else{
        if (index != 3) {
            current_section.classList.add("d-none");
            current_section.classList.remove("opened");
            document.getElementById("" + sections[index + 1]).classList.remove("d-none");
            document.getElementById("" + sections[index + 1]).classList.add("opened");
            console.log(current_section)
            if (current_section.id == 'goods_section' && order_data.type == "RAJON") {
                document.getElementById("rajon_order").classList.remove("d-none")
            }else if(current_section.id == 'goods_section' && order_data.type != "RAJON"){
                document.getElementById("other_order").classList.remove("d-none")
            }
        }
    }

    current_section = document.querySelector(".opened");
    if (current_section.id != 'name_section') {
        document.getElementById("rajon_order").classList.add("d-none")
        document.getElementById("other_order").classList.add("d-none")
        
    }
}

document.addEventListener("DOMContentLoaded", function () {
    var typeButtons = document.querySelectorAll(".type_button");
    var places_button = document.querySelectorAll(".place_button");
    var tables_button = document.querySelectorAll(".table_button");
    var items_button = document.querySelectorAll(".item_button");
    const tableElements = document.querySelectorAll('[id^="table_"]');
    var firstGoodsToDisplay = document.querySelector('[id*="_items"]');
    firstGoodsToDisplay.classList.remove("d-none")
    var nextButton = document.querySelectorAll('.button_controller');

    items_button.forEach(function (button){
        button.addEventListener("click", function(){
            document.getElementById("form_goods_name").innerHTML = button.innerHTML
            document.getElementById("goods_form").classList.remove("d-none")
        });
    });

    typeButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            order_data.type = button.getAttribute("data-value");
            console.log(order_data)
            MoveToAnotherSection(button)
        });
    });

    tables_button.forEach(function (button) {
        button.addEventListener("click", function () {
            var dataValue = button.getAttribute("data-value");
            document.getElementById("tables_display").classList.add("d-none")
            document.getElementById("tables_" + dataValue).classList.remove("d-none")
        });
    });

    places_button.forEach(element => {
        places.push(element.getAttribute("data-value"));
    });

    places_button.forEach(function (button) {
        button.addEventListener("click", function (){
            var dataValue = button.getAttribute("data-value");
            places.forEach(element => {
                var items_board = document.getElementById(element + "_items")
                if (!items_board.classList.contains("d-none")) {
                    items_board.classList.add("d-none")
                }
            });
            document.getElementById(dataValue + "_items").classList.remove("d-none")
        });
    });

    nextButton.forEach(function (button) {
        button.addEventListener("click", function () {
            MoveToAnotherSection(button);
        });
    });
});
