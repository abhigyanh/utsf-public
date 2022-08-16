from manim import *
config.max_files_cached = 1000
from utsf_common import *

class MadeOfQuarks(Scene):
    def construct(self):
        headerFS = 42
        topText1 = Tex("It turns out,", font_size = headerFS).to_edge(UP)
        
        bottomText1 = Tex("q = 'quark'", font_size = headerFS).to_edge(DOWN)
        
        
        #Big nucleons with solid color 
        BigNucleonRadius = 2
        protonBig = Circle(color=RED, fill_opacity = 1, radius = BigNucleonRadius)
        neutronBig = Circle(color=WHITE, fill_opacity = 1, radius = BigNucleonRadius)
        
        nucleonsBig = VGroup(protonBig, neutronBig)
        nucleonsBig.arrange(RIGHT, buff = 1)
        
        nucleonLabelSize = Large
        nucleonLabels = VGroup(
                                Tex("Proton", font_size = nucleonLabelSize, color = BLACK),
                                Tex("Neutron", font_size = nucleonLabelSize, color = BLACK)
                               )
        for i in range(len(nucleonLabels)):
            nucleonLabels[i].move_to(nucleonsBig[i].get_center())
        
        
        
        
        #Not solid color anymore
        proton2 = Circle(color=RED, radius = BigNucleonRadius)
        neutron2 = Circle(color=WHITE, radius = BigNucleonRadius)
        
        nucleons2 = VGroup(proton2, neutron2)
        nucleons2.arrange(RIGHT, buff = 1)
        
        
        #quarks and quark labels
        quarks = VGroup()
        
        for i in range(len(nucleons2)):
            c = Circle(color=WHITE, radius=BigNucleonRadius/2).move_to(nucleons2[i].get_center())
            c1 = c.point_at_angle(PI/2)
            c2 = c.point_at_angle(PI/2 + 2*PI/3)
            c3 = c.point_at_angle(PI/2 + 4*PI/3)
            quarks.add(Circle(color=PURPLE, radius=BigNucleonRadius/3, fill_opacity=0).move_to(c1))
            quarks.add(Circle(color=PURPLE, radius=BigNucleonRadius/3, fill_opacity=0).move_to(c2))
            quarks.add(Circle(color=PURPLE, radius=BigNucleonRadius/3, fill_opacity=0).move_to(c3))
            
        
        quarkLabelSize = Medium 
        quarkLabels = VGroup()
        
        for i in range(len(quarks)):
            qLabel = Tex("q", font_size = quarkLabelSize, color=WHITE)
            qLabel.move_to(quarks[i].get_center())
            quarkLabels.add(qLabel)
            
            
            
        #new quark labels
        qL2Str = ["u", "u", "d", "u", "d", "d"]
        quarkLabels2 = VGroup()
        for i in range(len(quarks)):
            newLabel = Tex(qL2Str[i], font_size = quarkLabelSize, color=WHITE) 
            newLabel.move_to(quarks[i].get_center())
            quarkLabels2.add(newLabel)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Sequence of animations
        
        self.play(DrawBorderThenFill(nucleonsBig))
        self.play(Write(nucleonLabels))
        self.wait()
        
        
        self.play(Write(topText1))                                          #it turns out...
        self.play(ReplacementTransform(nucleonsBig, nucleons2), FadeOut(nucleonLabels))
        
        self.play(DrawBorderThenFill(quarks))                               #draw quarks
        self.play(Write(quarkLabels))
        self.play(Write(bottomText1))
        
        self.wait()
        self.play(ReplacementTransform(quarkLabels, quarkLabels2))          #replace old quark labels with new ones
        self.wait()
        self.play(Indicate(proton2, color=proton2.get_color()))
        self.wait()
        self.play(Indicate(neutron2, color=neutron2.get_color()))
        self.wait()