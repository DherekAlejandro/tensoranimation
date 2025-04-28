from manim import *
import numpy as np

class CircleAnnouncement(ThreeDScene):
    def construct(self):
        """
        announcement = Text("Esto es un escalar")
        
        self.play(Write(announcement))
        self.wait()
        
        blue_circle = Circle(color=BLUE, fill_opacity=0.5, radius=0.1)

        self.play(announcement.animate.next_to(blue_circle, UP, buff=0.2))

        nl = NumberLine(x_range=[0, 10, 2],length=10, include_numbers=False)
        self.play(Create(nl))


        self.play(Create(blue_circle))
        
        text2 = Text("Esto es un vector")

        ax = Axes(x_range=[-10, 10, 2], y_range=[-10,10,2])
        self.play(Create(text2), text2.animate.next_to(ax, UP, buff=0.2), FadeOut(announcement))
        self.play(Create(ax), FadeOut(nl), blue_circle.animate.move_to(ax.c2p(5, 5)))
        

        vector_1 = Vector(direction = ax.c2p(5, 5))
        self.play(Create(vector_1))
        """

        axes = ThreeDAxes()

        #self.play(Create(axes), FadeOut(ax), FadeOut(text2))
        self.play(Create(axes))
        self.set_camera_orientation(
            theta = -90* DEGREES,
            phi = 90* DEGREES,
        )
        
        
        
        self.move_camera(
            theta = -45* DEGREES,
            phi = 45* DEGREES,
        )

def main():
    c = CircleAnnouncement()
    c.construct()


if __name__ == "__main__":
    main()
