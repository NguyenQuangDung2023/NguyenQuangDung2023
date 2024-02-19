from manim import *
from pathlib import Path
import os 
from colour import *
import math
from manim.mobject.geometry.tips import ArrowTriangleTip,\
                                        ArrowSquareTip, ArrowSquareFilledTip,\
                                        ArrowCircleTip, ArrowCircleFilledTip
FLAGS = f"-pqk"#Thử nghiệm chất lượng video qua các Render
SCENE = "example" #  Sân khấu mình cần renderimport math as m
class SinAndCosFunctionPlot(MovingCameraScene):
    def construct(self):
        self.camera.background_color = BLACK
        self.add_sound("The Nights - Citycreed")
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0,0 , 1),
                "numbers_with_elongated_ticks": np.arange(0, 0, 2)
            },
            tips=True
         )
        axes_new = axes.copy().scale(0.75).move_to(axes.coords_to_point(0,3.25))
        labels = axes_new.get_axis_labels(
            MathTex("x"),MathTex("y"))
        #axes_labels = axes.get_axis_labels()
        #I. Bảng biến thiên       
         #1.1.Định các điểm tạo khung BBT
        a = axes_new.coords_to_point(-4,0)
        b = axes_new.coords_to_point(6,0)
        c = axes_new.coords_to_point(-4,-1)
        d = axes_new.coords_to_point(6,-1)
        e = axes_new.coords_to_point(-4,-2)
        f = axes_new.coords_to_point(6,-2)
        g = axes_new.coords_to_point(-4,-4)
        h = axes_new.coords_to_point(6,-4)
        col1 = axes_new.coords_to_point(-2.5,0)
        col2 = axes_new.coords_to_point(-2.5,-4)
         #1.2. Vẽ khung BBT
        width = 2#(Độ dày của đường)
        AB = Line(a,b,stroke_width=width)
        CD = Line(c,d,stroke_width=width)
        EF = Line(e,f,stroke_width=width)
        GH = Line(g,h,stroke_width=width)
        AG = Line(a,g,stroke_width=width)
        BH = Line(b,h,stroke_width=width)
        line_col1=Line(col1,col2,stroke_width=width)
         #1.3. Node dòng đầu của x
        xx = VGroup()
        for x,y in [(-4.5,"x"),(-3.25,"-\\infty"),(-1,"-1"),(1,"1"),(4,"+\\infty")]:
            xt = MathTex(y).move_to(axes_new.coords_to_point(x-0.15,-3)).scale(0.65)
            xx.add(xt)
        xx[0].set_color(WHITE)
        xx[2].set_color(YELLOW)
        xx[4].set_color(YELLOW)
         #1.4. Dấu của đạo hàm
        ff = VGroup()
        for x,y in [(-4.5,"f'(x)"),(-2.5,"+"),(-1,"0"),(0,"-"),(1,"0"),(2.5,"+")]:
            t= MathTex(y).move_to(axes_new.coords_to_point(x-0.15,-4)).scale(0.65).set_color(BLUE)
            ff.add(t)
        ff[2].set_color(YELLOW)
        ff[4].set_color(YELLOW)
         #1.5. Dòng của f(x)
        y_00 = axes_new.coords_to_point(-4.5,-3)
        y_01 = axes_new.coords_to_point(-3.5,-3.5)
        y_02 = axes_new.coords_to_point(-1,-2.5)
        y_03 = axes_new.coords_to_point(1,-3.5)
        y_04 = axes_new.coords_to_point(4,-2.6)
        yyy = VGroup()
        for x,y in[(y_00,"f(x)"),(y_01,"-\\infty"),(y_02,"f\\left(x_1\\right)"),
                   (y_03,"f\\left(x_2\\right)"),(y_04,"+\\infty")]:
            yy = MathTex(y).move_to(x).shift(axes_new.coords_to_point(-0.15,-3.25)).scale(0.65)
            yyy.add(yy)
        yyy[2].set_color(PINK)
        yyy[0].set_color(ORANGE)
        yyy[1].set_color(GREEN)
        yyy[3].set_color(RED)
         #1.6. Vẽ mũi tên dòng f(x)
        yy_arrow = VGroup()
        for u,v in [(y_01,y_02),(y_02,y_03),(y_03,y_04)]:
            uv =Arrow(start = u, end=v,stroke_width=1,color=YELLOW).scale(0.8, scale_tips=True)
            yy_arrow.add(uv)#Vẽ từng mũi tên và add vào yy_arrow
        yy_arrow.move_to(axes_new.coords_to_point(-0,-5.5))
        yy_arrow[1].set_color(WHITE)
        BBT = VGroup(AB,CD,EF,GH,BH,AG,line_col1).move_to(axes_new.coords_to_point(-0.55,-4.5))
         #II. Các điểm cực trị.
         #2.1. Điểm cực đại
        M =Dot(axes_new.coords_to_point(-1,1.5)).scale(0.8)
        x_M = Dot(axes_new.coords_to_point(-1,0)).scale(0.8)
        y_M =Dot(axes_new.coords_to_point(0,1.5)).scale(0.8)
        Mx =DashedLine(M.get_center(),x_M.get_center(),stroke_width=1.5)
        My =DashedLine(M.get_center(),y_M.get_center(),stroke_width=1.5)
        My_node = MathTex("y_1").next_to(axes_new.coords_to_point(0,1.5)).scale(0.65)
        M_node = MathTex("M").next_to(axes_new.coords_to_point(-1,1.5),UP).scale(0.5)
        Mx_node = MathTex("x_1").next_to(axes_new.coords_to_point(-1,0),DOWN).scale(0.65)
        Mg = VGroup(M,x_M,y_M,My,Mx,My_node,M_node,Mx_node)
         #2.2. Điểm cực tiểu
        N =Dot(axes_new.coords_to_point(1,-1.5)).scale(0.8)
        x_N = Dot(axes_new.coords_to_point(1,0)).scale(0.8)
        y_N =Dot(axes_new.coords_to_point(0,-1.5)).scale(0.8)
        Nx =DashedLine(N.get_center(),x_N.get_center(),stroke_width=1.5)
        Ny =DashedLine(N.get_center(),y_N.get_center(),stroke_width=1.5)
        Ny_node = MathTex("y_2").next_to(axes_new.coords_to_point(0,-1.5),LEFT).scale(0.65)
        N_node = MathTex("N").next_to(axes_new.coords_to_point(1,-1.5),DOWN).scale(0.5)
        Nx_node = MathTex("x_2").next_to(axes_new.coords_to_point(1,0),UP).scale(0.65)
        Ng = VGroup(N,x_N,y_N,Ny,Nx,Ny_node,N_node,Nx_node)
        #III. Vẽ đường cong Controls từ tập nhiều điểm
         #3.1. Tạo tập điểm
        def coord(x,y):
            return axes_new.coords_to_point(x,y)
        points = [coord(x,y)
        for x,y in [(-3.5,-2),(-2.35,0),(-1,1.5),(0,0.1),(1,-1.5),(2,0),(3.25,4.5)]
        ]
            #dots = VGroup(*[Dot(p).scale(0.5) for p in points])(Dot tô các điểm bằng lệnh VGroup
            #Đây là cách tách thành các phần tử từ tập "points")
            #Vẽ Vmoject(option).set_points_smoothly. 
        polyline = VMobject(stroke_width=2).scale(0.75).set_points_smoothly(points)
        #3.2. Lệnh cắt, tô màu một phần đường cong đã vẽ.
            #a. Phần 1.
        partial_1 = polyline.get_subcurve(0,0.32)
            #b. Phần 2.
        partial_2 = polyline.get_subcurve(0.32,0.68)
            #c. Phần 3
        partial_3 = polyline.get_subcurve(0.68,1)
        Dothi = VGroup(polyline,partial_1,partial_2,partial_3)
        for i,mau in [(0,BLUE),(1,WHITE),(2,YELLOW),(3,PINK)]:
            Dothi[i].set_color(mau)
        #IV. Vẽ đường gấp khúc từ tập điểm. Sự thay đổi so với đường controls chỉ là
           #tùy chọn "set_points_as_corners"
           #Lệnh: Vmobject.set_points_as_corners(coords)
         #4.1. Tạo tập điểm:
        poin2 = [y_01,y_02,y_03,y_04]
         #4.2. Vẽ:
        gap_khuc = VMobject(color=BLUE,stroke_width=0).scale(0.75).set_points_as_corners(poin2).move_to(axes_new.coords_to_point(0.2,-5.5))
        #V. Lệnh tạo điểm chạy MoveAlongPath: Hai path ở đây
            #Một là đường controls
            #Đường ẩn gấp khúc nằm trên bảng biến thiên
        Nhom_BBT = VGroup(yy_arrow,BBT,gap_khuc,yyy,xx,ff)
        Nhom_Cuctri =VGroup(Mg,Ng,Dothi,axes_new)
        Tong_the =VGroup(Nhom_Cuctri,Nhom_BBT)
        dot2 =Star(fill_opacity=1,color=PINK).scale(.1).set_color(ORANGE)
        dot1 = Dot().scale(1.5).set_color(WHITE)
        ###Văn bản
        
        #VI. Đoạn kịch bản hiệu ứng(Tùy khả năng đạo diễn)
        self.add(Tong_the)
         #6.0. Điểm
        self.play(MoveAlongPath(dot2,polyline),MoveAlongPath(dot1,gap_khuc),run_time=10)
         #6.1.Phân cảnh 1: Mối liên hệ giữa đồ thị và dấu đạo hàm, mũi tên
          #6.1.1. Nhánh 1
        self.play(Write(Dothi[1].set_stroke_width(5)),run_time=5)
        self.play(Transform( Dothi[1],yy_arrow[0]),run_time=5)
        self.play(self.camera.frame.animate.move_to(yy_arrow[0]).set(width=yy_arrow[0].width*2))
        self.wait(5)
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))#Trả Camera về chính giữa khung hình
        self.play(Transform( Dothi[1],ff[1]),run_time=5)
        self.play(self.camera.frame.animate.move_to(ff[1]).set(width=ff[1].width*10))
        self.wait(5)
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))#Trả Camera về chính giữa khung hình
        self.play(FadeOut(Dothi[1])) 
          #6.1.2 Nhánh 2.
        self.play(Write(Dothi[2].set_stroke_width(5)),run_time=5)
        self.play(Transform( Dothi[2],yy_arrow[1]),run_time=5)
        self.play(self.camera.frame.animate.move_to(yy_arrow[1]).set(width=yy_arrow[1].width*2))
        self.wait(5)
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))#Trả Camera về chính giữa khung hình
        self.play(Transform( Dothi[2],ff[3]),run_time=5)
        self.play(self.camera.frame.animate.move_to(ff[3]).set(width=ff[3].width*10))
        self.wait(5)
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))#Trả Camera về chính giữa khung hình
        self.play(FadeOut(Dothi[2])) 
        #6.1.3. Nhánh 3
        self.play(Write(Dothi[3].set_stroke_width(5)),run_time=5)
        self.play(Transform( Dothi[3],yy_arrow[2]),run_time=5)
        self.play(self.camera.frame.animate.move_to(yy_arrow[2]).set(width=yy_arrow[2].width*2))
        self.wait(5)
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))#Trả Camera về chính giữa khung hình
        self.play(Transform( Dothi[3],ff[5]),run_time=5)
        self.play(self.camera.frame.animate.move_to(ff[5]).set(width=ff[5].width*10))
        self.wait(5)
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))#Trả Camera về chính giữa khung hình
        self.play(FadeOut(Dothi[3])) 
        #############################################################################
         ###Hoạt cảnh cuối với văn bản####################################
        ###Văn bản
        self.remove(dot1,dot2)
        self.play(AnimationGroup(Tong_the.animate.arrange(direction=DOWN, aligned_edge=LEFT).scale(0.75).move_to(0.8*UL).shift(LEFT)),run_time=5,lag_ratio=0.8)
        self.remove(Dothi[1],Dothi[2],Dothi[3])
        #Baigiang: Sự biến thiên của hàm số 
        t1 = Tex("1. Xét trên $(-\infty,x_1)$ và $(x_2,+\infty)$").set_color(WHITE)
        t11 =Tex("+ Hàm số đồng biến.")
        t12 =Tex("+ Đồ thị đi lên trên các khoảng")
        t13 =Tex("+ Đạo hàm mang dấu +")
        t2 = Tex("2. Xét trên khoảng ($x_1$,$x_2$)").set_color(WHITE)
        t21 =Tex("+ Hàm số nghịch biến.")
        t22 =Tex("+ Đồ thị đi xuống")
        t23 =Tex("+ Đạo hàm mang dấu -")
        x = VGroup(t1,t11,t12,t13,t2,t21,t22,t23).arrange(direction=DOWN, aligned_edge=LEFT).to_corner(UR).shift(RIGHT).scale(0.65)#.next_to(2*RIGHT+2*UP)
        x.set_opacity(0.75)
        self.play(Write(x),run_time=5)
        for i in range(1,4):
            self.play(Transform(x.submobjects[0].copy().set_opacity(1).set_color(YELLOW),x.submobjects[i].copy().set_opacity(1).set_color(YELLOW)),run_time=5)
        for i in range(4,8):
            self.play(Transform(x.submobjects[4].copy().set_opacity(1),x.submobjects[i].copy().set_opacity(1).set_color(BLUE)),run_time=5)
if __name__ == "__main__":
        script_name = f"{Path(__file__).resolve()}"
        os.system(f"manim {script_name} {SCENE} {FLAGS}")        
