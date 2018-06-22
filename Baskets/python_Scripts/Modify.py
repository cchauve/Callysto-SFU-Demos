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



from ipywidgets import interact, interact_manual

        
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


def get_inverse_pattern_dictionary(dictionary):
    
    col_char_dictionary =  {val:key for key,val in dictionary.items()}
    
    return col_char_dictionary

def circular_2D_dictionary(tri_height, num_color,num_tri,palette):
    col_dic = get_color_test(palette)
    
    tri_param = triangle_str(num_color, tri_height) 
    color_list = pattern_str_to_list(tri_param)
    
    largest_row = len(color_list[0])
    
    basket_h = tri_height;
    basket_w = largest_row*num_tri
    
    circular_dictionary = {}
    for n in range(0, num_tri):
        for i in range(0, len(color_list)):
            for j in range(0, len(color_list[i]) ):
                bottom_left = (len(color_list[0])*n + j, i)
        
                color = col_dic[color_list[i][j]]
                rect = Rectangle( bottom_left, 1, 1, fill = True, facecolor = color, edgecolor = "white", linewidth = 1)
                circular_dictionary[rect] = [i,color_list[i][j]]
    return [circular_dictionary, largest_row]

def update_dictionary(dictionary,selected_key,new_value):
    
    dictionary[selected_key] = new_value
    
    return dictionary

def circ_basket2D_tri(tri_height, num_color,num_tri,palette):
    
    def plot_palette(palette):
        fig = plt.figure(figsize=(6, 1), frameon=False)
        ax = fig.add_subplot(111)
        col_pos_dictionary = {}
        for x, color in enumerate(palette):
    #print(x)
            col_pos_dictionary[(Rectangle((x, 0), 1, 1, facecolor=color))] = (x,color)
            ax.add_patch(Rectangle((x, 0), 1, 1, facecolor=color))
            ax.add_patch(Rectangle((x, 0), 1, 1, facecolor=color))
        
        ax.set_xlim((0, len(pal_a)))
        ax.set_ylim((0, 1))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect("equal")
        global text_pal
        text_pal =fig.text(0,0, "", va="bottom", ha="left")
    
        def color_picker(event):

            tx = 'x=%f, y=%f' % (event.xdata, event.ydata)  ######################## THIS TOO
        #text.set_text(tx) ######################## AND THIS
            for key in col_pos_dictionary:
                w,h = key.get_width(),key.get_height()
                x0,y0 = key.xy
                if x0 <= event.xdata <= x0 + w and y0 <= event.ydata <= y0 + h:
                    value = col_pos_dictionary[key]
                    position = value[0]
                    global new_color
                    new_color = value[1]
                    text_pal.set_text(new_color)
                
        cid = fig.canvas.mpl_connect('button_press_event', color_picker)
        ax.set_xlim((0, len(pal_a)))
        ax.set_ylim((0, 1))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect("equal")
        plt.show()
    
    plot_palette(palette)
    fig =plt.figure(figsize = (8,5))
    global text
    text =fig.text(0,0, "", va="bottom", ha="left")

    def onclick(event):

        tx = 'x=%f, y=%f' % (event.xdata, event.ydata)  ######################## THIS TOO
        #global text
        #text.set_text(tx) ######################## AND THIS
        for key in circular_patches[0]:
            w,h = key.get_width(),key.get_height()
            x0,y0 = key.xy
            if x0 <= event.xdata <= x0 + w and y0 <= event.ydata <= y0 + h:
                #text.set_text(key)
                rect = Rectangle( (x0,y0), w,h, fill = True, facecolor = new_color, edgecolor = "white", linewidth = 1)
                current_axis.add_patch(rect)
                new_char = col_char_dic[new_color]
                #text.set_text(new_char)
                update_dictionary(circular_patches[0],rect,new_char)
                text.set_text(circular_patches[0][rect])
    
    
    
    #plt.figure( figsize = (tri_height*num_tri, tri_height*1.5))
    
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    current_axis = plt.gca()
    
    char_col_dic = get_color_test(palette)
    col_char_dic = get_inverse_pattern_dictionary(char_col_dic)
    
    global circular_patches
    circular_patches = circular_2D_dictionary(tri_height, num_color,num_tri,palette)
    
    for key in circular_patches[0]:
        current_axis.add_patch(key)
    
    
    basket_h = tri_height;
    basket_w = circular_patches[1]*num_tri
    plt.xlim(-0.25 , basket_w + 0.25)
    plt.ylim(-0.25 , basket_h + 0.25)
    current_axis.axis('off')
    plt.show()
    
    