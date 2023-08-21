
from manim import *
from pathlib import Path
import os 
from colour import *
import math
from manim.utils.color import Color
import numpy
from manim.mobject.geometry.tips import ArrowTriangleTip,\
                                        ArrowSquareTip, ArrowSquareFilledTip,\
                                        ArrowCircleTip, ArrowCircleFilledTip
FLAGS = f"-pqk"#Thử nghiệm chất lượng video qua các Render
SCENE = "example" #  Sân khấu mình cần renderimport math as m
class UpdatersExample(Scene):
    def construct(self):
        def get_full_sound_file_path(sound_file_name):
            return seek_full_path_from_defaults(sound_file_name,
                default_dir=config.get_dir("assets_dir"),
                extensions=[".wav", ".mp3"],
                )
            self.get_full_sound_file_path("click")

        self.add_sound("click",gain=3)
        self.add_sound("manim-music")
        #1. Định nghĩa bán kính, 
        r = 3
        a = np.array([r*math.cos(30*DEGREES),r*math.sin(30*DEGREES),0])
        b = np.array([r*math.cos(30*DEGREES),r*math.sin(30*DEGREES)+r,0])
        c = np.array([r*math.cos(30*DEGREES)-r*math.sqrt(3),r*math.sin(30*DEGREES)+r,0])
        A = Dot(a)
        B = Dot(b)
        C = Dot(c)
        #2. Vẽ hình cơ sở
        abc1 = VGroup()
        for i,mau in [(0,BLUE_A),(1,YELLOW),(2,GREEN),(3,PINK),(4,TEAL),(5,ORANGE)]:
            tam = Polygon(a,b,c,fill_opacity=0.75,color=mau,stroke_width=1.5).set_color(mau).scale(1)
            nhom = VGroup(A,B,C,tam)
            gap_khuc = nhom.rotate(i*60*DEGREES,about_point=[0,0,0])
            abc1.add(gap_khuc)
            #Vẽ một hình xoắn.
        abc2 = VGroup()
        for i,mau,o in [(0,YELLOW,1)]:
            tam = Polygon(a,b,c,fill_opacity=0,color=mau,stroke_width=0).scale(1)
            gap_khuc = tam.rotate(i*60*DEGREES,about_point=[0,0,0])
            abc2.add(gap_khuc)
        #Lục giác đều ghép bởi các tam giác.   
        n = np.array([r*math.cos(30*DEGREES),r*math.sin(30*DEGREES)+r,0])
        p = np.array([r*math.cos(30*DEGREES)-r*math.sqrt(3),r*math.sin(30*DEGREES)+r,0])
        m =np.array([0,0,0])   
        Lucgiac =VGroup()
        for i,mau in [(0,BLUE_A),(1,YELLOW),(2,GREEN),(3,PINK),(4,TEAL),(5,ORANGE)]:
            goc = Polygon(m,n,p,fill_opacity=1,color=mau,stroke_width=1.5).set_color(mau).scale(1)
            change = goc.rotate(i*60*DEGREES,about_point=[0,0,0])
            AB = Line(b,c)
            Bar = Brace(AB,UP).set_color(YELLOW_A)
            Ten = Bar.get_text("a").set_color(YELLOW)
            Lucgiac.add(Ten,Bar,change)     
        Lucgiac.scale(0.55)
        ####Tam giác
        tam = Polygon(a,b,c,fill_opacity=0.75,color=YELLOW,stroke_width=1.5).set_color(YELLOW_A).scale(1)
        tamgiac = VGroup()
        for i in range(1,10):
          tam1 = tam.copy().scale((math.sqrt(3)/3)**i).rotate(0*DEGREES,about_point=[0,0,0])
          tamgiac.add(tam1)
        new =VGroup()
        for i in range(1,10):
          new1 = abc1.copy().scale((math.sqrt(3)/3)**i).rotate((180-i*30)*DEGREES,about_point=[0,0,0])
          new.add(new1)
        new2 =VGroup()
        for i in range(1,10):
          new1 = abc2.copy().scale((math.sqrt(3)/3)**i).rotate((180-i*30)*DEGREES,about_point=[0,0,0]).move_to([r*(math.sqrt(3)/3)**i*math.cos((180-i*30)*DEGREES),r*(math.sqrt(3)/3)**i*math.sin((180-i*30)*DEGREES),0])
          new2.add(new1)
        O = Dot([4,0,0])
        abc1.width=config.frame_width-2
        abc1.width=config.frame_height-2
        Baitoan = Tex("\\begin{minipage}{8cm} Cho tam giác $A_1B_1C_1$ vuông tại A có diện tích $S_1$. Có $AB=a$, $AC=\\frac{a}{\\sqrt{3}}$. Tam giác $A_nB_nC_n$ đồng dạng với $A_1B_1C_1$ theo tỉ lệ $k=\\frac{1}{\\sqrt{3^n}}$ có diện tích $S_n$. Tính tổng vô hạn $S_1+S_2+\\cdots+S_n+\\cdots$ \\end{minipage}")
    
        tam2=tamgiac.arrange(direction=DOWN,aligned_edge=RIGHT,buff =0.1).move_to([3,0,0])
        S1 = MathTex("S_1=\\frac{a^2}{2\\sqrt{3}}").next_to(tamgiac[0]).scale(1)
        S2 = MathTex("S_2=\\frac{1}{3}S_1").next_to(tamgiac[1]).scale(0.75)
        S3 = MathTex("S_3=\\frac{1}{3^2}S_1").next_to(tamgiac[2]).scale(0.75)
        S4 = MathTex("S_4=\\frac{1}{3^3}S_1").next_to(tamgiac[3]).scale(0.75)
        S5 = MathTex("\\ldots").next_to(tamgiac[4])
        Sn = MathTex("S_n=\\frac{1}{3^n}S_1").next_to(tamgiac[8]).scale(0.75)
        Tong = MathTex("S=S_1+S_2+\\ldots+S_n+\\cdots")
        Tex1 = Tex("Ta có")
        Tong1 = MathTex("S=\\frac{1}{6}S_0=\\frac{a^2\\sqrt{3}}{4}").next_to(Tex1,RIGHT)
        Tong2 = MathTex("S=S_1\\left(1+\\frac{1}{3}+\\frac{1}{3^2}+\\ldots+\\frac{1}{3^n}+\\cdots\\right)=\\frac{a^2\\sqrt{3}}{4}")
        KL = Tex("Ta có: ")
        KL1 = MathTex("\\frac{a^2\\sqrt{3}}{4}","=","\\frac{a^2}{2\\sqrt{3}}","\\left(1+\\frac{1}{3}+\\frac{1}{3^2}+\\ldots+\\frac{1}{3^n}+\\cdots\\right)")
        KL2 = MathTex("\\frac{3}{2}=1+\\frac{1}{3}+\\frac{1}{3^2}+\\ldots+\\frac{1}{3^n}+\\cdots")
        Dan = Tex("Vậy tổng:" )
        Hoi = MathTex("1+\\frac{1}{3}+\\frac{1}{3^2}+\\ldots+\\frac{1}{3^n} +\\cdots= ???")
        Slide = VGroup(Tong,Tex1,Tong1,Tong2,KL,KL1,Dan,Hoi,KL2).scale(0.65).arrange(direction=DOWN,aligned_edge=LEFT).to_corner(UL)
        box1 = SurroundingRectangle(KL1[0],buff=0.05)
        box2 = SurroundingRectangle(KL1[2],buff=0.05) 
        S = VGroup(S1,S2,S3,S5,Sn).arrange(direction=DOWN,aligned_edge=LEFT).next_to(tamgiac,RIGHT).shift([0,-0.25,0])
        #self.call([" click ", S])
        Man1=VGroup(Baitoan,tam2.copy(),S.copy()).scale(0.75).arrange_in_grid(cols=3,buff=0.2)
        self.add_sound("click")
        self.play(Write(Man1))
        self.wait(10)
        self.add_sound("click")
        self.remove(Man1)
        self.play(Rotate(new[0], angle=2*PI, rate_func=linear),run_time=5)
        self.add_sound("click")
        self.play(Transform(abc1,new[0]),run_time=3)
        self.play(Create(new),Create(new2),run_time=5)
        self.add_sound("click",gain=3)
        self.play(Transform(new2,tam2),run_time=10)
        self.wait()
        self.add_sound("click",gain=3)
        self.play(Write(S),run_time=10)
        self.remove(new2,new,abc1,tam2,S)
        Man2=VGroup(new,tam2.copy(),S.copy()).arrange_in_grid(cols=3)
        self.wait()
        self.add_sound("click",gain=3)
        self.play(AnimationGroup(Man2.animate.scale(0.75).to_corner(UR)))
        self.remove(Man2)
        Man3=VGroup(Lucgiac,tam2,S).arrange_in_grid(cols=3).scale(0.6).to_corner(UR)
        self.add_sound("click",gain=3)
        self.play(FadeIn(Man3),run_time=2)
        self.wait(5)
        self.add_sound("click",gain=3)
        self.play(Write(Slide[0]),run_time=2)
        self.wait(2)
        self.add_sound("click",gain=3)
        self.play(Write(Slide[1]),run_time=2)
        self.wait(2)
        self.add_sound("click",gain=3)
        self.play(Write(Slide[2]),run_time=2)
        self.wait(2)
        self.add_sound("click",gain=3)
        self.play(Write(Slide[3]),run_time=2)
        self.wait(2)
        self.add_sound("click",gain=3)
        self.play(Write(Slide[4]),run_time=2)
        self.wait(2)
        self.add_sound("click",gain=3)
        self.play(TransformMatchingShapes(Slide[4].copy(),Slide[5]),run_time=2)
        self.wait(2)
        self.add_sound("click",gain=3)
        self.play(ReplacementTransform(box2.copy(),box1),run_time=5)
        self.wait(10)
        self.add_sound("click",gain=3)
        self.play(Write(Slide[6]),run_time=2)
        self.wait(2)
        self.add_sound("click",gain=3)
        self.play(Write(Slide[7]),run_time=2)
        self.wait(5)
        self.add_sound("click",gain=3)
        self.play(TransformMatchingShapes(Slide[7].copy(),Slide[8]),run_time=2)
        self.wait(10)
if __name__ == "__main__":
        script_name = f"{Path(__file__).resolve()}"
        os.system(f"manim {script_name} {SCENE} {FLAGS}")        
