from manim import *

# Configuración visual para que se vea "Tech"
config.background_color = "#1e1e1e" # Un gris oscuro elegante, mejor que negro puro

class VectorSpaceMasterclass(Scene):
    def construct(self):
        self.presentation_cover()
        # Solo lo que importa: Definición y Axiomas
        self.vector_space_axioms()

    def presentation_cover(self):
        # --- PORTADA ESTÉTICA ---
        
        # Lado Izquierdo: Placeholder para Foto
        # Nota: El usuario puede reemplazar "peano.jpg" con la ruta de su imagen
        # Usamos un rectángulo elegante como placeholder
        photo_frame = RoundedRectangle(corner_radius=0.5, height=5, width=4, color=WHITE)
        photo_placeholder = Tex(r"Insertar Foto\\Giuseppe Peano", color=GREY)
        
        # Intentar cargar imagen si existe, sino mostrar placeholder
        try:
            photo = ImageMobject("peano.jpg").scale_to_fit_height(5)
            left_content = Group(photo, photo_frame)
        except:
            left_content = VGroup(photo_frame, photo_placeholder)
            
        left_content.to_edge(LEFT, buff=1.5)

        # Lado Derecho: Título y Autor
        
        # Título principal
        title = Tex(r"\textbf{Espacios Vectoriales}", font_size=60, color=PINK)
        
        # Línea separadora elegante
        line = Line(LEFT, RIGHT, color=WHITE).set_length(6).next_to(title, DOWN)
        
        # Nombre del Matemático
        author = Tex(r"\textsc{Giuseppe Peano}", font_size=40, color=BLUE_B).next_to(line, DOWN, buff=0.5)
        
        # Agrupar lado derecho
        right_content = VGroup(title, line, author).next_to(left_content, RIGHT, buff=2)
        
        # Animación de entrada
        self.play(
            DrawBorderThenFill(photo_frame) if isinstance(left_content, VGroup) else FadeIn(left_content),
            run_time=1.5
        )
        if isinstance(left_content, VGroup):
             self.play(Write(photo_placeholder))

        self.play(
            Write(title),
            Create(line),
            FadeIn(author, shift=UP),
            run_time=2
        )
        
        self.wait(2)
        
        # Transición
        self.play(
            FadeOut(left_content),
            FadeOut(right_content),
            run_time=1
        )


    def vector_space_axioms(self):
        # --- DEFINICIÓN FORMAL ---
        self.formal_definition()

        # --- CONFIGURACIÓN VISUAL GLOBAL ---
        self.origin_point = DOWN * 2.5 + LEFT * 0.0 # Bajar el origen
        self.vec_scale = 1.5 # Hacer vectores más grandes

        # --- AXIOMAS DEL ESPACIO VECTORIAL (AHORA 8) ---
        
        # Configuración del plano
        plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 2,
                "stroke_opacity": 0.3
            }
        )
        # Mover el plano visualmente
        plane.shift(self.origin_point)
        
        self.play(Create(plane), run_time=1.5)

        title_main = Tex(r"\textbf{Los 8 Axiomas del Espacio Vectorial}", font_size=48).to_edge(UP)
        self.play(Write(title_main))
        self.wait(1)
        self.play(FadeOut(title_main))

        # --- AXIOMAS DE LA SUMA ---

        # 1. Conmutatividad (antes 2)
        self.axiom_commutativity()

        # 2. Asociatividad (antes 3)
        self.axiom_associativity()

        # 3. Elemento Neutro (antes 4)
        self.axiom_zero_vector()

        # 4. Inverso Aditivo (antes 5)
        self.axiom_additive_inverse()

        # --- AXIOMAS DE LA MULTIPLICACIÓN POR ESCALAR ---

        # 5. Distributividad 1: c(u+v) = cu + cv (antes 7)
        self.axiom_distributivity_scalar_sum()

        # 6. Distributividad 2: (c+d)u = cu + du (antes 8)
        self.axiom_distributivity_scalars()

        # 7. Asociatividad Escalar: c(du) = (cd)u (antes 9)
        self.axiom_scalar_associativity()

        # 8. Identidad Escalar: 1u = u (antes 10)
        self.axiom_scalar_identity()
        
        # Limpieza final
        self.clear()
        plane = NumberPlane(background_line_style={"stroke_opacity": 0.2})
        self.add(plane)

    def get_vec(self, coords, color=WHITE):
        """Helper para crear vectores escalados y posicionados desde el nuevo origen"""
        scaled = np.array(coords) * self.vec_scale
        # Si coords es 2D, asegurar 3D para manim
        if len(scaled) == 2:
            scaled = np.array([scaled[0], scaled[1], 0])
        return Vector(scaled, color=color).shift(self.origin_point)

    def formal_definition(self):
        # Texto matemático LaTeX solicitado - SIN CAMBIOS
        definition_title = Tex(r"\textbf{Definición de Espacio Vectorial}", font_size=40, color=PINK).to_edge(UP)
        def_text = Tex(r"Un espacio vectorial sobre un cuerpo $K$ es un conjunto no vacío $V$,\\", r"dotado de dos operaciones cerradas:", font_size=32).next_to(definition_title, DOWN, buff=0.5)
        # Parte 2: Suma
        suma_tex = MathTex(
            r"\text{Suma } + : V \times V &\rightarrow V \\",
            r"(u, v) &\mapsto w = u + v",
            tex_environment="align*",
            font_size=36, 
            color=YELLOW
        ).next_to(def_text, DOWN, buff=0.5)
        
        # Parte 3: Producto por Escalar
        prod_tex = MathTex(
            r"\text{Producto } \cdot : K \times V &\rightarrow V \\",
            r"(a, u) &\mapsto v = a \cdot u",
            tex_environment="align*",
            font_size=36, 
            color=BLUE
        ).next_to(suma_tex, DOWN, buff=0.5)
        self.play(Write(definition_title))
        self.play(FadeIn(def_text))
        self.wait(1)
        self.play(Write(suma_tex))
        self.wait(1)
        self.play(Write(prod_tex))
        self.wait(4)
        self.play(FadeOut(definition_title), FadeOut(def_text), FadeOut(suma_tex), FadeOut(prod_tex))

    def axiom_closure_sum(self): 
        pass 

    def axiom_commutativity(self):
        title = MathTex(r"\text{1. Conmutatividad: } u + v = v + u", color=YELLOW).to_corner(UL)
        self.play(Write(title))
        didactic_text = Tex(r"El orden de los factores no altera la suma", font_size=36, color=BLUE_B).next_to(title, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(didactic_text))

        u = self.get_vec([3, 0], color=RED)
        v = self.get_vec([1, 2], color=GREEN)
        
        # --- Camino 1: u + v ---
        lbl_u = MathTex("u").next_to(u.get_center(), DOWN)
        self.play(GrowArrow(u), Write(lbl_u))
        
        # v trasladado al final de u
        # Lógica robusta: shift por el vector de u (u.get_end() - origin)
        v_shifted = v.copy().shift(u.get_end() - self.origin_point)
        lbl_v = MathTex("v").next_to(v_shifted.get_center(), RIGHT)
        self.play(GrowArrow(v_shifted), Write(lbl_v))
        
        # Resultante
        sum_vec_1 = self.get_vec([4, 2], color=YELLOW) # 3+1, 0+2
        lbl_sum_1 = MathTex("u+v").next_to(sum_vec_1.get_end(), UP)
        self.play(GrowArrow(sum_vec_1), Write(lbl_sum_1))
        
        self.wait(1)
        self.play(FadeOut(u), FadeOut(v_shifted), FadeOut(lbl_u), FadeOut(lbl_v))
        
        # --- Camino 2: v + u ---
        lbl_v_orig = MathTex("v").next_to(v.get_center(), LEFT)
        self.play(GrowArrow(v), Write(lbl_v_orig))
        
        u_shifted = u.copy().shift(v.get_end() - self.origin_point)
        lbl_u_shifted = MathTex("u").next_to(u_shifted.get_center(), UP)
        self.play(GrowArrow(u_shifted), Write(lbl_u_shifted))
        
        sum_vec_2 = self.get_vec([4, 2], color=YELLOW) # Mismo vector
        lbl_sum_2 = MathTex("v+u").next_to(sum_vec_2.get_end(), UP)
        
        self.play(Transform(lbl_sum_1, lbl_sum_2))
        self.play(Flash(sum_vec_1, color=WHITE))
        self.wait(1)
        self.play(FadeOut(Group(v, u_shifted, lbl_v_orig, lbl_u_shifted, sum_vec_1, lbl_sum_1, title, didactic_text)))

    def axiom_associativity(self):
        title = MathTex(r"\text{2. Asociatividad: } (u + v) + w = u + (v + w)", color=YELLOW).to_corner(UL)
        self.play(Write(title))
        didactic_text = Tex(r"Agrupar de formas distintas no afecta el destino final", font_size=36, color=BLUE_B).next_to(title, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(didactic_text))

        u = self.get_vec([1, 1], color=RED)
        v = self.get_vec([2, 0], color=GREEN)
        w = self.get_vec([1, 1.5], color=BLUE)

        # Lado Izquierdo
        self.play(GrowArrow(u))
        lbl_u = MathTex("u").next_to(u.get_center(), UP+LEFT)
        self.play(Write(lbl_u))

        v_s = v.copy().shift(u.get_end() - self.origin_point)
        lbl_v = MathTex("v").next_to(v_s.get_center(), DOWN)
        self.play(GrowArrow(v_s), Write(lbl_v))
        
        u_plus_v = self.get_vec([3, 1], color=YELLOW) # 1+2, 1+0
        lbl_uv = MathTex("(u+v)").next_to(u_plus_v.get_center(), UP)
        self.play(GrowArrow(u_plus_v), Write(lbl_uv))
        
        w_s = w.copy().shift(u_plus_v.get_end() - self.origin_point)
        lbl_w = MathTex("w").next_to(w_s.get_center(), RIGHT)
        self.play(GrowArrow(w_s), Write(lbl_w))
        
        final_pt = Dot(w_s.get_end(), color=WHITE)
        final_vec = Arrow(start=self.origin_point, end=w_s.get_end(), color=WHITE, stroke_width=2, buff=0) 
        lbl_final = MathTex("R").next_to(final_pt, UP)
        
        self.play(Create(final_pt), GrowArrow(final_vec), Write(lbl_final))
        self.wait(1)
        
        self.play(FadeOut(u), FadeOut(v_s), FadeOut(u_plus_v), FadeOut(w_s), FadeOut(lbl_u), FadeOut(lbl_v), FadeOut(lbl_uv), FadeOut(lbl_w))

        # Lado Derecho
        self.play(GrowArrow(u))
        self.play(Write(lbl_u))
        
        v_on_u = v.copy().shift(u.get_end() - self.origin_point).set_opacity(0.5)
        w_on_v = w.copy().shift(v_on_u.get_end() - self.origin_point).set_opacity(0.5)
        
        self.play(GrowArrow(v_on_u))
        self.play(GrowArrow(w_on_v))
        
        # v+w empieza al final de u, y equivale a sumar vector(v)+vector(w)
        # Vector v+w (coords 3, 1.5)
        # Shifted to u
        v_plus_w_vec = np.array([3, 1.5, 0]) * self.vec_scale
        v_plus_w = Vector(v_plus_w_vec, color=ORANGE).shift(u.get_end()) # Shift normal funciona pq Vector crea desde ORIGIN
        lbl_vw = MathTex("(v+w)").next_to(v_plus_w.get_center(), RIGHT)
        
        self.play(GrowArrow(v_plus_w), Write(lbl_vw))
        self.play(Flash(final_pt))
        self.wait(1)
        self.play(FadeOut(Group(u, v_on_u, w_on_v, v_plus_w, final_pt, final_vec, lbl_final, lbl_vw, lbl_u, title, didactic_text)))

    def axiom_zero_vector(self):
        title = MathTex(r"\text{3. Elemento Neutro: } u + 0 = u", color=YELLOW).to_corner(UL)
        self.play(Write(title))
        didactic_text = Tex(r"El vector nulo no cambia nada", font_size=36, color=BLUE_B).next_to(title, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(didactic_text))
        
        u = self.get_vec([2, 2], color=RED)
        lbl_u = MathTex("u").next_to(u.get_center(), UP+LEFT)
        self.play(GrowArrow(u), Write(lbl_u))
        
        zero = Dot(u.get_end(), color=WHITE)
        lbl_zero = MathTex("0").next_to(zero, UP)
        self.play(Create(zero), Write(lbl_zero))
        self.play(Indicate(u))
        
        lbl_res = MathTex("u+0 = u").next_to(u.get_end(), RIGHT)
        self.play(Write(lbl_res))
        self.wait(1)
        self.play(FadeOut(Group(u, zero, lbl_u, lbl_zero, lbl_res, title, didactic_text)))

    def axiom_additive_inverse(self):
        title = MathTex(r"\text{4. Inverso Aditivo: } u + (-u) = 0", color=YELLOW).to_corner(UL)
        self.play(Write(title))
        didactic_text = Tex(r"Siempre podemos volver al origen", font_size=36, color=BLUE_B).next_to(title, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(didactic_text))
        
        u = self.get_vec([3, 1], color=RED)
        lbl_u = MathTex("u").next_to(u.get_center(), DOWN)
        self.play(GrowArrow(u), Write(lbl_u))
        
        minus_u = self.get_vec([-3, -1], color=BLUE).shift(u.get_end() - self.origin_point)
        lbl_mu = MathTex("-u").next_to(minus_u.get_center(), UP)
        self.play(GrowArrow(minus_u), Write(lbl_mu))
        
        origin = Dot(self.origin_point, color=RED)
        lbl_zero = MathTex("0").next_to(origin, DOWN)
        self.play(Flash(origin), Write(lbl_zero))
        self.wait(1)
        self.play(FadeOut(Group(u, minus_u, lbl_u, lbl_mu, origin, lbl_zero, title, didactic_text)))

    def axiom_closure_scalar(self):
        pass

    def axiom_distributivity_scalar_sum(self):
        title = MathTex(r"\text{5. Distributividad 1: } c(u + v) = cu + cv", color=YELLOW).to_corner(UL)
        self.play(Write(title))
        didactic_text = Tex(r"Escalar la suma es igual a sumar los escalados", font_size=36, color=BLUE_B).next_to(title, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(didactic_text))
        
        c = 2
        coords_u = [1, 0.5]
        coords_v = [0.5, 1]
        
        u = self.get_vec(coords_u, color=RED)
        lbl_u = MathTex("u").next_to(u.get_center(), UP)
        
        v = self.get_vec(coords_v, color=GREEN).shift(u.get_end() - self.origin_point)
        lbl_v = MathTex("v").next_to(v.get_center(), RIGHT)
        
        sum_vec = self.get_vec([1.5, 1.5], color=YELLOW)
        lbl_sum = MathTex("u+v").next_to(sum_vec.get_center(), UP+LEFT)
        
        self.play(GrowArrow(u), Write(lbl_u))
        self.play(GrowArrow(v), Write(lbl_v))
        self.play(GrowArrow(sum_vec), Write(lbl_sum))
        
        # Paso solicitado: Mostrar c(u+v) inmediatamente
        # Escalamos u+v visualmente
        sum_sc = self.get_vec([3, 3], color=GOLD) # 1.5*2
        lbl_sum_sc = MathTex("c(u+v)").next_to(sum_sc.get_end(), UP)
        
        self.play(
            TransformFromCopy(sum_vec, sum_sc), 
            Write(lbl_sum_sc)
        )
        self.wait(1)

        # Ahora mostramos que cu + cv es lo mismo
        # Limpiar originales pero dejar el resultado c(u+v)
        self.play(FadeOut(u), FadeOut(v), FadeOut(sum_vec), FadeOut(lbl_u), FadeOut(lbl_v), FadeOut(lbl_sum))
        
        # Versión escalada componentes
        u_sc = self.get_vec([2, 1], color=RED) # 1*2, 0.5*2
        lbl_u_sc = MathTex("cu", font_size=32).next_to(u_sc.get_center(), UP) # c=2
        
        v_sc = self.get_vec([1, 2], color=GREEN).shift(u_sc.get_end() - self.origin_point) # 0.5*2, 1*2
        lbl_v_sc = MathTex("cv", font_size=32).next_to(v_sc.get_center(), RIGHT)
        
        self.play(GrowArrow(u_sc), Write(lbl_u_sc))
        self.play(GrowArrow(v_sc), Write(lbl_v_sc))
        
        # El vector sum_sc ya está ahí, solo confirmamos
        self.play(Flash(sum_sc))
        
        lbl_res = MathTex(r"c(u+v) = cu + cv").to_corner(DR)
        self.play(Write(lbl_res))
        self.wait(1)
        self.play(FadeOut(Group(u_sc, v_sc, sum_sc, lbl_res, lbl_u_sc, lbl_v_sc, lbl_sum_sc, title, didactic_text)))

    def axiom_distributivity_scalars(self):
        title = MathTex(r"\text{6. Distributividad 2: } (c + d)u = cu + du", color=YELLOW).to_corner(UL)
        self.play(Write(title))
        didactic_text = Tex(r"Sumar escalas equivale a escalar por separado", font_size=36, color=BLUE_B).next_to(title, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(didactic_text))
        
        u_coords = [2, 1]
        u = self.get_vec(u_coords, color=RED)
        lbl_u = MathTex("cu").next_to(u.get_center(), UP)
        self.play(GrowArrow(u), Write(lbl_u))
        
        u_copy = self.get_vec(u_coords, color=GREEN).shift(u.get_end() - self.origin_point)
        lbl_u_d = MathTex("du").next_to(u_copy.get_center(), UP)
        self.play(GrowArrow(u_copy), Write(lbl_u_d))
        
        # Total
        total_coords = [4, 2]
        total = self.get_vec(total_coords, color=GOLD).shift(DOWN*0.2)
        lbl_total = MathTex("(c+d)u").next_to(total.get_center(), DOWN)
        self.play(GrowArrow(total), Write(lbl_total))
        self.wait(1)
        self.play(FadeOut(Group(u, u_copy, total, lbl_u, lbl_u_d, lbl_total, title, didactic_text)))

    def axiom_scalar_associativity(self):
        title = MathTex(r"\text{7. Asociatividad Escalar: } c(du) = (cd)u", color=YELLOW).to_corner(UL)
        self.play(Write(title))
        didactic_text = Tex(r"Escalar en pasos o de golpe es lo mismo", font_size=36, color=BLUE_B).next_to(title, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(didactic_text))
        
        u = self.get_vec([1, 0.5], color=RED)
        self.play(GrowArrow(u))
        
        u_d = self.get_vec([2, 1], color=ORANGE)
        lbl_d = MathTex("d \cdot u").next_to(u_d.get_center(), UP)
        self.play(Transform(u, u_d), Write(lbl_d))
        
        u_cd = self.get_vec([3, 1.5], color=GOLD)
        lbl_cd = MathTex("(cd)u").next_to(u_cd.get_end(), RIGHT)
        self.play(Transform(u, u_cd), Transform(lbl_d, lbl_cd))
        self.wait(1)
        self.play(FadeOut(Group(u, lbl_d, title, didactic_text)))

    def axiom_scalar_identity(self):
        title = MathTex(r"\text{8. Identidad Escalar: } 1 \cdot u = u", color=YELLOW).to_corner(UL)
        self.play(Write(title))
        didactic_text = Tex(r"Multiplicar por 1 te deja igual", font_size=36, color=BLUE_B).next_to(title, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(didactic_text))
        
        u = self.get_vec([2, 1], color=RED)
        self.play(GrowArrow(u))
        lbl_u = MathTex("u").next_to(u.get_end(), RIGHT)
        self.play(Write(lbl_u))
        self.play(Flash(u, color=WHITE)) 
        self.wait(1)
        self.play(FadeOut(Group(u, lbl_u, title, didactic_text)))


        self.play(FadeOut(Group(u, lbl_u, title, didactic_text)))