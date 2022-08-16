from manim import *
config.max_files_cached = 1000
from utsf_common import *




class ColorCycle0(Scene):
    def construct(self):
        ColCha = Tex(r"Color charge", font_size = Huge, color = YELLOW)
        self.play(Write(ColCha))
        self.wait()
        self.remove(ColCha)
        
        #We know nothing...
        WeKnowNaff = Tex(r"We know \textit{nothing} about this new quantum number, \\ but we \textit{can} deduce how it should work.", font_size = Medium).to_edge(UP)
        
        #...has three values...
        colHats = MathTex(r"= \left\{ \begin{pmatrix}1\\0\\0\end{pmatrix}, \begin{pmatrix}0\\1\\0\end{pmatrix}, \begin{pmatrix}0\\0\\1\end{pmatrix} \right\}", font_size = Medium)
        QNumThreeVals = VGroup(
            Tex(r"new quantum number = {{3}} values", font_size = Medium).set_color_by_tex("3", YELLOW),
            Brace(Rectangle(height = 2, width = 1), LEFT),
            VGroup(
                colHats,
                Tex(r"= \{ {{red}}, {{green}}, {{blue}} \} }", font_size = Medium),
            ).arrange(DOWN, buff = 0.2, aligned_edge = LEFT)
        ).arrange(RIGHT, buff = 0.2)
        QNumThreeVals[2][1][1].set_color(RED)
        QNumThreeVals[2][1][3].set_color(GREEN)
        QNumThreeVals[2][1][5].set_color(BLUE_D)
        
        #odd choices for name
        OddNames = Tex(r"Choice of names may seem random, \\ but it'll make sense later!", font_size = Tiny).next_to(QNumThreeVals[2], DOWN)
        
        
        
        #Animation Sequence
        self.play(Write(WeKnowNaff), run_time = 3)
        self.wait()
        
        self.play(Write(QNumThreeVals[0]))
        self.wait()
        
        self.play(Write(QNumThreeVals[2][0]))
        self.wait(0.5)
        
        self.play(Write(QNumThreeVals[2][1]), Write(QNumThreeVals[1]))
        self.wait()
        
        self.play(Write(OddNames))
        self.wait()
        self.play(FadeOut(*self.mobjects))
        










class ColorCycle1(Scene):
    def construct(self):

        #texts
        fontsizeM = 28
        topText1 = Tex(r"Proton: 3 quarks").to_edge(UP)

        rightTexGroup = VGroup()
        rightTexGroup.add(Tex(
                                r"Cyclic pattern!"
                             ))
        rightTexGroup.add(Tex(
                                r"(+) sign", color=YELLOW
                             ))
        rightTexGroup.add(Tex(
                                r"(-) sign", color=YELLOW
                             ))
        rightTexGroup.add(Tex(
                                r""" "Color cycle" """
                             ))
        rightTexGroup.arrange(ZERO, aligned_edge=UP, center=True).to_edge(RIGHT)
        
        



        #proton wave functions
        protonWFGeneric = MathTex(                                  #q1 q2 q3
                                  r"\ket{p} {{=}} C({{q_1}},{{q_2}},{{q_3}}) |{{q_1}}\rangle |{{q_2}}\rangle |{{q_3}}\rangle",
                                 )
        protonWaveFunctions = VGroup()
        protonWaveFunctions.add(MathTex(                           #order: r, g, b
                                    r"\ket{p} {{=}} C({{r}},{{g}},{{b}}) |{{r}}\rangle |{{g}}\rangle |{{b}}\rangle",
                                    )
                                )
        protonWaveFunctions.add(MathTex(                           #order: r, b, g
                                    r"- \ket{p} {{=}} C({{r}},{{b}},{{g}}) |{{r}}\rangle |{{b}}\rangle |{{g}}\rangle",
                                    )
                                )
        protonWaveFunctions.add(MathTex(                           #order: b, r, g
                                    r"\ket{p} {{=}} C({{b}},{{r}},{{g}}) |{{b}}\rangle |{{r}}\rangle |{{g}}\rangle",
                                    )
                                )
        protonWaveFunctions.add(MathTex(                           #order: b, g, r
                                    r"- \ket{p} {{=}} C({{b}},{{g}},{{r}}) |{{b}}\rangle |{{g}}\rangle |{{r}}\rangle",
                                    )
                                )
        protonWaveFunctions.add(MathTex(                           #order: g, b, r
                                    r"\ket{p} {{=}} C({{g}},{{b}},{{r}}) |{{g}}\rangle |{{b}}\rangle |{{r}}\rangle",
                                    )
                                )
        protonWaveFunctions.add(MathTex(                           #order: g, r, b
                                    r"- \ket{p} {{=}} C({{g}},{{r}},{{b}}) |{{g}}\rangle |{{r}}\rangle |{{b}}\rangle",
                                    )
                                )
        protonWaveFunctions.arrange(direction=ZERO, aligned_edge=RIGHT, center=False)
        for i in range(len(protonWaveFunctions)):                   #loop that colours the color labels in the entire VGroup
            ColorTexColours(protonWaveFunctions[i])                     




        #collated proton WFs on the left and arranged downwards
        protonWFsLeft = protonWaveFunctions.copy()
        protonWFsLeft.arrange(direction=ZERO, aligned_edge=RIGHT, center=False).to_corner(UP+LEFT).shift(DOWN)

        protonWFsPos = VGroup(
                                    protonWFsLeft[0], protonWFsLeft[2], protonWFsLeft[4]
                             )
        protonWFsNeg = VGroup(
                                    protonWFsLeft[1], protonWFsLeft[3], protonWFsLeft[5]
                             )                         


                     
        #p.e.p arrow and label
        pepTex = Tex(r"Pauli's exclusion principle", font_size = fontsizeM, color = YELLOW).to_edge(LEFT).shift(UP)
        pepArrow = Arrow(start = protonWaveFunctions[1].get_left(), 
                         end = pepTex.get_edge_center(DOWN), 
                         color = YELLOW, 
                         max_stroke_width_to_length_ratio = 2,
                         max_tip_length_to_length_ratio = 0.1,
                         )
        
        
        
        
        
        
        #color tracker
        quarkColorTracker = VGroup()
        quarkColorTracker.add(MathTex(                           #order: r, g, b
                                    r"(q_1, q_2, q_3) = ({{r}},{{g}},{{b}})", font_size = fontsizeM
                                    )
                                )
        quarkColorTracker.add(MathTex(                           #order: r, b, g
                                    r"(q_1, q_2, q_3) = ({{r}},{{b}},{{g}})", font_size = fontsizeM
                                    )
                                )
        quarkColorTracker.add(MathTex(                           #order: b, r, g
                                    r"(q_1, q_2, q_3) = ({{b}},{{r}},{{g}})", font_size = fontsizeM
                                    )
                                )
        quarkColorTracker.add(MathTex(                           #order: b, g, r
                                    r"(q_1, q_2, q_3) = ({{b}},{{g}},{{r}})", font_size = fontsizeM
                                    )
                                )
        quarkColorTracker.add(MathTex(                           #order: g, b, r
                                    r"(q_1, q_2, q_3) = ({{g}},{{b}},{{r}})", font_size = fontsizeM
                                    )
                                )
        quarkColorTracker.add(MathTex(                           #order: g, r, b
                                    r"(q_1, q_2, q_3) = ({{g}},{{r}},{{b}})", font_size = fontsizeM
                                    )
                                )
        quarkColorTracker.arrange(direction=ZERO, aligned_edge=RIGHT, center=False)
        quarkColorTracker.to_corner(RIGHT+DOWN)
        
        ColorTrackerLabel = Tex(r"Color tracker:", font_size = fontsizeM).next_to(quarkColorTracker,UP)
        
        for i in range(len(quarkColorTracker)):                   #loop that colours the color labels in the entire VGroup
            ColorTexColours(quarkColorTracker[i]) 
            




        #color wheel cycle thing wtf
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
                                CurvedArrow(start_point = threeColors[1].get_edge_center(DOWN),        #G TO B
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

        colorWheelGroup = VGroup(threeColors, cycleArrowsCW, cycleArrowsCCW).shift(2*UP + (SCREEN_WIDTH/4)*RIGHT)
        rightTexGroup.next_to(colorWheelGroup,DOWN)                                                         #move right text group here for better positioning
        
        




        #animation sequence
        self.play(Write(topText1))
        self.wait()
        
        self.play(Write(protonWFGeneric))                                           #write generic wave function
        self.wait()
        
        self.play(                                                                  #first color combo and quark tracker
                    ReplacementTransform(protonWFGeneric,protonWaveFunctions[0]), 
                    FadeIn(quarkColorTracker[0], run_time=0.6), 
                    FadeIn(ColorTrackerLabel, run_time=0.6)
                 )
        self.wait()
        
        for i in range(len(protonWaveFunctions) - 1):                               #cycle between all color combos
            self.play(
                      ReplacementTransform(protonWaveFunctions[i], protonWaveFunctions[i+1]), 
                      ReplacementTransform(quarkColorTracker[i], quarkColorTracker[i+1])
                     )
            if i == 0:
                self.play(GrowArrow(pepArrow), Write(pepTex))
                self.play(FadeOut(pepArrow), FadeOut(pepTex))
            self.wait(0.5)
        self.wait()
        
        self.play(FadeOut(quarkColorTracker[5]), FadeOut(ColorTrackerLabel))
        self.play(FadeOut(protonWaveFunctions[5]))                                  #clear out color tracker and center wave func
        
        
        
        FadeInAndSlideDownLeftWF = AnimationGroup(                                  #show all combs on the left and slide down
                                                  FadeIn(protonWFsLeft),
                                                  protonWFsLeft.animate.arrange(direction=DOWN, aligned_edge=RIGHT, center=False),
                                                  )
        self.play(FadeInAndSlideDownLeftWF)
        self.wait()
        
        
        self.play(Write(threeColors), Write(rightTexGroup[0]))                       #color cycle creation, write "Cyclic pattern!"
        cycleArrowsDraw = AnimationGroup(
                                            DrawBorderThenFill(cycleArrowsCW[0]),
                                            DrawBorderThenFill(cycleArrowsCW[1]),
                                            DrawBorderThenFill(cycleArrowsCW[2])
                                        )
        self.play(cycleArrowsDraw, run_time = 0.6)
        self.play(FadeOut(rightTexGroup[0]))                                         #fade out cyclic pattern!
        self.play(                                                                   #indicate CW arrows
                    Write(rightTexGroup[1], run_time=1),
                    Indicate(cycleArrowsCW, run_time=3, rate_func=there_and_back_with_pause),
                    Indicate(protonWFsPos, run_time=3, rate_func=there_and_back_with_pause),
                 )
        self.wait()
        
        
        self.remove(cycleArrowsCW)                                                  #remove CW arrows
        self.play(                                                                  #swap CW arrows with CCW arrows
                    ReplacementTransform(cycleArrowsCW.copy(), cycleArrowsCCW),
                    ReplacementTransform(rightTexGroup[1], rightTexGroup[2], run_time=1),
                 )
        self.play(                                                                  #indicate CW arrows
                    
                    Indicate(cycleArrowsCCW, run_time=3, rate_func=there_and_back_with_pause),
                    Indicate(protonWFsNeg, run_time=3, rate_func=there_and_back_with_pause),
                 )

        self.play(FadeOut(rightTexGroup[2]))
        self.play(FadeOut(cycleArrowsCCW), FadeIn(cycleArrowsCW))                   #reverse arrows back to correct oder
        self.play(Write(rightTexGroup[3]))                                          #The Color Cycle
        self.wait()