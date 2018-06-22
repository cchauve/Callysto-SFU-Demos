
#Libraries and palettes
import string
import seaborn as sns
from ipywidgets import interact, interact_manual
import string
import math
import numpy as np
from ipywidgets import widgets
from ipywidgets import interact
from ipywidgets import fixed
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
import pylab as pl
import scipy as sp

pal_a = ['#000000'] + ['#edf8fb','#b2e2e2','#66c2a4','#2ca25f','#006d2c'][::-1] + ['#d5a967']
pal_b =  ['#000000'] + ['#edf8fb','#b3cde3','#8c96c6','#8856a7','#810f7c'][::-1]+ ['#d5a967']
pal_c =  ['#000000'] + ['#f0f9e8','#bae4bc','#7bccc4','#43a2ca','#0868ac'][::-1]+ ['#d5a967']
pal_d =  ['#000000'] + ['#fef0d9','#fdcc8a','#fc8d59','#e34a33','#b30000'][::-1]+ ['#d5a967']
pal_e =  ['#000000'] + ['#f1eef6','#bdc9e1','#74a9cf','#2b8cbe','#045a8d'][::-1]+ ['#d5a967']
pal_f =  ['#000000'] + ['#f6eff7','#bdc9e1','#67a9cf','#1c9099','#016c59'][::-1]+ ['#d5a967']
pal_g =  ['#000000'] + ['#f1eef6','#d7b5d8','#df65b0','#dd1c77','#980043'][::-1]+ ['#d5a967']
pal_h =  ['#000000'] + ['#feebe2','#fbb4b9','#f768a1','#c51b8a','#7a0177'][::-1]+ ['#d5a967']
pal_i =  ['#000000'] + ['#ffffd4','#fed98e','#fe9929','#d95f0e','#993404'][::-1]+ ['#d5a967']
pal_j =  ['#000000'] + ['#ffffb2','#fecc5c','#fd8d3c','#f03b20','#bd0026'][::-1]+ ['#d5a967']
#single
pal_k =  ['#000000'] + ['#edf8e9','#bae4b3','#74c476','#31a354','#006d2c'][::-1]+ ['#d5a967']
pal_l =  ['#000000'] + ['#f2f0f7','#cbc9e2','#9e9ac8','#756bb1','#54278f'][::-1]+ ['#d5a967']
pal_m =  ['#000000'] + ['#fee5d9','#fcae91','#fb6a4a','#de2d26','#a50f15'][::-1]+ ['#d5a967']
ori_p =  ['#000000'] + ['wheat','maroon','gold','goldenrod','khaki']+ ['#d5a967']

def pattern_str_to_list( dashed_pattern_string ):

    str_rows = dashed_pattern_string.split("\n")
    str_rows = str_rows[::-1]
    str_rows = str_rows[1:len(str_rows)]
    output_list = []

    for cur_str_row in str_rows:
        char_split = list(cur_str_row)
        output_list.append(char_split)

    return output_list

def pattern_string(num_colors,triangle_height):

    alphabet_list = list(string.ascii_lowercase)
    colors = alphabet_list[:num_colors]

    num_colors = len(colors)
    default = '-'
    output_string = ''

    for i in range( 0 , triangle_height ):
        if ( i < num_colors):
            left_string = ''  
            right_string = ''

            for j in range(0,i):
                left_string = left_string + current_string[j]

            right_string = left_string[::-1]
            current_string = left_string + colors[i] + right_string
            output_string = output_string + current_string + "\n"

        else:
            left_string = ''

            for j in range(0,i):
                left_string = left_string + current_string[j]

            right_string = left_string[::-1]
            current_string = left_string + default + right_string
            output_string = output_string + current_string + "\n"

    output_string = output_string[::-1]
    return output_string

def dash_add_pattern(pattern_string):

    string_rows_0 = pattern_string.split('\n')
    string_rows = string_rows_0[1:len(string_rows_0)]
    max_string_width = len(string_rows[0])
    output_string = ''

    for cur_string in string_rows:

        if(len(cur_string) <= max_string_width):

            cur_string_width = len(cur_string)
            dashes_to_add = int((max_string_width - cur_string_width)/2)*"-"
            cur_string = dashes_to_add + cur_string + dashes_to_add 
            output_string = output_string + cur_string + "\n"
        
    return output_string

def double_char(dp_str):
    
    row_string = ''
    output_string = ''
    
    for ch in dp_str:

        if(ch == '\n'):
            output_string = output_string + row_string + "\n"
            row_string = ''
            
        else:
            row_string = row_string + 2*ch
            
    return(output_string)

def triangle_str(num_of_colors,height):
      
    return double_char(dash_add_pattern(pattern_string(num_of_colors,height)))



def get_color_test(palette):
    alphabet =  string.ascii_lowercase + '-'
    alphabet_arr = list(alphabet)
    
    char_col_dictionary = {}
    size = len(palette)

    char_col_dictionary[alphabet_arr[1]] = palette[-1]
    for i in range(size-1):
        char_col_dictionary[alphabet_arr[i]] = palette[i]
    char_col_dictionary[alphabet_arr[-1]] = palette[-1]
    return char_col_dictionary

def remove_repetitions(array):
    uniq_array = []
    for x in array:
        if x not in uniq_array:
            uniq_array.append(x)
    return uniq_array
        
def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

def shape_dictionary(num_c,theight,bwidth,num_t,palette):
    
    col_dic = get_color_test(palette)
    
    k = 8
    weave_w = bwidth/(2+4*k) 
    
    tri_param = triangle_str(num_c, theight) 
    color_list = pattern_str_to_list(tri_param)
    
    len_first_color = len(color_list[0])
    basket_mid = bwidth/2
    triangle_mid = len_first_color*weave_w/2

    triangle_start = basket_mid - triangle_mid
    
    coordinate_dictionary  = {}
    
    size_color_list = len(color_list)
    
    for n in range(0, num_t):
        for i in range(0, size_color_list):
            size_ith_color = len(color_list[i])
            for j in range(0, size_ith_color ):

                bottom_left = (triangle_start + weave_w*j, n*size_color_list + i)
                if (triangle_start + weave_w*j >=0 and triangle_start + weave_w*j < bwidth):
                    color = col_dic[color_list[i][j]]
                    rect = Rectangle( bottom_left, weave_w, 1, fill = True, facecolor = color, edgecolor = "white", linewidth = 1)
                    coordinate_dictionary[rect] = color_list[i][j]  
    
    
    return coordinate_dictionary

def outline_dictionary(bwidth,bheight,palette):
    col_dic = get_color_test(palette)
    k = 8
    weave_w = bwidth/(2+4*k) 
    outline_dictionary = {}
    # Produce outline
    
    basket_dic = {}
    color =col_dic['-']
    for i in range(0, bheight):
        for j in range(0, 2+4*k):
            bottom_left = (weave_w*j, i)
            # Displays rectangles row by row starting from the first column
            rect = Rectangle( bottom_left, weave_w, 1, fill = True, facecolor = color, edgecolor = "white", linewidth = 1)
            basket_dic[rect] = "-"
    return basket_dic



def shape_dictionary(num_c,theight,bwidth,num_t,palette):
    """This function creates a dictionary with rectangles as keys and characters in data structure as values"""
    
    # Get colour dictionary
    col_dic = get_color_test(palette)
    
    # Define weave width 
    k = 8
    weave_w = bwidth/(2+4*k) 
    
    # Get triangle data structure from triangle_str() function
    tri_param = triangle_str(num_c, theight) 
    
    # Turn string into list for plotting
    color_list = pattern_str_to_list(tri_param)
    
    # Get length of first row within data structure
    len_first_color = len(color_list[0])
    #get middle point in basket and middle point in triangle
    basket_mid = bwidth/2
    triangle_mid = len_first_color*weave_w/2

    # Position triangle so that it is centered
    triangle_start = basket_mid - triangle_mid
    
    # Define dictionary
    coordinate_dictionary  = {}
    
    size_color_list = len(color_list)
    
    # For n in range number of triangles, for i in range number of rows and for j in range length of jth row,
    # fill dictionary with rectangles, their appropriate character and corresponding colour
    for n in range(0, num_t):
        for i in range(0, size_color_list):
            size_ith_color = len(color_list[i])
            for j in range(0, size_ith_color ):

                bottom_left = (triangle_start + weave_w*j, n*size_color_list + i)
                if (triangle_start + weave_w*j >=0 and triangle_start + weave_w*j < bwidth):
                    color = col_dic[color_list[i][j]]
                    rect = Rectangle( bottom_left, weave_w, 1, fill = True, facecolor = color, edgecolor = "white", linewidth = 1)
                    coordinate_dictionary[rect] = color_list[i][j]  
    
    # Return dictionary
    return coordinate_dictionary

def vert_tri(basket_h, basket_w, tri_h, num_tri, num_color,palette,option):
    plt.figure( figsize = (5,5) )
    current_axis = plt.gca()
    col_dic = get_color_test(palette)
    k = 8
    weave_w = basket_w/(2+4*k) 
    
    tri_param = triangle_str(num_color, tri_h) 
    color_list = pattern_str_to_list(tri_param)
    
    # Produce outline
   
    for i in range(0, basket_h):
        for j in range(0, 2+4*k):
            bottom_left = (weave_w*j, i)
            # Displays rectangles row by row starting from the first column
            rect = Rectangle( bottom_left, weave_w, 1, fill = True, facecolor = '#d5a967', edgecolor = "white", linewidth = 1)
            current_axis.add_patch( rect )

    basket_mid = basket_w/2
    triangle_mid = len(color_list[0])*weave_w/2

    triangle_start = basket_mid - triangle_mid


    # Produce color fill

    for n in range(0, num_tri):
        for i in range(0, len(color_list)):
            for j in range(0, len(color_list[i]) ):

                bottom_left = (triangle_start + weave_w*j, n*len(color_list) + i)
                
                if (triangle_start + weave_w*j >=0 and triangle_start + weave_w*j < basket_w):
                    if(color_list[i][j] == '-'):
                        rect = Rectangle( bottom_left, weave_w, 1, fill = True, facecolor = '#d5a967', edgecolor = "white", linewidth = 1)
                        current_axis.add_patch(rect)
                    else:
                        color = col_dic[color_list[i][j]]
                        rect = Rectangle( bottom_left, weave_w, 1, fill = True, facecolor = color, edgecolor = "white", linewidth = 1)
                        current_axis.add_patch(rect)
    
    plt.xlim(-0.25 , basket_w + 0.25)
    plt.ylim(-0.25 , basket_h)
    current_axis.axis('off')
    plt.show()
    
    if option==True:
        rect_basket3d_rec(1,4,3,4,palette)
        
def circ_basket2D_tri_hor(num_c,theight,bwidth,bheight,num_t,palette,option):
    
    #plt.figure( figsize = (tri_height*num_tri, tri_height*1.5))
    col_dic = get_color_test(palette)
    
    plt.figure( figsize = (5,5) )
    current_axis = plt.gca()
    
    outline = outline_dictionary(bwidth,bheight,palette)
    
    for item in outline:
        current_axis.add_patch(item)
        
    shape = shape_dictionary(num_c,theight,bwidth,num_t,palette)
    
    for item in shape:
        current_axis.add_patch(item)
    plt.xlim(-0.25 , bwidth + 0.25)
    plt.ylim(-0.25 , bheight + 0.25)
    current_axis.axis('off')
    plt.show()
    
    if option==True:
        rect_basket3d_rec(1,4,3,4,palette)
    
def rect_basket3d_rec(height1, height2, space_size,tri_height,palette):
    #fig = plt.figure(figsize = (6,6))

    col_dic = get_color_test(palette)
    
    
    ax = a3.Axes3D(plt.figure(figsize = (6,6)))

    rect_param = draw_pattern(height1, height2, space_size)
    rect_col_lst = pattern_str_to_list(rect_param)
    
    tri_param = triangle_str(3, tri_height)
    tri_col_lst = pattern_str_to_list(tri_param)

    nonpattern_space_fb = 20
    nonpattern_space_lr = 5
    rows = len(rect_col_lst)+1
    cols_fb = len(rect_col_lst[0]) + 2*nonpattern_space_fb + 1
    cols_lr = len(tri_col_lst[0]) + 2*nonpattern_space_lr + 1
    
    num_tri = math.floor(rows/tri_height)

    basket_h = 10
    basket_w = 1
    basket_l = 1
    indent = max(basket_w, basket_l)/5
    weave_w = indent/(rows-1)
    z = np.linspace(0,basket_h, rows)
    basket_rim = (z[1]-z[0])/2
    
    n = 1

    x = []
    for i in range(0, rows):
        x.append(np.linspace(indent - i*weave_w, basket_l - indent + i*weave_w, cols_fb))
        
    y = []
    for i in range(0, rows):
        y.append(np.linspace(indent - i*weave_w, basket_w - indent + i*weave_w, cols_lr))

    # FRONT
    for i in range(0, rows-1):
        for j in range(0, cols_fb-1):

            bottom_left = [x[i][j], indent-i*weave_w, z[i]]
            top_left = [x[i+1][j], indent-(i+1)*weave_w, z[i+1]]
            top_right = [x[i+1][j+1], indent-(i+1)*weave_w, z[i+1]]
            bottom_right = [x[i][j+1], indent-i*weave_w, z[i]]
            rect_coords = [bottom_left, top_left, top_right, bottom_right]
            rect = a3.art3d.Poly3DCollection([rect_coords]) 

            if j >= nonpattern_space_fb and j < cols_fb - nonpattern_space_fb - 1:            
                color = get_color(rect_col_lst[i][j-nonpattern_space_fb])
                rect.set_color(color)
            else:
                rect.set_color('#d5a967')

            rect.set_edgecolor('#ad8a54')
            ax.add_collection3d(rect)
            
            if i == rows - 2:
                bottom_left = top_left
                bottom_right = top_right
                top_left = [x[i+1][j], indent-(i+1)*weave_w, z[i+1] + basket_rim]
                top_right = [x[i+1][j+1], indent-(i+1)*weave_w, z[i+1]+ basket_rim]

                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords]) 
                rect.set_color('#af8a52')
                rect.set_edgecolor('#87693c')
                ax.add_collection3d(rect)
                

    # BACK            
    for i in range(0, rows-1):
        for j in range(0, cols_fb-1):

            bottom_left = [x[i][j], basket_w - indent + i*weave_w, z[i]]
            top_left = [x[i+1][j], basket_w - indent + (i+1)*weave_w, z[i+1]]
            top_right = [x[i+1][j+1], basket_w - indent + (i+1)*weave_w, z[i+1]]
            bottom_right = [x[i][j+1], basket_w - indent + i*weave_w, z[i]]

            rect_coords = [bottom_left, top_left, top_right, bottom_right]
            rect = a3.art3d.Poly3DCollection([rect_coords]) 
            
            if j >= nonpattern_space_fb and j < cols_fb - nonpattern_space_fb - 1:            
                color = get_color(rect_col_lst[i][j-nonpattern_space_fb])
                rect.set_color(color)
            else:
                rect.set_color('#d5a967')

            rect.set_edgecolor('#ad8a54')
            ax.add_collection3d(rect)
            
            if i == rows - 2:
                bottom_left = top_left
                bottom_right = top_right
                top_left = [x[i+1][j], basket_w - indent + (i+1)*weave_w, z[i+1] + basket_rim]
                top_right = [x[i+1][j+1], basket_w - indent + (i+1)*weave_w, z[i+1]+ basket_rim]

                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords]) 
                rect.set_color('#af8a52')
                rect.set_edgecolor('#87693c')
                ax.add_collection3d(rect)

    # RIGHT
    for i in range(0,rows-1):
        
        if i > 0 and i % tri_height == 0:
            n += 1
            
        for j in range(0, cols_lr-1):
            bottom_left = [basket_l - indent + i*weave_w, y[i][j], z[i]]
            top_left = [basket_l - indent + (i+1)*weave_w, y[i+1][j], z[i+1]]
            top_right = [basket_l - indent + (i+1)*weave_w, y[i+1][j+1], z[i+1]]
            bottom_right = [basket_l - indent + i*weave_w, y[i][j+1], z[i]]

            rect_coords = [bottom_left, top_left, top_right, bottom_right]
            rect = a3.art3d.Poly3DCollection([rect_coords])  
            
            if j >= nonpattern_space_lr and j < cols_lr - nonpattern_space_lr - 1 and n <= num_tri: 
                color = get_color(tri_col_lst[i % tri_height][j-nonpattern_space_lr])
                rect.set_color(color)
            else:
                rect.set_color('#d5a967')

            rect.set_edgecolor('#ad8a54')
            ax.add_collection3d(rect)
            
            if i == rows - 2:
                bottom_left = top_left
                bottom_right = top_right
                top_left = [basket_l - indent + (i+1)*weave_w, y[i+1][j], z[i+1] + basket_rim]
                top_right = [basket_l - indent + (i+1)*weave_w, y[i+1][j+1], z[i+1] + basket_rim]

                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords]) 
                rect.set_color('#af8a52')
                rect.set_edgecolor('#87693c')
                ax.add_collection3d(rect)
            
        
        

    # LEFT  
    n = 1
    for i in range(0,rows-1):
        if i > 0 and i % tri_height == 0:
            n += 1
            
        for j in range(0, cols_lr-1):
            bottom_left = [indent - i*weave_w, y[i][j], z[i]]
            top_left = [indent - (i+1)*weave_w, y[i+1][j], z[i+1]]
            top_right = [indent - (i+1)*weave_w, y[i+1][j+1], z[i+1]]
            bottom_right = [indent - i*weave_w, y[i][j+1], z[i]]

            rect_coords = [bottom_left, top_left, top_right, bottom_right]
            rect = a3.art3d.Poly3DCollection([rect_coords])  

            if j >= nonpattern_space_lr and j < cols_lr - nonpattern_space_lr - 1 and n <= num_tri:            
                color = get_color(tri_col_lst[i % tri_height][j-nonpattern_space_lr])
                rect.set_color(color)
            else:
                rect.set_color('#d5a967')
            rect.set_edgecolor('#ad8a54')
            ax.add_collection3d(rect)
            
            if i == rows - 2:
                bottom_left = top_left
                bottom_right = top_right
                top_left = [indent - (i+1)*weave_w, y[i+1][j], z[i+1] + basket_rim]
                top_right = [indent - (i+1)*weave_w, y[i+1][j+1], z[i+1] + basket_rim]

                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords]) 
                rect.set_color('#af8a52')
                rect.set_edgecolor('#87693c')
                ax.add_collection3d(rect)
    plt.title("Square Basket: Final Version")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim(0, basket_l)
    ax.set_ylim(0, basket_w)
    ax.set_zlim(0,basket_h)
    ax.axis('off')
    plt.show()

