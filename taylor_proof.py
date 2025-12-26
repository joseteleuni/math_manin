from manim import *

class TaylorPolynomialDerivation(Scene):
    def construct(self):
        # --- CONFIGURACIÓN DE COLORES Y ESTILOS ---
        COLOR_CN = ORANGE
        COLOR_VAL = TEAL
        COLOR_FX = BLUE
        COLOR_RESULT = GREEN
        COLOR_APPROX = YELLOW
        
        # --- INTRODUCCIÓN ---
        title = Text("Teorema de Taylor", font_size=40, color=GREEN).to_edge(UP)
        intro_text_1 = Text("¿Cómo calculamos funciones trascendentes?", font_size=30, color=GRAY)
        intro_text_2 = Text("sen(x), cos(x), e^x, ln(x)...", font_size=30, color=BLUE).next_to(intro_text_1, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(intro_text_1), FadeIn(intro_text_2))
        self.wait(2)
        
        approx_text = Text("¡Las aproximamos con polinomios!", font_size=32, color=YELLOW).next_to(intro_text_2, DOWN)
        self.play(Write(approx_text))
        self.wait(1)
        
        approx_eq = MathTex(
            "f(x)", "\\approx", "c_0 + c_1(x-a) + c_2(x-a)^2 + \\dots"
        ).scale(1.2).next_to(approx_text, DOWN, buff=1)
        approx_eq.set_color_by_tex("f(x)", COLOR_FX)
        self.set_color_cn(approx_eq, COLOR_CN)
        
        self.play(Write(approx_eq))
        self.wait(2)
        
        self.play(
            FadeOut(intro_text_1), FadeOut(intro_text_2), 
            FadeOut(approx_text), FadeOut(approx_eq)
        )

        # --- LAYOUT ---
        # Coeficientes a la izquierda
        results_start_pos = UP * 2.8 + LEFT * 5.5
        found_coeffs = [] 
        
        # Área de trabajo (Centro-Derecha)
        # Definimos posiciones verticales para los 3 pasos
        # 1. Función a derivar
        POS_LINE_1 = UP * 2.2 + RIGHT * 0.5
        # 2. Función derivada
        POS_LINE_2 = UP * 0.0 + RIGHT * 0.5
        # 3. Función evaluada
        POS_LINE_3 = DOWN * 2.2 + RIGHT * 0.5
        
        LABEL_DERIV_POS = (POS_LINE_1 + POS_LINE_2) / 2
        LABEL_EVAL_POS = (POS_LINE_2 + POS_LINE_3) / 2
        
        EQ_SCALE = 0.75 # Un poco más pequeño para que quepa todo verticalmente

        # Textos reutilizables
        deriv_text = Text("Derivando", font_size=24, color=YELLOW).move_to(LABEL_DERIV_POS)
        eval_text = Text("Evaluando en x = a", font_size=24, color=YELLOW).move_to(LABEL_EVAL_POS)

        # ============ c_0 ============
        # f(x) = ...
        # Evaluando -> f(a) = ...
        
        poly_tex = [
            "f(x)", "=", 
            "c_0", "+", 
            "c_1", "(x-a)", "+", 
            "c_2", "(x-a)^2", "+", 
            "c_3", "(x-a)^3", "+", 
            "c_4", "(x-a)^4", "+", 
            "\\dots"
        ]
        
        eq_main = MathTex(*poly_tex).scale(EQ_SCALE).move_to(POS_LINE_2) # Start in middle
        eq_main.set_color_by_tex("f(x)", COLOR_FX)
        self.set_color_cn(eq_main, COLOR_CN)
        
        self.play(Write(eq_main))
        self.wait(1)

        # Evaluar
        self.play(FadeIn(eval_text))
        
        eq_c0_eval = MathTex(
            "f(a)", "=", "c_0", "+", "0", "+", "0", "+", "\\dots"
        ).scale(EQ_SCALE).move_to(POS_LINE_3)
        eq_c0_eval.set_color_by_tex("f(a)", COLOR_FX)
        self.set_color_cn(eq_c0_eval, COLOR_CN)
        
        self.play(Write(eq_c0_eval)) # Write below instead of transform
        self.wait(1)
        
        # Resultado
        res_c0 = MathTex("c_0", "=", "f(a)").scale(0.7)
        res_c0.set_color_by_tex("c_0", COLOR_CN)
        res_c0.set_color_by_tex("f(a)", COLOR_RESULT)
        res_c0.move_to(results_start_pos)
        
        # Transform from evaluated equation to result list
        self.play(Transform(eq_c0_eval, res_c0))
        found_coeffs.append(eq_c0_eval) 
        
        # Clean up for next act
        self.play(FadeOut(eq_main), FadeOut(eval_text))


        # ============ c_1 ============
        # 1. Función previa (f(x))
        prev_func = MathTex(
             "f(x)", "=", "c_0", "+", "c_1", "(x-a)", "+", "c_2", "(x-a)^2", "+", "\\dots"
        ).scale(EQ_SCALE).move_to(POS_LINE_1)
        prev_func.set_color_by_tex("f(x)", COLOR_FX)
        self.set_color_cn(prev_func, COLOR_CN)
        
        self.play(FadeIn(prev_func))
        self.play(FadeIn(deriv_text))

        # 2. Derivar (f'(x))
        eq_d1 = MathTex(
            "f'(x)", "=", "c_1", "+", "2", "c_2", "(x-a)", "+", "3", "c_3", "(x-a)^2", "+", "\\dots"
        ).scale(EQ_SCALE).move_to(POS_LINE_2)
        eq_d1.set_color_by_tex("f'(x)", COLOR_FX)
        self.set_color_cn(eq_d1, COLOR_CN)
        
        self.play(Write(eq_d1))
        self.wait(1)
        
        # 3. Evaluar (f'(a))
        self.play(FadeIn(eval_text))
        
        eq_d1_eval = MathTex(
            "f'(a)", "=", "c_1", "+", "0", "+", "0", "+", "\\dots"
        ).scale(EQ_SCALE).move_to(POS_LINE_3)
        eq_d1_eval.set_color_by_tex("f'(a)", COLOR_FX)
        self.set_color_cn(eq_d1_eval, COLOR_CN)
        
        self.play(Write(eq_d1_eval))
        self.wait(1)
        
        # 4. Resultado (Move to left)
        res_c1 = MathTex("c_1", "=", "\\frac{f'(a)}{1!}").scale(0.7)
        res_c1.set_color_by_tex("c_1", COLOR_CN)
        res_c1.set_color_by_tex("f'(a)", COLOR_RESULT)
        res_c1.next_to(found_coeffs[-1], DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Transform(eq_d1_eval, res_c1))
        found_coeffs.append(eq_d1_eval)
        
        # Clear Right Side
        self.play(
            FadeOut(prev_func), FadeOut(deriv_text), 
            FadeOut(eq_d1), FadeOut(eval_text)
        )

        # ============ c_2 ============
        prev_func = MathTex(
            "f'(x)", "=", "c_1", "+", "2", "c_2", "(x-a)", "+", "3", "c_3", "(x-a)^2", "+", "\\dots"
        ).scale(EQ_SCALE).move_to(POS_LINE_1)
        prev_func.set_color_by_tex("f'(x)", COLOR_FX)
        self.set_color_cn(prev_func, COLOR_CN)
        
        self.play(FadeIn(prev_func), FadeIn(deriv_text))
        
        eq_d2 = MathTex(
            "f''(x)", "=", "2 \\cdot 1", "c_2", "+", "3 \\cdot 2", "c_3", "(x-a)", "+", "4 \\cdot 3", "c_4", "(x-a)^2", "+", "\\dots"
        ).scale(EQ_SCALE).move_to(POS_LINE_2)
        eq_d2.set_color_by_tex("f''(x)", COLOR_FX)
        self.set_color_cn(eq_d2, COLOR_CN)
        
        self.play(Write(eq_d2))
        self.wait(1)
        
        self.play(FadeIn(eval_text))
        
        eq_d2_eval = MathTex(
            "f''(a)", "=", "2!", "c_2"
        ).scale(EQ_SCALE).move_to(POS_LINE_3)
        eq_d2_eval.set_color_by_tex("f''(a)", COLOR_FX)
        eq_d2_eval.set_color_by_tex("2!", RED)
        self.set_color_cn(eq_d2_eval, COLOR_CN)
        
        self.play(Write(eq_d2_eval))
        self.wait(1)
        
        res_c2 = MathTex("c_2", "=", "\\frac{f''(a)}{2!}").scale(0.7)
        res_c2.set_color_by_tex("c_2", COLOR_CN)
        res_c2.set_color_by_tex("f''(a)", COLOR_RESULT)
        res_c2.next_to(found_coeffs[-1], DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Transform(eq_d2_eval, res_c2))
        found_coeffs.append(eq_d2_eval)
        
        self.play(
            FadeOut(prev_func), FadeOut(deriv_text), 
            FadeOut(eq_d2), FadeOut(eval_text)
        )

        # ============ c_3 ============
        prev_func = MathTex(
             "f''(x)", "=", "2!", "c_2", "+", "3 \\cdot 2", "c_3", "(x-a)", "+", "\\dots"
        ).scale(EQ_SCALE).move_to(POS_LINE_1)
        prev_func.set_color_by_tex("f''(x)", COLOR_FX)
        self.set_color_cn(prev_func, COLOR_CN)
        
        self.play(FadeIn(prev_func), FadeIn(deriv_text))

        eq_d3 = MathTex(
            "f'''(x)", "=", "3 \\cdot 2 \\cdot 1", "c_3", "+", "4 \\cdot 3 \\cdot 2", "c_4", "(x-a)", "+", "\\dots"
        ).scale(EQ_SCALE).move_to(POS_LINE_2)
        eq_d3.set_color_by_tex("f'''(x)", COLOR_FX)
        self.set_color_cn(eq_d3, COLOR_CN)
        
        self.play(Write(eq_d3))
        self.wait(1)
        
        self.play(FadeIn(eval_text))
        
        eq_d3_eval = MathTex(
            "f'''(a)", "=", "3!", "c_3"
        ).scale(EQ_SCALE).move_to(POS_LINE_3)
        eq_d3_eval.set_color_by_tex("f'''(a)", COLOR_FX)
        eq_d3_eval.set_color_by_tex("3!", RED)
        self.set_color_cn(eq_d3_eval, COLOR_CN)
        
        self.play(Write(eq_d3_eval))
        self.wait(1)
        
        res_c3 = MathTex("c_3", "=", "\\frac{f'''(a)}{3!}").scale(0.7)
        res_c3.set_color_by_tex("c_3", COLOR_CN)
        res_c3.set_color_by_tex("f'''(a)", COLOR_RESULT)
        res_c3.next_to(found_coeffs[-1], DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Transform(eq_d3_eval, res_c3))
        found_coeffs.append(eq_d3_eval)
        
        self.play(
            FadeOut(prev_func), FadeOut(deriv_text), 
            FadeOut(eq_d3), FadeOut(eval_text)
        )

        # ============ c_4 ============
        prev_func = MathTex(
            "f'''(x)", "=", "3!", "c_3", "+", "4 \\cdot 3 \\cdot 2", "c_4", "(x-a)", "+", "\\dots"
        ).scale(EQ_SCALE).move_to(POS_LINE_1)
        prev_func.set_color_by_tex("f'''(x)", COLOR_FX)
        self.set_color_cn(prev_func, COLOR_CN)
        
        self.play(FadeIn(prev_func), FadeIn(deriv_text))

        eq_d4 = MathTex(
            "f^{(4)}(x)", "=", "4 \\cdot 3 \\cdot 2 \\cdot 1", "c_4", "+", "\\dots"
        ).scale(EQ_SCALE).move_to(POS_LINE_2)
        eq_d4.set_color_by_tex("f^{(4)}(x)", COLOR_FX)
        self.set_color_cn(eq_d4, COLOR_CN)
        
        self.play(Write(eq_d4))
        self.wait(1)
        
        self.play(FadeIn(eval_text))
        
        eq_d4_eval = MathTex(
            "f^{(4)}(a)", "=", "4!", "c_4"
        ).scale(EQ_SCALE).move_to(POS_LINE_3)
        eq_d4_eval.set_color_by_tex("f^{(4)}(a)", COLOR_FX)
        eq_d4_eval.set_color_by_tex("4!", RED)
        self.set_color_cn(eq_d4_eval, COLOR_CN)
        
        self.play(Write(eq_d4_eval))
        self.wait(1)
        
        res_c4 = MathTex("c_4", "=", "\\frac{f^{(4)}(a)}{4!}").scale(0.7)
        res_c4.set_color_by_tex("c_4", COLOR_CN)
        res_c4.set_color_by_tex("f^{(4)}(a)", COLOR_RESULT)
        res_c4.next_to(found_coeffs[-1], DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Transform(eq_d4_eval, res_c4))
        found_coeffs.append(eq_d4_eval)
        
        self.play(
            FadeOut(prev_func), FadeOut(deriv_text), 
            FadeOut(eq_d4), FadeOut(eval_text)
        )

        # --- INDUCCIÓN ---
        induc_text = Text("Por inducción matemática...", font_size=32, color=YELLOW).move_to(POS_LINE_2).shift(UP*1)
        self.play(Write(induc_text))
        self.wait(1)
        
        res_cn = MathTex("c_n", "=", "\\frac{f^{(n)}(a)}{n!}").scale(0.9)
        res_cn.set_color_by_tex("c_n", COLOR_CN)
        res_cn.set_color_by_tex("f^{(n)}(a)", COLOR_RESULT)
        res_cn.next_to(found_coeffs[-1], DOWN, buff=0.5, aligned_edge=LEFT)
        
        box_cn = SurroundingRectangle(res_cn, color=YELLOW, buff=0.15)
        
        self.play(Write(res_cn))
        self.play(Create(box_cn))
        self.wait(2)
        
        # --- CONCLUSIÓN FINAL ---
        self.play(FadeOut(induc_text))
        
        final_formula = MathTex(
            "f(x) = \\sum_{n=0}^{\\infty} \\frac{f^{(n)}(a)}{n!} (x-a)^n"
        ).scale(1.3).move_to(POS_LINE_2)
        
        final_formula.set_color_by_tex("f(x)", COLOR_FX)
        
        final_label = Text("Serie de Taylor", font_size=36).next_to(final_formula, UP)
        
        self.play(Write(final_label), Write(final_formula))
        self.play(Indicate(final_formula, color=COLOR_APPROX))
        self.wait(3)


    def set_color_cn(self, mobject, color):
        indices = ["c_0", "c_1", "c_2", "c_3", "c_4", "c_n"]
        for idx in indices:
            mobject.set_color_by_tex(idx, color)
