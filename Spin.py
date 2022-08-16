from manim import *
import numpy as np
config.max_files_cached = 1000
from utsf_common import *


class Spin_1(Scene):
    def construct(self):    
        SpinDesc = VGroup(
            Tex(r"{{Spin}}: it's like if particles were spinning", font_size = Large).set_color_by_tex("Spin", YELLOW),
            Tex(r"...but they aren't spinning.", font_size = Medium),
            Tex(r"Yet they still have \underline{angular momentum}!", font_size = Large),
            Tex(r"(the details are complex)", font_size = Small)
        ).arrange(DOWN).shift(2*UP)
        
        SpinIsSpin = ImageMobject("images/Spin/SpinIsSpin.png").set(height = FRAME_HEIGHT/3)
        NotReally = Tex(r"(not really)", font_size = Tiny)
        Meme = Group(SpinIsSpin, NotReally).arrange(DOWN)
        
        Eagle = Tex(r"The maths is easy to describe{{, so we'll do that instead.}}", font_size = Medium)
        
        Scene1Group = Group(SpinDesc, Meme, Eagle)
        
        
        #Animation Sequence
        for d in SpinDesc[0:2]:
            self.play(Write(d))
            self.wait(0.6)
            
        self.play(FadeIn(Meme), run_time = 0.6)
        self.play(FadeOut(Meme), run_time = 0.6)
        
        for d in SpinDesc[2:4]:
            self.play(Write(d))
            self.wait()
        for w in Eagle:
            self.play(Write(w))
            self.wait(0.4)
        self.wait()
        
        
        
        
        
class Spin_2(Scene):
    def construct(self): 
        SzArray = VGroup(
            MathTex(r"-S", font_size = Medium),
            MathTex(r"-S+1", font_size = Medium),
            MathTex(r"...", font_size = Medium),
            MathTex(r"S-1", font_size = Medium),
            MathTex(r"S", font_size = Medium),
        ).arrange(DOWN, aligned_edge = LEFT)
        
        SpinBrace = Brace(SzArray, LEFT, sharpness = 1)
        
        Equation = VGroup(
            MathTex(r"s"),
            MathTex(r"="),
            SpinBrace,
            SzArray,
        ).arrange(RIGHT)
        
        Magnitude = Tex(r"$|S|$ = spin magnitude", color = YELLOW, font_size = Medium).next_to(SzArray, 2*RIGHT)
        
        SQNBox = SurroundingRectangle(Equation[0])
        SQNLabel = Tex(r"spin quantum number", font_size = Medium, color = YELLOW).next_to(SQNBox, 4*LEFT)
        SQNArrow = Arrow(SQNBox.get_left(), SQNLabel.get_right(), color = YELLOW)
        
        Equation.add(Magnitude, SQNBox, SQNLabel, SQNArrow)
        
        #Fermions example
        FermList = VGroup(
            Tex("electrons"),
            Tex("protons"),
            Tex("neutrons")
        ).arrange(DOWN, aligned_edge = RIGHT)
        FermBrace = Brace(FermList, RIGHT)
        FermSpins = MathTex(r"s = -\frac{1}{2}, +\frac{1}{2}", font_size = Medium)
        Fermion = Tex(r"(S = $\frac{1}{2}$, fermions)", color = YELLOW, font_size = Medium)
        
        FermExample = VGroup(
            Tex(r"For example,", font_size = Large),
            FermList, FermBrace, FermSpins, Fermion
        ).arrange(RIGHT, buff = 0.5)
        
        
        #Photon exchange
        Electron = VGroup(
            Circle(radius = 0.2, color = BLUE, fill_opacity = 1),
            MathTex(r"e^-", color = BLACK, font_size = Small)
        )
        PhotonExchange1 = VGroup(
            Electron.copy(),
            MathTex(r"(s = -\frac{1}{2})", font_size = Small),
            MathTex(r"+", font_size = Small),
            Tex(r"photon (s = +1)", font_size = Small),
            MathTex(r"=", font_size = Small),
            Electron.copy(),
            MathTex(r"(s = \frac{1}{2})", font_size = Small),
        ).arrange(RIGHT, buff = 0.2)    
        PhotonExchange2 = VGroup(
            MathTex(r"\qquad \text{ or } \qquad", font_size = Small),
            Electron.copy(),
            MathTex(r"(s = +\frac{1}{2})", font_size = Small),
            MathTex(r"+", font_size = Small),
            Tex(r"photon (s = -1)", font_size = Small),
            MathTex(r"=", font_size = Small),
            Electron.copy(),
            MathTex(r"(s = -\frac{1}{2})", font_size = Small),
        ).arrange(RIGHT, buff = 0.2)   
        PhotonExchange = VGroup(PhotonExchange1, PhotonExchange2).arrange(DOWN).next_to(FermExample, DOWN)
        
        BosonExample = VGroup(
            Tex(r"Photons are spin-1 particles", font_size = Medium),
            Tex(r"($S = 1$, bosons)", font_size = Medium, color = YELLOW)
        ).arrange(RIGHT).to_edge(DOWN)
        
        
        
        
        
        
        #Animation Sequence
        self.play(Write(Equation[0]), run_time = 0.5)
        self.play(
            Create(SQNBox),
            Write(SQNLabel),
            GrowArrow(SQNArrow),
            run_time = 1
        )
        self.play(Write(Equation[1:4]))
        self.wait()
        self.play(Write(Magnitude))
        
        self.play(Equation.animate.to_edge(UP))
        
        self.play(Write(FermExample[0]))
        self.play(Write(FermExample[1:5]), run_time = 3)
        self.wait()
        
        self.play(Write(PhotonExchange1))
        self.wait()
        self.play(Write(PhotonExchange2))
        self.wait()
        
        self.play(Write(BosonExample))
        self.wait()
        
        self.play(FadeOut(*self.mobjects))
        
        
        
        
        
        
        
        
class Spin_3(Scene):
    def construct(self): 
        InherentlyProbabilistic = VGroup(
            Tex(r"Quantum Mechanics: {{inherently probabilistic}}", font_size = Medium),
            Tex(r"Probabilities contained in {{wavefunctions}}", font_size = Medium).set_color_by_tex("wavefunctions", YELLOW),
        ).arrange(DOWN).to_edge(UP)
        
        Wavefunction = MathTex(r"{{\ket{e} }} = {{\sqrt{\frac{3}{5}} }} \Ket{\frac{1}{2}} + {{\sqrt{\frac{2}{5}} }} \Ket{-\frac{1}{2}}")
        Wavefunction2 = MathTex(r"\implies {{\ket{e} }} = {{\sqrt{\frac{3}{5}} }} \begin{pmatrix}1\\0\end{pmatrix} + {{\sqrt{\frac{2}{5}} }} \begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}\sqrt{3/5}\\\sqrt{2/5}\end{pmatrix}").next_to(Wavefunction, DOWN)
        
        Highlights = VGroup(
            SurroundingRectangle(Wavefunction[0], YELLOW, stroke_width = 2),
            SurroundingRectangle(Wavefunction[2], YELLOW, stroke_width = 2),
            SurroundingRectangle(Wavefunction[4], YELLOW, stroke_width = 2),
            
        )
        
        AmpBrace = Brace(
                VGroup(Highlights[1], Highlights[2]),
                DOWN, color = YELLOW
        )
        
        Labels = VGroup(
            Tex(r"a \textit{ket}", font_size = Medium, color = YELLOW).next_to(Highlights[0], UP),
            Tex(r"probability amplitudes", font_size = Medium, color = YELLOW).next_to(AmpBrace, DOWN)
        )
        
        RightNote = Tex(r"Note: probability \\= (probability amplitude$)^2$", font_size = Small).to_edge(RIGHT)
        
        Probabilities = VGroup(
            Tex(r"Probability of measuring $\Ket{\frac{1}{2}}$ = $\frac{3}{5}$ = 60\%", font_size = Medium),
            Tex(r"Probability of measuring $\Ket{-\frac{1}{2}}$ = $\frac{2}{5}$ = 40\%", font_size = Medium),
        ).arrange(DOWN, aligned_edge = LEFT).to_edge(DOWN)
        
        Wait = Tex(r"Pause here and come back to this animation \\ after the moving vector animation is over", color = RED)
        
        
        
        
        #Animation Sequence
        self.play(Write(InherentlyProbabilistic[0]))
        self.wait(0.4)
        self.play(Write(InherentlyProbabilistic[1]))
        self.wait()
        
        self.play(Write(Wavefunction))
        self.wait()
        
        self.play(Create(Highlights[0]), Write(Labels[0]))
        self.wait()
        
        self.play(Create(Highlights[1:3]), Write(Labels[1]), DrawBorderThenFill(AmpBrace), run_time = 1)
        self.wait()
        
        
        for prob in Probabilities:
            self.play(Write(prob))
            self.wait(0.5)
        self.play(FadeIn(RightNote))
        self.wait()
        
        self.add(Wait)
        self.wait(4)
        self.remove(Wait)
        self.wait()
        
        self.play(
            FadeOut(Labels), FadeOut(Highlights), FadeOut(AmpBrace), FadeOut(Probabilities), FadeOut(RightNote)
        )
        self.play(Write(Wavefunction2), run_time = 2)
        self.wait(2)
        
        
        




class Spin_4(Scene):
    def construct(self): 
        p = ValueTracker(0.6)
        
        XNumber = DecimalNumber(p.get_value(), font_size = Small)               #Tracking numbers for x and y coordinate
        XNumber.add_updater(
            lambda x: x.set_value(p.get_value())
        )
        YNumber = DecimalNumber(1-p.get_value(), font_size = Small)
        YNumber.add_updater(
            lambda y: y.set_value(1-p.get_value())
        )
        
        ProbabilityTable = VGroup(                                              #Table of numbers
            MathTex(r"P \left(\frac{1}{2}\right) =", font_size = Small),
            MathTex(r"P \left(-\frac{1}{2}\right) =", font_size = Small),
            XNumber,
            YNumber
        ).arrange_in_grid(cols = 2, rows = 2, flow_order = 'dr', col_alignments = 'rr')
        
        ax = Axes(
            x_range=[0, 1, 0.2], 
            y_range=[0, 1, 0.2], 
            axis_config={"include_tip": False, "numbers_to_include": [1,1], "font_size": 24,},
            x_length=4, 
            y_length=4,
        )
        VGroup(ax, ProbabilityTable).arrange(RIGHT, buff = 2)
        labels = VGroup(
            ax.get_x_axis_label(
                MathTex(r"P(\frac{1}{2})").scale(0.6), edge=RIGHT,
            ),
            ax.get_y_axis_label(
                MathTex(r"P(-\frac{1}{2})").scale(0.6), edge=UP,
            )
        )
        
        State = Arrow(                                                          #Arrow vector of the ket state
            start = ax.get_origin(), 
            end = ax.c2p(p.get_value(), 1-p.get_value()),
            max_tip_length_to_length_ratio = 0.06,
            max_stroke_width_to_length_ratio = 1.0,
            buff = 0,
            color = YELLOW
        )
        State.add_updater(
            lambda t: t.become(
                Arrow(
                    start = ax.get_origin(), 
                    end = ax.c2p(p.get_value(), 1-p.get_value()),
                    max_tip_length_to_length_ratio = 0.06,
                    max_stroke_width_to_length_ratio = 1.0,
                    buff = 0,
                    color = YELLOW
                )
            )
        )
        
        TipLabel = VGroup(                                                      #Ket next to the vector
            Tex(r"(", font_size = Huge),
            VGroup(
                XNumber.copy(),
                YNumber.copy()
            ).arrange(DOWN),
            Tex(r")", font_size = Huge),
        ).arrange(RIGHT, buff = 0.08).next_to(State, UL/2) 
        TipLabel.add_updater(
            lambda k: k.next_to(State, UL/2) 
        )
        
        Footnote = Tex(r"""$\therefore$ Measuring $\ket{\frac{1}{2}}$ = $\begin{pmatrix}1\\0\end{pmatrix}$ 
        and measuring $\ket{-\frac{1}{2}}$ = $\begin{pmatrix}0\\1\end{pmatrix}$!""", font_size = Medium).to_edge(DOWN)
        

        #Animation Sequence
        self.add(ax, State)
        self.wait()
        self.play(Write(labels))
        self.wait()
        

        self.play(FadeIn(TipLabel), Write(ProbabilityTable), run_time = 1.5)
        self.wait()
        

        for val in [0.42, 0.75, 0.69, 1.0, 0.0, 0.35]:
            self.play(p.animate.set_value(val))
            self.wait(0.36)
            
        self.play(Write(Footnote[0]), run_time = 2)
        self.wait()
        
        
        
        
        
        
class Spin_5(Scene):
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
        AtomGroup.shift(3*LEFT)                                                    
        
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
        
        #Perspectives
        Perspectives = VGroup(
            Tex(r"Ways of looking at it:", font_size = Large),
            Tex(r"1. Two separate fermions", font_size = Small),
            Tex(r"2. One boson", font_size = Small),
            Tex(r"3. The \textbf{He} atom system", font_size = Small),
            Tex(r"Various perspectives reveal various facts!", font_size = Medium),
        ).arrange(DOWN, aligned_edge = LEFT).to_edge(RIGHT)
        
        PerspRects = VGroup(
            VGroup(
                SurroundingRectangle(electron1),
                SurroundingRectangle(electron2)
            ),
            SurroundingRectangle(
                VGroup(electron1, electron2), buff = 0.25
            ),
            SurroundingRectangle(AtomGroup, buff = 0.5)
        )
        
        #SpinTable
        SpinTable = MobjectTable(
            [[MathTex(r"\frac{1}{2}_A \frac{1}{2}_B"), MathTex(r"\frac{1}{2}_A -\frac{1}{2}_B")],
            [MathTex(r"-\frac{1}{2}_A \frac{1}{2}_B"), MathTex(r"-\frac{1}{2}_A -\frac{1}{2}_B")]],
            include_outer_lines = False,
            row_labels = [MathTex(r"\frac{1}{2}"), MathTex(r"-\frac{1}{2}")],
            col_labels = [MathTex(r"\frac{1}{2}"), MathTex(r"-\frac{1}{2}")],
            top_left_entry=MathTex(r"e_A \backslash e_B"),
            line_config = {'stroke_width': 1.4},
        ).scale(0.5).shift(3*RIGHT)
        
        #Footnote
        Foot = Tex(r"Want to assign a \textit{vector} to each of these outcomes: {{use \textbf{tensor product}!}}", font_size = Medium).to_edge(DOWN)
        Foot[1].set(color = YELLOW)
        
        
        #Animation Sequence
        self.play(GrowFromCenter(AtomGroup))
        self.play(FadeIn(chargeLabels))
        
        self.play(Write(Names))
        self.wait(2)
        
        self.play(Write(Perspectives[0]), run_time = 2)
        
        self.play(Create(PerspRects[0]), Write(Perspectives[1]), run_time = 1)
        self.play(FadeOut(PerspRects[0]))
        
        self.play(Create(PerspRects[1]), Write(Perspectives[2]), run_time = 1)
        self.play(FadeOut(PerspRects[1]))
        
        self.play(Create(PerspRects[2]), Write(Perspectives[3]), run_time = 1)
        self.play(FadeOut(PerspRects[2]))
        
        self.wait()
        self.play(Write(Perspectives[4]))
        self.wait(2)
        
        self.play(FadeOut(Perspectives))
        
        self.play(SpinTable.create())
        self.wait()
        
        self.play(Write(Foot[0]))
        self.wait(0.5)
        self.play(Write(Foot[1]))
        self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
        
        
class Spin_6(Scene):
    def construct(self): 
        Title6 = Tex(r"\textbf{Tensor product}: denoted by $\otimes$").to_edge(UP)
        
        Product1 = VGroup(
            MathTex(r"\Ket{\frac{1}{2}_A, \frac{1}{2}_B} = "),
            MathTex(r"\Ket{\frac{1}{2} }_A \otimes \Ket{\frac{1}{2} }_B = "), 
            MathTex(r"\begin{pmatrix}1\\0\end{pmatrix} \otimes \begin{pmatrix}1\\0\end{pmatrix} = "),
            MathTex(r"\begin{pmatrix} 1\begin{pmatrix}1\\0\end{pmatrix} \\ 0\begin{pmatrix}1\\0\end{pmatrix} \end{pmatrix} = "),
            MathTex(r"\begin{pmatrix} 1\\0\\0\\0 \end{pmatrix}"),
        ).arrange(RIGHT, buff = 0.2)
        
        Product2 = VGroup(
            MathTex(r"\Ket{\frac{1}{2}_A, -\frac{1}{2}_B} = "),
            MathTex(r"\Ket{\frac{1}{2} }_A \otimes \Ket{-\frac{1}{2} }_B = "), 
            MathTex(r"\begin{pmatrix}1\\0\end{pmatrix} \otimes \begin{pmatrix}0\\1\end{pmatrix} = "),
            MathTex(r"\begin{pmatrix} 1\begin{pmatrix}0\\1\end{pmatrix} \\ 0\begin{pmatrix}0\\1\end{pmatrix} \end{pmatrix} = "),
            MathTex(r"\begin{pmatrix} 0\\1\\0\\0 \end{pmatrix}"),
        ).arrange(RIGHT, buff = 0.2)
        
        Product3 = VGroup(
            MathTex(r"\Ket{-\frac{1}{2}_A, \frac{1}{2}_B} = "),
            MathTex(r"\Ket{-\frac{1}{2} }_A \otimes \Ket{\frac{1}{2} }_B = "), 
            MathTex(r"\begin{pmatrix}0\\1\end{pmatrix} \otimes \begin{pmatrix}1\\0\end{pmatrix} = "),
            MathTex(r"\begin{pmatrix} 0\begin{pmatrix}1\\0\end{pmatrix} \\ 1\begin{pmatrix}1\\0\end{pmatrix} \end{pmatrix} = "),
            MathTex(r"\begin{pmatrix} 0\\0\\1\\0 \end{pmatrix}"),
        ).arrange(RIGHT, buff = 0.2)
        
        Product4 = VGroup(
            MathTex(r"\Ket{-\frac{1}{2}_A, -\frac{1}{2}_B} = "),
            MathTex(r"\Ket{-\frac{1}{2} }_A \otimes \Ket{-\frac{1}{2} }_B = "), 
            MathTex(r"\begin{pmatrix}0\\1\end{pmatrix} \otimes \begin{pmatrix}0\\1\end{pmatrix} = "),
            MathTex(r"\begin{pmatrix} 0\begin{pmatrix}0\\1\end{pmatrix} \\ 1\begin{pmatrix}0\\1\end{pmatrix} \end{pmatrix} = "),
            MathTex(r"\begin{pmatrix} 0\\0\\0\\1 \end{pmatrix}"),
        ).arrange(RIGHT, buff = 0.2)
        
        ProductsTable = VGroup(
            Product1, Product2,
            Product3, Product4
           
        ).arrange_in_grid(flow_order = 'rd', buff = 1.2, col_alignments = 'rl').set(width = 0.96*FRAME_WIDTH)
        
        Footnote6 = Tex(r"Conveniently, each outcome is a \textit{basis (unit) vector}!", font_size = Medium).to_edge(DOWN)
        
        #Animation Sequence
        self.play(Write(Title6))
        self.wait()
        
        self.play(
            *[Write(prod[0]) for prod in ProductsTable],
            run_time = 2
        )
        self.play(
            *[Write(prod[1]) for prod in ProductsTable],
            run_time = 2
        )
        self.play(
            *[Write(prod[2]) for prod in ProductsTable],
            run_time = 2
        )
        self.play(
            *[Write(prod[3]) for prod in ProductsTable],
            run_time = 2
        )
        self.play(
            *[Write(prod[4]) for prod in ProductsTable],
            run_time = 2
        )
        
        self.wait()
        self.play(Write(Footnote6))
        self.wait()
        self.play(FadeOut(*self.mobjects))
        
        
        
        
class Spin_7(Scene):
    def construct(self): 
        Header = Tex(r"Now we can write the wavefunction of both electrons as a vector:", font_size = Large).to_edge(UP)
        Wavefunction = VGroup(
            MathTex(r"""
                \Ket{\psi} = c_1\Ket{\frac{1}{2}_A, \frac{1}{2}_B} + c_2\Ket{\frac{1}{2}_A, -\frac{1}{2}_B} + c_3\Ket{-\frac{1}{2}_A, \frac{1}{2}_B} + c_4\Ket{-\frac{1}{2}_A, -\frac{1}{2}_B} 
            """, font_size = Medium),
            VGroup(
                MathTex(r"""\implies \Ket{\psi}
                    = c_1\begin{pmatrix}1\\0\\0\\0 \end{pmatrix} + c_2\begin{pmatrix}0\\1\\0\\0 \end{pmatrix} + c_3\begin{pmatrix}0\\0\\1\\0 \end{pmatrix} + c_4\begin{pmatrix}0\\0\\0\\1 \end{pmatrix}
                """, font_size = Medium),
                MathTex(r"""
                    = \begin{pmatrix}c_1 \\ c_2 \\ c_3 \\ c_4 \end{pmatrix}
                """, font_size = Medium)
            ).arrange(RIGHT)
        ).arrange(DOWN, aligned_edge = LEFT)
        
        WavefunctionSmol = VGroup(
            MathTex(r"\Ket{\psi}", font_size = Medium),
            Wavefunction[1][1].copy()
        ).arrange(RIGHT, buff = 0.2).to_edge(UP)
        
        ToGetCoeffs = VGroup(
            Tex(r"To find these coefficients, we have to solve the {{Schr{\"o}dinger Equation}}.", font_size = Medium),
            MathTex(r"-i\hbar\frac{\partial}{\partial t}\Ket{\psi} = \left(\frac{\Hat{p}^2}{2m} + \Hat{V}\right) \Ket{\psi}", font_size = Small),
            Tex(r"...we won't do it; it's really difficult. Thankfully, we don't need to!", font_size = Small),
            Tex(r"The important bits are the \underline{coefficients}:", font_size = Medium)
        ).arrange(DOWN).next_to(WavefunctionSmol, DOWN)
        ToGetCoeffs[0][1].set_color(YELLOW)                                 #color the schrodinger equation bit
        
        CFunction = VGroup(
            MathTex(
            r"{{C(\Ket{e_A e_B})}} \xrightarrow{\text{difficult calculations} } \text{coefficient of the state} \Ket{e_A e_B}", font_size = Medium,
            ).set_color_by_tex("C(\Ket{e_A e_B})", YELLOW),
            MathTex(
            r"C\left(\Ket{\frac{1}{2}_A -\frac{1}{2}_B}\right) = \sqrt{\frac{1}{4}} \implies \text{25\% chance of measuring spin $\frac{1}{2}$ for A and $-\frac{1}{2}$ for B}", font_size = Small,
            )
        ).arrange(DOWN).next_to(ToGetCoeffs, 2*DOWN)
        #\text{25% chance of measuring spin $\frac{1}{2}$ for A and $-\frac{1}{2}$ for B}
        #Animation Sequence
        self.play(Write(Header))
        self.wait()
        
        self.play(Write(Wavefunction[0]), run_time = 3)
        self.wait(0.5)
        self.play(Write(Wavefunction[1][0]), run_time = 3)
        self.wait(0.5)
        self.play(Write(Wavefunction[1][1]))
        self.wait(1)
        
        self.play(
            FadeOut(Header), FadeOut(Wavefunction[0]), FadeOut(Wavefunction[1][0])
        )
        self.play(
            Write(WavefunctionSmol[0]),
            Wavefunction[1][1].animate.become(WavefunctionSmol[1]),
        )
        self.wait()
        
        for c in ToGetCoeffs:
            self.play(Write(c))
            self.wait(0.6)
        self.wait()
        
        self.play(Write(CFunction[0][0]))
        self.wait(0.5)
        self.play(Write(CFunction[0][1]), run_time = 2)
        self.wait(0.5)
        self.play(Write(CFunction[1]), run_time = 3)
        self.wait(1)
        
        
      







      
class Spin_2b(Scene):
    def construct(self):
    
        #Hydrogen Atom
        nucleonSize = 0.2
        a_orbit = 8*nucleonSize
        
        
        proton = Dot(radius=nucleonSize).set_color(RED)    
        orbit = Circle(color=WHITE, radius = a_orbit)   
        electron = Dot(color=BLUE, radius = nucleonSize/2).move_to(orbit.point_at_angle(2*PI/3))
        
        plus = MathTex(r"+", font_size = 24, stroke_width = 2).move_to(proton)
        minus = MathTex(r"-", font_size = 12, stroke_width = 2).move_to(electron)
        
        atom = VGroup(proton, orbit, electron, plus, minus)
        

        
        #Incoming photon arrow
        def PhotonArrow(mobj, object_side, s = 1):
            if s == -1:
                squiggleDown = MathTex(r"""
                \begin{tikzpicture} 
                    \begin{feynhand} 
                        \vertex (a) at (-1, 0); \vertex (b) at (1, 0); 
                        \propag [photon, mom = {$\gamma$ \text{(spin -1)} }] (a) to (b); 
                    \end{feynhand} 
                \end{tikzpicture}""", color = YELLOW, fill_opacity=0, stroke_width=1.2, font_size = Small).next_to(mobj,object_side)
                return(squiggleDown)

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
        
        #Spin labels on the particles
        electronSpinLabels = VGroup(
            MathTex(r"-\frac{1}{2}"), MathTex(r"+\frac{1}{2}")
        )
        
        for lbl in [*electronSpinLabels]:                #make labels smol
            lbl.set(font_size = Small)
            
        electronSpinLabels.next_to(electron, UP)                          #move them to the resp. particles
        

        
        #Animation Sequence 
        self.play(GrowFromCenter(atom))                                     #introduce atom, electron, proton                            

        self.play(
            FadeIn(electronSpinLabels[0])
        )
        self.wait()
        
        IncomingPhotonAnim(PhotonArrow(electron, LEFT), RIGHT)                  #send in a photon
        self.play(                                                          #change the highlight rectangle and spin labels                 
            TransformFromCopy(electronSpinLabels[0], electronSpinLabels[1]),
        )
        self.wait()
        
        
        IncomingPhotonAnim(PhotonArrow(electron, LEFT, s = -1), RIGHT)                  #send in a photon 
        self.remove(electronSpinLabels[1])
        self.play(                                                          #change the highlight rectangle and spin labels                 
            Transform(electronSpinLabels[1], electronSpinLabels[0]),
        )
        self.wait()
        