from manim import *
config.max_files_cached = 1000
from utsf_common import *
                    
                    
                    
                    
                    
                    
class RGBSys1(Scene):
    def construct(self):
        RGBColSpace = Tex(r"The RGB Color System", font_size = Huge, color = YELLOW)
        self.play(Write(RGBColSpace))
        self.wait()
        self.remove(RGBColSpace)
        

        RGBMeans = VGroup(
            Tex(r"{{R}}{{G}}{{B}} stands for {{Red}}-{{Green}}-{{Blue}}", font_size = Large),
            Tex(r"The system used to display colour in screens!", font_size = Small)
        ).arrange(DOWN)
        for r in [0,4]:
            RGBMeans[0][r].set(color = RED) 
        for g in [1,6]:
            RGBMeans[0][g].set(color = GREEN) 
        for b in [2,8]:
            RGBMeans[0][b].set(color = BLUE_D) 
              
              
              
        #LED pixel arrangement
        r = ValueTracker(25)
        g = ValueTracker(100)
        b = ValueTracker(251)
        Trackers = Group(r, g, b)
        
        Pixel = VGroup(
            Rectangle(height = 1, width = 1, stroke_color = WHITE, fill_opacity = 1, color = rgb_to_color([r.get_value()/255, g.get_value()/255, b.get_value()/255])),
            Tex(r"Pixel"),
            Tex(r"(one LED of each color type)", font_size = Tiny),
        ).arrange(DOWN)
        
        RedLED = Rectangle(height = 2, width = 2/3, color = PURE_RED, stroke_color = PURE_RED, fill_opacity = r.get_value()/255)
        GreenLED = Rectangle(height = 2, width = 2/3, color = PURE_GREEN, stroke_color = PURE_GREEN, fill_opacity = g.get_value()/255)
        BlueLED = Rectangle(height = 2, width = 2/3, color = PURE_BLUE, stroke_color = PURE_BLUE, fill_opacity = b.get_value()/255)
        
        SeparateLEDs = VGroup(RedLED, GreenLED, BlueLED).arrange(RIGHT, buff = 0.1)
        LEDBrace = Brace(SeparateLEDs, LEFT, sharpness = 1)
        
        DisplayArrangement = VGroup(Pixel, LEDBrace, SeparateLEDs).arrange(RIGHT, buff = 0.5)
        
        ColorMeters = VGroup(
            DecimalNumber(r.get_value(), num_decimal_places=0, font_size = Small, color = PURE_RED),
            DecimalNumber(g.get_value(), num_decimal_places=0, font_size = Small, color = PURE_GREEN),
            DecimalNumber(b.get_value(), num_decimal_places=0, font_size = Small, color = PURE_BLUE),
        )
        for i in range(len(ColorMeters)):
            ColorMeters[i].next_to(SeparateLEDs[i], UP)
        
        
        #Add all updaters
        RedLED.add_updater(
            lambda t: t.become(
                Rectangle(height = 2, width = 2/3, color = PURE_RED, stroke_color = PURE_RED, fill_opacity = r.get_value()/255).move_to(RedLED)
            )
        )
        GreenLED.add_updater(
            lambda t: t.become(
                Rectangle(height = 2, width = 2/3, color = PURE_GREEN, stroke_color = PURE_GREEN, fill_opacity = g.get_value()/255).move_to(GreenLED)
            )
        )
        BlueLED.add_updater(
            lambda t: t.become(
                Rectangle(height = 2, width = 2/3, color = PURE_BLUE, stroke_color = PURE_BLUE, fill_opacity = b.get_value()/255).move_to(BlueLED)
            )
        )
        ColorMeters[0].add_updater(
            lambda u: u.set_value(r.get_value()).next_to(RedLED, UP)
        )
        ColorMeters[1].add_updater(
            lambda u: u.set_value(g.get_value()).next_to(GreenLED, UP)
        )
        ColorMeters[2].add_updater(
            lambda u: u.set_value(b.get_value()).next_to(BlueLED, UP)
        )
        Pixel[0].add_updater(
            lambda h: h.set_color(color = rgb_to_color([r.get_value()/255, g.get_value()/255, b.get_value()/255]))
        )
        
        
        
        
        #Animation Sequence
        self.play(Write(RGBMeans[0]))
        self.wait(0.5)
        self.play(Write(RGBMeans[1]))
        self.wait()
        self.play(FadeOut(RGBMeans))
        
        self.add(r, g, b)
        self.play(DrawBorderThenFill(Pixel))
        self.play(Write(LEDBrace))
        self.play(
            *[FadeIn(led.copy()) for led in SeparateLEDs], 
            FadeIn(ColorMeters),
        )

        
        self.wait()
        self.play(
            r.animate.set_value(200),
            g.animate.set_value(69), 
            b.animate.set_value(144), 
            run_time = 1,
            rate_func = linear,
        )
        self.play(
            r.animate.set_value(65),
            g.animate.set_value(199), 
            b.animate.set_value(242), 
            run_time = 1,
            rate_func = linear,
        )
        self.wait()
        self.play(
            r.animate.set_value(255),
            g.animate.set_value(255), 
            b.animate.set_value(255), 
            run_time = 1
        )
        self.wait()
        self.play(
            r.animate.set_value(255),
            g.animate.set_value(255), 
            b.animate.set_value(0), 
            run_time = 2
        )
        
        
class RGBSys2(Scene):
    def construct(self):
        ThreeCones = ImageMobject(r"images/RGBSys/ThreeCones.jpg").set(width = FRAME_WIDTH/3)
        ConeSpectralResponse = ImageMobject(r"images/RGBSys/ConeSpectralResponse.png").set(width = FRAME_WIDTH/3)
        
        Images = Group(ThreeCones, ConeSpectralResponse).arrange(RIGHT, buff = 1)
        self.play(FadeIn(ThreeCones))
        self.wait()
        self.play(FadeIn(ConeSpectralResponse))
        self.wait()
        self.play(FadeOut(*self.mobjects))
        
        
        
        
        
        
class RGBSys3(Scene):
    def construct(self):
        RGBVec = Tex(r"{{R}}{{G}}{{B}} colors: {{vectors}}").to_edge(UP)
        RGBVec[0].set(color = RED)
        RGBVec[1].set(color = GREEN)
        RGBVec[2].set(color = BLUE_D)
        
        WhiteVec = MathTex(r"\text{white} = \begin{pmatrix}255\\255\\255\end{pmatrix}", font_size = Medium)
        YellowVec = MathTex(r"{{\text{yellow}}} = \begin{pmatrix}255\\255\\0\end{pmatrix}", font_size = Medium).set_color_by_tex(r"yellow", YELLOW)
        WhiteAndYellow = VGroup(
            WhiteVec, Tex(r"and", font_size = Medium), YellowVec
        ).arrange(RIGHT).next_to(RGBVec, DOWN)
        
        
        WaitASec = Tex(r"wait a second...", font_size = Small).next_to(WhiteAndYellow, DOWN)
        
        YellowIsMinusBlue = VGroup(
            VGroup(#blue
                Tex(r"b", color = BLUE_D),
                MathTex(r"\begin{pmatrix}0\\0\\255\end{pmatrix}")
            ).arrange(DOWN),
            MathTex(r"+"),
            VGroup(#yellow
                Tex(r"y", color = YELLOW),
                MathTex(r"\begin{pmatrix}255\\255\\0\end{pmatrix}")
            ).arrange(DOWN), 
            MathTex(r"="),
            VGroup(#white
                Tex(r"w", color = WHITE),
                MathTex(r"\begin{pmatrix}255\\255\\255\end{pmatrix}")
            ).arrange(DOWN), 
            Tex(r"$\implies$ $\cancelto{0}{\text{w}}$ - {{b}} = {{y}} =").set_color_by_tex('y', YELLOW).set_color_by_tex('b', BLUE_D),
            VGroup(#red
                Tex(r"r", color = RED),
                MathTex(r"\begin{pmatrix}255\\0\\0\end{pmatrix}")
            ).arrange(DOWN), 
            MathTex(r"+"),
            VGroup(#green
                Tex(r"g", color = GREEN),
                MathTex(r"\begin{pmatrix}0\\255\\0\end{pmatrix}")
            ).arrange(DOWN), 
        ).arrange(RIGHT, buff = 0.2).scale(0.8)
        
        CyanIsMinusRed = VGroup(
            Tex(r"-{{r}} = {{c}} =").set_color_by_tex('c', rgb_to_color([0,1,1])).set_color_by_tex('r', RED),
            VGroup(#red
                Tex(r"g", color = GREEN),
                MathTex(r"\begin{pmatrix}0\\255\\0\end{pmatrix}")
            ).arrange(DOWN), 
            MathTex(r"+"),
            VGroup(#green
                Tex(r"b", color = BLUE_D),
                MathTex(r"\begin{pmatrix}0\\0\\255\end{pmatrix}")
            ).arrange(DOWN), 
        ).arrange(RIGHT, buff = 0.2).scale(0.52)
        
        MagentaIsMinusGreen = VGroup(
            Tex(r"-{{g}} = {{m}} =").set_color_by_tex('m', rgb_to_color([1,0,1])).set_color_by_tex('g', GREEN),
            VGroup(#red
                Tex(r"r", color = RED),
                MathTex(r"\begin{pmatrix}255\\0\\0\end{pmatrix}")
            ).arrange(DOWN), 
            MathTex(r"+"),
            VGroup(#green
                Tex(r"b", color = BLUE_D),
                MathTex(r"\begin{pmatrix}0\\0\\255\end{pmatrix}")
            ).arrange(DOWN), 
        ).arrange(RIGHT, buff = 0.2).scale(0.52)
        
        VGroup(CyanIsMinusRed, MagentaIsMinusGreen).arrange(RIGHT, buff = 4).next_to(YellowIsMinusBlue, DOWN)
        
        IdenticalMaths = Tex(r"RGB color mathematics $\equiv$ Strong force 'color' mathematics!", font_size = Large).to_edge(DOWN)
        
        
        #Animation Sequence
        self.play(*[Write(RGBVec[i]) for i in range(4)])
        self.wait(0.5)
        self.play(Write(RGBVec[4]))
        self.wait()
        
        
        for wy in WhiteAndYellow:
            self.play(Write(wy))
        self.wait()
        self.play(Write(WaitASec))
        self.wait()
        
        
        self.play(Write(YellowIsMinusBlue[0]))
        self.wait()
        self.play(*[Write(YellowIsMinusBlue[i]) for i in [1,2]], run_time = 1)
        self.play(*[Write(YellowIsMinusBlue[i]) for i in [3,4]], run_time = 1)
        self.wait()
        self.play(*[Write(YellowIsMinusBlue[i]) for i in [5]], run_time = 1)
        self.play(*[Write(YellowIsMinusBlue[i]) for i in [6,7,8]], run_time = 1)
        
        self.wait()
        self.play(YellowIsMinusBlue.animate.scale(0.65))
        self.play(Write(CyanIsMinusRed))
        
        self.wait()
        self.play(Write(MagentaIsMinusGreen))
        
        self.wait()
        self.play(Write(IdenticalMaths))
        
        self.wait()
        self.play(FadeOut(*self.mobjects))