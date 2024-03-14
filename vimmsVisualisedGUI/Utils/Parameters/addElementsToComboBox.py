def add_elements_to_combo_box(combo_box, element_dict):
    
    for option in element_dict.keys():
        combo_box.addItem(option)