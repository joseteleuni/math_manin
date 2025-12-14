from manim import *

class FasorEulerFinalConTitulo(Scene):
    def construct(self):
        # --- PARÁMETROS GEOMÉTRICOS ---
        radio = 1.2
        # Centro del círculo (Referencia absoluta, arriba izquierda)
        centro_circulo = LEFT * 3 + UP * 2.0 
        
        # --- 1. EL CÍRCULO Y REFERENCIAS ---
        circulo = Circle(radius=radio, color=WHITE).move_to(centro_circulo)
        punto_centro = Dot(centro_circulo)
        
        # Ejes locales del círculo (Cruz gris tenue)
        ejes_circulo = Axes(
            x_range=[-radio, radio, 1], y_range=[-radio, radio, 1],
            x_length=2*radio, y_length=2*radio,
            axis_config={"include_tip": False, "color": GREY, "stroke_width": 1}
        ).move_to(centro_circulo)

        # --- 2. GRÁFICA SENO (DERECHA) ---
        ejes_seno = Axes(
            x_range=[0, 7, 1], y_range=[-radio, radio, 1],
            x_length=5, y_length=2*radio,
            axis_config={"color": BLUE, "include_tip": False},
        ).move_to(centro_circulo + RIGHT * 4.5) 
        
        shift_y = centro_circulo[1] - ejes_seno.c2p(0,0)[1]
        ejes_seno.shift(UP * shift_y)
        
        etiq_seno = MathTex(r"\text{Im: } \sin(\theta)", color=RED, font_size=30).next_to(ejes_seno, UP)

        # --- 3. GRÁFICA COSENO (ABAJO) - ALINEADA ---
        ejes_coseno = Axes(
            x_range=[0, 6.5, 1], y_range=[-radio, radio, 1],
            x_length=3.5, y_length=2*radio,
            axis_config={"color": BLUE, "include_tip": False},
        ).rotate(-90 * DEGREES)

        # Alineación vertical precisa
        origen_actual = ejes_coseno.c2p(0,0)
        destino_deseado = np.array([centro_circulo[0], centro_circulo[1] - radio - 0.8, 0])
        ejes_coseno.shift(destino_deseado - origen_actual)
        
        etiq_coseno = MathTex(r"\text{Re: } \cos(\theta)", color=BLUE, font_size=30).next_to(ejes_coseno, LEFT, buff=0.5)

        # --- 4. FÓRMULA DE EULER CON TÍTULO ---
        
        # A. La Fórmula
        formula_euler = MathTex(
            r"e^{i\theta}", r" = ", r"\cos(\theta)", r" + i", r"\sin(\theta)",
            font_size=45
        ).move_to(RIGHT * 2.5 + DOWN * 1.5)
        
        formula_euler[0].set_color(YELLOW) 
        formula_euler[2].set_color(BLUE)   
        formula_euler[4].set_color(RED)    

        # B. El Título (NUEVO)
        titulo_euler = Tex("Identidad de Euler", font_size=32, color=WHITE)
        titulo_euler.next_to(formula_euler, UP, buff=0.3) # Puesto encima de la fórmula


        # --- ELEMENTOS DINÁMICOS ---
        theta = ValueTracker(0.001) 

        def get_pos_fasor():
            ang = theta.get_value()
            return centro_circulo + np.array([radio * np.cos(ang), radio * np.sin(ang), 0])

        # A. El Fasor y Theta
        fasor = always_redraw(lambda: Arrow(
            start=centro_circulo, end=get_pos_fasor(), buff=0, color=YELLOW, stroke_width=4
        ))
        
        arco_theta = always_redraw(lambda: Arc(
            radius=0.4, start_angle=0, angle=theta.get_value(), arc_center=centro_circulo, color=YELLOW, stroke_width=2
        ))
        label_theta = always_redraw(lambda: MathTex(r"\theta", color=YELLOW, font_size=24).move_to(
            centro_circulo + np.array([
                0.6 * np.cos(theta.get_value()/2),
                0.6 * np.sin(theta.get_value()/2),
                0
            ])
        ))

        # B. Dinámica SENO
        punto_seno = always_redraw(lambda: Dot(
            point=ejes_seno.c2p(theta.get_value(), np.sin(theta.get_value()) * radio), color=RED
        ))
        linea_proy_seno = always_redraw(lambda: DashedLine(
            start=get_pos_fasor(), end=punto_seno.get_center(), color=RED_E, stroke_width=2
        ))
        rastro_seno = TracedPath(punto_seno.get_center, stroke_color=RED, stroke_width=3)

        # C. Dinámica COSENO
        cateto_coseno = always_redraw(lambda: Line( 
            start=centro_circulo, 
            end=centro_circulo + np.array([radio * np.cos(theta.get_value()), 0, 0]),
            color=BLUE, stroke_width=4
        ))
        punto_coseno = always_redraw(lambda: Dot(
            point=ejes_coseno.c2p(theta.get_value(), np.cos(theta.get_value()) * radio), color=BLUE
        ))
        linea_bajada_coseno = always_redraw(lambda: DashedLine( 
            start=cateto_coseno.get_end(), end=punto_coseno.get_center(), color=BLUE_E, stroke_width=2
        ))
        rastro_coseno = TracedPath(punto_coseno.get_center, stroke_color=BLUE, stroke_width=3)

        # --- ANIMACIÓN ---
        self.add(circulo, punto_centro, ejes_circulo)
        self.add(ejes_seno, etiq_seno, ejes_coseno, etiq_coseno)
        
        # Añadimos Fórmula y Título
        self.add(formula_euler, titulo_euler) 

        self.add(fasor, arco_theta, label_theta)
        self.add(punto_seno, linea_proy_seno, rastro_seno)
        self.add(punto_coseno, cateto_coseno, linea_bajada_coseno, rastro_coseno)

        self.play(theta.animate.set_value(2 * PI), run_time=8, rate_func=linear)
        self.wait()