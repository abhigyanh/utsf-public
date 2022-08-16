from manim import *
from utsf_common import *
config.max_files_cached = 1000

def DipoleMagneticField(v, M):
    B = 3*rHat(v)*np.dot(rHat(v),M) - M
    return(B)



class SU3_1(Scene):
    def construct(self):
        SU3Headline = Tex(r"SU(3) Symmetry Group", color = YELLOW)
        self.play(Write(SU3Headline))
        self.wait()
        self.remove(SU3Headline)
        
        QuiteCool = VGroup(
            Tex(r"Pauli's exclusion principle $\rightarrow$ a new property: color charge", font_size = Medium),
            Tex(r"Color cancels out far away $\rightarrow$ color charges similar to visual color", font_size = Medium),
            Tex(r"Still a problem: magnetism", font_size = Large)
        ).arrange(DOWN)
        
        for c in QuiteCool:
            self.play(Write(c))
            self.wait(0.5)






class SU3_2(Scene):
    def construct(self):
        M_neutron = 1*UP
        M_magnet = 1*RIGHT
        
        texts = VGroup(
                        Tex(r"Magnetic fields").to_edge(UP),
                      )
        
        
        
        
        
        #magnetic field lines graphic of neutron
        neutronField = lambda v: DipoleMagneticField(v, M_neutron)
        neutronLines = StreamLines(
            neutronField, x_range=[-2, 2, 0.4], y_range=[-2, 2, 0.2], padding = 0.1, colors = [WHITE, PINK, BLUE, WHITE]
        )
        neutronRect = SurroundingRectangle(neutronLines, buff = 0, stroke_width = 1, color = WHITE)
        neutronLabel = Tex(r"Neutron", font_size = Medium).next_to(neutronRect, DOWN)
        
        neutronDot = Circle(color = WHITE, radius = 0.2, fill_opacity = 1)
        neutronN = Tex(r"n", font_size = Tiny, color = BLACK).move_to(neutronDot)
        
        neutronGraphic = VGroup(neutronLines, neutronLabel, neutronRect, neutronDot, neutronN)
        
        
        
        
        
        
        
        #magnetic field lines graphic of bar magnet
        barSize = 0.25
        barField = lambda v: DipoleMagneticField(v, M_magnet)
        barLines = StreamLines(
            barField, x_range=[-2, 2, 0.1], y_range=[-2, 2, 0.5], padding = 0.1, #colors = [WHITE, PINK, WHITE, ORANGE],
            min_color_scheme_value = 0.1, max_color_scheme_value = 2
        )
        
        barRect = SurroundingRectangle(barLines, buff = 0, stroke_width = 1, color = WHITE)
        barLabel = Tex(r"Bar magnet", font_size = Medium).next_to(barRect, DOWN)
        
        barMagnet = VGroup(
                            Rectangle(width = barSize*1.4, height = barSize, color = WHITE, fill_opacity = 1),
                            Rectangle(width = barSize*1.4, height = barSize, color = BLACK, fill_opacity = 1)
                          ).arrange(RIGHT, buff = 0.02)
        barMagnetPoles = VGroup(
                                    Tex(r"N", font_size = Tiny, color = BLACK). move_to(barMagnet[0].get_center()),
                                    Tex(r"S", font_size = Tiny). move_to(barMagnet[1].get_center()),
                               )
        barGraphic = VGroup(barLines, barRect, barLabel, barMagnet, barMagnetPoles)
        
        
        
        #keep the two graphics beside the other
        VGroup(neutronGraphic, barGraphic).arrange(RIGHT, buff = 2)
        
        
        #bottom text
        bottomText = VGroup(
                            Tex(r"Reason: Quantum Electrodynamics; we can't go into the details yet...", font_size = Small),
                            Tex(r"but it has to do with the photon being charge neutral", font_size = Small)
        ).to_edge(DOWN)
        
        
        
        
        #ANIMATION SEQUENCE
        self.play(Write(texts[0]))
        
        self.play(
                    Write(barLabel),
                    Write(neutronLabel),
        )
        self.play(
                    Create(barRect),
                    Create(neutronRect),
        )
        self.wait()
        
        self.play(
                    neutronLines.create(),
                    barLines.create(),
                    run_time = 1
        )
        self.play(
                    DrawBorderThenFill(barMagnet),
                    DrawBorderThenFill(neutronDot),
                    Write(barMagnetPoles),
                    Write(neutronN),
        )
        
        self.wait()
        
        self.play(Write(bottomText[0]), run_time = 2)
        self.wait(2)
        self.play(FadeOut(bottomText[0]))
        self.play(Write(bottomText[1]), run_time = 2)
        self.wait()
        
        self.play(FadeOut(*self.mobjects))
        
        
        
        
        
        
        
        
        
class SU3_3(Scene):
    def construct(self):

        #EM Feynman Diagram
        EMTikz = MathTex(r"""
                    \begin{tikzpicture}
                     \begin{feynhand}
                        \vertex[] (v1) at (0,0.5);   \vertex[above left=of v1] (f1) {$e^-$};     \vertex[above right=of v1] (f2) {$e^-$};
                        \propag [fermion] (f1) to (v1);     \propag [fermion] (v1) to (f2);
                        \vertex[] (v2) at (0,-0.5);    \vertex[below left=of v2] (f3) {$p$};     \vertex[below right=of v2] (f4) {$p$};
                        \propag [photon] (v1) to [edge label' = $\gamma$] (v2);
                        \propag [fermion] (f3) to (v2);     \propag [fermion] (v2) to (f4);
                     \end{feynhand}
                    \end{tikzpicture}
                 """, color = WHITE, fill_opacity=0.25, stroke_width=2).scale(TikzScaleFactor)
        PhotonArrw = Arrow(1.6*LEFT, 0.2*LEFT, color = YELLOW)
        PhotonLbl = Tex(r"Photon \\ (neutral)", color = YELLOW, font_size = Small).next_to(PhotonArrw, LEFT)
        EMLbl = Tex(r"EM Interaction", font_size = Medium).next_to(EMTikz, DOWN)
        EMDiagram = VGroup(
            PhotonArrw, PhotonLbl, EMLbl, EMTikz,
        )
        
        
        
        #Strong Feynman Diagram
        StrTikz = MathTex(r"""
                    \begin{tikzpicture}
                     \begin{feynhand}
                        \vertex[] (v1) at (0,0.5);   \vertex[above left=of v1] (f1) {$u$};     \vertex[above right=of v1] (f2) {$u$};
                        \propag [fermion] (f1) to (v1);     \propag [fermion] (v1) to (f2);
                        \vertex[] (v2) at (0,-0.5);    \vertex[below left=of v2] (f3) {$d$};     \vertex[below right=of v2] (f4) {$d$};
                        \propag [gluon] (v1) to [edge label = $g$] (v2);
                        \propag [fermion] (f3) to (v2);     \propag [fermion] (v2) to (f4);
                     \end{feynhand}
                    \end{tikzpicture}
                 """, color = WHITE, fill_opacity=0.25, stroke_width=2).scale(TikzScaleFactor)
        GluonArrw = Arrow(1.6*RIGHT, 0.2*RIGHT, color = YELLOW)
        GluonLbl = Tex(r"Gluon \\ {{(color?)}}", color = YELLOW, font_size = Small).next_to(GluonArrw, RIGHT)
        GluonLbl2 = Tex(r"Gluon \\ {{(colored!)}}", color = YELLOW, font_size = Small).move_to(GluonLbl)
        StrLbl = Tex(r"Strong Interaction", font_size = Medium).next_to(StrTikz, DOWN)
        StrDiagram = VGroup(
            GluonArrw, GluonLbl, GluonLbl2, StrLbl, StrTikz,
        )
        VGroup(EMDiagram, StrDiagram).arrange(RIGHT, buff = 2)
        
        
        
        #Text stuff with gluon color etc
        GluonTexts = VGroup(
            Tex(r"If gluons were color neutral, we'd see \textit{'Strong magnetism'}, {{but we don't.}}", font_size = Small), 
        ).to_edge(DOWN)
        
        
        
        #Animation Sequence
        self.play(Write(EMTikz), Write(StrTikz))
        self.wait()
        
        self.play(Write(EMLbl), run_time = 1)
        self.play(
            GrowArrow(PhotonArrw), Write(PhotonLbl)
        )
        
        self.wait()
        
        self.play(Write(StrLbl), run_time = 1)
        self.play(
            GrowArrow(GluonArrw), Write(GluonLbl[0])
        )
        
        self.wait()
        self.play(Write(GluonLbl[1]))
        
        self.wait()
        
        self.play(Write(GluonTexts[0][0]))
        self.wait()
        self.play(Write(GluonTexts[0][1]))
        self.wait()
        
        self.play(FadeOut(GluonTexts))
        self.play(ReplacementTransform(GluonLbl, GluonLbl2))
        self.wait()
        













class SU3_4(Scene):
    def construct(self):
        #header text
        header = Tex(r"What color are gluons?", font_size = Large).to_edge(UP)
        
        #Reference Legend
        Legend = VGroup(
            #Tex(r"Legend:", font_size = Tiny),
            Tex(r"""
            photons = 
            \begin{tikzpicture} 
                \begin{feynhand} 
                    \vertex (a) at (-0.5, 0); \vertex (b) at (0.5, 0); 
                    \propag [photon] (a) to (b); 
                \end{feynhand} 
            \end{tikzpicture}
            \\ gluons = 
            \begin{tikzpicture} 
                \begin{feynhand} 
                    \vertex (a) at (-0.5, 0); \vertex (b) at (0.5, 0); 
                    \propag [gluon] (a) to (b); 
                \end{feynhand} 
            \end{tikzpicture}
            """, color = WHITE, fill_opacity=0, stroke_width=1, font_size = Tiny),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UP+LEFT)
        
        
        
        #Color Exchange Feynman Diagram
        GreenTikz = MathTex(r"""
                    \begin{tikzpicture}
                     \begin{feynhand}
                        \vertex[] (v1) at (0,0.5);   \vertex[above left=of v1] (f1) {$u_g$};
                        \propag [fermion] (f1) to (v1);
                        \vertex[] (v2) at (0,-0.5);     \vertex[below right=of v2] (f4) {$u_g$};
                        \propag [gluon] (v1) to (v2);
                        \propag [fermion] (v2) to (f4);
                     \end{feynhand}
                    \end{tikzpicture}
                    """, color = WHITE, fill_opacity=0.1, stroke_width=1.5)

        BlueTikz = MathTex(r"""
                    \begin{tikzpicture}
                     \begin{feynhand}
                        \vertex[] (v1) at (0,0.5);   \vertex[above right=of v1] (f2) {$u_b$};
                        \propag [fermion] (v1) to (f2);
                        \vertex[] (v2) at (0,-0.5);     \vertex[below left=of v2] (f3) {$u_b$};
                        \propag [gluon] (v1) to (v2);
                        \propag [fermion] (f3) to (v2);
                     \end{feynhand}
                    \end{tikzpicture}
                    """, color = WHITE, fill_opacity=0.1, stroke_width=1.5)
        ColorExchangeTikz = VGroup(GreenTikz, BlueTikz)
        
        
        GreenAntiBlueTikz = MathTex(r"""
                    \begin{tikzpicture}
                     \begin{feynhand}
                        \vertex[] (v1) at (0,0.5);   \vertex[above left=of v1] (f1) {$u_g$};    \vertex[above right=of v1] (f2) {$u_b$};
                        \propag [fermion] (f1) to (v1);     \propag [fermion] (v1) to (f2);
                        \vertex[] (v2) at (0,-0.5);   \vertex[below left=of v2] (f3) {$u_b$};   \vertex[below right=of v2] (f4) {$u_{b+g-b=g}$};
                        \propag [gluon, mom = $g-b$] (v1) to (v2);
                        \propag [fermion] (f3) to (v2);     \propag [fermion] (v2) to (f4);
                     \end{feynhand}
                    \end{tikzpicture}
                    """, color = WHITE, fill_opacity=0.1, stroke_width=1.5).align_to(ColorExchangeTikz, LEFT)
                    
        BlueAntiGreenTikz = MathTex(r"""
                    \begin{tikzpicture}
                     \begin{feynhand}
                        \vertex[] (v1) at (0,0.5);   \vertex[above left=of v1] (f1) {$u_g$};    \vertex[above right=of v1] (f2) {$u_{g+b-g=b}$};
                        \propag [fermion] (f1) to (v1);     \propag [fermion] (v1) to (f2);
                        \vertex[] (v2) at (0,-0.5);   \vertex[below left=of v2] (f3) {$u_b$};   \vertex[below right=of v2] (f4) {$u_{g}$};
                        \propag [gluon, revmom = $b-g$] (v1) to (v2);
                        \propag [fermion] (f3) to (v2);     \propag [fermion] (v2) to (f4);
                     \end{feynhand}
                    \end{tikzpicture}
                    """, color = WHITE, fill_opacity=0.1, stroke_width=1.5).align_to(ColorExchangeTikz, LEFT)
            
        VGroup(GreenTikz, BlueTikz, GreenAntiBlueTikz, BlueAntiGreenTikz).scale(TikzScaleFactor)           #resize all the feynman diagrams 
        
        
        ColorAntiColorTikz = VGroup(
            GreenAntiBlueTikz.copy(), 
            Tex(r"or,"),
            BlueAntiGreenTikz,
        ).arrange(RIGHT, buff = 1)
        
        



        #Footer Text
        footer1 = Tex(r"Two gluons... {{or, one gluon carrying \underline{two} colors!}}", font_size = Small).to_edge(DOWN)
        footer2 = Tex(r"Remember: \\ colorless quarks/gluons not \\ allowed, no strong magnetism!", font_size = 14).to_edge(RIGHT)
        footer3 = Tex(r"How do we know which one it is?", font_size = Medium).to_edge(DOWN)



        #Animation Sequence
        self.play(Write(ColorExchangeTikz))
        self.play(FadeIn(Legend), run_time = 1)
        self.play(Write(header))
        
        self.wait()
        
        self.play(ShowPassingFlash(GreenTikz.copy().set_color(PURE_GREEN), time_width = 0.5), run_time = 2)
        self.wait()
        
        self.play(FadeIn(footer2), run_time = 0.5)
        self.wait()
        self.play(FadeOut(footer2), run_time = 0.5)
        
        self.play(ShowPassingFlash(BlueTikz.copy().set_color(PURE_BLUE), time_width = 0.5), run_time = 2)
        self.wait()
        
        self.play(Write(footer1[0]))
        self.wait()
        self.play(Write(footer1[1]))
        self.wait(2)
        
        
        self.play(
            FadeOut(ColorExchangeTikz), FadeIn(GreenAntiBlueTikz), run_time = 2
        )
        
        self.wait(2)
        
        self.play(FadeOut(footer1), FadeOut(header), FadeOut(Legend))                              #clean up all the extra
        self.play(
            ReplacementTransform(GreenAntiBlueTikz, ColorAntiColorTikz[0]), 
        )
        self.play(Write(ColorAntiColorTikz[1]))
        self.play(Write(BlueAntiGreenTikz), run_time = 1)
        self.play(Write(footer3))
        self.wait(2)
        
        
        self.add(ImageMobject("images\SU3\ThatsTheFunPartYouDont.png"))
        self.wait(2)
        







class SU3_5(Scene):
    def construct(self):
        GluonCases = VGroup(
                Tex(r"= green ({{$g$}}) and anti-blue ({{$\Bar{b}$}})"),
                Tex(r"= blue ({{$b$}}) and anti-green ({{$\Bar{g}$}})")
        ).arrange(DOWN, aligned_edge = LEFT)
        for t in GluonCases:
            t.set(font_size = Medium)
            ColorMathTexColours(t)
            
        GluonLinComb = Tex(r"$\frac{1}{ \sqrt{2} }$ ({{$g$}}{{$\Bar{b}$}} + {{$b$}}{{$\Bar{g}$}})").align_to(GluonCases, LEFT)
        ColorMathTexColours(GluonLinComb)
        
        Kangaroo = VGroup(
            Tex(r"gluon"),
            Brace(GluonCases, LEFT),
            GluonCases,
            Tex(r"="),
            GluonLinComb
        ).arrange(RIGHT)
        
        Mouse = VGroup(
            Tex(r"How many different combinations?", font_size = Large),
            Tex(r"i.e, How many \textbf{linearly independent} superpositions?", font_size = Small),
        ).arrange(DOWN).to_edge(UP)
        
        footnote = Tex(r"""
            The $\frac{1}{\sqrt{2}}$ factor in front is a \textit{normalization}. 
            In short, it means that the gluon is equally likely to be $g\Bar{b}$ or $b\Bar{g}$, but no other color-anticolor combo.
        """, font_size = Tiny).to_edge(DOWN)
        
        #Animation Sequence
        self.play(Write(Kangaroo[0]))
        for case in GluonCases: 
            self.play(Write(case), run_time = 1)
            self.wait()
        
        self.play(Write(Kangaroo[1]))
        
        self.wait()
        
        self.play(
        Write(Kangaroo[3]), Write(Kangaroo[4], run_time = 2)
        )
        self.play(FadeIn(footnote), run_time = 1)
        
        self.wait()
        
        for tex in Mouse:
            self.play(Write(tex))
            self.wait()
        
        
        
        
        
        
        
        
        
        
        
        
class SU3_4b(Scene):
    def construct(self):
        feynhand = TexTemplate(post_doc_commands = r"""
            \newcommand{\feynhand}[1]{
                \begin{tikzpicture}
                    \begin{feynhand}
                    #1
                    \end{feynhand}
                \end{tikzpicture}
            }
        """)
        #header text
        header = Tex(r"What color are gluons?", font_size = Large).to_edge(UP)
        
        #Reference Legend
        Legend = VGroup(
            #Tex(r"Legend:", font_size = Tiny),
            Tex(r"""
            photons = 
            \feynhand{
                    \vertex (a) at (-0.5, 0); \vertex (b) at (0.5, 0); 
                    \propag [photon] (a) to (b); 
            }
            \\ gluons = 
            \feynhand{ 
                    \vertex (a) at (-0.5, 0); \vertex (b) at (0.5, 0); 
                    \propag [gluon] (a) to (b); 
            }
            """, color = WHITE, fill_opacity=0, stroke_width=1, font_size = Tiny, tex_template = feynhand),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UP+LEFT)
        
        
        
        #Color Exchange Feynman Diagram
        u1 = MathTex(r"""
            \feynhand{
                \vertex (a) at (0,0.5); \vertex[above left=of a] (u1) {$u_g$};
                \propagator[fermion] (u1) to (a);
            }
        """, color = GREEN, fill_opacity=0.1, stroke_width=1.5, tex_template = feynhand)
        u3 = MathTex(r"""
            \feynhand{
                \vertex (a) at (0,0.5); \vertex[above right=of a] (u3) {$u$};
                \propagator[fermion] (a) to (u3);
            }
        """, color = WHITE, fill_opacity=0.1, stroke_width=1.5, tex_template = feynhand)
        u2 = MathTex(r"""
            \feynhand{
                \vertex (b) at (0,-0.5); \vertex[below left=of b] (u2) {$u_b$};
                \propagator[fermion] (u2) to (b);
            }
        """, color = BLUE, fill_opacity=0.1, stroke_width=1.5, tex_template = feynhand)
        u4 = MathTex(r"""
            \feynhand{
                \vertex (b) at (0,-0.5); \vertex[below right=of b] (u4) {$u$};
                \propagator[fermion] (b) to (u4);
            }
        """, color = WHITE, fill_opacity=0.1, stroke_width=1.5, tex_template = feynhand)
        
        gluonGreen = MathTex(r"""
            \feynhand{
                \vertex (a) at (0,0.5); \vertex (b) at (0,-0.5);
                \propagator[gluon, mom'={$g$}] (a) to [half right, looseness=1.5] (b);
            }
        """, color = GREEN, fill_opacity=0, stroke_width=1.2, tex_template = feynhand)
        gluonBlue = MathTex(r"""
            \feynhand{
                \vertex (a) at (0,0.5); \vertex (b) at (0,-0.5);
                \propagator[gluon, mom'={$b$}] (b) to [half right, looseness=1.5] (a);
            }
        """, color = BLUE_D, fill_opacity=0, stroke_width=1.2, tex_template = feynhand)
        
        SampleTikz = VGroup(
            VGroup(u1, u3).arrange(RIGHT, aligned_edge = DOWN, buff = 0),
            VGroup(gluonGreen, gluonBlue).arrange(RIGHT, aligned_edge = DOWN, buff = 0),
            VGroup(u2, u4).arrange(RIGHT, aligned_edge = UP, buff = 0),
        ).arrange(DOWN, buff = 0).scale(TikzScaleFactor)
        SampleTikz[1].shift([0.045, 0,0])
        
        GroupOfUps = VGroup(u1, u2, u3, u4)
        
        
        gluonSingle = MathTex(r"""
            \feynhand{
                \vertex (a) at (0,0.5); \vertex (b) at (0,-0.5);
                \propagator[gluon, mom={$g\Bar{b}$}] (a) to (b);
            }
        """, color = WHITE, fill_opacity=0, stroke_width=1.2, tex_template = feynhand).scale(0.82).align_to(gluonBlue, UL).shift([-0.045, 0,0])
        u3B = MathTex(r"""
            \feynhand{
                \vertex (a) at (0,0.5); \vertex[above right=of a] (u3) {$u_b$};
                \propagator[fermion] (a) to (u3);
            }
        """, color = BLUE_D, fill_opacity=0.1, stroke_width=1.5, tex_template = feynhand).scale(TikzScaleFactor).align_to(u3, DL)
        u4G = MathTex(r"""
            \feynhand{
                \vertex (b) at (0,-0.5); \vertex[below right=of b] (u4) {$u_g$};
                \propagator[fermion] (b) to (u4);
            }
        """, color = GREEN, fill_opacity=0.1, stroke_width=1.5, tex_template = feynhand).scale(TikzScaleFactor).align_to(u4, UL)
        gluonSingle2 = MathTex(r"""
            \feynhand{
                \vertex (a) at (0,0.5); \vertex (b) at (0,-0.5);
                \propagator[gluon, mom={$b\Bar{g}$}] (b) to (a);
            }
        """, color = WHITE, fill_opacity=0, stroke_width=1.2, tex_template = feynhand).scale(0.82).align_to(gluonGreen, UR).shift([0.045, 0,0])
        
            
        Diagram1 = VGroup(
            u1, u2, u3B, u4G, gluonSingle,
        )
        
        Diagram2 = VGroup(
            *[x.copy() for x in [u1, u2, u3B, u4G]], gluonSingle2
        )

        #Footer Text
        footer1 = Tex(r"Two gluons... {{or, one gluon carrying \underline{two} colors!}}", font_size = Small).to_edge(DOWN)
        footer2 = Tex(r"Remember: \\ colorless quarks/gluons not \\ allowed, no strong magnetism!", font_size = 14).to_edge(RIGHT)
        footer3 = Tex(r"How do we know which one it is?", font_size = Medium).to_edge(DOWN)

        #ArrowsColorDirection   
        g_anti_b = VGroup(
            Arrow(LEFT, RIGHT),
            MathTex(r"{{g}} - ({{g}} - {{b}}) = {{b}}")
        ).arrange(UP, buff = 0.2).scale(TikzScaleFactor).next_to(SampleTikz, UP)
        
        b_anti_g = VGroup(
            Arrow(LEFT, RIGHT),
            MathTex(r"{{b}} + ({{g}} - {{b}}) = {{g}}")
        ).arrange(DOWN, buff = 0.2).scale(TikzScaleFactor).next_to(SampleTikz, DOWN)
        
        ColorTransferArrows = VGroup(g_anti_b, b_anti_g)
        
        
        


        #Animation Sequence
        self.play(FadeIn(Legend), run_time = 1)
        self.play(Write(header))   
        self.wait()
      
        self.play(Write(GroupOfUps), FadeOut(header))
        self.play(FadeIn(footer2), run_time = 0.5)
        self.wait()
        
        self.play(Write(gluonGreen))
        self.play(ReplacementTransform(u4, u4G))
        self.wait()
        
        self.play(Write(gluonBlue))
        self.play(ReplacementTransform(u3, u3B))
        self.wait()
        
        self.play(ReplacementTransform(SampleTikz[1], gluonSingle))
        self.play(Write(footer1))
        self.wait()
        self.play(FadeOut(footer1))
        self.wait()
        
        for arrow in ColorTransferArrows:
            ColorTexColours(arrow[1])
            self.play(GrowArrow(arrow[0]))
            self.play(Write(arrow[1]))
            self.wait()
            self.play(FadeOut(arrow))
        self.wait()
        
        self.play(
            FadeIn(Diagram2),
            VGroup(
                Diagram1, Diagram2
            ).animate.arrange(RIGHT, buff = 2),
        )
        
        self.play(Write(footer3))
        self.wait(2)
        
        
        self.add(ImageMobject("images\SU3\ThatsTheFunPartYouDont.png"))
        self.wait(2)