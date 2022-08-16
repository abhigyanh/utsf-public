from manim import *
config.max_files_cached = 1000


CYAN = rgb_to_color([0,1,1])
MAGENTA = rgb_to_color([1,0,1])

from utsf_common import *
        
        
class Intro0(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().set(color = GREY)
        
        circle = Circle(radius = 4, color = GREY, stroke_width = 2)
        nucleusBorder = Circle(radius = 0.2, stroke_width = 0)
        
        proton = Sphere(
            radius = 0.2, resolution = (8,8)
        ).set(color = RED)
        neutron = Sphere(
            radius = 0.2, resolution = (8,8)
        ).set(color = WHITE)
        electron = Sphere(
            radius = 0.1, resolution = (4,4)
        )
        
        electrons = VGroup(
            electron.copy().move_to(circle.point_at_angle(0)),
            electron.copy().move_to(circle.point_at_angle(PI)),
        )
        protons = VGroup(
            proton.copy().move_to(nucleusBorder.point_at_angle(PI/3)),
            proton.copy().move_to(nucleusBorder.point_at_angle(PI)),
        )
        neutrons = VGroup(
            neutron.copy().move_to(nucleusBorder.point_at_angle(5*PI/3)),
            neutron.copy().move_to([0, 0, 0.25]),
        )
        
        atom = VGroup(
            circle, electrons, protons, neutrons
        )
        
        self.set_camera_orientation(phi=45 * DEGREES, theta=30 * DEGREES)
        self.add(atom)
        self.begin_ambient_camera_rotation(rate=-0.8)
        self.play(
            Rotate(electrons[0], angle = PI/2, about_point=ORIGIN), 
            Rotate(electrons[1], angle = PI/2, about_point=ORIGIN), 
            run_time=2, 
            rate_func=linear,
        )
        self.move_camera(zoom = 2)
        self.wait(2)
        #self.play(*[mobj.animate.scale(4) for mobj in self.mobjects])
        
        
        
        
        
        
class Intro1(Scene):
    def construct(self):
        inThisVideo = Text("In this video:").to_edge(UP)
        self.play(Write(inThisVideo))
        self.wait()
        
        #group of six boxes for six preview animations
        boxesVGroup = VGroup()
        
        for i in range(6):                              #create six boxes
            aBox = Rectangle(color=WHITE, height=3, width=4)
            boxesVGroup.add(aBox)
            
        boxesVGroup.arrange_in_grid(rows=2,cols=3, buff=1)      #arrange all boxes in a grid
        boxesVGroup.next_to(inThisVideo,DOWN)                     #below the top text
        
        if boxesVGroup.height > 0.75*config.frame_height:
            boxesVGroup.scale(boxesVGroup.height/config.frame_height * 0.75)    #this will fit all the boxes in the screen, if overflow
        
        self.play(Create(boxesVGroup), run_time = 2)
        
        
        #preview animation labels
        labelsVGroup = VGroup()
        
        labelsVGroup.add(Tex(r"Looking at the atom"))                       #label 1
        labelsVGroup.add(Tex(r"Spin of particles"))                         #label 2
        labelsVGroup.add(Tex(r"Pauli's Exclusion Principle"))               #label 3
        labelsVGroup.add(Tex(r"Colour"))                                    #label 4
        labelsVGroup.add(Tex(r"Colour in gluons \\ (the Strong Force)"))    #label 5
        labelsVGroup.add(Tex(r"The SU(3) Symmetry Group"))               #label 6
        
        for i in range(6):
            if labelsVGroup[i].width > 0.9*boxesVGroup[i].width:
                labelsVGroup[i].set(width = boxesVGroup[i].width * 0.9)    #fit label to box, if overflow
                
            labelsVGroup[i].next_to(boxesVGroup[i],DOWN)                     #labels below the box  
            self.play(Write(labelsVGroup[i]), run_time = 1)                     #write the labels out
        
        self.wait()
        
        
        
        previewsVGroup = VGroup()
       
        #box1 VGroup: Helium-4 atom
        nucleonSize = 0.1
        
        proton1 = Dot(radius=nucleonSize).set_color(RED)
        neutron1 = Dot(radius=nucleonSize).next_to(proton1,RIGHT,buff=0).set_color(WHITE)
        neutron2 = Dot(radius=nucleonSize).next_to(proton1,DOWN,buff=0)
        proton2 = Dot(radius=nucleonSize).next_to(neutron1,DOWN,buff=0).set_color(RED)
        
        nucleus = VGroup(proton1,neutron1,proton2,neutron2)
        
        orbit = Circle(radius=1, color=WHITE).surround(nucleus).scale(10*nucleus.width)
        
        electron1 = Dot(color=BLUE).next_to(orbit,RIGHT,buff=-0.075)
        electron2 = Dot(color=BLUE).next_to(orbit,LEFT,buff=-0.075)
        
        AtomGroup = VGroup(orbit,electron1,electron2,nucleus)
        AtomGroup.move_to(boxesVGroup[0].get_center())
        
        
        previewsVGroup = previewsVGroup.add(AtomGroup)  #add the atom preview to previews
        
        
        #box2 VGroup: electron spin
        preview2Text = Tex(r"(diagram of \\ Stern-Gerlach \\ experiment?)")
        previewsVGroup = previewsVGroup.add(preview2Text)       #add text to previews
        
        
        #box3 VGroup: pauli exclusion
        preview3Tex = MathTex(r"|\Psi(A,B)\rangle = \\ - |\Psi(B,A)\rangle")
        previewsVGroup = previewsVGroup.add(preview3Tex)       #add to previews
        
        
        #box4 VGroup: colours
        preview4Tex = Tex(r"diagram \\ of the RGB \\ colour space")
        previewsVGroup = previewsVGroup.add(preview4Tex)       #add to previews
        
        #box5 VGroup: feynman diagram
        preview5Tex = Tex(r"Feynman diagram \\ of a quark color \\ exchange process?")
        previewsVGroup = previewsVGroup.add(preview5Tex)       #add to previews
        
        #box6 VGroup: feynman diagram
        preview6Tex = Tex(r"The 8 generators \\ of the SU(3) \\ Lie algebra?")
        previewsVGroup = previewsVGroup.add(preview6Tex)       #add to previews
        
        
        
        #move all the preview things inside their boxes
        for i in range(len(previewsVGroup)):
            if previewsVGroup[i].height > 0.8*boxesVGroup[i].height:
                previewsVGroup[i].set(height = 0.8*boxesVGroup[i].height)
            if previewsVGroup[i].width > 0.8*boxesVGroup[i].width:
                previewsVGroup[i].set(width = 0.8*boxesVGroup[i].width)
                
            previewsVGroup[i].move_to(boxesVGroup[i].get_center())          
        
        
        
        
        
        #play preview 1: atom
        self.play(GrowFromCenter(AtomGroup))            #create AtomGroup
        electronMovement = AnimationGroup(              #two electrons on the orbit
                                Rotate(electron1, about_point=AtomGroup.get_center(), angle=2*PI, rate_func=linear),
                                Rotate(electron2, about_point=AtomGroup.get_center(), angle=2*PI, rate_func=linear)
                           )
        self.play(electronMovement, run_time=2)
        self.wait()
        
        #play preview 2,3,4,5,6: stern-gerlach text
        for i in range(1,6):
            self.play(Write(previewsVGroup[i]))
            self.wait()
            
            
            
            
            
class Intro2(Scene):
    def construct(self):
        scalar = 5
        BigBox = Rectangle(width = 1.44*scalar, height = 1*scalar)
        ThisIsOurSubmission = VGroup(
            Tex(r"This is our submission to the").next_to(BigBox, UP),
            Tex(r"2nd Summer of Math Exposition!").next_to(BigBox, DOWN),
        )
        
        self.play(Create(BigBox))
        self.play(Write(ThisIsOurSubmission))
        self.wait(8)
        
        
            