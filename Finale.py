from manim import *
config.max_files_cached = 1000
from utsf_common import *


class Finale1(Scene):
    def construct(self):
        NotACoincidence = VGroup(
            Tex(r"{{SU(3)}} here, not a coincidence!").set_color_by_tex("SU(3)", YELLOW),
            Tex(r"Symmetries in nature {{$\rightarrow$}} Properties of the Strong Force")
        ).arrange(DOWN)
        
        
        #Animation Sequence
        self.play(Write(NotACoincidence[0]), run_time = 1)
        self.wait()
        
        for x in NotACoincidence[1]:
            self.play(Write(x), run_time = 1)
        self.wait()
        
        self.play(FadeOut(*self.mobjects))
        
        
class Finale2(Scene):
    def construct(self):
        Header = VGroup(
            Tex(r"Group theory:"),
            Tex(r"{{SU(3)}} has 8 independent parameters, so 8 gluons", font_size = Large).set_color_by_tex("SU(3)", YELLOW),
        ).arrange(DOWN).to_edge(UP)
        
        #Left side box
        LeftTable = VGroup(
            MathTex(r"{{r}} + {{g}} + {{b}} = 0"),
            MathTex(r"{{ \Bar{r} }} + {{ \Bar{g} }} + {{ \Bar{b} }} = 0"),
            MathTex(r".", fill_opacity = 0, stroke_width = 0, color = BLACK),
            MathTex(r"{{r}} + {{ \Bar{r} }} = 0"),
            MathTex(r"{{g}} + {{ \Bar{g} }} = 0"),
            MathTex(r"{{b}} + {{ \Bar{b} }} = 0"),
        ).arrange_in_grid(flow_order = 'dr', cols = 2, rows = 3)
        for eq in LeftTable:
            ColorTexColours(eq)
            eq.set(font_size = Medium)
            
        SixColors = MathTex(r"{{r}}, {{ \Bar{r} }}, {{g}}, {{ \Bar{g} }}, {{b}}, {{ \Bar{b} }}", font_size = Large).next_to(LeftTable, UP)
        ColorTexColours(SixColors)
        
        LeftCaption = Tex(r"6 color charges that are \\ cyclic and antisymmetric", font_size = Small).next_to(LeftTable, DOWN)
        
        LeftBox = VGroup(LeftTable, SixColors, LeftCaption).to_edge(LEFT)
        
        
        #Right side box
        HiddenRight = Tex(r"Replay animation of the gluon octet cycling", font_size = Tiny)
        RightSurrounding = Rectangle(width = FRAME_WIDTH/2, color = WHITE, height = FRAME_WIDTH/2*9/16)
        RightBox = VGroup(HiddenRight, RightSurrounding).to_edge(RIGHT)
        
        
        
        
        
        #Animation Sequence
        self.add(Header, RightBox)
        
        self.play(Write(SixColors))
        self.wait()
        self.play(Write(LeftCaption))
        
        for eq in LeftTable:
            self.play(FadeIn(eq), run_time = 0.5)
            
        self.wait()
        
        
        
        
        
        
class Finale3(Scene):
    def construct(self):
      
        #Left side box
        HiddenLeft = Tex(r"Replay animation of the three 'singlet + triplet' groups", font_size = Tiny)
        LeftSurrounding = Rectangle(width = FRAME_WIDTH/2, color = WHITE, height = FRAME_WIDTH/2*9/16)
        LeftBox = VGroup(HiddenLeft, LeftSurrounding).to_edge(LEFT)
                
        
        #Right side stuff
        color_SU3 = BLUE_D
        color_SU2 = GREEN_B
        
        SU3Sphere = Circle(radius = 2, color = color_SU3, fill_opacity = 0.25)
        SU3Label = Tex(r"SU(3)", color = color_SU3).next_to(SU3Sphere, UP)
        
        SU2SphereDummy = Circle(radius = 0.6, color = color_SU2, fill_opacity = 0.5)
        SU2LabelDummy = Tex(r"SU(2)", font_size = Tiny, color = color_SU2)
        SU2Sphere = VGroup(SU2LabelDummy, SU2SphereDummy)
        SU2Spheres = VGroup(
            SU2Sphere.copy().shift(UR/2),
            SU2Sphere.copy().shift(UL/2),
            SU2Sphere.copy().shift(DOWN/3),
        )

        others = Tex(r"and other subgroups", font_size = Tiny).next_to(SU2Spheres[2], DOWN)
        
        RightCaption = Tex(r"(just a heuristic image, the reality \\ is \textit{much} more complicated)", font_size = Tiny).next_to(SU3Sphere, DOWN)
        
        
        RightSide = VGroup(SU2Spheres, SU3Sphere, SU3Label, others, RightCaption).to_edge(RIGHT)
        
        
        #Animation Sequence
        self.add(LeftBox)
        
        self.play(GrowFromCenter(SU3Sphere))
        self.play(Write(SU3Label))
        self.wait()
        
        for su2 in SU2Spheres:
            self.play(GrowFromCenter(su2), run_time = 0.5)
            
        self.play(Write(others), run_time = 1)
        self.wait()
        
        self.play(Write(RightCaption))
        self.wait()











class Finale4(Scene):
    def construct(self):
        #Left side
        LeftDiagram = ImageMobject(r"images/Finale/RGB.png").set(height = FRAME_HEIGHT/3)
        LeftBorder = SurroundingRectangle(LeftDiagram)
        LeftCaption = VGroup(
            Tex(r"Strong Force", font_size = Large),
            Tex(r"(3 color charges)", font_size = Medium),
        ).arrange(DOWN).next_to(LeftBorder, DOWN)
        
        LeftSide = Group(LeftDiagram, LeftCaption)
        
        
        #Right side
        RightDiagram = ImageMobject(r"images/Finale/ThreeCones.jpg").set(height = FRAME_HEIGHT/3)
        RightBorder = SurroundingRectangle(RightDiagram)
        RightCaption = VGroup(
            Tex(r"RGB Color System", font_size = Large),
            Tex(r"(3 human eye color receptors)", font_size = Small),
        ).arrange(DOWN).next_to(RightBorder, DOWN)
        
        RightSide = Group(RightDiagram, RightCaption)
        
        
        
        
        Group(LeftSide, RightSide).arrange(RIGHT, buff = 4).to_edge(UP)
        BraceTwo = Brace(Group(LeftSide, RightSide), direction = DOWN, sharpness = 1.0)
        
        Punchline = VGroup(
            Tex(r"\underline{SU(3)}", color = YELLOW),
            Tex(r"Similar math!", font_size = Large)
        ).arrange(DOWN).next_to(BraceTwo, DOWN)
        
        ItWasSU3Barry = ImageMobject(r"images/Finale/ItWasSU3Barry.png").set(height = FRAME_HEIGHT/2)
        
        
        #Animation Sequence
        self.play(
            GrowFromCenter(LeftDiagram), 
            FadeIn(RightDiagram),
            )
        self.play(
            Write(LeftCaption),
            Write(RightCaption)
        )
        self.play(
            GrowFromCenter(BraceTwo), run_time = 1
        )
        self.wait()
        self.play(
            Write(Punchline)
        )
        self.wait()
        
        self.play(GrowFromCenter(ItWasSU3Barry), run_time = 4, rate_func = linear)
        self.wait(1)
        
        
        
        
        
        
        
class Finale5(Scene):
    def construct(self):
        SU3Unmasked = ImageMobject(r"images/Finale/SU3Unmasked.png").set(height = FRAME_HEIGHT/3).to_edge(UP)
        
        Mindblowing = Tex(r"Mathematical symmetries $\rightarrow$ {{forces in nature!}}", font_size = Medium).next_to(SU3Unmasked, DOWN)
        ForcesBrace = Brace(Mindblowing[1], DOWN)
        
        ForcesAndSymmetries = VGroup(
            Tex(r"Strong force", font_size = Medium),
            Tex(r"Electromagnetism", font_size = Medium),
            Tex(r"Weak force", font_size = Medium),
            Tex(r"SU(3)", color = YELLOW),
            Tex(r"U(1)", color = YELLOW),
            Tex(r"SU(2)", color = YELLOW),
        ).arrange_in_grid(flow_order = 'dr', cols = 2, rows = 3).next_to(ForcesBrace, DOWN)
        
        CantTalkAboutGravity = Tex(r"We can't talk about gravity...", font_size = Tiny).to_edge(DOWN)
        
        
        
        
        #Animation Sequence
        self.add(SU3Unmasked)
        
        self.play(Write(Mindblowing), run_time = 2)
        self.wait()
        
        self.play(GrowFromCenter(ForcesBrace), run_time = 0.5)
        self.play(Write(ForcesAndSymmetries), run_time = 3)
        self.wait()
        
        self.play(FadeIn(CantTalkAboutGravity))
        self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
        
        
        
        
        
        
        
        
        
class Finale6(Scene):
    def construct(self):
        SMGroup = MathTex(r"\text{Standard Model: }  {{SU(3)}} \otimes {{SU(2)}} \otimes {{U(1)}}")
        SU3Box = SurroundingRectangle(SMGroup[1], stroke_width = 2)
        SU2Box = SurroundingRectangle(SMGroup[3], stroke_width = 2)
        U1Box = SurroundingRectangle(SMGroup[5], stroke_width = 2)
        GroupBoxes = VGroup(SU3Box, SU2Box, U1Box)
        
        LabelArrows = VGroup(
            Arrow(start = SU3Box.get_top(), end = SU3Box.get_top()+UP, color = YELLOW, buff = 0.5),
            Arrow(start = SU2Box.get_bottom(), end = SU2Box.get_bottom()+DOWN, color = YELLOW, buff = 0.5),
            Arrow(start = U1Box.get_top(), end = U1Box.get_top()+UR/1.41, color = YELLOW, buff = 0.5),
        )
        
        Labels = VGroup(
            Tex(r"Strong force"),
            Tex(r"Weak force"),
            Tex(r"Electromagnetism")
        )
        for i in range(len(Labels)):
            Labels[i].set(font_size = Small, color = YELLOW)
            Labels[i].move_to(LabelArrows[i].get_end())
        
        #SM Lagrangian Mug
        SMLagrangianMugImg = ImageMobject(r"images/Finale/SMLagrangianMug.jpg")
        SMLagrangianMugCaption = Tex(r"A simplified version of the Standard Model Lagrangian (Image: CERN)", font_size = Small).next_to(SMLagrangianMugImg, DOWN)
        SMLagrangianMug = Group(SMLagrangianMugImg, SMLagrangianMugCaption).to_edge(DOWN)
        
        

        
        
        #Animation Group
        self.play(Write(SMGroup))
        self.play(
            Create(SU3Box),
            Write(Labels[0])
        )
        self.play(
            Create(SU2Box),
            Write(Labels[1])
        )
        self.play(
            Create(U1Box),
            Write(Labels[2])
        )
        self.wait()
        
        self.play(
            VGroup(SMGroup, GroupBoxes, Labels).animate.to_edge(UP)
        )    
        
        self.play(FadeIn(SMLagrangianMugImg))
        self.play(Write(SMLagrangianMugCaption))
        self.wait(4)
        self.play(FadeOut(*self.mobjects))
        
        
        
        
        
        
        
class Finale7(Scene):
    def construct(self):
        ThankYou = Tex(r"Thank you for watching!")
        
        Credits = Tex(r"Credits", font_size = Medium)
        CreditsTable = Table(
                            [["Writing, Scripting, Narration", "Fernando Franco Félix"],
                            ["Animations, Editing", "Abhigyan Hazarika"]],
                            line_config={"stroke_width": 0, "color": WHITE},
                            
                            ).set_column_colors(GREY, WHITE).set(height = FRAME_HEIGHT/6)
                            
        CreditScene = VGroup(ThankYou, Credits, CreditsTable).arrange(DOWN)
        
        #Animation Sequence
        self.play(Write(ThankYou))
        self.wait(4)
        
        self.play(Write(Credits))
        self.play(FadeIn(CreditsTable), run_time = 1)
        self.wait(2)