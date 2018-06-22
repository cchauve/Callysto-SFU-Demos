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

pal_a_s = ['#000000'] + ['#edf8fb','#b2e2e2','#66c2a4','#2ca25f','#006d2c','wheat'][::-1] + ['#d5a967']
pal_b_s =  ['#000000'] + ['#edf8fb','#b3cde3','#8c96c6','#8856a7','#810f7c','wheat'][::-1]+ ['#d5a967']
pal_c_s =  ['#000000'] + ['#f0f9e8','#bae4bc','#7bccc4','#43a2ca','#0868ac','wheat'][::-1]+ ['#d5a967']
pal_d_s =  ['#000000'] + ['#fef0d9','#fdcc8a','#fc8d59','#e34a33','#b30000','wheat'][::-1]+ ['#d5a967']
pal_e_s =  ['#000000'] + ['#f1eef6','#bdc9e1','#74a9cf','#2b8cbe','#045a8d','wheat'][::-1]+ ['#d5a967']
pal_f_s =  ['#000000'] + ['#f6eff7','#bdc9e1','#67a9cf','#1c9099','#016c59','wheat'][::-1]+ ['#d5a967']
pal_g_s =  ['#000000'] + ['#f1eef6','#d7b5d8','#df65b0','#dd1c77','#980043','wheat'][::-1]+ ['#d5a967']
pal_h_s =  ['#000000'] + ['#feebe2','#fbb4b9','#f768a1','#c51b8a','#7a0177','wheat'][::-1]+ ['#d5a967']
pal_i_s =  ['#000000'] + ['#ffffd4','#fed98e','#fe9929','#d95f0e','#993404','wheat'][::-1]+ ['#d5a967']
pal_j_s =  ['#000000'] + ['#ffffb2','#fecc5c','#fd8d3c','#f03b20','#bd0026','wheat'][::-1]+ ['#d5a967']
#single
pal_k_s =  ['#000000'] + ['#edf8e9','#bae4b3','#74c476','#31a354','#006d2c','wheat'][::-1]+ ['#d5a967']
pal_l_s =  ['#000000'] + ['#f2f0f7','#cbc9e2','#9e9ac8','#756bb1','#54278f','wheat'][::-1]+ ['#d5a967']
pal_m_s =  ['#000000'] + ['#fee5d9','#fcae91','#fb6a4a','#de2d26','#a50f15','wheat'][::-1]+ ['#d5a967']
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

    string_rows = pattern_string.split('\n')
    string_rows = string_rows[1:len(string_rows)]
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

def pattern_str_to_list( dashed_pattern_string ):

    str_rows = dashed_pattern_string.split("\n")
    str_rows = str_rows[::-1]
    str_rows = str_rows[1:len(str_rows)]
    output_list = []

    for cur_str_row in str_rows:
        char_split = list(cur_str_row)
        output_list.append(char_split)

    return output_list

def triangle_str(num_of_colors,height):
      
    return double_char(dash_add_pattern(pattern_string(num_of_colors,height)))

def get_color(ch):
    
    color_dict = { '-' : '#d5a967'     ,
                   'a' : 'black'    , 
                   'b' : 'wheat'   , 
                   'c' : 'maroon'     , 
                   'd' : 'gold'    , 
                   'e' : 'goldenrod'  , 
                   'f' : 'khaki'    , 
                   'g' : 'cyan'    , 
                   'h' : 'orange'    }
    
    return color_dict[ch]

color_list = list(string.ascii_lowercase)

def height_one(height,width_num,num_colors):

    row = ""
    st = ""
    
    for i in range(num_colors):
        
        row = row + 2*color_list[i]
    
    for i in range(height):
        
        st = st + width_num*"-" + row + "\n"
        
    return st

def height_two(height,width_num,num_colors):

    row = ""
    st = ""
    
    for i in range(num_colors):
        
        row = row + 2*color_list[i]
    
    for i in range(height):
        
        st = st + row  + width_num*"-" + "\n"
        
    return st

def width(height,num_colors):

    row = ""    
    st = ""
    
    for i in range(num_colors):
        
        row = row + 2*color_list[i]
        
    for i in range(height):
        
        if(i==0):
            left_st = ""
        else:
            left_st = row[0:(2*i)]
            
        right_st = row[2*i:((2*i)+2)*num_colors]
        
        st = st + left_st + 5*color_list[i] + right_st + "\n"
        
    return st

def draw_space(st,num_spaces):
    
    row_strings = st.split("\n")
    row_strings = row_strings[:len(row_strings)-1]
    st_out = ""
    
    for row in row_strings:
        
        row = row + num_spaces*"-"
        st_out = st_out + row + "\n"

    return st_out

def reflect(st):
    
    row_strings = st.split("\n")
    row_strings = row_strings[:len(row_strings)-1]
    st_out = ""
    
    for row in row_strings:
        
        row = row + row[::-1]
        st_out = st_out + row + "\n"
        
    return st_out

def draw_pattern(height1, height2, space_size):
    
    num_colors = 3 # change to allow user to parametrize
    w = 5 # change to allower user to parametrize
    
    h1 = height_one(height1,w,num_colors)
    h2 = height_two(height2,w,num_colors)
    w = width(num_colors,num_colors)
    
    splitted = w.split("\n")[::-1]
    chunk = ""
    for i in range(1,len(splitted)):
        chunk = chunk + splitted[i] + "\n"
    
    st = h1 + w + h2 + chunk + h1
    new_st = draw_space(st,space_size)
    
    return(reflect(new_st))

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

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim(0, basket_l)
    ax.set_ylim(0, basket_w)
    ax.set_zlim(0,basket_h)
    ax.axis('off')
    plt.show()

