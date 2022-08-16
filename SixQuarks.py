from manim import *
config.max_files_cached = 1000
from utsf_common import *

class SixQuarks(Scene):
    def construct(self):
        headerFS = 42
        labelFS = 24
        topText1 = Tex("We know of 6 quarks:", font_size = headerFS).to_edge(UP)
    
        QuarkRadius = 0.5
        QuarkColor = PURPLE
        sixQuarks = VGroup()
        
        for i in range(6):
            quark = Circle(radius = QuarkRadius, color = QuarkColor)
            sixQuarks.add(quark)
        sixQuarks.arrange_in_grid(rows = 2, cols = 3, buff = 2.5, flow_order = 'dr')                        #arrange the six quarks in order
        
        labelStr = ["up", "down", "strange", "charm", "top", "bottom"]                                      #labels of the six 
        sixLabels = VGroup()
        for i in range(len(sixQuarks)):
            L = Tex(labelStr[i], color=WHITE, font_size=labelFS).move_to(sixQuarks[i].get_center())
            sixLabels.add(L)
        
        images = Group(
            ImageMobject(r"images/SixQuarks/up.png").set(height = 1),
            ImageMobject(r"images/SixQuarks/down.png").set(height = 1.5),
            ImageMobject(r"images/SixQuarks/strange.png").set(height = 2),
            ImageMobject(r"images/SixQuarks/charm.png").set(height = 2),
            ImageMobject(r"images/SixQuarks/top.png").set(height = 2),
            ImageMobject(r"images/SixQuarks/bottom.png").set(height = 2),
        )
        for i in range(6):
            images[i].next_to(sixQuarks[i], RIGHT)

        
        
        
        #animation sequence
        self.play(Write(topText1))
        self.wait()
        
        for i in range(len(sixQuarks)):
            self.play(Create(sixQuarks[i]), Write(sixLabels[i]), run_time = 0.6)
            self.play(FadeIn(images[i]))
        self.wait()