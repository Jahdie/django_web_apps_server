buttons_array = document.getElementsByName("tabs_for_disp_svodka")
console.log(buttons_array, '!!!!!!!!!!!!!!!!!!')
button_class = buttons_array.item(0).classList
button_class.add("active")
var prev_btn_index = 0
// var btn_index =0
for (let i = 0; i < buttons_array.length; i++) {
    buttons_array.item(i).onclick = function (f) {
        var date = document.getElementById("datepicker")
        console.log(buttons_array)
        console.log(date.value)
        var date_selected = date.value
        var tab_name = buttons_array.item(i).id
        btn_index = i
        button_class = buttons_array.item(btn_index).classList
        button_class.add("active")
        console.log(prev_btn_index, btn_index, tab_name)
        if (prev_btn_index !== btn_index) {
            button_class = buttons_array.item(prev_btn_index).classList
            button_class.remove("active")
        }
        prev_btn_index = btn_index
        // console.log(date_selected, tab_name)
        $.ajax({
            url: "/summary_per_hour/" + date_selected + "/" + tab_name + "/",
            success: function (data) {
                // console.log(data)
                $("#test").html(data)
                // $("#test").html(data)
            }
        })
    }
}
