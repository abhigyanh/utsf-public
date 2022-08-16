from manim import *

FRAME_WIDTH = config["frame_width"]
FRAME_HEIGHT = config["frame_height"]

#Text Size Variables
Huge = 72
Large = 42
Medium = 34
Small = 26
Tiny = 20

TikzScaleFactor = 0.75

def cart2pol(v):
    rho = np.linalg.norm(v)
    phi = np.arctan2(v[1], v[0])
    return(rho, phi)

def rHat(v):
    r = v[0]*RIGHT + v[1]*UP
    Hat = r/np.linalg.norm(r)
    return(Hat)
    
def thetaHat(v):
    theta = -v[1]*RIGHT + v[0]*UP
    Hat = theta/np.linalg.norm(theta)
    return(Hat)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)
    
def ColorTexColours(tex):                               #function to colour the r,g,b strings separately
            for i in range(len(tex)):
                if tex[i].get_tex_string() == 'r':
                    tex[i].set_color(RED)
                if tex[i].get_tex_string() == 'g':
                    tex[i].set_color(GREEN)  
                if tex[i].get_tex_string() == 'b':
                    tex[i].set_color(BLUE_D) 
                if tex[i].get_tex_string() == ' \\Bar{b} ':
                    tex[i].set_color(YELLOW)  
                if tex[i].get_tex_string() == ' \\Bar{g} ':
                    tex[i].set_color(LIGHT_PINK) 
                if tex[i].get_tex_string() == ' \\Bar{r} ':
                    tex[i].set_color(BLUE_B) 

def ColorMathTexColours(tex):                           #function to colour the r,g,b strings separately, supported for $$ environments
            for i in range(len(tex)):
                if tex[i].get_tex_string() == '$r$':
                    tex[i].set_color(RED)
                if tex[i].get_tex_string() == '$g$':
                    tex[i].set_color(GREEN)  
                if tex[i].get_tex_string() == '$b$':
                    tex[i].set_color(BLUE_D) 
                if tex[i].get_tex_string() == '$\Bar{b}$':
                    tex[i].set_color(YELLOW)  
                if tex[i].get_tex_string() == '$\Bar{g}$':
                    tex[i].set_color(LIGHT_PINK) 
                if tex[i].get_tex_string() == '$\Bar{r}$':
                    tex[i].set_color(BLUE_B) 