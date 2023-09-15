document.addEventListener("DOMContentLoaded", function () {
    var commonButtons = document.querySelectorAll(".type_button");
    var goods_button = document.querySelectorAll(".place_button");
    console.log(placesData)

    commonButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            // var dataValue = button.getAttribute("data-value");
            document.getElementById("type_section").classList.add("d-none");
            document.getElementById("goods_section").classList.remove("d-none");
            document.getElementById(placesData[0].name + "_items").classList.remove("d-none")
        });
    });

    goods_button.forEach(function (button) {
        button.addEventListener("click", function (){
            var dataValue = button.getAttribute("data-value");
            placesData.forEach(element => {
                var items_board = document.getElementById(element.name + "_items")
                if (!items_board.classList.contains("d-none")) {
                    items_board.classList.add("d-none")
                }
            });
            document.getElementById(dataValue + "_items").classList.remove("d-none")
        });
    });
});
