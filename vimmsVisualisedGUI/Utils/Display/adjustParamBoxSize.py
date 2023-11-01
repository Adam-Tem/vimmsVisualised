def adjust_param_box_size(param_box, new_widget_count, current_widget_count):
    grid = param_box.parent()
    box = grid.parent()
    new_height = ((new_widget_count-1)//3) + 1
    current_height = ((current_widget_count-1)//3) + 1
    change_in_height = new_height - current_height

    grid.setFixedHeight(grid.height() + (change_in_height*20))
    box.setFixedHeight(box.height() +  (change_in_height*20))