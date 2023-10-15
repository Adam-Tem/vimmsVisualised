

def checkInput(user_input, has_to_be_int = False, range_check = False, overlap=False):

    error = False
    error_msg = ""
    for val in user_input:    
        if len(user_input) == 0:
            error = True
            error_msg = "Please enter a value."

        if has_to_be_int and "." in val:
            error = True
            error_msg = "Please enter a whole number."

        val = float(val)
        if val < 0:
            error = True
            error_msg = "Please enter a value > 0."
        
    if overlap:
        if float(user_input[0]) >= float(user_input[1]) or float(user_input[1]) <= float(user_input[0]):
            error = True
            error_msg = "Please enter valid range values."
    
    if range_check:    
        if float(user_input[0]) < float(range_check[0]) or float(user_input[1]) > float(range_check[1]):
            error = True
            error_msg = f"Values exceed range limits of {range_check[0]} - {range_check[1]}."

    
    return error, error_msg
                  
