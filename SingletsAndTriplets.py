from manim import *
config.max_files_cached = 1000

from utsf_common import *

def Radians(deg):
    return(deg*PI/180)



class SingsTrips_0(Scene):
    def construct(self):
        Banner = Tex(r"Triplets and Singlets", color = YELLOW, font_size = Huge)
        self.play(Write(Banner))
        self.wait()
        self.remove(Banner)




class SingsTrips_1(Scene):
    def construct(self):
        Dew = Tex(r"We can get the answer{{, by talking about spin}}{{, some more.}}", font_size = Large)
        for subtex in Dew:
            self.play(
                Write(subtex)
            )
            self.wait()
            
            


class SingsTrips_2(Scene):
    def construct(self):
    
        #Hydrogen Atom
        nucleonSize = 0.2
        a_orbit = 10*nucleonSize
        
        
        proton = Dot(radius=nucleonSize).set_color(RED)    
        orbit = Circle(color=WHITE, radius = a_orbit)   
        electron = Dot(color=BLUE).move_to(orbit.point_at_angle(PI/3))
        
        plus = MathTex(r"+", font_size = 24, stroke_width = 2).move_to(proton)
        minus = MathTex(r"-", font_size = 12, stroke_width = 2).move_to(electron)
        
        atom = VGroup(proton, orbit, electron, plus, minus).move_to(3*LEFT)
        
        
        #Slightly Bigger Hydrogen Atom    
        orbit2 = Circle(color=WHITE, radius = 1.2*a_orbit) 
        electron2 = Dot(color=BLUE).move_to(orbit2.point_at_angle(PI/3))
        minus2 = MathTex(r"-", font_size = 12, stroke_width = 2).move_to(electron2)
        atom2 = VGroup(orbit2, electron2, minus2).move_to(atom.get_center())
        
        
        
        
        #Incoming photon arrow
        def PhotonArrow(mobj, object_side):
            squiggle = MathTex(r"""
            \begin{tikzpicture} 
                \begin{feynhand} 
                    \vertex (a) at (-1, 0); \vertex (b) at (1, 0); 
                    \propag [photon, mom = {$\gamma$ \text{(spin 1)} }] (a) to (b); 
                \end{feynhand} 
            \end{tikzpicture}""", color = YELLOW, fill_opacity=0, stroke_width=1.2, font_size = Small).next_to(mobj,object_side)
            return(squiggle)
        def IncomingPhotonAnim(arr, approach_vec):
            arr.shift(-approach_vec)

            self.play(
                FadeIn(arr, run_time=0.2), arr.animate.shift(approach_vec)
            )
            self.play(
                FadeOut(arr, run_time=1)
            )
        
        
        
        
        #Spin state tally table on the right
        nameRow = VGroup(
            Tex(r"$e^-$"), Tex(r"$p^+$"), Tex(r"atom")
        ).set(color = YELLOW)
        State1 = VGroup(
            MathTex(r"- \frac{1}{2}"), MathTex(r"- \frac{1}{2}"), MathTex(r"- 1"), 
        )
        State2 = VGroup(
            MathTex(r"- \frac{1}{2}"), MathTex(r"+ \frac{1}{2}"), MathTex(r"0"), 
        )
        State3 = VGroup(
            MathTex(r"+ \frac{1}{2}"), MathTex(r"- \frac{1}{2}"), MathTex(r"0"), 
        )
        State4 = VGroup(
            MathTex(r"+ \frac{1}{2}"), MathTex(r"+ \frac{1}{2}"), MathTex(r"+ 1"), 
        )
        spinTable = VGroup(*nameRow, *State1, *State2, *State3, *State4).arrange_in_grid(cols = 3, buff = .75).set(height = FRAME_HEIGHT/2).shift(FRAME_WIDTH/4*RIGHT)
        
        rect1 = SurroundingRectangle(State1, buff = 0.2)
        rect2 = SurroundingRectangle(VGroup(State2, State3), buff = 0.2)
        rect3 = SurroundingRectangle(State4, buff = 0.2)
        
        
        #Spin labels on the particles
        electronSpinLabels = VGroup(
            MathTex(r"-\frac{1}{2}"), MathTex(r"\mp\frac{1}{2}"), MathTex(r"+\frac{1}{2}")
        )
        protonSpinLabels = VGroup(
            MathTex(r"-\frac{1}{2}"), MathTex(r"\pm\frac{1}{2}"), MathTex(r"+\frac{1}{2}")
        )
        
        for lbl in [*electronSpinLabels, *protonSpinLabels]:                #make labels smol
            lbl.set(font_size = Tiny)
            
        electronSpinLabels.next_to(electron, UR/6)                          #move them to the resp. particles
        protonSpinLabels.next_to(proton,UR/6)
        
        
        #Ket states below the atom
        States = VGroup(
            MathTex(r"\ket{-\frac{1}{2}}_e \ket{-\frac{1}{2}}_p}"), 
            MathTex(r"\frac{1}{\sqrt{2}} \biggl( \ket{+\frac{1}{2} }_e \ket{-\frac{1}{2} }_p}  {{+ }}  \ket{-\frac{1}{2} }_e \ket{+\frac{1}{2} }_p} \biggr)"), 
            MathTex(r"\ket{+\frac{1}{2}}_e \ket{+\frac{1}{2}}_p}"), 
            MathTex(r"\frac{1}{\sqrt{2}} \biggl( \ket{+\frac{1}{2} }_e \ket{-\frac{1}{2} }_p}  {{- }}  \ket{-\frac{1}{2} }_e \ket{+\frac{1}{2} }_p} \biggr)"), 
        ).next_to(atom, DOWN)
        
        Triplet = VGroup(
            States[0], States[1], States[2]
        )
        Singlet = States[3]
        
        for stt in [*States]:
            stt.set(font_size = Small)
        
        TripletText = Tex(r"\textit{Triplet} states!", color = YELLOW).to_edge(DOWN)
        
        
        
        
        
        
        #Singlet States 
        SingletCanc = MathTex(r"""
        &\approx \ket{+\frac{1}{2} }_e \ket{+\frac{1}{2} }_p - \ket{+\frac{1}{2} }_e \ket{+\frac{1}{2} }_p \\
        &= 0 \quad \text{(this isn't right...)}
        """, font_size = Small)
        
        AtomGrows = Tex(r"($e^-$ and $p^+$ don't change their spin states)", font_size = Tiny).next_to(atom, 2*DOWN)
        SingletStateText = Tex(r"A \textit{singlet} state!", color = YELLOW).to_edge(DOWN)
        footnote = Tex(r"""Deliberate digression: 
            The spins add as follows: $\frac{1}{2} \otimes \frac{1}{2} = 1 \oplus 0$. In other words, the 'simplest' description of the composite atom system is a combination of the three states of a spin-1 system (hence, triplet) and one state of a spin-0 system (hence, singlet).
        """, font_size = 14, tex_environment='flushright').to_corner(UR)
        
        
        
        
        
        
        
        
        
        #Animation Sequence 
        self.play(GrowFromCenter(atom))                                     #introduce atom, electron, proton                            
        self.play(Flash(proton, flash_radius = nucleonSize, color = RED), run_time = 0.5)
        self.play(Flash(electron, flash_radius = 0.08, color = BLUE), run_time = 0.5)
        self.wait()
        
        
        self.play(GrowFromEdge(spinTable, UP))                              #spin table
        self.wait()
        
        self.play(Create(rect1))                                            #highlight the DD state
        self.play(
            FadeIn(electronSpinLabels[0]), FadeIn(protonSpinLabels[0])
        )
        self.play(Write(States[0]))
        self.wait()
        
        IncomingPhotonAnim(PhotonArrow(atom, LEFT), RIGHT)                  #send in a photon
        self.play(                                                          #change the highlight rectangle and spin labels
            ReplacementTransform(rect1, rect2),                             
            ReplacementTransform(electronSpinLabels[0], electronSpinLabels[1]),
            ReplacementTransform(protonSpinLabels[0], protonSpinLabels[1])
        )
        self.wait()
        
        self.remove(States[0])
        self.play(                                                          #transition to the spin 0 state
            ReplacementTransform(States[0].copy(), States[1])
        )
        
        self.wait()
        
        IncomingPhotonAnim(PhotonArrow(atom, LEFT), RIGHT)                  #send in a photon 
        self.play(                                                          #change the highlight rectangle and spin labels
            ReplacementTransform(rect2, rect3),                             
            ReplacementTransform(electronSpinLabels[1], electronSpinLabels[2]),
            ReplacementTransform(protonSpinLabels[1], protonSpinLabels[2])
        )
        self.wait()
        
        self.remove(States[1])
        self.play(                                                          #transition to the spin 1 state
            ReplacementTransform(States[1].copy(), States[2])
        )
        self.wait()
        
        self.play(                                                          #FadeOut the table and move the three states there
            FadeOut(spinTable), FadeOut(rect3), FadeOut(States[2]), FadeOut(electronSpinLabels[2]), FadeOut(protonSpinLabels[2])
        )
        
        States.move_to([2, 1, 0])                                           #move States to the right and cascade down
        self.play(
            FadeIn(Triplet),
            Triplet.animate.arrange(DOWN, aligned_edge = LEFT, center = False),
        )
        
        TripletBrace = Brace(Triplet, LEFT)
        self.play(DrawBorderThenFill(TripletBrace), run_time = 1)           #draw the brace on the left of the triplet state
        self.play(Write(TripletText))
        
        self.wait(2)
        
        self.play(                                                          #remove stuff except the spin 0 state and the atom
            FadeOut(TripletBrace), FadeOut(TripletText), FadeOut(Triplet[0]), FadeOut(Triplet[2])
        )
        self.play(Flash(Triplet[1][1], flash_radius = 0.2))
        Singlet.move_to(Triplet[1])
        
        self.remove(Triplet[1])
        self.play(
            ReplacementTransform(Triplet[1].copy(), Singlet)
        )
        self.wait()
        
        SingletCanc.next_to(Singlet, DOWN/2)                                #move the cancellation below singlet state
        IncomingPhotonAnim(PhotonArrow(Singlet, LEFT), RIGHT)
        self.play(FadeIn(SingletCanc), run_time = 1)
        self.wait(2)
        self.play(FadeOut(SingletCanc))
        
        
        IncomingPhotonAnim(PhotonArrow(Singlet, LEFT), RIGHT)
        self.play(                                                          #resize the atom
            Transform(electron, electron2, rate_func = there_and_back),
            Transform(orbit, orbit2, rate_func = there_and_back),
            Transform(minus, minus2, rate_func = there_and_back),
            FadeIn(AtomGrows, rate_func = there_and_back),
            run_time = 3
        )
        self.wait()
        
        self.play(Write(SingletStateText))
        self.play(FadeIn(footnote), run_time = 0.5)
        self.wait(2)
        
        self.play(FadeOut(*self.mobjects))









class SingsTrips_3(Scene):
    def construct(self):
    
        #Gluon Diagram
        gluonFig = VGroup(
            MathTex(r"""
            \begin{tikzpicture} 
                    \begin{feynhand} 
                        \vertex (a) at (0, 1); \vertex (b) at (0, -1); 
                        \propag [gluon] (a) to [edge label' = $g$] (b); 
                    \end{feynhand} 
            \end{tikzpicture}
        """, stroke_width = 2, fill_opacity = 0),
            MathTex(r"="),
        )
        
        gluonTripletStates = VGroup(
            Tex(r"$\frac{1}{ \sqrt{2} }$ ({{$r$}}{{$\Bar{b}$}} + {{$b$}}{{$\Bar{r}$}})"),
            Tex(r"$\frac{1}{ \sqrt{2} }$ ({{$b$}}{{$\Bar{g}$}} + {{$g$}}{{$\Bar{b}$}})"),
            Tex(r"$\frac{1}{ \sqrt{2} }$ ({{$g$}}{{$\Bar{r}$}} + {{$r$}}{{$\Bar{g}$}})")
        )
        for state in gluonTripletStates:
            ColorMathTexColours(state)
            
        TripletBrace = Brace(gluonTripletStates.copy().arrange(DOWN, aligned_edge = LEFT), LEFT)
        
        VGroup(*gluonFig, TripletBrace, gluonTripletStates).arrange(RIGHT)
        
        
        
        
        #The Color Cycle, again.
        backCircle = Circle(radius = 1, stroke_width = 0)
        
        ColorTexMobjs = VGroup(
            Tex(r"r"), Tex(r"g"), Tex(r"b")
        )
        ColorTexColours(ColorTexMobjs)
        
        CycleArrows = VGroup(
            CurvedArrow(start_point = backCircle.point_at_angle(Radians(75)), end_point = backCircle.point_at_angle(Radians(345)), radius = -1, 
            arc_center = ORIGIN, tip_length = 0.2),
            CurvedArrow(start_point = backCircle.point_at_angle(Radians(315)), end_point = backCircle.point_at_angle(Radians(225)), radius = -1, 
            arc_center = ORIGIN, tip_length = 0.2),
            CurvedArrow(start_point = backCircle.point_at_angle(Radians(195)), end_point = backCircle.point_at_angle(Radians(105)), radius = -1, 
            arc_center = ORIGIN, tip_length = 0.2),
        )
        
        ColorCycle = VGroup(backCircle, ColorTexMobjs, CycleArrows).scale(0.75).to_corner(UR)
        CyclePositions = [backCircle.point_at_angle(PI/2), backCircle.point_at_angle(PI/2 - 2*PI/3), backCircle.point_at_angle(PI/2 + 2*PI/3)]
        for i in [0, 1, 2]:
            ColorTexMobjs[i].move_to(CyclePositions[i])
            
            
        
        #Marquee text
        Marquee = VGroup(
            Tex(r"Like triplet states!", font_size = Medium),
            Tex(r"We can also find the singlet states like before... {{but there is a small caveat}}", font_size = Small)
        ).arrange(DOWN).to_edge(DOWN)





        #Animation Sequence
        self.play(Write(gluonFig), run_time = 2)
        self.play(Write(gluonTripletStates[0]), run_time = 2)
        
        self.play(GrowFromCenter(ColorCycle))
        self.wait()
        
        self.play(                                                                      #Before red is blue
            Indicate(ColorTexMobjs[0]), Indicate(ColorTexMobjs[2]), run_time = 1
        )
        self.play(                                                                      #Before blue is green
            Indicate(ColorTexMobjs[2]), Indicate(ColorTexMobjs[1]), run_time = 1
        )
        self.wait()
        
        for i in [0, 1, 2]:                                                             #Go through the cycle
            self.remove(gluonTripletStates[i]),
            self.play(  
                ColorTexMobjs[0].animate.move_to(CyclePositions[(i+1) % 3]),
                ColorTexMobjs[1].animate.move_to(CyclePositions[(i+2) % 3]),
                ColorTexMobjs[2].animate.move_to(CyclePositions[(i+0) % 3]),
                Transform(gluonTripletStates[i].copy(), gluonTripletStates[(i+1) % 3], replace_mobject_with_target_in_scene = True)
            )
            self.wait(2)
        
        self.play(gluonTripletStates[0].animate.shift(UP + RIGHT/10), run_time = 1)
        
        #gluonTripletStates.shift(UP + RIGHT/10)                                         #Make the triplet states cascade down
        self.play(
            FadeIn(gluonTripletStates[1]), FadeIn(gluonTripletStates[2]), 
            gluonTripletStates.animate.arrange(DOWN, aligned_edge = LEFT, center = False),
            
        )
        self.play(DrawBorderThenFill(TripletBrace), run_time = 0.6)                     #Triplet brace
        self.wait(2)
        
        self.play(Write(Marquee[0]))
        self.wait()
        self.play(FadeIn(Marquee[1][0]))
        self.wait(2)
        
        self.play(Write(Marquee[1][1]), run_time = 1.2)
        self.wait(2)
        
        self.remove((*self.mobjects))
        
        Previously = VGroup(
            Tex(r"Previously:"),
            Rectangle(color = WHITE, fill_opacity = 0, height = 4, width = 4), stroke_width = 1.5
        ).arrange(DOWN).shift(LEFT*FRAME_WIDTH/4)
        self.add(Previously)
        self.wait(1)
        
        








class SingsTrips_4(Scene):
    def construct(self):
        Previously = VGroup(
            Tex(r"Previously:"),
            Rectangle(color = WHITE, fill_opacity = 0, height = 4, width = 4), stroke_width = 1.5
        ).arrange(DOWN).shift(LEFT*FRAME_WIDTH/4)
        
        
        RightSide = VGroup(
            Tex(r"Then, in this case:", font_size = Medium),
            MathTex(r"\frac{1}{\sqrt{2}}  (b\Bar{g} + g\Bar{b})", font_size = Medium),
            MathTex(r"\hookrightarrow \frac{1}{\sqrt{2}}  (b\Bar{g} - g\Bar{b})", font_size = Medium),
            Tex(r"(analogous to the singlet)", font_size = Small)
        ).arrange(DOWN).shift(RIGHT*FRAME_WIDTH/4)
        
        ActualSinglet = MathTex(r"\hookrightarrow \frac{-i}{\sqrt{2}}  (b\Bar{g} - g\Bar{b})", font_size = Medium).move_to(RightSide[2])
        
        Footnote1 = Tex(r"A factor of $-i$ also has to go in. \\ The reason is quite interesting, but out of the scope of this video.", font_size = Tiny).to_edge(DOWN)
        
        
        
        
        
        #AnimationSequence
        self.add(Previously)
        self.wait(3)
        
        for s in RightSide:
            self.play(Write(s))
            
        self.wait()
        self.play(FadeIn(Footnote1))
        self.wait()

        self.play(Transform(RightSide[2], ActualSinglet, replace_mobject_with_target_in_scene = True))
        self.wait()
        
        self.play(FadeOut(*self.mobjects), run_time = 0.5)
        
        
   








   
class SingsTrips_5(Scene):
    def construct(self):
    
        #Dummy states
        TripletSumStates = VGroup(
            Tex(r"$\frac{1}{ \sqrt{2} }$ ({{$r$}}{{$\Bar{b}$}} + {{$b$}}{{$\Bar{r}$}})", font_size = Medium),
            Tex(r"$\frac{1}{ \sqrt{2} }$ ({{$b$}}{{$\Bar{g}$}} + {{$g$}}{{$\Bar{b}$}})", font_size = Medium),
            Tex(r"$\frac{1}{ \sqrt{2} }$ ({{$g$}}{{$\Bar{r}$}} + {{$r$}}{{$\Bar{g}$}})", font_size = Medium),
        ).arrange(DOWN)
        SingletTypeStates = VGroup(
            Tex(r"$\frac{-i}{\sqrt{2}}  (r\Bar{b} - b\Bar{r})$", font_size = Medium), 
            Tex(r"$\frac{-i}{\sqrt{2}}  (b\Bar{g} - g\Bar{b})$", font_size = Medium), 
            Tex(r"$\frac{-i}{\sqrt{2}}  (g\Bar{r} - r\Bar{g})$", font_size = Medium), 
        )
        TripletBrace = Brace(TripletSumStates, LEFT)
        SingletBrace = Brace(SingletTypeStates, LEFT)
        
        
        
        
        #The three blocks of triplet + singlet
        Block0 = VGroup(
            TripletSumStates[0].copy(), TripletSumStates[1].copy(), TripletSumStates[2].copy(),
            SingletTypeStates[0], TripletBrace.copy(), SingletBrace.copy(),
        ).arrange(DOWN)
        Block1 = VGroup(
            TripletSumStates[1].copy(), TripletSumStates[2].copy(), TripletSumStates[0].copy(),
            SingletTypeStates[1], TripletBrace.copy(), SingletBrace.copy(),
        ).arrange(DOWN)
        Block2 = VGroup(
            TripletSumStates[2].copy(), TripletSumStates[0].copy(), TripletSumStates[1].copy(),
            SingletTypeStates[2], TripletBrace.copy(), SingletBrace.copy(),
        ).arrange(DOWN)
        
        Blocks = VGroup(Block0, Block1, Block2)
        for block in Blocks:
            trip = VGroup(block[0], block[1], block[2])
            sing = block[3]
            block[4].next_to(trip, LEFT)
            block[5].next_to(sing, LEFT)
        Blocks.arrange(RIGHT, buff = 2)
        
        
        
        #The Color Cycle, again.
        backCircle = Circle(radius = 1, stroke_width = 0)
        
        ColorTexMobjs = VGroup(
            Tex(r"r"), Tex(r"g"), Tex(r"b")
        )
        ColorTexColours(ColorTexMobjs)
        
        CycleArrows = VGroup(
            CurvedArrow(start_point = backCircle.point_at_angle(Radians(75)), end_point = backCircle.point_at_angle(Radians(345)), radius = -1, 
            arc_center = ORIGIN, tip_length = 0.2),
            CurvedArrow(start_point = backCircle.point_at_angle(Radians(315)), end_point = backCircle.point_at_angle(Radians(225)), radius = -1, 
            arc_center = ORIGIN, tip_length = 0.2),
            CurvedArrow(start_point = backCircle.point_at_angle(Radians(195)), end_point = backCircle.point_at_angle(Radians(105)), radius = -1, 
            arc_center = ORIGIN, tip_length = 0.2),
        )
        
        ColorCycle = VGroup(backCircle, ColorTexMobjs, CycleArrows).scale(0.75).to_edge(UP)
        CyclePositions = [backCircle.point_at_angle(PI/2), backCircle.point_at_angle(PI/2 - 2*PI/3), backCircle.point_at_angle(PI/2 + 2*PI/3)]
        for i in [0, 1, 2]:
            ColorTexMobjs[i].move_to(CyclePositions[i])
        
        
        
        #Marquee texts
        Marquee = VGroup(
            Tex(r"\textbf{Six} of them are unique, and give us \textbf{six} possible (colored) gluon states!", font_size = Medium, color = YELLOW),
            
        ).to_edge(DOWN)
        
        #Rectangles around six unique states
        SixRects = VGroup()
        for block in Blocks:
            rect1 = SurroundingRectangle(block[0], buff = 0.2)
            rect2 = SurroundingRectangle(block[3], buff = 0.2)
            SixRects.add(rect1, rect2)
        
        
        
        #AnimationSequence
        self.play(GrowFromEdge(Block0, LEFT))
        self.wait()
        
        self.play(SpinInFromNothing(ColorCycle))
        
        self.play(TransformFromCopy(Block0, Block1))
        self.play(TransformFromCopy(Block1, Block2))
        self.wait(2)
        
        self.play(Write(Marquee[0]))
        self.play(FadeIn(SixRects))
        self.wait(4)
        
        self.play(FadeOut(*self.mobjects))
        
        








class SingsTrips_6(Scene):
    def construct(self):
        #Earlier...
        Earlier = VGroup(
            Tex(r"""Earlier: `colorless gluons cannot exist'"""),
            Tex(r"More precisely, colorless gluons that \textit{aren't} affected by:", font_size = Medium),
            Tex(r"i) Moving through the color cycle ({{r}} $\rightarrow$ {{g}} $\rightarrow$ {{b}} $\rightarrow$ {{r}})", font_size = Small),
            Tex(r"ii) Swapping two colors ({{r}} $\leftrightarrow$ {{b}}, etc.)", font_size = Small),
            Tex(r"cannot exist, as only they can interact with protons and neutrons.", font_size = Medium)
        ).arrange(DOWN, aligned_edge = LEFT).to_edge(UP)
        ColorTexColours(Earlier[2])
        ColorTexColours(Earlier[3])
        
        ForExample = Tex(r"For example:")
        
        Examples = VGroup(
            MathTex(r"\frac{1}{\sqrt{2}} ( {{r}}{{ \Bar{r} }} + {{b}}{{ \Bar{b} }} )", font_size = Medium),
            Tex(r"(unchanged by {{r}} $\leftrightarrow$ {{b}})", font_size = Small),
            MathTex(r"\frac{1}{\sqrt{3}} ( {{g}}{{ \Bar{g} }} + {{b}}{{ \Bar{b} }} + {{r}}{{ \Bar{r} }})", font_size = Medium),
            Tex(r"(unchanged by {{r}} $\rightarrow$ {{g}} $\rightarrow$ {{b}} $\rightarrow$ {{r}})", font_size = Small),
        ).arrange_in_grid(rows = 2, cols = 2, buff = 1.5, flow_order = 'dr').next_to(ForExample, 2*DOWN)
        for eg in Examples:
            ColorTexColours(eg)

        RealSinglet = VGroup(
            SurroundingRectangle(Examples[2], buff = 0.2),
            Tex(r"The real color singlet!", font_size = Small, color = YELLOW)
        )
        RealSinglet[1].next_to(RealSinglet[0], DOWN)
        
        
        
        
        #Animation Sequence
        
        self.play(Write(Earlier[0]))
        self.wait()
        
        self.play(Write(Earlier[1]))
        self.play(FadeIn(Earlier[2]), FadeIn(Earlier[3]))
        self.play(Write(Earlier[4]))
        self.wait()
        
        self.play(Write(ForExample))
        self.play(Write(Examples[1]), Write(Examples[0]))
        self.wait()
        
        self.play(Write(Examples[2]), Write(Examples[3]))
        self.play(Create(RealSinglet[0]), FadeIn(RealSinglet[1]))
        self.wait(2)
        
        
        
        
        
        
        
        
        
        
        
        
        
class SingsTrips_7(Scene):
    def construct(self):
        #However.
        However = VGroup(
            Tex(r"However..."),
            Tex(r"Colorless gluons that \textit{are} affected by (i) and (ii): totally fine!", font_size = Medium)
        ).arrange(DOWN).to_edge(UP)
        
        ForExample = Tex(r"For example:").next_to(However, 4*DOWN)
        
        
        Examples = MathTex(r"""
            (i): {{r}} \leftrightarrow {{b}} &\implies \frac{1}{\sqrt{2}} ( {{r}}{{ \Bar{r} }} - {{b}}{{ \Bar{b} }} ) 
            \rightarrow \frac{-1}{\sqrt{2}} ( {{r}}{{ \Bar{r} }} - {{b}}{{ \Bar{b} }} )\\
            (ii): {{r}} \rightarrow {{g}} \rightarrow {{b}} \rightarrow {{r}} &\implies \frac{1}{\sqrt{3}} ( {{r}}{{ \Bar{r} }} + {{b}}{{ \Bar{b} }} -2 {{g}}{{ \Bar{g} }})
            \rightarrow \frac{1}{\sqrt{3}} ( {{g}}{{ \Bar{g} }} + {{r}}{{ \Bar{r} }} -2 {{b}}{{ \Bar{b} }})
        """, font_size = Medium)
        ColorTexColours(Examples)
        
        ExampleBoxes = VGroup(
            #Rectangle(height = 2, width = 3, color = YELLOW).shift(RIGHT/3),
            Polygon(LEFT + DOWN, LEFT + UP, RIGHT/1.1 + UP, RIGHT/1.1, 2*RIGHT, 2*RIGHT + DOWN, color = YELLOW).shift(0.1*LEFT)
        )
        
        Marquee = VGroup(
            Tex(r"colorless, but modified by (i) and (ii).", font_size = Small, color = YELLOW),
            Tex(r"We've found \textit{two more} gluon states!", font_size = Small)
        ).arrange(DOWN).next_to(Examples, DOWN)
        
        Footer = Tex(r"""Turns out that every other valid colorless gluon is some \textit{combination} of these two, hence,
        we already have all the \textbf{independent} choices.""", font_size = Tiny).to_edge(DOWN)
        
        #Animation Sequence
        for however in However:
            self.play(Write(however))
            
        self.play(Write(ForExample))
        self.play(FadeIn(Examples), run_time = 2)
        self.wait()
        
        self.play(Create(ExampleBoxes), run_time = 2)
        self.play(Write(Marquee[0]))
        self.wait()
        
        self.play(FadeIn(Footer))
        self.wait(1)
        
        self.play(Write(Marquee[1]))
        self.wait(2)
        











class SingsTrips_8(Scene):
    def construct(self):
        WeHave = Tex(
            r"We have 8 gluons now: (an \underline{octet})"
        ).to_edge(UP)
        
        TheGluons = VGroup(
            MathTex(r"\frac{1}{\sqrt{2}} ({{g}}{{ \Bar{r} }} + {{r}}{{ \Bar{g} }})"),
            MathTex(r"\frac{1}{\sqrt{2}} ({{b}}{{ \Bar{g} }} + {{g}}{{ \Bar{b} }})"),
            MathTex(r"\frac{1}{\sqrt{2}} ({{r}}{{ \Bar{b} }} + {{b}}{{ \Bar{r} }})"),
            MathTex(r"\frac{-i}{\sqrt{2}} ({{g}}{{ \Bar{r} }} - {{r}}{{ \Bar{g} }})"),
            MathTex(r"\frac{-i}{\sqrt{2}} ({{b}}{{ \Bar{g} }} - {{g}}{{ \Bar{b} }})"),
            MathTex(r"\frac{-i}{\sqrt{2}} ({{r}}{{ \Bar{b} }} - {{b}}{{ \Bar{r} }})"),
            MathTex(r"\frac{1}{\sqrt{2}} ({{r}}{{ \Bar{r} }} - {{b}}{{ \Bar{b} }})"),
            MathTex(r"\frac{1}{\sqrt{6}} ({{r}}{{ \Bar{r} }} + {{b}}{{ \Bar{b} }} - 2{{g}}{{ \Bar{g} }})"),
        )
        for gluon in TheGluons:
            gluon.set(font_size = Medium)
            ColorTexColours(gluon)
            
        ColoredGluons = VGroup(*[TheGluons[i] for i in range(6)])
        
        
        ColorlessGluons = VGroup(TheGluons[6], TheGluons[7]).arrange(DOWN)
        ColorlessGluons3 = VGroup(
            MathTex(r"\frac{1}{\sqrt{2}} ({{g}}{{ \Bar{g} }} - {{r}}{{ \Bar{r} }})"),
            MathTex(r"\frac{1}{\sqrt{6}} ({{g}}{{ \Bar{g} }} + {{r}}{{ \Bar{r} }} - 2{{b}}{{ \Bar{b} }})"),
        ).arrange(DOWN)
        ColorlessGluons2 = VGroup(
            MathTex(r"\frac{1}{\sqrt{2}} ({{b}}{{ \Bar{b} }} - {{g}}{{ \Bar{g} }})"),
            MathTex(r"\frac{1}{\sqrt{6}} ({{b}}{{ \Bar{b} }} + {{g}}{{ \Bar{g} }} - 2{{r}}{{ \Bar{r} }})"),
        ).arrange(DOWN)
        for cl in [*ColorlessGluons2, *ColorlessGluons3]:
            cl.set(font_size = Medium)
            ColorTexColours(cl)
            
            
        Wheel = Ellipse(width = 7, height = 4, stroke_width = 0)
        WheelPositions = []
        for i in range(6):
            WheelPositions.append(Wheel.point_at_angle(i*PI/3))
            TheGluons[i].move_to(WheelPositions[i])
            
        AllGluons = Tex(r"All gluons are a \textbf{linear combination} of these eight!", font_size = Medium).to_edge(DOWN)
        But = Tex(r"A different-looking octet, {{but the relationship between the states is the same.}}", font_size = Small).to_edge(DOWN)
        ItsAGroup = VGroup(
            Tex(r"Set that's symmetric under an action: {{a \textbf{group}.}}", font_size = Small),
            Tex(r"Our octet is symmetric in regards to the color cycle:\textbf{ {{SU(3)}} }", font_size = Small).set_color_by_tex("SU(3)", color = YELLOW),
        ).arrange(DOWN).to_edge(DOWN)
                
        OctetRect = SurroundingRectangle(TheGluons, color = YELLOW)
        OctetLabel = Tex(r"SU(3)", color = YELLOW).next_to(OctetRect, UP)
                
                
                
        #The Color Cycle, again.
        backCircle = Circle(radius = 1, stroke_width = 0)
        
        ColorTexMobjs = VGroup(
            Tex(r"r"), Tex(r"g"), Tex(r"b")
        )
        ColorTexColours(ColorTexMobjs)
        
        CycleArrows = VGroup(
            CurvedArrow(start_point = backCircle.point_at_angle(Radians(75)), end_point = backCircle.point_at_angle(Radians(345)), radius = -1, 
            arc_center = ORIGIN, tip_length = 0.2),
            CurvedArrow(start_point = backCircle.point_at_angle(Radians(315)), end_point = backCircle.point_at_angle(Radians(225)), radius = -1, 
            arc_center = ORIGIN, tip_length = 0.2),
            CurvedArrow(start_point = backCircle.point_at_angle(Radians(195)), end_point = backCircle.point_at_angle(Radians(105)), radius = -1, 
            arc_center = ORIGIN, tip_length = 0.2),
        )
        
        ColorCycle = VGroup(backCircle, ColorTexMobjs, CycleArrows).scale(0.75).to_corner(UR)
        CyclePositions = [backCircle.point_at_angle(PI/2), backCircle.point_at_angle(PI/2 - 2*PI/3), backCircle.point_at_angle(PI/2 + 2*PI/3)]
        for i in [0, 1, 2]:
            ColorTexMobjs[i].move_to(CyclePositions[i])
        

        
        
        
        #Animation Sequence
        self.play(Write(WeHave))
        
        for gluon in TheGluons:
            self.play(FadeIn(gluon), run_time = 0.25)
        self.wait()    
        
        self.play(Write(AllGluons))
        self.wait()
        self.play(FadeOut(AllGluons))
        
        self.play(GrowFromCenter(ColorCycle), FadeOut(WeHave))
        self.play(
            *[ColorTexMobjs[i].animate.move_to(CyclePositions[(i+1)%3]) for i in range(3)],
            *[ColoredGluons[j].animate.move_to(WheelPositions[(j-1)%6]) for j in range(6)],
            Transform(ColorlessGluons, ColorlessGluons2, replace_mobject_with_target_in_scene = True),
        )
        self.wait()
        
        self.play(
            *[ColorTexMobjs[i].animate.move_to(CyclePositions[(i+2)%3]) for i in range(3)],
            *[ColoredGluons[j].animate.move_to(WheelPositions[(j-2)%6]) for j in range(6)],
            Transform(ColorlessGluons2, ColorlessGluons3, replace_mobject_with_target_in_scene = True),
        )
        self.wait()

        
        self.play(FadeIn(But[0]))
        self.wait()
        self.play(Write(But[1]))
        self.wait()
        self.play(FadeOut(But))
        
        for thing in ItsAGroup:
            self.play(Write(thing[0]))
            self.play(Write(thing[1]))
            
        self.play(
            Create(OctetRect),
            Write(OctetLabel),
            run_time = 2
        )
        self.wait()