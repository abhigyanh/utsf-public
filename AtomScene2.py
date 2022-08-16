from manim import *
config.max_files_cached = 1000
from utsf_common import *


class AtomScene2(Scene):
    def construct(self):
    
        #ATOM SCHEMATIC DIAGRAM: 2E, 2P, 2N 
        nucleonSize = 0.14
        
        #the nucleus
        proton1 = Dot(radius=nucleonSize).set_color(RED)                                                 
        neutron1 = Dot(radius=nucleonSize).next_to(proton1,RIGHT,buff=0).set_color(WHITE)
        neutron2 = Dot(radius=nucleonSize).next_to(proton1,DOWN,buff=0)
        proton2 = Dot(radius=nucleonSize).next_to(neutron1,DOWN,buff=0).set_color(RED)
        
        nucleus = VGroup(proton1,neutron1,proton2,neutron2)
        
        #orbit
        a_orbit = 10*nucleus.width
        orbit = Circle(color=WHITE).surround(nucleus).scale(a_orbit)
        
        #electrons on orbit
        electronBuffer = -0.014
        electron1 = Dot(color=BLUE).next_to(orbit, UP*a_orbit, buff=electronBuffer)
        electron2 = Dot(color=BLUE).next_to(orbit, DOWN*a_orbit, buff=electronBuffer)
        
        #VGroup of orbit, nucleus and electronx2
        AtomGroup = VGroup(orbit,electron1,electron2,nucleus)
        AtomGroup.to_edge(UP)                                                     
        
        #self.add(AtomGroup)
        
        
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
        
        #self.add(chargeLabels)
        
        
       
        
        #force vectors
        vecEIn1 = Arrow(start = electron1.get_center(), end = electron1.get_center()+DOWN)
        vecEIn2 = Arrow(start = electron2.get_center(), end = electron2.get_center()+UP)
        
        vecEOut1 = Arrow(start = proton1.get_center(), end = proton1.get_center()+LEFT/2+UP)
        vecEOut2 = Arrow(start = proton2.get_center(), end = proton2.get_center()+RIGHT/2+DOWN)
        
        vecG1 = Arrow(start = nucleus.get_center()+LEFT, end = nucleus.get_center()).scale(0.6)
        vecG2 = Arrow(start = nucleus.get_center()+RIGHT, end = nucleus.get_center()).scale(0.6)
        
        vecS1 = Arrow(color = YELLOW, start = nucleus.get_center()+LEFT, end = nucleus.get_center())
        vecS2 = Arrow(color = YELLOW, start = nucleus.get_center()+RIGHT, end = nucleus.get_center())
        
        vecVG = VGroup(vecEIn1, vecEIn2, vecEOut1, vecEOut2, vecG1, vecG2, vecS1, vecS2)

        #self.add(vecVG)
        
       
        #force vector labels
        labelSize = 22
        vecLabels = VGroup(
                           MathTex(r"E", font_size=labelSize),
                           MathTex(r"E", font_size=labelSize),
                           MathTex(r"E", font_size=labelSize),
                           MathTex(r"E", font_size=labelSize),
                           MathTex(r"G", font_size=labelSize),
                           MathTex(r"G", font_size=labelSize),
                           MathTex(r"S", font_size=labelSize, color = YELLOW),
                           MathTex(r"S", font_size=labelSize, color = YELLOW),
                           )
                           
        vecLabelsOrient = [RIGHT, RIGHT, UP+LEFT, DOWN+RIGHT, UP+LEFT, DOWN+RIGHT, UP+LEFT, DOWN+RIGHT]
        for i in range(len(vecVG)):
            vecLabels[i].move_to(vecVG[i].get_tip()).shift(0.2*vecLabelsOrient[i])
            
        #self.add(vecLabels)
        
        
        
        
        
        
        #text elements
        textSize1 = 30
        textSize2 = 40
        textSize3 = 26
        
        
        
        textVG1 = VGroup()
        textVG1.add(Tex(
                        r"Atom:", font_size=textSize2
                        )
                    )
        textVG1.add(Tex(
                        r"- {{protons}} ($+$ charged)", font_size=textSize1
                        ).set_color_by_tex("protons", RED)
                    )
        textVG1.add(Tex(
                        r"- \textbf{neutrons} (neutral)", font_size=textSize1
                        )
                    )
        textVG1.add(Tex(
                        r"- {{electrons}}: ($-$ charged)", font_size=textSize1
                        ).set_color_by_tex("electrons", BLUE)
                    )
        textVG1.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.12).to_edge(LEFT).shift(UP)       #tally the Tex items in the VGroup into a left-aligned list
        
        
        
        
        textVG2 = VGroup()
        textVG2.add(Tex(
                        r"Opposite charges attract,", font_size=textSize3
                        )
                    )
        textVG2.add(Tex(
                        r"like charges repel!", font_size=textSize3
                        )
                    )
        textVG2.add(Tex(
                        r"{{Electrons}} hold on", font_size=textSize3
                        ).set_color_by_tex("electrons", BLUE)
                    )
                    
        textVG2.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.12).to_edge(RIGHT).shift(UP) 
        
        
        
        
        textVG3 = VGroup()
        textVG3.add(Tex(
                        r"But {{protons}} should repel!", font_size=textSize3
                        ).set_color_by_tex("protons", RED)
                    )
        textVG3.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.12).to_edge(RIGHT).shift(UP) 
        
        
        
        
        
        textVG4 = VGroup()
        textVG4.add(Tex(
                        r"Gravity isn't strong enough", font_size=textSize1
                        ).to_edge(LEFT)
                    )
        textVG4.add(MathTex(
                        r"\frac{\text{Gravity}}{\text{Electric force}} \approx 10^{-36}", font_size=textSize3-4
                        )
                    )
        textVG4.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.12).to_edge(LEFT).shift(UP) 
        
        
        

        
        
        
        
        bottomText1 = Tex(
                        r"Why is the \textit{nucleus} staying together?", font_size=textSize2
                        ).to_edge(DOWN)
                        
                        
        bottomText2 = VGroup()
        bottomText2.add(Tex(
                        r"Conclusion: There \underline{must} be another force!", font_size=textSize2
                        )
                        )
        bottomText2.add(Tex(
                        r"And it has to be {{strong}}er than the electric attraction", font_size=textSize3
                        ).set_color_by_tex("strong", YELLOW)
                        )
        bottomText2.arrange(DOWN, buff=0.12).to_edge(DOWN)
        #self.add(bottomText2)
        
        
        
        #ANIMATIONS
        nucleonIndicateScaleFactor = 1.4
        self.play(GrowFromCenter(AtomGroup), Write(textVG1[0]))                     #create atom and write Atom
        self.play(Write(chargeLabels, run_time=1))                                  #write charge labels
        self.play(Write(textVG1[1]), run_time=0.6)                                                #write protons
        
        self.play(
                  Indicate(proton1, color=RED, scale_factor=nucleonIndicateScaleFactor), 
                  Indicate(proton2, color=RED, scale_factor=nucleonIndicateScaleFactor),
                  run_time = 1.5
                  )
                  
        self.play(Write(textVG1[2]), run_time=0.6)                                                #write neutrons
        self.play(
                  Indicate(neutron1, color=WHITE, scale_factor=nucleonIndicateScaleFactor), 
                  Indicate(neutron2, color=WHITE, scale_factor=nucleonIndicateScaleFactor),
                  run_time = 1.5
                  )
                  
        self.play(Write(textVG1[3]), run_time=0.6)                                                #write electrons
        
        
        
        
        electronMovement = AnimationGroup(                                                          #two electrons on the orbit
                                Rotate(electronSign1, about_point=AtomGroup.get_center(), angle=2*PI, rate_func=linear, run_time=3),
                                Rotate(electronSign2, about_point=AtomGroup.get_center(), angle=2*PI, rate_func=linear, run_time=3)
                           )
        self.play(electronMovement)                                                                 #orbit the electrons
        self.wait()
       

        showElectronArrow = AnimationGroup(
                                GrowArrow(vecEIn1), 
                                GrowArrow(vecEIn2),
                                Write(vecLabels[0]), 
                                Write(vecLabels[1])
                            )
        self.play(showElectronArrow)                                                                #electron force arrows and labels
        for i in range(len(textVG2)):                                                               #write textVG2
            self.play(Write(textVG2[i]), run_time=1)
        self.wait()
        self.play(FadeOut(textVG2))
        
        
        self.play(Write(textVG3), run_time=1.5)                                                       #write textVG3
        showProtonArrow = AnimationGroup(
                                GrowArrow(vecEOut1), 
                                GrowArrow(vecEOut2),
                                Write(vecLabels[2]), 
                                Write(vecLabels[3])
                            )
        self.play(showProtonArrow)                                                                #proton force arrows and labels
        self.wait()
                            
        self.play(FadeOut(textVG1), FadeOut(textVG3))
        self.play(Write(bottomText1), run_time=2)                                               #fade all out and write bottom text 1
        self.wait()
        

        showGravArrow = AnimationGroup(
                                GrowArrow(vecG1), 
                                GrowArrow(vecG2),
                                Write(vecLabels[4]), 
                                Write(vecLabels[5])
                            )
        self.play(showGravArrow)                                                                #proton force arrows and labels
        self.play(Write(textVG4[0]))
        self.play(Write(textVG4[1]))
        self.wait()
        
        self.play(FadeOut(vecG1), FadeOut(vecG2),                                               #wipe out grav arrow and labels
                  FadeOut(vecLabels[4]), FadeOut(vecLabels[5]))   
                  
        self.play(FadeOut(bottomText1), FadeOut(textVG4))                                       #fade out bottom text 1 and left text 4
        
        self.play(Write(bottomText2))                                                           #write bottom text 2
        showStrongArrow = AnimationGroup(                                                       #strong vector and labels
                                GrowArrow(vecS1), 
                                GrowArrow(vecS2),
                                Write(vecLabels[6]), 
                                Write(vecLabels[7])
                            )
        self.play(showStrongArrow)
        self.wait(5)
        
       
       
       
        #THE    S T R O N G    FORCE
        self.clear()
        
        self.play(Write(
                        Tex(r"The Strong Force", color=YELLOW, font_size=100)
                        ))
        self.wait()