
# IMPORTING LIBRARIES
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

"""Function Definition Area"""
### PATTERN STRINGS
### TRIANGULAR PATTERN
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

### SQUARE/RECTANGLE PATTERN

def height_1(height,width_num,num_colors):
    
    color_list = ['a','b','c']
    row = ""
    st = ""
    
    for i in range(num_colors):
        
        row = row + 2*color_list[i]
    
    for i in range(height):
        
        st = st + width_num*"-" + row + "\n"
        
    return st

def height_2(height,width_num,num_colors):
    
    color_list = ['a','b','c']
    row = ""
    st = ""
    
    for i in range(num_colors):
        
        row = row + 2*color_list[i]
    
    for i in range(height):
        
        st = st + row  + width_num*"-" + "\n"
        
    return st

def width(height,num_colors):

    color_list = ['a','b','c']
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

def space(st,num_spaces,option):
    
    row_strings = st.split("\n")
    row_strings = row_strings[:len(row_strings)-1]
    st_out = ""
    
    if option=="right":
        for row in row_strings:
        
            row = row + num_spaces*"-"
            st_out = st_out + row + "\n"
    elif option=="left":
        for row in row_strings:
        
            row = num_spaces*"-" + row 
            st_out = st_out + row + "\n"
    elif option=="both":
        for row in row_strings:
        
            row = num_spaces*"-" + row +num_spaces*"-"
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

def square_rectangle(height_one,height_two,wi,height_three,num_colors,num_space):
    h1 = height_1(height_one,wi,num_colors)
    h2 = height_2(height_two,wi,num_colors)
    w = width(height_three,num_colors)
    splitted = w.split("\n")[::-1]
    chunk = ""
    for i in range(1,len(splitted)):
        chunk = chunk + splitted[i] + "\n"
    
    st = h1 + w + h2 + chunk + h1
    new_st = space(st,num_space,"right")
    
    reflected = reflect(new_st)
    
    return reflected

## FROM PATTERN STRING TO LIST

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

### 2D DEMO

def vert_tri(basket_h, basket_w, tri_h, num_tri, num_color):
    plt.figure( figsize = (5,5) )
    current_axis = plt.gca()
    
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
                        color = get_color(color_list[i][j])
                        rect = Rectangle( bottom_left, weave_w, 1, fill = True, facecolor = color, edgecolor = "white", linewidth = 1)
                        current_axis.add_patch(rect)
    
    plt.xlim(-0.25 , basket_w + 0.25)
    plt.ylim(-0.25 , basket_h)
    current_axis.axis('off')
    plt.show()
    
def plot_2D_face(shape):

    plt.figure( figsize = (5,5) )
    current_axis = plt.gca()
   
    basket_h = 2*2 + 6 + 2*2 + 2
    basket_w = 2^3 + 5*2 + 4*2 
    k = 8
    weave_w = basket_w/(2+4*k) 

    trim_param = shape
    color_list = pattern_str_to_list(shape)

    for i in range(0, basket_h):
        for j in range(0, 2+4*k):
            bottom_left = (weave_w*j, i)
            # Displays rectangles row by row starting from the first column
            rect = Rectangle( bottom_left, weave_w, 1, fill = True, facecolor = '#d5a967', edgecolor = "white", linewidth = 1)
            current_axis.add_patch( rect )
    
    basket_mid = basket_w/2
    triangle_mid = len(color_list[0])*weave_w/2

    triangle_start = basket_mid - triangle_mid

    for n in range(0, 1):
        for i in range(0, len(color_list)):
            for j in range(0, len(color_list[i]) ):

                bottom_left = (triangle_start + weave_w*j, n*len(color_list) + i)
                
                if (triangle_start + weave_w*j >=0 and triangle_start + weave_w*j < basket_w):
                    if(color_list[i][j] == '-'):
                        rect = Rectangle( bottom_left, weave_w, 1, fill = True, facecolor = '#d5a967', edgecolor = "white", linewidth = 1)
                        current_axis.add_patch(rect)
                    else:
                        color = get_color(color_list[i][j])
                        rect = Rectangle( bottom_left, weave_w, 1, fill = True, facecolor = color, edgecolor = "white", linewidth = 1)
                        current_axis.add_patch(rect)
    
    plt.xlim(-0.25 , basket_w + 0.25)
    plt.ylim(-1.25 , basket_h)
    current_axis.axis('off')
    plt.show()
    
    
def extended_basket_four_faces(shape):
    
    plt.figure( figsize = (80,20))
    current_axis = plt.gca()

    
    tri_param = shape
    color_list = pattern_str_to_list(tri_param)

    basket_h = 2*2 + 6 + 2*2 + 2
    basket_w = (2^3 + 5*2 + 4*2 )*8

    
    for n in range(0, 1):
        for i in range(0, len(color_list)):
            for j in range(0, len(color_list[i]) ):
                
                if n == 0:
                    
                    bottom_left = (len(color_list[0])*n + j, i)
                
                else:
                    bottom_left = (len(color_list[0])*n + j - 2*n, i)
                    
                if(color_list[i][j] == '-'):
                    rect = Rectangle( bottom_left, 1, 1, fill = True, facecolor = '#d5a967', edgecolor = "white", linewidth = 1)
                    current_axis.add_patch(rect)
                else:
                    color = get_color(color_list[i][j])
                    rect = Rectangle( bottom_left, 1, 1, fill = True, facecolor = color, edgecolor = "white", linewidth = 1)
                    current_axis.add_patch(rect)

    
    plt.xlim(-0.25 , basket_w + 0.25)
    plt.ylim(-0.25 , basket_h + 0.25)
    current_axis.axis('off')
    plt.show()
def hor_tri(tri_height, num_tri, num_color):
    
    plt.figure( figsize = (4*num_tri,4))
    current_axis = plt.gca()

    
    tri_param = triangle_str(num_color, tri_height) 
    color_list = pattern_str_to_list(tri_param)

    basket_h = tri_height;
    basket_w = len(color_list[0])*num_tri
    
    for n in range(0, num_tri):
        for i in range(0, len(color_list)):
            for j in range(0, len(color_list[i]) ):
                
                if n == 0:
                    
                    bottom_left = (len(color_list[0])*n + j, i)
                
                else:
                    bottom_left = (len(color_list[0])*n + j - 2*n, i)
                    
                if(color_list[i][j] == '-'):
                    rect = Rectangle( bottom_left, 1, 1, fill = True, facecolor = '#d5a967', edgecolor = "white", linewidth = 1)
                    current_axis.add_patch(rect)
                else:
                    color = get_color(color_list[i][j])
                    rect = Rectangle( bottom_left, 1, 1, fill = True, facecolor = color, edgecolor = "white", linewidth = 1)
                    current_axis.add_patch(rect)

    
    plt.xlim(-0.25 , basket_w + 0.25)
    plt.ylim(-0.25 , basket_h + 0.25)
    current_axis.axis('off')
    plt.show()

### 3D MODELS

def rect_tri(basket_h, basket_l, basket_w, tri_h, num_tri, num_color):

    current_axis = a3.Axes3D(plt.figure())
    
    thinness = 8
    weave_front_w = basket_l/(2+4*thinness) 
    
    tri_param = triangle_str(num_color, tri_h) 
    color_list = pattern_str_to_list(tri_param)
    
    # Produces empty front face of basket
   
    for z in range(0, basket_h):
        for x in range(0, 2+4*thinness):
            bottom_left = [weave_front_w*x,0,z]
            top_left = [weave_front_w*x,0, z+1]
            top_right = [weave_front_w*(x+1), 0, z+1]
            bottom_right = [weave_front_w*(x+1), 0, z]

            rect_coords = [bottom_left, top_left, top_right, bottom_right]
            rect = a3.art3d.Poly3DCollection([rect_coords])
            rect.set_color('#d5a967')
            rect.set_edgecolor('white')
            current_axis.add_collection3d(rect)

    # Produces triangle pattern in the centre of basket front
    
    basket_mid = basket_l/2
    triangle_mid = len(color_list[0])*weave_front_w/2

    triangle_start = basket_mid - triangle_mid

    
    for n in range(0, num_tri):
        for i in range(0, len(color_list)):
            for j in range(0, len(color_list[i]) ):

                bottom_left = [triangle_start + weave_front_w*j, 0, n*tri_h+i]
                top_left = [triangle_start + weave_front_w*j,0, n*tri_h+i+1]
                top_right = [triangle_start + weave_front_w*(j+1), 0, n*tri_h+i+1]
                bottom_right = [triangle_start + weave_front_w*(j+1), 0, n*tri_h+i]
                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords])
                
                if (math.ceil(triangle_start + weave_front_w*j) >=0 and triangle_start + weave_front_w*j < basket_l and n*tri_h+i < basket_h):
                    color = get_color(color_list[i][j])
                    rect.set_color(color)
                    rect.set_edgecolor('white')
                    current_axis.add_collection3d(rect)

    # Sides of box
    
    weave_side_w = basket_w/(2+4*thinness) 
    
    for z in range(0, basket_h):
        for y in range(0, basket_w):
            bottom_left = [0,weave_side_w*y,z]
            top_left = [0,weave_side_w*y, z+1]
            top_right = [0, weave_side_w*(y+1), z+1]
            bottom_right = [0, weave_side_w*(y+1), z]
            
            rect_coords = [bottom_left, top_left, top_right, bottom_right]
            rect = a3.art3d.Poly3DCollection([rect_coords])
            rect.set_color('#d5a967')
            rect.set_edgecolor('white')
            current_axis.add_collection3d(rect)
            
    for z in range(0, basket_h):
        for y in range(0, basket_w):
            bottom_left = [basket_l,weave_side_w*y,z]
            top_left = [basket_l,weave_side_w*y, z+1]
            top_right = [basket_l, weave_side_w*(y+1), z+1]
            bottom_right = [basket_l, weave_side_w*(y+1), z]
            
            rect_coords = [bottom_left, top_left, top_right, bottom_right]
            rect = a3.art3d.Poly3DCollection([rect_coords])
            rect.set_color('#d5a967')
            rect.set_edgecolor('white')
            current_axis.add_collection3d(rect)

    # Back of box (With Triangle)
    
    for z in range(0, basket_h):
        for x in range(0, 2+4*thinness):
            bottom_left = [weave_front_w*x, weave_side_w*basket_w,z]
            top_left = [weave_front_w*x, weave_side_w*basket_w, z+1]
            top_right = [weave_front_w*(x+1), weave_side_w*basket_w, z+1]
            bottom_right = [weave_front_w*(x+1), weave_side_w*basket_w, z]
            
            rect_coords = [bottom_left, top_left, top_right, bottom_right]
            rect = a3.art3d.Poly3DCollection([rect_coords])
            rect.set_color('#d5a967')
            rect.set_edgecolor('white')
            current_axis.add_collection3d(rect)
    
    for n in range(0, num_tri):
        for i in range(0, len(color_list)):
            for j in range(0, len(color_list[i]) ):

                bottom_left = [triangle_start + weave_front_w*j, weave_side_w*basket_w, n*tri_h+i]
                top_left = [triangle_start + weave_front_w*j, weave_side_w*basket_w, n*tri_h+i+1]
                top_right = [triangle_start + weave_front_w*(j+1), weave_side_w*basket_w, n*tri_h+i+1]
                bottom_right = [triangle_start + weave_front_w*(j+1), weave_side_w*basket_w, n*tri_h+i]
                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords])            
                if (math.ceil(triangle_start + weave_front_w*j) >=0 and triangle_start + weave_front_w*j < basket_l and n*tri_h+i < basket_h):
                    color = get_color(color_list[i][j])
                    rect.set_color(color)
                    rect.set_edgecolor('white')
                    current_axis.add_collection3d(rect)
                    
                  
    current_axis.set_xlim(0, basket_l)
    current_axis.set_ylim(0, basket_w)
    current_axis.set_zlim(0, basket_h)
    
    current_axis.set_xlabel('x')
    current_axis.set_ylabel('y')
    current_axis.set_zlabel('z')
    current_axis.axis('off')
    plt.show()

def circ_tri(tri_height, num_tri, num_color):
    
    current_axis = a3.Axes3D(plt.figure(figsize=(5,5)))

    tri_param = triangle_str(num_color, tri_height) #color, height
    color_list = pattern_str_to_list(tri_param)
    nphi,nz=20*tri_height, tri_height# Number of columns # Number of rows


    r=1 # radius of cylinder
    phi = np.linspace(0,360, nphi)/180.0*np.pi
    z= np.linspace(0,1*tri_height,nz+1)

    for i in range(len(phi)-1): #columns
        cp0= r*np.cos(phi[i])
        cp1= r*np.cos(phi[i+1])
        sp0= r*np.sin(phi[i])
        sp1= r*np.sin(phi[i+1])

        for j in range(0, len(color_list)): # number of rows, gives height
            z0=z[j]
            z1=z[j+1]

            bottom_left = [cp0, sp0, z0]
            top_left = [cp1, sp1, z0]
            top_right = [cp1, sp1, z1]
            bottom_right = [cp0, sp0, z1]
            rect_coords = [bottom_left, top_left, top_right, bottom_right]
            rect = a3.art3d.Poly3DCollection([rect_coords])  

            color = get_color(color_list[j % len(color_list)][i % len(color_list[0])])
            rect.set_color(color)
            rect.set_edgecolor('white')

            current_axis.add_collection3d(rect)
    current_axis.set_xlim(-1,1)
    current_axis.set_ylim(-1,1)
    current_axis.set_zlim(0,tri_height)
    
    current_axis.set_xlabel('x')
    current_axis.set_ylabel('y')
    current_axis.set_zlabel('z')
    current_axis.axis('off')
    plt.show()
    


