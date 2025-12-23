from manim import *
import numpy as np

# --- CONFIGURACIÓN ESTÉTICA ---
config.background_color = "#1e1e1e"
ACTION_COLOR = "#FFD700"  # Dorado
MATH_COLOR = "#89CFF0"    # Azul Hielo

class GaussianIntegralVisualizer(ThreeDScene):
    def construct(self):
        self.main_eq = None # Variable para rastrear la ecuación activa

        # 1. INTRODUCCIÓN (Gauss a la Izq, Título a la Der)
        self.intro_scene()
        
        # 2. PLANTEAMIENTO 1D
        self.setup_1d_problem()
        
        # 3. EL TRUCO (Elevar al cuadrado y pasar a 3D)
        self.the_squaring_trick()
        
        # 4. SOLUCIÓN EN POLARES Y GRAN FINAL
        self.polar_solution()

    def intro_scene(self):
        # Grupo derecho: Título e Integral
        title_text = Text("La Integral de Gauss", color=MATH_COLOR, font_size=48)
        intro_integral = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx", color=WHITE).scale(1.5)
        right_group = VGroup(title_text, intro_integral).arrange(DOWN, buff=0.8)
        right_group.to_edge(RIGHT, buff=1.0)
        
        underline = Line(LEFT, RIGHT, color=ACTION_COLOR).next_to(title_text, DOWN, buff=0.2).set_width(title_text.width)

        try:
            # Grupo izquierdo: Imagen de Gauss
            gauss_img = ImageMobject("young_gauss.jpg")
            gauss_img.set_height(5)
            gauss_img.to_edge(LEFT, buff=1.5)
            frame = SurroundingRectangle(gauss_img, color=ACTION_COLOR, buff=0.1)
            
            # Animación de entrada
            self.play(FadeIn(gauss_img, shift=RIGHT*0.5), Create(frame), run_time=1.5)
            self.play(Write(title_text), GrowFromCenter(underline), run_time=1)
            self.play(Write(intro_integral), run_time=1.5)
            self.wait(2)
            
            # Limpieza total
            self.play(*[FadeOut(mob) for mob in self.mobjects])
            
        except FileNotFoundError:
            # Fallback si no hay imagen
            center_group = VGroup(title_text, underline, intro_integral).arrange(DOWN, buff=0.5).move_to(ORIGIN)
            self.play(Write(center_group))
            self.wait(2)
            self.play(FadeOut(center_group))

    def setup_1d_problem(self):
        # Ecuación inicial
        self.main_eq = MathTex(r"I = \int_{-\infty}^{\infty} e^{-x^2} dx", color=MATH_COLOR).scale(1.5)
        
        # Gráficos
        axes = Axes(x_range=[-4, 4, 1], y_range=[0, 1.2, 1], x_length=8, y_length=4, axis_config={"color": GREY}).to_edge(DOWN)
        gauss_curve = axes.plot(lambda x: np.exp(-x**2), color=ACTION_COLOR, stroke_width=4)
        area = axes.get_area(gauss_curve, x_range=[-4, 4], color=ACTION_COLOR, opacity=0.3)
        
        self.play(Write(self.main_eq))
        self.wait(1)
        self.play(self.main_eq.animate.to_edge(UP).scale(0.7))
        
        self.play(Create(axes))
        self.play(Create(gauss_curve), run_time=1.5)
        self.play(FadeIn(area))
        
        q_mark = Text("?", color=RED, font_size=96).move_to(axes.c2p(0, 0.5))
        self.play(Write(q_mark))
        self.wait(2)
        
        self.play(FadeOut(axes), FadeOut(gauss_curve), FadeOut(area), FadeOut(q_mark))

    def the_squaring_trick(self):
        expl_text = Text("El truco: ¡Elevar al cuadrado!", color=ACTION_COLOR).next_to(self.main_eq, DOWN, buff=0.5)
        
        # I^2 explícito
        i_squared = MathTex(
            r"I^2", r"=", 
            r"\left(\int_{-\infty}^{\infty} e^{-x^2} dx\right)", 
            r"\left(\int_{-\infty}^{\infty} e^{-y^2} dy\right)",
            color=MATH_COLOR
        ).scale(1.2).move_to(ORIGIN)
        
        self.play(Write(expl_text))
        self.play(Write(i_squared))
        self.wait(1)
        
        # Integral Doble
        double_int = MathTex(r"I^2 = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{-(x^2 + y^2)} dx dy", color=MATH_COLOR).scale(1.2)
        
        self.play(ReplacementTransform(i_squared, double_int), run_time=1.5)
        self.wait(2)
        
        # Mover arriba y limpiar
        self.play(FadeOut(expl_text), FadeOut(self.main_eq), double_int.animate.to_edge(UP, buff=0.5).scale(0.8))
        self.main_eq = double_int
        
        # --- 3D ---
        axes3d = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3], z_range=[0, 1])
        surface = Surface(
            lambda u, v: axes3d.c2p(u, v, np.exp(-(u**2 + v**2))),
            u_range=[-3, 3], v_range=[-3, 3], resolution=(32, 32)
        )
        surface.set_style(fill_opacity=0.8, fill_color=BLUE_E, stroke_color=ACTION_COLOR, stroke_width=0.5)
        
        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES, run_time=2)
        self.play(Create(axes3d), Create(surface), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(surface), FadeOut(axes3d))
        self.move_camera(phi=0, theta=-90*DEGREES, run_time=1.5)

    def polar_solution(self):
        # Texto y cambio de variable
        polar_text = Text("Cambio a Coordenadas Polares", color=ACTION_COLOR, font_size=32).next_to(self.main_eq, DOWN, buff=0.5)
        subs = MathTex(r"x^2 + y^2 = r^2", r"dx dy = r dr d\theta", color=YELLOW).arrange(DOWN).next_to(polar_text, DOWN, buff=0.5)
        
        self.play(Write(polar_text), Write(subs))
        self.wait(2)
        
        # Integral en polares
        polar_int = MathTex(r"I^2 =", r"\int_{0}^{2\pi}", r"\int_{0}^{\infty}", r"e^{-r^2}", r"r dr d\theta", color=MATH_COLOR).scale(1.2)
        self.play(TransformMatchingShapes(VGroup(self.main_eq, polar_text, subs), polar_int))
        
        # Separación
        separated = MathTex(r"I^2 =", r"\left(\int_{0}^{2\pi} d\theta\right)", r"\cdot", r"\left(\int_{0}^{\infty} e^{-r^2} r dr\right)", color=MATH_COLOR).scale(1.2)
        self.play(TransformMatchingTex(polar_int, separated))
        
        # Resolver Theta
        part1 = MathTex(r"I^2 =", r"(2\pi)", r"\cdot", r"\left(\int_{0}^{\infty} e^{-r^2} r dr\right)", color=MATH_COLOR).scale(1.2)
        frame_t = SurroundingRectangle(separated[1], color=YELLOW)
        self.play(Create(frame_t))
        self.play(TransformMatchingTex(separated, part1), FadeOut(frame_t))
        
        # Resolver r
        part2 = MathTex(r"I^2 =", r"2\pi", r"\cdot", r"\frac{1}{2}", color=MATH_COLOR).scale(1.2)
        frame_r = SurroundingRectangle(part1[3], color=YELLOW)
        self.play(Create(frame_r))
        self.play(TransformMatchingTex(part1, part2), FadeOut(frame_r))
        
        # Resultado I^2
        res_sq = MathTex(r"I^2 = \pi", color=ACTION_COLOR).scale(2)
        self.play(ReplacementTransform(part2, res_sq))
        self.wait(1)
        
        # Resultado I (Simplificado)
        res_simple = MathTex(r"I = \sqrt{\pi}", color=YELLOW).scale(2.5)
        self.play(ReplacementTransform(res_sq, res_simple))
        self.wait(1)
        
        # --- GRAN FINAL: ECUACIÓN COMPLETA ---
        # Aquí sustituimos la "I" por la integral original
        full_equation = MathTex(
            r"\int_{-\infty}^{\infty} e^{-x^2} dx", # 0
            r"=",                                   # 1
            r"\sqrt{\pi}"                           # 2
        ).scale(1.5)
        
        # Colores: Integral azul (como al inicio), Resultado Dorado
        full_equation[0].set_color(MATH_COLOR)
        full_equation[2].set_color(YELLOW)
        
        # Transformación final
        self.play(ReplacementTransform(res_simple, full_equation))
        
        # Marco final parpadeante o destacado
        final_box = SurroundingRectangle(full_equation, color=WHITE, buff=0.3)
        self.play(Create(final_box), run_time=1)
        self.play(Indicate(full_equation, scale_factor=1.1, color=ACTION_COLOR))
        
        self.wait(4)
