const form = $('.form');

function showAlerts (event) {
  var form = $(event.currentTarget);
  var alerts = form.find('.alert')
  var inputs = form.find('textarea, input')
  var emptyInputs = inputs.filter(function() {
    return $(this).val() == "";
  });
  if (alerts.length === 1 && inputs.length != alerts.length && emptyInputs.length > 0) {
    event.preventDefault();
    alerts.show();
  }
  else {
    inputs.each(function(index) {
      if ($(this).val() === "") {
        event.preventDefault();
        if (alerts.length == 1) {
          alerts.show();
        }
        else {
          console.log(index, inputs.eq(index), alerts.eq(index))
          alerts.eq(index-1).show();
        }
      }
      else {
        alerts.eq(index).hide()
      }
    });
  }
}

form.on('submit', showAlerts);