<!DOCTYPE html>
<html lang="en">
{% include 'headercss.html' %}
<body>
{% include 'navbar.html' %}
<div class="container">       
    <form>  
            <div class="row">
                <div class="col-md-2"></div>
                <div class="col-md-8">
                    <div class="form-group row">
                    <label for="first_name" class="col-sm-3 col-form-label">First Name <span style="color:red;">*</span></label>
                        <div class="col-sm-9">
                            <input type="text" class="form-control" id="add_first_name" name="add_first_name" placeholder="First Name">
                        </div>
                    </div>

                    <div class="form-group row">
                        <label for="last_name" class="col-sm-3 col-form-label">Last Name <span style="color:red;">*</span></label>
                        <div class="col-sm-9">
                            <input type="text" class="form-control" id="add_last_name" name="add_last_name" placeholder="Last Name">
                        </div>
                    </div>

                    <div class="form-group row">
                        <label for="email" class="col-sm-3 col-form-label">Email <span style="color:red;">*</span></label>
                        <div class="col-sm-9">
                            <input type="text" class="form-control" id="add_email" name="add_email" placeholder="Email">
                        </div>
                    </div>

                    <div class="form-group row">
                        <label for="phone" class="col-sm-3 col-form-label">Phone <span style="color:red;">*</span></label>
                        <div class="col-sm-9">
                            <input type="number" class="form-control" id="add_phone" name="add_phone" placeholder="Phone">
                        </div>
                    </div>

                    <div class="form-group row">
                        <label for="phone" class="col-sm-3 col-form-label">Address <span style="color:red;">*</span></label>
                        <div class="col-sm-9">
                            <textarea class="form-control" id="add_address" name="add_address" placeholder="Address"></textarea>
                        </div>
                    </div>

                    <div class="pull-right">
                        <!-- <button type="button" class="btn btn-danger">Close</button> -->
                        <a href = "/" class="btn btn-danger">Close</a>
                        <button type="button" class="btn btn-primary" id="btn_add">Add</button>
                    </div>
                </div>
                <div class="col-md-2"></div>
            </div>
    </form>

</div>
</body>
{% include 'footer.html' %}
{% include 'scriptjs.html' %}

<script>
            //add student
            $('#btn_add').click(function(){

var first_name = $('#add_first_name').val();
var last_name = $('#add_last_name').val();
var email = $('#add_email').val();
var phone = $('#add_phone').val();
var address = $('#add_address').val();
var password = $('#add_password').val();
if(first_name != ''){
  if(last_name != ''){
    if(email != ''){
      if(phone != ''){
        if(address != ''){
          if(password != ''){
            $.ajax({
              type: 'post',
              url: "/insert_student",
              data: {'first_name': first_name, 'last_name': last_name, 'email': email,
              'phone': phone, 'address': address, 'password': password},
              dataType: "text",
              success: function(data){
                data = JSON.parse(data);
                if(data.value==1){
                  $.notify("Record created successfully", { position: 'top right', className: 'success' });
                  $('#AddModal').modal('hide');
                        setTimeout(function() {
                        window.location.href = "/"
                        }, 3000);
                }
                if(data.value==2){
                  $.notify("Email already exist", { position: 'top right', className: 'error' });
                }
              }
            });
          }else{
            $.notify("Please enter the password", { position: 'top right', className: 'error' });
            return false;
          }
        }else{
          $.notify("Please enter the address", { position: 'top right', className: 'error' });
          return false;
        }
      }else{
        $.notify("Please enter the phone number", { position: 'top right', className: 'error' });
        return false;
      }
    }else{
      $.notify("Please enter email address", { position: 'top right', className: 'error' });
      return false;
    }
  }else{
    $.notify("Please enter last name", { position: 'top right', className: 'error' });
    return false;
  }
}else{
  $.notify("Please enter first name", { position: 'top right', className: 'error' });
  return false;
}
});

</script>
</html>