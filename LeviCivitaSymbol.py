from manim import *
config.max_files_cached = 1000
from utsf_common import *

class LeviCivitaSymbol(Scene):
    def construct(self):

        #opening text
        texVGrp = VGroup()
        texVGrp.add(
                    Tex(r"Mathematics: {{ $\epsilon_{ijk}$ }} ", font_size=Large)
                   )  
        texVGrp.add(
                    Brace(texVGrp[0][1],DOWN)                      
                    )
        texVGrp[0][1].set_color(YELLOW)                                     #make the EPSILON    yellow
        texVGrp[1].set_color(YELLOW)                                        #make the underbrace yellow
        texVGrp.add(
                    Tex(r""" ``Levi-Civita symbol'' \\ or ``antisymmetric symbol'' """, font_size=Medium, color=YELLOW)
                    )
        texVGrp.move_to(ORIGIN)                                             #center the thing
        texVGrp[2].next_to(texVGrp[1],DOWN)                                 #move the name below the underbrace
        
        #self.add(index_labels(texVGrp[0]))                                 #debug tool, string indices
        
        topMath = MathTex(r"""
                            \ket{p} &= \sum_{ \text{\footnotesize (all color combos) } } \epsilon_{q_1 q_2 q_3} C(q_1, q_2, q_3) \ket{q_1} \ket{q_2} \ket{q_3}
                            """
                            ).to_edge(UP)
        
        

        
        
        
        
        
        
        
        #color wheel cycle thing 
        threeColors = VGroup(
                                Tex(r"r"), 
                                Tex(r"g"), 
                                Tex(r"b"),
                            )
        threeColors[1].shift(RIGHT)
        threeColors[2].shift((threeColors[0].get_center() + threeColors[1].get_center())/2 + DOWN)
        
        for i in range(len(threeColors)):                   #loop that colours the color labels in the entire VGroup
            ColorTexColours(threeColors[i])
        
        cycleArrowsCW = VGroup(
                                CurvedArrow(start_point = threeColors[0].get_edge_center(UP),           #R TO G
                                            end_point = threeColors[1].get_edge_center(UP),
                                            radius = -1,
                                            angle = 2*PI/3,
                                            tip_length = 0.2
                                            ).shift(0.1*UP),
                                CurvedArrow(start_point = threeColors[1].get_edge_center(DOWN),         #G TO B
                                            end_point = threeColors[2].get_edge_center(RIGHT),
                                            radius = -1,
                                            angle = 2*PI/3,
                                            tip_length = 0.2
                                            ).shift(0.1*RIGHT+0.1*DOWN),
                                CurvedArrow(start_point = threeColors[2].get_edge_center(LEFT),         #B TO R
                                            end_point = threeColors[0].get_edge_center(DOWN),
                                            radius = -1,
                                            angle = 2*PI/3,
                                            tip_length = 0.2
                                            ).shift(0.1*LEFT+0.1*DOWN),            
                            )
        cycleArrowsCCW = VGroup(
                                CurvedArrow(start_point = threeColors[1].get_edge_center(UP),               #G TO R
                                            end_point = threeColors[0].get_edge_center(UP),
                                            radius = 1,
                                            angle = 2*PI/3,
                                            tip_length = 0.2
                                            ).shift(0.1*UP),  
                                CurvedArrow(start_point = threeColors[2].get_edge_center(RIGHT),            #B TO G
                                            end_point = threeColors[1].get_edge_center(DOWN),
                                            radius = 1,
                                            angle = 2*PI/3,
                                            tip_length = 0.2
                                            ).shift(0.1*RIGHT+0.1*DOWN),
                                CurvedArrow(start_point = threeColors[0].get_edge_center(DOWN),             #R TO B
                                            end_point = threeColors[2].get_edge_center(LEFT),
                                            radius = 1,
                                            angle = 2*PI/3,
                                            tip_length = 0.2
                                            ).shift(0.1*DOWN+0.1*LEFT),
                            )
        
        cycleCW = VGroup(threeColors, cycleArrowsCW)
        cycleCCW = VGroup(threeColors.copy(), cycleArrowsCCW)
        
        
        
        
        
        
        
        
        
        
        
        #big equation block
        bigMathTex = MathTex(r"""
                    \implies \ket{p} &=  (+1){{ \begin{pmatrix} & & \\ & & \end{pmatrix} }}
                            +  (-1) {{ \begin{pmatrix} & & \\ & & \end{pmatrix} }}
                            + 0 {{ \begin{pmatrix} \text{one color occurs} \\ \text{more than once} \end{pmatrix} }} \\
                      
                             """, font_size = Large)
        bigBracket1 = bigMathTex[1]
        bigBracket2 = bigMathTex[3]
        bigBracket3 = bigMathTex[5]

        cycleCW.set(width = 0.6*bigBracket1.width).move_to(bigBracket1)                             #move color cycles inside their resp. brackets
        cycleCCW.set(width = 0.6*bigBracket2.width).move_to(bigBracket2)
        
        bigBrace1 = Brace(bigBracket1, sharpness = 0.5, color=YELLOW)                               #braces under the brackets
        bigBrace2 = Brace(bigBracket2, sharpness = 0.5, color=YELLOW)
        bigBrace3 = Brace(bigBracket3, sharpness = 0.5, color=YELLOW)
        bigBraces = VGroup(bigBrace1, bigBrace2, bigBrace3)

        braceLabel1 = Tex(r"quark colors \\ in cyclic order", font_size=Small, color=YELLOW).next_to(bigBrace1,DOWN)
        braceLabel2 = Tex(r"quark colors \\ in anti-cyclic order", font_size=Small, color=YELLOW).next_to(bigBrace2,DOWN)
        braceLabel3 = Tex(r"repeated colors \\ (unphysical)", font_size=Small, color=YELLOW).next_to(bigBrace3,DOWN)
        braceLabels = VGroup(braceLabel1, braceLabel2, braceLabel3)                                 #brace text labels

        bigMathGroup = VGroup(bigMathTex, cycleCW, cycleCCW)
        
        
        
        

        
        
        
        
        
        
        #epsilon delta values in the middle
        middleMath = MathTex(r"""
                            \epsilon_{q_1 q_2 q_3} = \begin{dcases}
                                                        1, & \text{if $(q_1, q_2, q_3)$ is a cyclic permutation of (r,g,b)} \\
                                                        -1, & \text{if $(q_1, q_2, q_3)$ is an anti-cyclic permutation of (r,g,b)} \\
                                                        0, & \text{if any color occurs more than once}
                                                     \end{dcases} 
                             """, font_size=Small)
        middleMath.next_to(topMath,DOWN)
        
        
        
        
        
        
        
        
        
        
        
        
        #bottom detail math
        bottomMath = MathTex(r"""\therefore \ket{p} = 
                            &
                            C(
                            {{r}},{{g}},{{b}}) |{{r}}\rangle |{{g}}\rangle |{{b}}\rangle + C({{b}},{{r}},{{g}}) |{{b}}\rangle |{{r}}\rangle |{{g}}\rangle + C({{g}},{{b}},{{r}}) |{{g}}\rangle |{{b}}\rangle |{{r}}\rangle
                            \\
                            &
                            - C({{r}},{{b}},{{g}}) |{{r}}\rangle |{{b}}\rangle |{{g}}\rangle
                            - C({{b}},{{g}},{{r}}) |{{b}}\rangle |{{g}}\rangle |{{r}}\rangle
                            - C({{g}},{{r}},{{b}}) |{{g}}\rangle |{{r}}\rangle |{{b}}\rangle
                            
                             """, font_size = Medium).to_edge(DOWN)
        ColorTexColours(bottomMath)
        bottomText = Tex(r"6 non-zero contributing terms left:", font_size=Medium).next_to(bottomMath,UP)
        bottomRightFoot = Tex(r"Same 6 combinations \\ we previously found!", font_size=Tiny).to_corner(DOWN+RIGHT).shift(UP*bottomMath.height)
        
        
        bottomVGroup = VGroup(bottomText, bottomMath, bottomRightFoot)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #animation sequence
        for i in range(len(texVGrp[0])):                                    #first lines
            self.play(Write(texVGrp[0][i], run_time = 1))
        self.play(Write(texVGrp[1], run_time=1), Write(texVGrp[2], run_time=2))
        self.wait()
        
        self.play(FadeOut(texVGrp))
        
        self.play(Write(topMath), run_time = 3)                             #write Top math
        self.play(FadeIn(middleMath), run_time = 1)                          #write middle epsilon
        
        self.play(                                                          #write Big Math in the middle, and color cycles
                    Write(bigMathTex),
                    Create(cycleCW), 
                    Create(cycleCCW),
                    run_time = 3
                  )
        self.wait()
        
        self.play(Write(bigBraces), run_time=1)                             #write braces and labels
        for i in range(len(braceLabels)):
            self.play(Write(braceLabels[i]), run_time=2)
        self.wait()
        
        self.play(
                    FadeOut(bigBraces),                                     #disappear big braces and labels
                    FadeOut(braceLabels),
                 )
        
        self.play(Write(bottomText))
        self.wait()
        self.play(Write(bottomMath), run_time=4)
        self.wait()
        self.play(Write(bottomRightFoot, run_time=0.6)) 
        self.wait()