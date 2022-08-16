from manim import *
config.max_files_cached = 1000
from utsf_common import *




                    
                    
class PEP_1(Scene):
    def construct(self):
        ToSolveThisMystery = Tex(r"To solve this mystery, physicists built the first particle accelerators in the 1960s", font_size = Medium).to_edge(UP)
        
        Images = Group(
            ImageMobject(r"images/PauliExclusion/SLACLong.jpg"),
            ImageMobject(r"images/PauliExclusion/SLAC_tunnel_2.jpg")
        )
        for img in Images:
            img.set(width = FRAME_WIDTH/2.2)
        Images.arrange(DOWN, buff = 0.2).next_to(ToSolveThisMystery, DOWN)
        
        ImageCaption = Tex(r"The \textbf{SLAC National Accelerator Laboratory}, where the \\ Deep Inelastic experiments were performed.", font_size = Tiny).next_to(Images, DOWN)
        
        
        #Animation Sequence
        self.play(Write(ToSolveThisMystery), run_time = 2)
        self.wait()
        
        for img in Images:
            self.play(FadeIn(img), run_time = 1)
        self.play(Write(ImageCaption))
        self.wait()
        
        
        
        
        
        
class PEP_2(Scene):
    def construct(self):
        PauliPhoto = Group(
            ImageMobject(r"images/PauliExclusion/Wolfgang_Pauli.jpg").set(width = FRAME_WIDTH/5),
            Tex(r"Wolfgang Pauli, ca. 1924 \\ (Image: CERN)", font_size = Tiny),
        ).arrange(DOWN).to_edge(RIGHT)
        
        PauliExclusionPrinciple = VGroup(
            Tex(r"{{P}}auli", font_size = Huge).set_color_by_tex("P", YELLOW),
            Tex(r"{{E}}xclusion", font_size = Huge).set_color_by_tex("E", YELLOW),
            Tex("{{P}}rinciple", font_size = Huge).set_color_by_tex("P", YELLOW),
            Tex("and talking about {{spin}}", font_size = Medium).set_color_by_tex("spin", YELLOW),
        ).arrange(DOWN).shift(LEFT)
        
        
        
        #Animation Sequence
        self.add(PauliPhoto)
        self.play(Write(PauliExclusionPrinciple), run_time = 3)
        self.wait(2)
        
        






class PEP_3(Scene):
    def construct(self):
        def ColVecMobject(c1, c2, c3, c4, fs = Medium):
            v = VGroup(
                MathTex(r"\Biggl(", font_size = 60),
                VGroup(
                    MathTex(c1, font_size = fs),
                    MathTex(c2, font_size = fs),
                    MathTex(c3, font_size = fs),
                    MathTex(c4, font_size = fs)
                ).arrange(DOWN),
                MathTex(r"\Biggr)", font_size = 60),
            ).arrange(RIGHT, buff = 0.2)
            return(v)
            
            
        
        ItGetsInteresting = VGroup(
            Tex(r"Here's where things get interesting...", font_size = Large),
            Tex(r"Consider: $\Ket{\frac{1}{2}_A ,-\frac{1}{2}_B}$", font_size = Medium),
        ).arrange(DOWN).to_edge(UP)
        
        
        TensorProductEvals = VGroup(
            VGroup(
                Tex(r"A $\otimes$ B:", color = YELLOW),
                MathTex(r"\Ket{\frac{1}{2}_A} \otimes \Ket{-\frac{1}{2}_B} =", font_size = Medium),
                ColVecMobject(r"0", r"1", r"0", r"0"),
            ).arrange(RIGHT, buff = 0.2),
            VGroup(
                Tex(r"B $\otimes$ A:", color = YELLOW),
                MathTex(r"\Ket{-\frac{1}{2}_B} \otimes \Ket{\frac{1}{2}_A} =", font_size = Medium),
                ColVecMobject(r"0", r"0", r"1", r"0"),
            ).arrange(RIGHT, buff = 0.2),
        ).arrange(DOWN).scale(0.75)
        for prod in TensorProductEvals:
            prod[2][1][1].set(color = YELLOW)
            prod[2][1][2].set(color = YELLOW)
        EvalsBrace = Brace(TensorProductEvals, RIGHT, sharpness = 1)
        TheyAreTheSame = Tex(r"Both describe the same \\ physical situation", font_size = Small).next_to(EvalsBrace, RIGHT)
        
        PauliSays = Tex(r"Pauli: They're related to each other, and the relationship depends on {{spin}}!", font_size = Medium).set_color_by_tex("spin", YELLOW).to_edge(DOWN)
        
        
        #Animation Sequence
        for interesting in ItGetsInteresting:
            self.play(Write(interesting))
            self.wait()
            
        for math in TensorProductEvals[0]:
            self.play(Write(math))
            self.wait(0.5)
        for math in TensorProductEvals[1]:
            self.play(Write(math))
            self.wait(0.5)
        self.wait()
        
        self.play(
            Write(EvalsBrace), Write(TheyAreTheSame)
        )
        self.wait()
        self.play(Write(PauliSays))
        self.wait()
        
        
        
        





class PEP_4(Scene):
    def construct(self):
        #ATOM SCHEMATIC DIAGRAM: 2E, 2P, 2N 
        nucleonSize = 0.12
        
        #the nucleus
        proton1 = Dot(radius=nucleonSize).set_color(RED)                                                 
        neutron1 = Dot(radius=nucleonSize).next_to(proton1,RIGHT,buff=0).set_color(WHITE)
        neutron2 = Dot(radius=nucleonSize).next_to(proton1,DOWN,buff=0)
        proton2 = Dot(radius=nucleonSize).next_to(neutron1,DOWN,buff=0).set_color(RED)
        
        nucleus = VGroup(proton1,neutron1,proton2,neutron2)
        
        #orbit
        a_orbit = 6*nucleus.width
        orbit = Circle(color=WHITE).surround(nucleus).scale(a_orbit)
        
        #electrons on orbit
        electronBuffer = -0.014
        electron1 = Dot(color=BLUE).move_to(orbit.point_at_angle(PI/6))
        electron2 = Dot(color=BLUE).move_to(orbit.point_at_angle(-PI/6))
        
        #VGroup of orbit, nucleus and electronx2
        AtomGroup = VGroup(orbit,electron1,electron2,nucleus)
        AtomGroup.shift(3*LEFT + UP/2)                                                    
        
        #plus/minus charge labels
        LabelTextSize = 20
        
        minusStr = r"\textbf{-}"
        minus1 = MathTex(minusStr, font_size = LabelTextSize)
        minus2 = MathTex(minusStr, font_size = LabelTextSize)

        minus1.move_to(electron1)
        minus2.move_to(electron2)
        
        electronSign1 = VGroup(electron1, minus1)
        electronSign2 = VGroup(electron2, minus2)
        
        plusStr = r"\textbf{+}"
        plus1 = MathTex(plusStr, font_size = LabelTextSize)
        plus2 = MathTex(plusStr, font_size = LabelTextSize)
        
        plus1.move_to(proton1)
        plus2.move_to(proton2)
        
        chargeLabels = VGroup(minus1,minus2,plus1,plus2)
        
        #Naming the electrons
        Names = VGroup(
            Tex(r"A", font_size = Small).next_to(electron1, UR/4),
            Tex(r"B", font_size = Small).next_to(electron2, DR/4),
        )
        
        #Naming the nuclei
        nucleus2 = nucleus.copy().next_to(nucleus, 2*DOWN)
        nucleusLabels = VGroup(
            VGroup(plus1, plus2).copy().move_to(nucleus),
            VGroup(plus1, plus2).copy().move_to(nucleus2),
        )
        nucleusNames = VGroup(
            Tex(r"$n_1$").next_to(nucleus, RIGHT),
            Tex(r"$n_2$").next_to(nucleus2, RIGHT),
        )
        
        #Right Column
        BosonCat = VGroup(
            Tex(r"Bosons: integer spin (0, 1, ...)", font_size = Medium),
            MathTex(r"\Ket{\psi(n_1, n_2)} = \Ket{\psi(n_2, n_1)", font_size = Medium)
        ).arrange(DOWN, aligned_edge = LEFT)
        
        FermionCat = VGroup(
            Tex(r"Fermions: half-integer spin ($\frac{1}{2}$, $\frac{3}{2}$, ...)", font_size = Medium),
            MathTex(r"\Ket{\psi(A, B)} = -\Ket{\psi(B, A)", font_size = Medium)
        ).arrange(DOWN, aligned_edge = LEFT)
        
        RightCats = VGroup(BosonCat, FermionCat).arrange(DOWN, aligned_edge = LEFT, buff = 2).to_edge(RIGHT)
        Rectangles = VGroup(
            SurroundingRectangle(BosonCat[1], color = YELLOW),
            SurroundingRectangle(FermionCat[1], color = YELLOW),
        )
        PEPText = Tex(r"Pauli Exclusion Principle", color = YELLOW).next_to(Rectangles[1], DOWN)
        
        #Animation Sequence
        self.add(nucleus, nucleus2, nucleusNames, nucleusLabels)
        self.wait()
        
        self.play(Write(BosonCat), run_time = 3)
        self.wait()
        
        self.play(
            FadeOut(nucleus), FadeOut(nucleus2), FadeOut(nucleusNames), FadeOut(nucleusLabels)
        )
        self.play(
            GrowFromCenter(AtomGroup)
        )
        self.play(Write(Names), FadeIn(chargeLabels))
        self.wait()
        
        self.play(Write(FermionCat), run_time = 3)
        self.wait()
        
        self.play(Create(Rectangles), run_time = 2)
        self.play(Write(PEPText))
        self.wait()
        self.play(FadeOut(*self.mobjects))








class PEP_5(Scene):
    def construct(self):
        SST = Tex(r"Spin-Statistics Theorem")
        
        Box = Rectangle(width = 4.112*2, height = 2.0*2, color = WHITE, stroke_width = 2)
        BoxText = Tex(r"Put an video of scrolling down the Wikipedia page of this topic", font_size = Tiny)
        
        Underbox = Tex(r"It's really hard to explain, so we'll take it for granted", font_size = Small).next_to(Box, DOWN)
        
        
        self.play(Write(SST))
        self.play(SST.animate.to_edge(UP))
        self.play(Create(Box))
        self.add(BoxText)
        self.wait(3)
        self.play(Write(Underbox))
        self.wait()
       
       
       
       
class PEP_6(Scene):
    def construct(self):
        SthInteresting = Tex(
            r"Something interesting about the function {{$C(\Ket{e_A e_B})$}}", font_size = Medium
        ).set_color_by_tex("C(\Ket{e_A e_B})", YELLOW).to_edge(UP)
        
        UpUp = MathTex(r"""
            C(+\frac{1}{2}, +\frac{1}{2}) &= C(+\frac{1}{2}, +\frac{1}{2}) \qquad \text{if we switched A and B} \\
            {{ &= -C(+\frac{1}{2}, +\frac{1}{2}) \qquad \text{(Pauli's exclusion)} }}\\
            {{ \implies C(+\frac{1}{2}, +\frac{1}{2}) &= 0 }} \\
            {{\text{Similarly, } \quad C(-\frac{1}{2}, -\frac{1}{2}) &= 0 }}
        """, font_size = Medium).shift(RIGHT)
        
        Bottom_6 = Tex(
            r"\textbf{Impossible} to measure both electrons in the \textit{same spin state}!", font_size = Medium
        ).to_edge(DOWN)
        
        
        
        #Animation Sequence
        self.play(Write(SthInteresting))
        self.wait()
        
        for line in UpUp:
            self.play(Write(line))
            self.wait(0.5)
        self.wait()
        self.play(FadeIn(Bottom_6))
        self.wait()
        self.play(FadeOut(*self.mobjects))
            
        
        
        
        
class PEP_7(Scene):
    def construct(self):
        CanOnlyHave = Tex(r"We can only have states with \underline{opposite} electron spins!", font_size = Large).to_edge(UP)
        
        Wavefunction_7 = MathTex(r"""
            \Ket{\psi} = {{c_1\Ket{\frac{1}{2}_A, \frac{1}{2}_B} }}
            + {{c_2\Ket{\frac{1}{2}_A, -\frac{1}{2}_B} }}
            + {{c_3\Ket{-\frac{1}{2}_A, \frac{1}{2}_B} }}
            + {{c_4\Ket{-\frac{1}{2}_A, -\frac{1}{2}_B} }}
        """, font_size = Small).shift(UP)
        Cancels = VGroup()
        Zeros = VGroup()
        for st in [Wavefunction_7[1], Wavefunction_7[7]]:
            st.set_color(GREY)
            arr = Arrow(
                st.get_corner(DL), st.get_corner(UR), 
                buff = 0, max_tip_length_to_length_ratio = 0.05,
                max_stroke_width_to_length_ratio = 1.2,
            )
            z = MathTex(r"0", font_size = Small).next_to(arr.get_tip(),UR/4)
            Cancels.add(arr)
            Zeros.add(z)
        
        Probabs_7 = VGroup(
            VGroup(
                Tex(r"In the above,", font_size = Medium),
                MathTex(r"c_2 = - c_3", font_size = Medium, color = YELLOW),
                Tex(r"and", font_size = Medium),
                MathTex(r"|c_2|^2 + |c_3|^2 = 1", font_size = Medium, color = YELLOW),
            ).arrange(RIGHT, buff = 0.2),
            MathTex(r"\therefore |c_2|^2 = |c_3|^2 = \frac{1}{2}", font_size = Medium, color = YELLOW),
        ).arrange(DOWN).next_to(Wavefunction_7, 3*DOWN)
        
        FiftyFifty = VGroup(
            Tex(r"A {{50-50}} chance of measuring either state", font_size = Large).set_color_by_tex("50-50", YELLOW),
            Tex(r"We got real physics from a mathematical restriction. Neat!", font_size = Medium)
        ).arrange(DOWN).to_edge(DOWN)
        
        
        
        
        #Animation Sequence
        self.play(
            FadeIn(Wavefunction_7), Write(CanOnlyHave)
        )
        self.play(
            *[GrowArrow(canc) for canc in Cancels], Write(Zeros)
        )
        self.wait()
        
        for kek in Probabs_7:
            self.play(Write(kek))
            self.wait(0.5)
        self.wait()
        for blep in FiftyFifty:
            self.play(Write(blep))
            self.wait(1)
        
        
        
        
        
        
class PEP_8(Scene):
    def construct(self):
        electron = Circle(color = BLUE, fill_opacity = 1, radius = 0.35)
        def ElectronWithName(mathtex, fs = Medium):
            name = MathTex(mathtex, font_size = fs, stroke_width = 0.6)
            e = VGroup(electron.copy(), name)
            return(e)
        WhatIfThree = Tex(r"What happens if there are three electrons?", font_size = Large).to_edge(UP)
        
        
        #SpinTable
        SpinTable = MobjectTable(
            [
            [MathTex(r"\frac{1}{2}"), MathTex(r"\frac{1}{2}"), MathTex(r"-\frac{1}{2}")],
            [MathTex(r"\frac{1}{2}"), MathTex(r"-\frac{1}{2}"), MathTex(r"\frac{1}{2}")],
            [MathTex(r"-\frac{1}{2}"), MathTex(r"\frac{1}{2}"), MathTex(r"\frac{1}{2}")],
            ],
            include_outer_lines = False,
            col_labels = [ElectronWithName(r"e_A"), ElectronWithName(r"e_B"), ElectronWithName(r"e_C")],
            line_config = {'stroke_width': 1.4},
        ).set(height = FRAME_HEIGHT/2)
        HighlightPos = [(2,1), (2,2), (3,1), (3,3), (4,2), (4,3)]
        HighlightedSpins = VGroup(
            *[SpinTable.get_cell(pos, color = YELLOW, stroke_width = 1.2).set(width = 0.8) for pos in HighlightPos],
        )
        
        ExchangeStates = VGroup(
            MathTex(r"\Ket{\psi(A, B, C)} = \Ket{\psi(B, A, C)}", font_size = Small),
            MathTex(r"\Ket{\psi(A, B, C)} = \Ket{\psi(C, B, A)}", font_size = Small),
            MathTex(r"\Ket{\psi(A, B, C)} = \Ket{\psi(A, C, B)}", font_size = Small),
        ).arrange(DOWN, aligned_edge = LEFT, buff = 0.8).next_to(SpinTable, RIGHT).shift(DOWN/2.4)
        
        NotAntisymmetric = VGroup(
            Brace(ExchangeStates, DOWN, sharpness = 1),
            Tex(r"Not antisymmetric", font_size = Small)
        ).arrange(DOWN).next_to(ExchangeStates, DOWN)
        
        NotAProblem = Tex(
            r"Not a problem, as {{spin}} \underline{isn't} the only quantum number", font_size = Large
        ).set_color_by_tex("spin", YELLOW).to_edge(DOWN)
        
        
        
        #Animation Sequence
        self.play(Write(WhatIfThree))
        self.wait()
        
        self.play(SpinTable.create(), run_time = 4)
        self.wait()
        
        self.play(FadeIn(HighlightedSpins))
        self.wait()
        
        for es in ExchangeStates:
            self.play(Write(es), run_time = 1)
            self.wait(0.4)

        self.wait()
        self.play(Write(NotAntisymmetric))
        self.wait()
        self.play(Write(NotAProblem))
        self.wait()
        
        
        
        
        
class PEP_9(Scene):
    def construct(self):
        electron = Circle(color = BLUE, fill_opacity = 1, radius = 0.12)
        def ElectronWithName(mathtex, fs = Tiny):
            name = MathTex(mathtex, font_size = fs, stroke_width = 0.6)
            e = VGroup(electron.copy(), name)
            return(e)
        
        nucc = VGroup(
            Circle(color = RED, radius = 0.2, fill_opacity = 1),
            Tex(r"\textbf{nuc}", font_size = Tiny)
        )
        orbits = VGroup(
            Circle(radius = 1, stroke_width = 1.5, color = WHITE),
            Circle(radius = 2.5, stroke_width = 1.5, color = WHITE),
        )
        orbitLevels = VGroup(
            MathTex(r"n=1", font_size = Small).next_to(orbits[0],DOWN),
            MathTex(r"n=2", font_size = Small).next_to(orbits[1],DOWN),
        )
        eThree = VGroup(
            ElectronWithName(r"e_A").move_to(orbits[0].point_at_angle(PI/3)),
            ElectronWithName(r"e_B").move_to(orbits[0].point_at_angle(-PI/3)),
            ElectronWithName(r"e_C").move_to(orbits[1].point_at_angle(PI/12)),
        )
        ThreeElectronAtom = VGroup(nucc, orbitLevels, orbits, eThree).shift(2*LEFT)
        
        #Right Side Function C
        RightFunctionC = VGroup(
            MathTex(r"C\left( \Ket{s = \pm\frac{1}{2} }_A, \Ket{s = \pm\frac{1}{2} }_B\right)", font_size = Small),
            MathTex(r"\downarrow"),
            MathTex(r"C\left( \Ket{s = +\frac{1}{2}, n = 1}_A, \Ket{s = -\frac{1}{2}, n = 1}_B, \Ket{s = +\frac{1}{2}, n = 2}_C\right)", font_size = Tiny),
        ).arrange(DOWN, buff = 0.5).to_edge(RIGHT)
        
        RememberChem = VGroup(
            Tex(r"Remember chemistry?", font_size = Tiny),
            Tex(r"Only $<2$ $e^-$ allowed per orbital!", font_size = Tiny),
        ).arrange(DOWN, aligned_edge = LEFT).to_corner(UR)
        
        
        #Animation Sequence
        self.add(nucc, orbits, eThree)
        self.wait()
        
        self.play(Write(orbitLevels))
        self.wait()
        
        for r in RightFunctionC:
            self.play(Write(r))
        self.wait()
        
        self.play(Write(RememberChem))
        self.wait()
        
        self.play(FadeOut(*self.mobjects))
            
            
            
            
            
            
class PEP_10(Scene):
    def construct(self):
        ConfusingQuark = Tex(r"Quarks were confusing at first, and now we know why:", font_size = Large).to_edge(UP)
        
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
        quarkNames = ["u", "u", "d", "u", "d", "d"]
        for i in range(len(quarks)):
            qLabel = Tex(quarkNames[i], font_size = quarkLabelSize, color=WHITE)
            qLabel.move_to(quarks[i].get_center())
            quarkLabels.add(qLabel)
        
        #Problem
        Problems = VGroup(
            Tex(r"Problems:", font_size = Small),
            Tex(r"- quarks are spin $\frac{1}{2}$", font_size = Tiny),
            Tex(r"- need 3 quarks", font_size = Tiny),
            Tex(r"- too close together", font_size = Tiny)
        ).arrange(DOWN, aligned_edge = LEFT).to_edge(LEFT)
        
        #Solution
        Solution = Tex(r"Must be yet \textit{another} quantum number that antisymmetrizes the wavefunction!", font_size = Medium).to_edge(DOWN)
        ThereIsAnother = ImageMobject(r"images/PauliExclusion/ThereIsAnother.png")
        
        
        
        #Animation Sequence
        self.add(quarks, quarkLabels, nucleons2)
        self.play(Write(ConfusingQuark))
        self.wait()
        
        self.play(Write(Problems[0]))
        self.play(Write(Problems[1]))
        self.wait(.5)
        self.play(
            Write(Problems[2]),
            Transform(nucleons2, nucleonsBig, rate_func = there_and_back_with_pause), 
            FadeIn(nucleonLabels, rate_func = there_and_back_with_pause), 
            run_time = 2,
        )
        self.wait(.5)
        self.play(Write(Problems[3]))
        self.wait(2)
        self.play(
            Write(Solution),
            FadeIn(ThereIsAnother, rate_func = there_and_back_with_pause, run_time = 2),
        )    
        self.wait()
