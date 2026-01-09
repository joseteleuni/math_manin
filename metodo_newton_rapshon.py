from manim import *
import numpy as np

class NewtonMethod(Scene):
    def construct(self):
        # 1. Configuración de Ejes y Función
        # Definimos los rangos de los ejes [min, max, paso]
        axes = Axes(
            x_range=[-1, 7, 1],
            y_range=[-2, 4, 1],
            axis_config={"include_tip": False}
        )
        
        # Definimos la función matemática (similar a la del video: cos(x) - 0.3x)
        def func(x):
            return 2 * np.cos(x/1.5) - 0.2 * x

        # Definimos la derivada de la función para calcular la pendiente
        def d_func(x):
            h = 0.0001
            return (func(x + h) - func(x)) / h

        # Crear la gráfica azul
        graph = axes.plot(func, color=BLUE, x_range=[-1, 7])
        
        # Etiquetas de la gráfica
        func_label = MathTex("f(x)").next_to(graph, UP).set_color(BLUE)

        # 2. Fórmula de Newton en la parte superior
        formula = MathTex(
            r"x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}"
        ).to_edge(UP)

        # 3. Animación de Intro
        self.play(Write(Title("Método de Newton")))
        self.wait(1)
        self.play(FadeOut(Title("Método de Newton")))
        
        self.play(Create(axes), Create(graph))
        self.play(Write(formula))
        self.wait(1)

        # 4. Proceso Iterativo (El bucle del método)
        
        # Punto inicial (x0) - Puedes cambiar este valor para probar otros inicios
        x_val = 1.0 
        colors = [YELLOW, ORANGE, RED, PINK] # Colores para cada iteración

        # Hacemos 3 iteraciones como en el video
        for i in range(4):
            # Calcular el punto en la curva
            y_val = func(x_val)
            point_on_curve = axes.c2p(x_val, y_val)
            point_on_axis = axes.c2p(x_val, 0)

            # Crear los elementos visuales
            dot_axis = Dot(point_on_axis, color=WHITE)
            dot_curve = Dot(point_on_curve, color=WHITE)
            
            # Línea punteada vertical
            dashed_line = DashedLine(point_on_axis, point_on_curve, color=GREY)
            
            # Etiqueta x_0, x_1, etc.
            label = MathTex(f"x_{i}").next_to(point_on_axis, DOWN)

            # Animar aparición del punto x_n
            if i == 0:
                self.play(FadeIn(dot_axis), Write(label))
            else:
                self.play(FadeIn(dot_axis), Write(label), run_time=0.5)

            self.play(Create(dashed_line), FadeIn(dot_curve), run_time=0.8)

            # Calcular el siguiente punto (x_{n+1}) usando la fórmula
            slope = d_func(x_val)
            next_x_val = x_val - (y_val / slope)
            
            # Crear la línea tangente (Roja en el video)
            # Dibujamos una línea que pase por el punto en la curva y corte el eje X
            tangent_line = Line(
                start=axes.c2p(x_val - 0.5, func(x_val) - slope*0.5), # Un poco hacia atrás
                end=axes.c2p(next_x_val, 0), # Hasta el eje X
                color=RED,
                stroke_width=3
            )
            # Extendemos un poco la línea visualmente pasado el eje X
            tangent_full = Line(
                start=axes.c2p(x_val, y_val),
                end=axes.c2p(next_x_val + (next_x_val-x_val)*0.2, 0 - (y_val)*0.2),
                color=RED
            )

            self.play(Create(tangent_line))
            
            # Pausa dramática en la intersección
            self.wait(0.5)

            # Limpiar elementos viejos para que no se sature (opcional, el video los deja)
            # En el video las líneas viejas se quedan un rato, aquí las atenuamos
            self.play(
                dashed_line.animate.set_opacity(0.3),
                tangent_line.animate.set_opacity(0.3),
                dot_curve.animate.set_opacity(0.5)
            )

            # Actualizar valor para la siguiente vuelta
            x_val = next_x_val

        self.wait(2)