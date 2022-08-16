from manim import *
import numpy as np
config.max_files_cached = 1000

CYAN = rgb_to_color([0,1,1])
MAGENTA = rgb_to_color([1,0,1])

from utsf_common import *




    
    

class ColorNeutral1(Scene):
    def construct(self):
        #on screen texts 1
        Texts1 = VGroup()                                                    #TEXTS IN THE FIRST SLIDE  
        Texts1.add(Tex(
                        r"Ask question: \\ How does the \textit{nucleus} stay together?", font_size = Medium
                       )
                   )
        Texts1.add(Tex(
                        r"Introduce {{strong}} force", font_size = Medium
                       )
                   )
        Texts1.add(Tex(
                        r"Color cycle \\ and antisymmetry", font_size = Medium
                        )
                   )
        Texts1.add(Tex(
                        r"Find color charge", font_size = Medium
                       )
                   )
        Texts1.arrange_in_grid(rows = 2, cols = 2, flow_order='rd', buff = 3)
        
        
        Arrows1 = VGroup()
        Arrows1.add(Arrow(                                                  #UL > UR
                            start = Texts1[0].get_edge_center(RIGHT), 
                            end = Texts1[1].get_edge_center(LEFT),
                            max_stroke_width_to_length_ratio = 2,
                            max_tip_length_to_length_ratio=0.1,
                         )
                   )
        Arrows1.add(Arrow(                                                  #UR > DR
                            start = Texts1[1].get_edge_center(DOWN), 
                            end = Texts1[3].get_edge_center(UP),
                            max_stroke_width_to_length_ratio = 2,
                            max_tip_length_to_length_ratio=0.1,
                         )
                   )
        Arrows1.add(Arrow(                                                  #DR > DL
                            start = Texts1[3].get_edge_center(LEFT), 
                            end = Texts1[2].get_edge_center(RIGHT),
                            max_stroke_width_to_length_ratio = 2,
                            max_tip_length_to_length_ratio=0.1,
                         )
                   )
        Arrows1.add(Arrow(                                                  #DL > UL
                            start = Texts1[2].get_edge_center(UP), 
                            end = Texts1[0].get_edge_center(DOWN),
                            max_stroke_width_to_length_ratio = 2,
                            max_tip_length_to_length_ratio=0.1,
                            color = YELLOW
                         )
                   )
        


        #ANIMATION SEQUENCE 
        self.play(Write(Texts1[0]))
        self.play(Write(Texts1[1]), GrowArrow(Arrows1[0]), run_time = 0.6)
        self.play(Write(Texts1[3]), GrowArrow(Arrows1[1]), run_time = 0.6)
        self.play(Write(Texts1[2]), GrowArrow(Arrows1[2]), run_time = 0.6)
        self.wait()
        self.play(GrowArrow(Arrows1[3]))
        self.wait()
        self.play(FadeOut(*self.mobjects))















class ColorNeutral2(Scene):
    def construct(self):
        #ON SCREEN TEXTS 2 
        Texts2 = VGroup()                                                       #screen 2 texts
        Texts2.add(Tex(
                        r"Electric charges \\ (+,-)"
                       )
                  )
        Texts2.add(MathTex(
                        r"\xleftrightarrow[]{\text{interacts} }"
                       )
                  )
        Texts2.add(Tex(
                        r"Electromagnetic \\ fields"
                       )
                  )
        Texts2.add(Tex(
                        r"Color `charges' \\ ({{r}},{{g}},{{b}})"
                       )
                  )
        ColorTexColours(Texts2[3])
        Texts2.add(MathTex(
                        r"\xleftrightarrow[]{\text{interacts} }"
                       )
                  )
        Texts2.add(Tex(
                        r"Strong \\ fields"
                       )
                  )
        Texts2.arrange_in_grid(rows = 2, cols = 3, buff = 1, flow_order='rd')


        #ANIMATION SEQUENCE
        for i in [0,1,2]:
            self.play(
                        Write(Texts2[i]),
                        Write(Texts2[i+3]),
                        
                     )
            
        self.wait()
        self.play(FadeOut(*self.mobjects))












class ColorNeutral3(Scene):
    def construct(self):
        #SCREEN 3 STUFF
        Texts3 = VGroup()                                                      #screen 3 texts
        Texts3.add(Tex(
                        r"$\therefore$ colored quarks"
                        )
                    )
        Texts3.add(MathTex(
                        r"\xRightarrow[\text{strong force}]{ \text{quark-quark attraction} }"
                        )
                    )
        Texts3.add(Tex(
                        r"protons, neutrons \\ bound together", font_size = Large
                        )
                    )
        Texts3.arrange_in_grid(rows = 1, cols = 3, buff = 0.5, flow_order='rd').to_edge(UP)

        Image3Quark = ImageMobject("images\ColorNeutral\RGB.png").set(height = 5).next_to(Texts3, DOWN)
        


        #ANIMATION SEQUENCE
        
        self.play(Write(Texts3[0]))
        self.play(GrowFromEdge(Texts3[1], LEFT))
        self.play(GrowFromCenter(Image3Quark))
        self.wait()
        self.play(Write(Texts3[2]))
        self.wait()
        self.play(FadeOut(*self.mobjects))
        
        
        
        
        
        
        
        
        
        
class ColorNeutral4(Scene):
    def construct(self):
        Texts4 = VGroup(
            Tex(r"...wait", font_size = Large),
            Tex(r"Strong force: strong, interacts with {{protons}} and {{neutrons}}", font_size = Medium).set_color_by_tex("protons", YELLOW).set_color_by_tex("neutrons", YELLOW),
            Tex(r"Shouldn't we see it {{everywhere}}?", font_size = Large).set_color_by_tex("everywhere", YELLOW),
        ).arrange(DOWN)
        
        
        #ANIMATION SEQUENCE
        for i in range(len(Texts4)):
            self.play(Write(Texts4[i]), run_time = 0.5+i)
            self.wait()
        self.wait()
        self.play(FadeOut(*self.mobjects))
        
        
        
        
        
        
        
        
        
        
        
        
        
class ColorNeutral5(Scene):
    def construct(self):
        IMGHeight = 3.5
        EMFlowChart = Group(
            Tex(r"Electromagnetism:", font_size = Small),
            ImageMobject("images\ColorNeutral\Atom.png").set(height = IMGHeight),
            Arrow(LEFT/2, RIGHT/2),
            ImageMobject("images\ColorNeutral\DNA.png").set(height = IMGHeight),
            Arrow(LEFT/2, RIGHT/2),
            ImageMobject("images\ColorNeutral\Fetus.png").set(height = IMGHeight),
        ).arrange(RIGHT, buff = 0.2)
        
        GravFlowChart = Group(
            Tex(r"Gravity:", font_size = Small),
            ImageMobject("images\ColorNeutral\SolSystem.png").set(height = IMGHeight),
            Arrow(LEFT/2, RIGHT/2),
            ImageMobject("images\ColorNeutral\Galaxy.jpg").set(height = IMGHeight),
        ).arrange(RIGHT, buff = 0.2).to_edge(LEFT)
        
        Group(EMFlowChart, GravFlowChart).arrange(DOWN)
        
        
        
        
        
        #ANIMATION SEQUENCE
        self.play(Write(EMFlowChart[0]), run_time = 1)
        self.play(GrowFromCenter(EMFlowChart[1]), run_time = 1)
        self.play(
            GrowArrow(EMFlowChart[2]),
            GrowFromCenter(EMFlowChart[3])
        )
        self.play(
            GrowArrow(EMFlowChart[4]),
            GrowFromCenter(EMFlowChart[5])
        )
        
        self.wait(1)
        
        self.play(Write(GravFlowChart[0]), run_time = 1)
        self.play(GrowFromCenter(GravFlowChart[1]), run_time = 1)
        self.play(
            GrowArrow(GravFlowChart[2]),
            GrowFromCenter(GravFlowChart[3])
        )
        
        self.wait()
        self.play(FadeOut(*self.mobjects))
        
        








class ColorNeutral6(Scene):
    def construct(self):
        IMGHeight = 3.5
        StrFlowChart = Group(
            Tex(r"Strong force:", font_size = Medium),
            ImageMobject(r'images\ColorNeutral\Nucleus.png').set(height = IMGHeight),
            
            Arrow(LEFT, RIGHT),
            Tex(r"?", font_size = 100),
        ).arrange(RIGHT, buff = 0.2)
        

        
        #ANIMATION SEQUENCE
        self.play(Write(StrFlowChart[0]), run_time = 1)
        self.play(GrowFromCenter(StrFlowChart[1]), run_time = 1)
        self.play(
            GrowArrow(StrFlowChart[2]),
            GrowFromCenter(StrFlowChart[3])
        )
        
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        
        
        
        
        
        
        
        
        
        
class ColorNeutral7(Scene):
    def construct(self):
        FormulasQuestionMark = Tex(r"Force Law?").to_edge(UP)
        
        EMBlock = VGroup(
            Tex(r"Electromagnetism", font_size = Medium),
            MathTex(r"F(r) = k\frac{q_1 q_2}{r^2}", font_size = Medium)
        ).arrange(DOWN)
        
        GravBlock = VGroup(
            Tex(r"Gravity", font_size = Medium),
            MathTex(r"F(r) = -G\frac{m_1 m_2}{r^2}", font_size = Medium)
        ).arrange(DOWN)
        
        StrongBlock = VGroup(
            Tex(r"Strong force:", font_size = Medium),
            MathTex(r"F(r) = \frac{\alpha}{r^2} + \sigma", font_size = Medium),
        ).arrange(DOWN)
                
        
        UpBlocks = VGroup(EMBlock, GravBlock).arrange(RIGHT, buff = 3).shift(UP)
        StrongBlock.next_to(UpBlocks, 2*DOWN)
        
        FormulaBlocks = VGroup(EMBlock, GravBlock, StrongBlock)
        StrongCaption = Tex(r"(comes from the \textbf{Cornell potential}, but it's rarely used)", font_size = Tiny).next_to(StrongBlock, DOWN)
        
        #Animation Sequence
        self.play(Write(FormulasQuestionMark))
        self.wait()
        
        for blc in FormulaBlocks:
            self.play(Write(blc), run_time = 2)
            self.wait(0.5)
        self.play(Write(StrongCaption))
        self.wait()
        self.play(FadeOut(*self.mobjects))
        
        
        
        
        
        
class ColorNeutral8(Scene):
    def construct(self):
        def rHat(v):
            r = v[0]*RIGHT + v[1]*UP
            Hat = r/np.linalg.norm(r)
            return(Hat) 
        def EFieldPointCharge(r, r0, q):
            if np.linalg.norm(r-r0) == 0:
                return(100000*(r-r0))
            rho = np.linalg.norm(r - r0)
            field = rHat(r-r0)*q/(rho)**2 
            return(field)
            
        UpQuark = VGroup(
            Circle(radius = 0.5, color = PURPLE, fill_opacity = 1),
            Tex(r"up \\ $\frac{2}{3} e$", font_size = Tiny)
        )
        DownQuark = VGroup(
            Circle(radius = 0.5, color = PURPLE, fill_opacity = 1),
            Tex(r"down \\ $-\frac{1}{3} e$", font_size = Tiny)
        )
        
        CalledNeutron = Tex(r"Neutron: (udd)", font_size = Large).to_edge(UP)
        NeutronCirc = Circle(radius = 3, color = WHITE, stroke_width = 2)
        
        func = lambda pos: EFieldPointCharge(pos, UP, 2) + EFieldPointCharge(pos, DL, -1) + EFieldPointCharge(pos, DR, -1)
        electric_field = ArrowVectorField(
            func, 
        )
        
        TheQuarks = VGroup(
            UpQuark.copy().move_to(UP),
            DownQuark.copy().move_to(DL),
            DownQuark.copy().move_to(DR),
        )
        
        NoNetCharge = Tex(r"Net charge = 0, \\ no electric attraction", font_size = Medium)
        
        AceFlag = ImageMobject(r"images\ColorNeutral\AceFlag.png").set(width = 3).to_edge(RIGHT)
        
        Maybe = VGroup(
            Tex(r"Maybe three color charges behave similarly?", font_size = Medium),
            Tex(r"They attract at short distances but cancel out farther away, making protons and neutrons color-less.", font_size = Small)
        ).arrange(DOWN).to_edge(DOWN)
        
        #Animation Sequence
        self.play(Write(CalledNeutron), Create(NeutronCirc))
        self.play(
            DrawBorderThenFill(TheQuarks, run_time = 2),
            DrawBorderThenFill(electric_field, run_time = 1),
        )
        self.add(TheQuarks)
        self.wait(2)
        self.play(
            #*[thing.animate.scale(0.6) for thing in [NeutronCirc, TheQuarks, electric_field]],
            *[thing.animate.shift(UP).scale(0.6) for thing in [NeutronCirc, TheQuarks, electric_field]],
            FadeOut(electric_field)
        )
        
        NoNetCharge.next_to(NeutronCirc, DOWN)
        self.play(Write(NoNetCharge))
        self.play(FadeIn(AceFlag), rate_func = there_and_back_with_pause, run_time = 3)
        for m in Maybe:
            self.play(Write(m))
            self.wait(0.5)
        self.wait()
        self.play(FadeOut(*self.mobjects))
        
        
        
        
        
        
class ColorNeutral9(Scene):
    def construct(self):
        SimpleEquation = VGroup(
            Tex(r"This idea has a simple equation:"),
            MathTex(r"{{r}}+{{g}}+{{b}} = 0"),
            Tex(r"But that also means...", font_size = Medium),
            VGroup(
                MathTex(r"{{g}} = -{{r}} -{{b}}", font_size = Medium),
                MathTex(r"{{r}} = -{{g}} -{{b}}", font_size = Medium),
                MathTex(r"{{b}} = -{{r}} -{{g}}", font_size = Medium),
            ).arrange(RIGHT, buff = 2),
            Tex(r"Sounds weird...", font_size = Small),
            Tex(r"What even is a 'negative color'?")
        ).arrange(DOWN)
        ColorTexColours(SimpleEquation[1])
        for e in SimpleEquation[3]:
            ColorTexColours(e)
        
        
        self.play(Write(SimpleEquation[0]))
        self.play(Write(SimpleEquation[1]))
        self.wait()
        self.play(Write(SimpleEquation[2]))
        self.wait()
        self.play(Write(SimpleEquation[3][1]))
        self.play(*[FadeIn(SimpleEquation[3][j]) for j in [0,2]])
        self.wait()
        self.play(Write(SimpleEquation[4]))
        self.wait()
        self.play(Write(SimpleEquation[5]))
        self.wait()
        self.play(FadeOut(*self.mobjects))
        
        
        
        
class ColorNeutral10(Scene):
    def construct(self):
        JustLike = Tex(r"Just like $+$ or $-$ \textbf{electric} charges, \\ there are $+$ or $-$ \textbf{color} charges!", font_size = Large).to_edge(UP)
        
        Quark = Circle(radius = 0.4, fill_opacity = 1)
        Red = VGroup(
            Quark.copy().set(color = RED),
            MathTex("r")
        ).shift(UP)
        Green = VGroup(
            Quark.copy().set(color = GREEN),
            MathTex("g")
        ).shift(DL)
        Blue = VGroup(
            Quark.copy().set(color = PURE_BLUE),
            MathTex("b")
        ).shift(DR)
        
        QuarkBlock = VGroup(Red, Green, Blue)
        
        AntiRed = VGroup(
            Quark.copy().set(color = CYAN),
            MathTex(r"\Bar{r}")
        ).shift(UP)
        AntiGreen = VGroup(
            Quark.copy().set(color = MAGENTA),
            MathTex(r"\Bar{g}")
        ).shift(DL)
        AntiBlue = VGroup(
            Quark.copy().set(color = YELLOW_D),
            MathTex(r"\Bar{b}")
        ).shift(DR)
        
        AntiQuarkBlock = VGroup(AntiRed, AntiGreen, AntiBlue)
        QuarkAntiQuarkBlocks = VGroup(QuarkBlock, AntiQuarkBlock).arrange(RIGHT, buff = 2)
        
        Names = VGroup(
            Tex("quarks"),
            Tex("anti-quarks")
        )
        Captions = VGroup(
            Tex("Positive color charges", font_size = Small),
            Tex("Negative color charges", font_size = Small),
        )
        for i in [0,1]:
            Names[i].next_to(QuarkAntiQuarkBlocks[i], UP)
            Captions[i].next_to(QuarkAntiQuarkBlocks[i], DOWN)
        
        AndOfCourse = VGroup(
            Tex(r"Of course,"),
            MathTex(r"{{ \Bar{r} }} + {{ \Bar{g} }} + {{ \Bar{b} }} = 0")
        ).arrange(DOWN).to_edge(DOWN)
        ColorTexColours(AndOfCourse[1])
        
        SmolExample = MathTex(r"= - {{r}} = {{g}} + {{b}}", font_size = Small).next_to(AntiRed, RIGHT)
        ColorTexColours(SmolExample)
        
        IfThisMakesSense = Tex(r"If this makes sense to you,\\ you're probably a photographer \\ or graphic designer.", font_size = Tiny).to_edge(LEFT)
        
        
        #Animation Sequence
        #self.add(JustLike, QuarkBlock, AntiQuarkBlock, Captions)
        self.play(Write(JustLike), run_time = 3)
        self.wait()
        for i in [0,1]:
            self.play(
                Write(Names[i]),
                DrawBorderThenFill(QuarkAntiQuarkBlocks[i]),
                Write(Captions[i])
            )
        
        self.play(Write(AndOfCourse))
        self.wait(0.5)
        self.play(Write(SmolExample))
        self.wait()
        self.play(Write(IfThisMakesSense))
        self.wait()
        self.play(FadeOut(*self.mobjects))