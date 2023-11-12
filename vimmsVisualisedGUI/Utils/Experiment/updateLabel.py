def update_label(scroll_area_contents, text_label, text_to_add, label_type, count= None):

    current_text = text_label.text()
    if len(current_text) > 0:
        current_text = current_text + ", "
    if label_type == "fullscan":
        text_label.setText(current_text + text_to_add.split(".")[0] + " x" + str(count) )
    elif label_type == "experiment_case":
        text_label.setText(current_text + text_to_add)
    text_label.adjustSize()
    scroll_area_contents.setFixedWidth(text_label.width())