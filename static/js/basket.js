window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var t_hr = event.target;

        $.ajax({
            url: "/baskets/edit/" + t_hr.name + "/" + t_hr.value + "/",
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        })
        event.preventDefault()
    })

}