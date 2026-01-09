from manim import *

class EulerIdentityProof(Scene):
    def construct(self):
        # --- COLORES Y ESTILOS ---
        COLOR_E = YELLOW
        COLOR_I = RED
        COLOR_X = BLUE
        COLOR_SIN = GREEN
        COLOR_COS = PURPLE
        COLOR_TITLE = TEAL
        
        # --- 1. INTRODUCCIÓN Y DEFINICIÓN DE e^x ---
        title = Text("La Fórmula de Euler", font_size=60, color=COLOR_TITLE).to_edge(UP)
        
        # Imagen de Euler
        try:
            euler_img = ImageMobject("euler.jpg")
            euler_img.scale(0.6).shift(DOWN * 0.5)
        except:
            # Placeholder si no existe la imagen
            euler_img = Square(side_length=3, color=GRAY, fill_opacity=0.5)
            euler_img.add(Text("Foto de\nLeonhard Euler", font_size=20))
            euler_img.shift(DOWN * 0.5)

        subtitle = Text("Una demostración visual usando Series de Taylor", font_size=30, color=GRAY).next_to(euler_img, DOWN)
        
        self.play(Write(title), FadeIn(euler_img), FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(subtitle), FadeOut(euler_img))
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
            ex_def.animate.to_edge(UP).scale(0.8),
            FadeOut(title) # Desaparece el título mientras sube la fórmula para evitar traslape
        )

        # --- 2. DEFINICIÓN DE e^{ix} ---
        # Explicación texto
        def_text = Text("Definimos e elevado a un imaginario:", font_size=32).next_to(ex_def, DOWN, buff=1)
        self.play(Write(def_text))
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
        
        self.play(TransformMatchingTex(ex_def.copy(), eix_eq), FadeOut(def_text)) # Transformación visual
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
        ref_group = VGroup(cox_eq, sin_eq).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_corner(DL, buff=0.5).scale(0.9)
        
        self.play(Write(ref_group))
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
            FadeOut(ref_group), # Ocultar definiciones de referencia
            Transform(eix_eq, final_formula)
        )
        
        # Caja final
        box = SurroundingRectangle(eix_eq, color=WHITE, buff=0.2)
        self.play(Create(box))
        
        # Toque final bonito: Brillito o indicación
        self.play(Indicate(eix_eq, scale_factor=1.2, color=YELLOW))
        
        self.wait(3)
