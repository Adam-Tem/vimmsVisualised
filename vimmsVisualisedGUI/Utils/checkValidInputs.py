from Utils.Parameters.CustomWidgets import QXMLUpload

def check_valid_inputs(button_to_set, line_edits = [], combo_boxes = [], stored_required_lists = [], stored_named_vals=[], peak_picking_params=None):

    valid_inputs = True
    for combo_box in combo_boxes:
            if combo_box.currentText() == "---":
                valid_inputs = False
        
    for text_val in line_edits:
        if len(text_val.strip()) == 0:
            valid_inputs = False
        for stored_list in stored_named_vals:
            if text_val in stored_list:
                valid_inputs = False

    for stored_list in stored_required_lists:
         if len(stored_list) == 0:
              valid_inputs = False

    if peak_picking_params:
         if peak_picking_params[0] == "MZMine":
              if len(peak_picking_params[1].findChildren(QXMLUpload)) == 0:
                  valid_inputs = False
              else:
                mzmine_template = peak_picking_params[1].findChildren(QXMLUpload)[0].file_location
                if mzmine_template == "":
                    valid_inputs = False
    
    if valid_inputs:
        button_to_set.setEnabled(True)
    else:
        button_to_set.setEnabled(False)
