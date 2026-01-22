from manim import *

# Configuración para TikTok (Vertical 1080x1920)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class EulerIdentityProof(Scene):
    def construct(self):
        # --- COLORES Y ESTILOS ---
        COLOR_E = YELLOW
        COLOR_I = RED
        COLOR_X = BLUE
        COLOR_SIN = GREEN
        COLOR_COS = PURPLE
        COLOR_TITLE = TEAL
        
        # --- 1. INTRODUCCIÓN (PORTADA) ---
        # Lado Izquierdo (Ahora Superior en TikTok): Imagen
        try:
            euler_img = ImageMobject("euler.jpg")
            euler_img.scale(1.2).to_edge(UP, buff=1)
        except:
            # Placeholder si no existe la imagen
            euler_img = Square(side_length=4, color=GRAY, fill_opacity=0.5)
            euler_img.add(Text("Cargar euler.jpg", font_size=24))
            euler_img.to_edge(UP, buff=1)

        # Lado Derecho: Título y Fórmula
        title_right = Text("La fórmula de Euler", font_size=48, color=COLOR_TITLE)
        formula_right = MathTex(
            "e^{ix} = \\cos x + i \\sin x",
            font_size=48
        )
        # Aplicamos colores a la fórmula para mantener consistencia
        formula_right.set_color_by_tex("e", COLOR_E)
        formula_right.set_color_by_tex("i", COLOR_I)
        formula_right.set_color_by_tex("\\cos", COLOR_COS)
        formula_right.set_color_by_tex("\\sin", COLOR_SIN)
        
        right_content = VGroup(title_right, formula_right).arrange(DOWN, buff=0.8)
        right_content.next_to(euler_img, DOWN, buff=1)

        # Animación inicial
        self.play(
            FadeIn(euler_img, shift=RIGHT),
            Write(right_content)
        )
        self.wait(3)
        
        # Limpiar pantalla para la demostración
        self.play(FadeOut(euler_img), FadeOut(right_content))
        self.wait(1)

        # Definición de Taylor de e^x
        ex_def = MathTex(
            "e^x", "=", "\\sum_{n=0}^{\\infty} \\frac{x^n}{n!}", "=", 
            "1", "+", "x", "+", "\\frac{x^2}{2!}", "+", "\\frac{x^3}{3!}", "+", "\\frac{x^4}{4!}", "+", "\\dots"
        )
        ex_def.set_color_by_tex("x", COLOR_X)
        ex_def.set_color_by_tex("e^x", COLOR_E)
        
        self.play(Write(ex_def))
        self.wait(2)
        
        # Mover arriba para hacer espacio
        self.play(
            ex_def.animate.to_edge(UP).scale(0.8)
        )

        # --- 2. DEFINICIÓN DE e^{ix} ---
        # Explicación texto
        def_text = Text(
            "Extendiendo analíticamente el valor de x\nal número imaginario ix", 
            font_size=32,
            t2c={"analíticamente": YELLOW, "imaginario ix": COLOR_I}
        ).next_to(ex_def, DOWN, buff=1)
        
        self.play(SpiralIn(def_text))
        self.wait(1)
        
        # Sustitución x -> ix
        eix_eq = MathTex(
            "e^{ix}", "=", 
            "1", "+", "(ix)", "+", "\\frac{(ix)^2}{2!}", "+", "\\frac{(ix)^3}{3!}", "+", "\\frac{(ix)^4}{4!}", "+", "\\frac{(ix)^5}{5!}", "+", "\\dots"
        )
        eix_eq.set_color_by_tex("x", COLOR_X)
        eix_eq.set_color_by_tex("i", COLOR_I)
        eix_eq.set_color_by_tex("e^{ix}", COLOR_E)
        eix_eq.scale(0.9)
        eix_eq.next_to(def_text, DOWN)
        
        self.play(
            TransformMatchingTex(ex_def.copy(), eix_eq, path_arc=PI/2), 
            FadeOut(def_text, shift=DOWN)
        )
        self.wait(2)

        # --- 3. POTENCIAS DE i ---
        # Mostrar simplificación de potencias
        # i^0 = 1, i^1 = i, i^2 = -1, i^3 = -i, i^4 = 1
        
        powers_explanation = VGroup(
            MathTex("i^2 = -1", color=COLOR_I),
            MathTex("i^3 = -i", color=COLOR_I),
            MathTex("i^4 = 1", color=COLOR_I)
        ).arrange(RIGHT, buff=1).to_edge(DOWN)
        
        self.play(FadeIn(powers_explanation))
        self.wait(2)
        
        eix_simplified = MathTex(
            "e^{ix}", "=", 
            "1", "+", "i", "x", "-", "\\frac{x^2}{2!}", "-", "i", "\\frac{x^3}{3!}", "+", "\\frac{x^4}{4!}", "+", "i", "\\frac{x^5}{5!}", "-", "\\dots"
        )
        eix_simplified.set_color_by_tex("x", COLOR_X)
        eix_simplified.set_color_by_tex("i", COLOR_I)
        eix_simplified.set_color_by_tex("e^{ix}", COLOR_E)
        eix_simplified.scale(0.9).move_to(eix_eq)

        # Animación de simplificación término a término
        self.play(Transform(eix_eq, eix_simplified))
        self.play(FadeOut(powers_explanation))
        self.wait(2)
        
        # Mover e^{ix} arriba
        self.play(
            FadeOut(ex_def), # Ya no necesitamos la original
            eix_eq.animate.to_edge(UP)
        )

        # --- 4. SERIES DE TAYLOR DE COS Y SIN ---
        
        cox_eq = MathTex(
            "\\cos(x)", "=", "1", "-", "\\frac{x^2}{2!}", "+", "\\frac{x^4}{4!}", "-", "\\dots"
        ).scale(0.8)
        cox_eq.set_color_by_tex("cos", COLOR_COS)
        cox_eq.set_color_by_tex("x", COLOR_X)
        
        sin_eq = MathTex(
            "\\sin(x)", "=", "x", "-", "\\frac{x^3}{3!}", "+", "\\frac{x^5}{5!}", "-", "\\dots"
        ).scale(0.8)
        sin_eq.set_color_by_tex("sin", COLOR_SIN)
        sin_eq.set_color_by_tex("x", COLOR_X)
        
        # Posicionamiento a la izquierda abajo
        ref_group = VGroup(cox_eq, sin_eq).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Título para las series
        taylor_title = Text(
            "desarrollo de series de taylor para sinx y cosx", 
            font_size=20, 
            color=GRAY_A,
            slant=ITALIC
        ).next_to(ref_group, DOWN, buff=0.3)
        
        full_ref = VGroup(ref_group, taylor_title).to_corner(DL, buff=0.5).scale(0.9)
        
        self.play(
            LaggedStart(
                Write(ref_group),
                FadeIn(taylor_title, shift=UP),
                lag_ratio=0.5
            )
        )
        self.play(Indicate(ref_group, color=TEAL))
        self.wait(2)
        
        # --- 5. REAGRUPACIÓN ---
        
        group_text = Text("Agrupamos términos reales e imaginarios", font_size=24, color=YELLOW).next_to(eix_eq, DOWN)
        self.play(FadeIn(group_text))
        
        # Crear versión agrupada
        # Real: (1 - x^2/2! + x^4/4! ...)
        # Imag: + i(x - x^3/3! + x^5/5! ...)
        
        eix_grouped = MathTex(
            "e^{ix}", "=", 
            "\\left(", "1", "-", "\\frac{x^2}{2!}", "+", "\\frac{x^4}{4!}", "-", "\\dots", "\\right)",
            "+", "i", 
            "\\left(", "x", "-", "\\frac{x^3}{3!}", "+", "\\frac{x^5}{5!}", "-", "\\dots", "\\right)"
        )
        eix_grouped.set_color_by_tex("x", COLOR_X)
        eix_grouped.set_color_by_tex("i", COLOR_I)
        eix_grouped.set_color_by_tex("e^{ix}", COLOR_E)
        eix_grouped.set_color_by_tex("1", COLOR_COS) # Highlight real part parts roughly
        eix_grouped.set_color_by_tex("x^2", COLOR_COS)
        eix_grouped.set_color_by_tex("x^4", COLOR_COS)
        
        eix_grouped.scale(0.8).move_to(UP * 0.5) # Escalar y mover arriba para no chocar con las referencias en DL
        
        self.play(
            FadeOut(group_text),
            Transform(eix_eq, eix_grouped)
        )
        self.wait(2)
        
        # --- 6. IDENTIFICACIÓN Y CONCLUSIÓN ---
        
        # Resaltar parte Real = Cos
        brace_real = Brace(eix_grouped[2:11], UP) # parts corresponding to real group
        text_real = brace_real.get_text("$\\cos(x)$").set_color(COLOR_COS)
        
        self.play(GrowFromCenter(brace_real), Write(text_real))
        self.wait(1)
        
        # Resaltar parte Imag = Sin
        brace_imag = Brace(eix_grouped[13:], UP) # parts corresponding to imag group (after i)
        text_imag = brace_imag.get_text("$\\sin(x)$").set_color(COLOR_SIN)
        
        self.play(GrowFromCenter(brace_imag), Write(text_imag))
        self.wait(1)
        
        # Transformar a la fórmula final
        final_formula = MathTex(
            "e^{ix}", "=", "\\cos(x)", "+", "i", "\\sin(x)"
        ).scale(1.5)
        final_formula.set_color_by_tex("e^{ix}", COLOR_E)
        final_formula.set_color_by_tex("cos", COLOR_COS)
        final_formula.set_color_by_tex("sin", COLOR_SIN)
        final_formula.set_color_by_tex("i", COLOR_I)
        final_formula.set_color_by_tex("x", COLOR_X)
        
        self.play(
            FadeOut(brace_real), FadeOut(text_real),
            FadeOut(brace_imag), FadeOut(text_imag),
            FadeOut(full_ref), # Ocultar definiciones de referencia
            ReplacementTransform(eix_eq, final_formula)
        )
        
        # Caja final aplicada directamente al nuevo objeto
        box = SurroundingRectangle(final_formula, color=WHITE, buff=0.2)
        self.play(Create(box))
        
        # Toque final bonito: Brillito o indicación
        self.play(Indicate(final_formula, scale_factor=1.2, color=YELLOW))
        self.wait(2)

        # --- 7. INTERPRETACIÓN GEOMÉTRICA (CIRCUNFERENCIA TRIGONOMÉTRICA) ---
        # Definimos el grupo con los objetos actuales en escena
        final_group = VGroup(final_formula, box)
        
        self.play(
            final_group.animate.to_edge(UP, buff=0.3).scale(0.6),
            run_time=2
        )
        self.wait(0.5)

        # Crear Plano y Circunferencia ajustados a vertical
        plane = ComplexPlane(
            x_range=[-1.2, 1.2, 0.5],
            y_range=[-1.2, 1.2, 0.5],
            x_length=8,
            y_length=8,
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 2,
                "stroke_opacity": 0.2
            }
        ).shift(DOWN * 2)
        
        RADIUS = plane.c2p(1, 0)[0] - plane.c2p(0, 0)[0]
        circle = Circle(radius=RADIUS, color=WHITE, stroke_width=3).move_to(plane.get_origin())
        
        # Etiquetas de ejes profesionales
        real_label = MathTex("\\text{Re}", font_size=32).next_to(plane.get_x_axis(), RIGHT)
        imag_label = MathTex("\\text{Im}", font_size=32).next_to(plane.get_y_axis().get_top(), DOWN + RIGHT, buff=0.4)

        self.play(
            Create(plane),
            Create(circle),
            Write(real_label),
            Write(imag_label),
            run_time=2
        )

        # Variables dinámicas (ValueTracker para el ángulo)
        theta_tracker = ValueTracker(0)

        # Vector radio (e^{ix})
        vector = always_redraw(lambda: 
            Arrow(
                start=plane.get_origin(),
                end=plane.c2p(
                    np.cos(theta_tracker.get_value()), 
                    np.sin(theta_tracker.get_value())
                ),
                buff=0,
                color=COLOR_E,
                stroke_width=6
            )
        )

        # Componente Coseno (Horizontal)
        cos_line = always_redraw(lambda:
            Line(
                start=plane.get_origin(),
                end=plane.c2p(np.cos(theta_tracker.get_value()), 0),
                color=COLOR_COS,
                stroke_width=7
            )
        )

        # Componente Seno (Vertical)
        sin_line = always_redraw(lambda:
            Line(
                start=plane.c2p(np.cos(theta_tracker.get_value()), 0),
                end=plane.c2p(np.cos(theta_tracker.get_value()), np.sin(theta_tracker.get_value())),
                color=COLOR_SIN,
                stroke_width=7
            )
        )

        # Etiquetas dinámicas
        cos_label = always_redraw(lambda:
            MathTex("\\cos(x)", color=COLOR_COS, font_size=36)
            .next_to(cos_line, DOWN, buff=0.1)
            .add_background_rectangle()
        )
        
        sin_label = always_redraw(lambda:
            MathTex("\\sin(x)", color=COLOR_SIN, font_size=36)
            .next_to(sin_line, RIGHT, buff=0.1)
            .add_background_rectangle()
        )

        # Punto en el extremo
        dot = always_redraw(lambda:
            Dot(point=vector.get_end(), color=COLOR_E, radius=0.08)
        )

        # ARCO DEL ÁNGULO CORREGIDO: Centrado en el origen del plano
        angle_arc = always_redraw(lambda:
            Arc(
                radius=0.6, 
                start_angle=0, 
                angle=theta_tracker.get_value(),
                color=YELLOW,
                stroke_width=4,
                arc_center=plane.get_origin()
            )
        )
        
        angle_text = always_redraw(lambda:
            MathTex(f"x = {theta_tracker.get_value():.2f} \\text{{ rad}}", font_size=36)
            .to_corner(UR, buff=0.5)
            .add_background_rectangle()
        )

        # Etiqueta e^{ix} en la punta del vector
        vector_label = always_redraw(lambda:
            MathTex("e^{ix}", color=COLOR_E, font_size=32)
            .next_to(dot, UR, buff=0.1)
            .add_background_rectangle()
        )

        # Animación de elementos dinámicos
        self.play(
            GrowArrow(vector),
            Create(cos_line),
            Create(sin_line),
            FadeIn(cos_label),
            FadeIn(sin_label),
            FadeIn(dot),
            FadeIn(vector_label),
            Create(angle_arc),
            Write(angle_text)
        )
        self.wait(1)

        # ROTACIÓN DE 360 GRADOS
        self.play(
            theta_tracker.animate.set_value(2 * PI),
            run_time=10,
            rate_func=linear
        )
        
        # Terminar el video inmediatamente después de la rotación
        self.wait(2)
