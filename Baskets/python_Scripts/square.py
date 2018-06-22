def rect_basket2D_rec(height1, height2, space_size):
    
    rect_param = draw_pattern(height1, height2, space_size)
    col_lst = pattern_str_to_list(rect_param)
    nonpattern_space = 10
    basket_h = len(col_lst)
    basket_w = len(col_lst[0]) + 2*nonpattern_space

    plt.figure( figsize = (6,6) )
    current_axis = plt.gca()
    weave_w = 0.5

    for i in range(0, basket_h):
        for j in range(0, basket_w ):
            bottom_left = (weave_w*j, i)
            
            if j >= nonpattern_space and j < basket_w - nonpattern_space:
                color = get_color(col_lst[i][j - nonpattern_space])
            
            else: 
                color = "#d5a967"
                
            rect = Rectangle( bottom_left, weave_w, 1, fill = True, facecolor = color, edgecolor = "white", linewidth = 1)
            current_axis.add_patch(rect)
    
    plt.xlim(-0.25 , basket_w*weave_w + 0.25)
    plt.ylim(-0.25 , basket_h)
    current_axis.axis('off')
    plt.show()