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

from ipywidgets import interact, interact_manual

def circ_basket3D_tri(num_tri, tri_height, num_color,palette):
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(111, projection='3d')
    
    col_dic = get_color_test(palette)

    tri_param = triangle_str(num_color, tri_height)
    color_list = pattern_str_to_list(tri_param)
    min_radius = 2
    max_radius = 5

    theta = np.linspace(0, 2 * np.pi, num_tri*len(color_list[0])+1)
    z = np.linspace(min_radius, max_radius, len(color_list)+1)
    theta, R = np.meshgrid(theta, z)    

    X = R * np.cos(theta)
    Y = R * np.sin(theta)
    Z = np.sqrt(X**2 + Y**2) - 1
    
    basket_rim = (z[1] - z[0])/2

    for i in range(0,len(color_list)+1):
        for j in range(0,num_tri*len(color_list[0])):
            if i == len(color_list):
                bottom_left = [X[i][j], Y[i][j], Z[i][j]]
                bottom_right = [X[i][j+1], Y[i][j+1], Z[i][j+1]]
                top_left = [X[i][j], Y[i][j], Z[i][j] + basket_rim]
                top_right = [X[i][j+1], Y[i][j+1], Z[i][j+1]+ basket_rim]
                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords])  

                rect.set_color('#6d5a3d')
                rect.set_edgecolor('#493a23')
                ax.add_collection3d(rect)
                
            else:
                bottom_left = [X[i][j], Y[i][j], Z[i][j]] 
                top_left = [X[i+1][j], Y[i+1][j], Z[i+1][j]]
                top_right = [X[i+1][j+1], Y[i+1][j+1], Z[i+1][j+1]]
                bottom_right = [X[i][j+1], Y[i][j+1], Z[i][j+1]]

                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords])
                
                color = col_dic[color_list[i][j % len(color_list[0])]]
                rect.set_color(color)
                rect.set_edgecolor('#6d5634')
                ax.add_collection3d(rect)



    ax.set_xlim(-max_radius, max_radius)
    ax.set_ylim(-max_radius, max_radius)
    ax.set_zlim(0, max_radius-1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.axis('off')
    
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

# Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('white')
    ax.yaxis.pane.set_edgecolor('white')
    ax.zaxis.pane.set_edgecolor('white')

# Bonus: To get rid of the grid as well:
    ax.grid(False)
    plt.title("Circular Basket: Final Version")
    plt.show()
    
from IPython.display import Javascript

from ipywidgets import Button
