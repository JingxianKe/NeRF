from manimlib import *

class InteractiveDevelopment(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()

        # 这会打开一个iPython终端，你可以在其中继续写你想要执行的代码
        # 在这个例子中，square/circle/self都会成为终端中的实例
        self.embed()