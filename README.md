from manim import *

class ProyectoCompleto(Scene):
    # =========================
    # Helpers generales
    # =========================
    def crear_auto(self, color=BLUE):
        return VGroup(
            Rectangle(
                width=1.2,
                height=0.35,
                fill_color=color,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=2
            ),
            Rectangle(
                width=0.55,
                height=0.2,
                fill_color=YELLOW,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=1.5
            ).shift(UP * 0.25),
            Circle(radius=0.09, fill_color=BLACK, fill_opacity=1).shift(LEFT * 0.32 + DOWN * 0.22),
            Circle(radius=0.09, fill_color=BLACK, fill_opacity=1).shift(RIGHT * 0.32 + DOWN * 0.22)
        )

    def crear_auto_icono(self, color=BLUE):
        return VGroup(
            Rectangle(
                width=0.6,
                height=0.18,
                fill_color=color,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=1.2
            ),
            Rectangle(
                width=0.28,
                height=0.12,
                fill_color=YELLOW,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=1
            ).shift(UP * 0.13),
            Circle(radius=0.045, fill_color=BLACK, fill_opacity=1).shift(LEFT * 0.16 + DOWN * 0.11),
            Circle(radius=0.045, fill_color=BLACK, fill_opacity=1).shift(RIGHT * 0.16 + DOWN * 0.11)
        )

    def crear_panel(self, titulo_texto, color_panel, lineas, ancho=7.0, alto=4.6, font_size=31):
        fondo = RoundedRectangle(
            width=ancho,
            height=alto,
            corner_radius=0.18,
            stroke_color=color_panel,
            stroke_width=3,
            fill_color=color_panel,
            fill_opacity=0.08
        )

        titulo = Text(
            titulo_texto,
            font_size=28,
            weight=BOLD,
            color=color_panel
        ).move_to(fondo.get_top() + DOWN * 0.28)

        contenido = VGroup()
        for linea in lineas:
            contenido.add(MathTex(linea, font_size=font_size, color=WHITE))

        contenido.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        contenido.next_to(titulo, DOWN, buff=0.42)

        return VGroup(fondo, titulo, contenido)

    def crear_subtitulo(self, texto):
        subtitulo = Text(
            texto,
            font_size=30,
            weight=BOLD
        ).next_to(self.titulo_general, DOWN, buff=0.35)

        linea = Line(
            LEFT * 3.2, RIGHT * 3.2,
            color=GRAY_B,
            stroke_width=2
        ).next_to(subtitulo, DOWN, buff=0.2)

        return subtitulo, linea

    # =========================
    # Escena 1
    # =========================
    def escena1_portada(self):
        titulo_grande = Text(
            "Simulación de Cinemática",
            font_size=42,
            weight=BOLD
        ).to_edge(UP, buff=0.7)

        self.titulo_general = Text(
            "Simulación de Cinemática",
            font_size=28,
            weight=BOLD
        ).to_edge(UP, buff=0.25)

        subtitulo = Text(
            "Movimiento de tres vehículos en una pista recta",
            font_size=24
        ).next_to(titulo_grande, DOWN, buff=0.25)

        linea_titulo = Line(
            LEFT * 2.8, RIGHT * 2.8,
            color=BLUE_E,
            stroke_width=3
        ).next_to(subtitulo, DOWN, buff=0.25)

        pista = Line(
            LEFT * 5.5, RIGHT * 5.5,
            color=GRAY,
            stroke_width=6
        ).shift(DOWN * 1.3)

        marcas = VGroup()
        for x in range(-5, 6):
            marca = Line(
                UP * 0.12, DOWN * 0.12,
                color=GRAY_B,
                stroke_width=2
            ).move_to([x, -1.3, 0])
            marcas.add(marca)

        num_0 = Text("0 m", font_size=18, color=GRAY_A).move_to([-4.5, -1.65, 0])
        num_60 = Text("60 m", font_size=18, color=GRAY_A).move_to([-1.5, -1.65, 0])
        num_150 = Text("150 m", font_size=18, color=GRAY_A).move_to([2.5, -1.65, 0])
        numeros_pista = VGroup(num_0, num_60, num_150)

        auto_a = self.crear_auto(BLUE).move_to([-4.5, -1.02, 0])
        auto_b = self.crear_auto(RED).move_to([-1.5, -1.02, 0])
        auto_c = self.crear_auto(GREEN).move_to([2.5, -1.02, 0])

        label_a = Text("A", font_size=24, weight=BOLD, color=BLUE).next_to(auto_a, UP, buff=0.18)
        label_b = Text("B", font_size=24, weight=BOLD, color=RED).next_to(auto_b, UP, buff=0.18)
        label_c = Text("C", font_size=24, weight=BOLD, color=GREEN).next_to(auto_c, UP, buff=0.18)

        pos_a = MathTex(r"x_A(0)=0\ \text{m}", font_size=28, color=BLUE).next_to(auto_a, DOWN, buff=0.35)
        pos_b = MathTex(r"x_B(0)=60\ \text{m}", font_size=28, color=RED).next_to(auto_b, DOWN, buff=0.35)
        pos_c = MathTex(r"x_C(0)=150\ \text{m}", font_size=28, color=GREEN).next_to(auto_c, DOWN, buff=0.35)

        flecha_a = Arrow(start=LEFT * 0.35, end=RIGHT * 0.35, buff=0, color=BLUE).scale(0.75).next_to(auto_a, RIGHT, buff=0.18)
        flecha_b = Arrow(start=RIGHT * 0.35, end=LEFT * 0.35, buff=0, color=RED).scale(0.75).next_to(auto_b, LEFT, buff=0.18)
        reposo_c = MathTex(r"v_0=0", font_size=24, color=GREEN).next_to(auto_c, RIGHT, buff=0.18)

        tipos = Text(
            "MRU   •   MRUA   •   Aceleración Variable",
            font_size=26
        ).to_edge(DOWN, buff=0.45)

        self.play(FadeIn(titulo_grande, shift=DOWN * 0.3), run_time=1.2)
        self.play(FadeIn(subtitulo, shift=DOWN * 0.2), Create(linea_titulo), run_time=1)
        self.wait(0.2)

        self.play(Create(pista), run_time=1.2)
        self.play(LaggedStart(*[Create(m) for m in marcas], lag_ratio=0.06), run_time=1)
        self.play(FadeIn(numeros_pista, shift=UP * 0.1), run_time=0.8)

        self.play(
            FadeIn(auto_a, shift=UP * 0.5),
            FadeIn(auto_b, shift=UP * 0.5),
            FadeIn(auto_c, shift=UP * 0.5),
            run_time=1.2
        )

        self.play(Write(label_a), Write(label_b), Write(label_c), run_time=0.8)
        self.play(GrowArrow(flecha_a), GrowArrow(flecha_b), FadeIn(reposo_c, shift=RIGHT * 0.2), run_time=1)
        self.play(FadeIn(pos_a), FadeIn(pos_b), FadeIn(pos_c), run_time=1)
        self.play(Write(tipos), run_time=1.2)
        self.wait(2)

        self.play(
            Transform(titulo_grande, self.titulo_general),
            FadeOut(subtitulo),
            FadeOut(linea_titulo),
            FadeOut(pos_a),
            FadeOut(pos_b),
            FadeOut(pos_c),
            FadeOut(tipos),
            FadeOut(flecha_a),
            FadeOut(flecha_b),
            FadeOut(reposo_c),
            FadeOut(label_a),
            FadeOut(label_b),
            FadeOut(label_c),
            FadeOut(auto_a),
            FadeOut(auto_b),
            FadeOut(auto_c),
            FadeOut(pista),
            FadeOut(marcas),
            FadeOut(numeros_pista),
            run_time=1.3
        )
        self.wait(0.3)

    # =========================
    # Escena 2
    # =========================
    def escena2_datos(self):
        subtitulo, linea_subtitulo = self.crear_subtitulo("Datos iniciales del problema")

        def crear_panel_datos(titulo_texto, color_panel, lineas_tex, icono_auto=None, flecha=None, formula_destacada=None):
            panel = RoundedRectangle(
                width=3.6,
                height=3.9,
                corner_radius=0.2,
                stroke_color=color_panel,
                stroke_width=3,
                fill_color=color_panel,
                fill_opacity=0.08
            )

            titulo = Text(
                titulo_texto,
                font_size=26,
                weight=BOLD,
                color=color_panel
            ).move_to(panel.get_top() + DOWN * 0.35)

            elementos_superiores = VGroup()
            if icono_auto is not None:
                elementos_superiores.add(icono_auto)
            if flecha is not None:
                elementos_superiores.add(flecha)

            if len(elementos_superiores) > 0:
                elementos_superiores.arrange(RIGHT, buff=0.2)
                elementos_superiores.next_to(titulo, DOWN, buff=0.18)

            contenido = VGroup()
            for linea in lineas_tex:
                contenido.add(MathTex(linea, font_size=30, color=WHITE))

            contenido.arrange(DOWN, aligned_edge=LEFT, buff=0.24)

            if len(elementos_superiores) > 0:
                contenido.next_to(elementos_superiores, DOWN, buff=0.25)
            else:
                contenido.next_to(titulo, DOWN, buff=0.35)

            grupo = VGroup(panel, titulo, elementos_superiores, contenido)

            if formula_destacada is not None:
                caja_formula = RoundedRectangle(
                    width=2.6,
                    height=0.65,
                    corner_radius=0.12,
                    stroke_color=color_panel,
                    stroke_width=2,
                    fill_color=color_panel,
                    fill_opacity=0.12
                )
                formula = MathTex(formula_destacada, font_size=32, color=color_panel)
                formula_group = VGroup(caja_formula, formula)
                formula_group.next_to(contenido, DOWN, buff=0.28)
                grupo.add(formula_group)

            return grupo

        auto_a_icono = self.crear_auto_icono(BLUE)
        auto_b_icono = self.crear_auto_icono(RED)
        auto_c_icono = self.crear_auto_icono(GREEN)

        flecha_b = Arrow(start=RIGHT * 0.28, end=LEFT * 0.28, buff=0, color=RED, stroke_width=5).scale(0.8)

        panel_a = crear_panel_datos(
            "Vehículo A",
            BLUE,
            [r"\text{MRU}", r"x_A(0)=0\ \text{m}", r"v_A=25\ \text{m/s}"],
            icono_auto=auto_a_icono
        )

        panel_b = crear_panel_datos(
            "Vehículo B",
            RED,
            [r"\text{MRUA}", r"x_B(0)=60\ \text{m}", r"v_{0B}=-10\ \text{m/s}", r"a_B=4\ \text{m/s}^2"],
            icono_auto=auto_b_icono,
            flecha=flecha_b
        )

        panel_c = crear_panel_datos(
            "Vehículo C",
            GREEN,
            [r"\text{Aceleración variable}", r"x_C(0)=150\ \text{m}", r"v_{0C}=0\ \text{m/s}"],
            icono_auto=auto_c_icono,
            formula_destacada=r"a_C(t)=12-4t"
        )

        paneles = VGroup(panel_a, panel_b, panel_c).arrange(RIGHT, buff=0.35)
        paneles.scale(0.8)
        paneles.move_to(DOWN * 0.65)

        self.play(FadeIn(subtitulo, shift=UP * 0.2), Create(linea_subtitulo), run_time=0.9)
        self.play(FadeIn(panel_a, shift=UP * 0.3), run_time=0.8)
        self.play(FadeIn(panel_b, shift=UP * 0.3), run_time=0.8)
        self.play(FadeIn(panel_c, shift=UP * 0.3), run_time=0.8)
        self.wait(1.5)

        self.play(panel_a.animate.scale(1.03), run_time=0.25)
        self.play(panel_a.animate.scale(1 / 1.03), run_time=0.25)
        self.play(panel_b.animate.scale(1.03), run_time=0.25)
        self.play(panel_b.animate.scale(1 / 1.03), run_time=0.25)
        self.play(panel_c.animate.scale(1.03), run_time=0.25)
        self.play(panel_c.animate.scale(1 / 1.03), run_time=0.25)

        self.wait(1.5)
        self.play(FadeOut(paneles), FadeOut(subtitulo), FadeOut(linea_subtitulo), run_time=1.0)

    # =========================
    # Escena 3
    # =========================
    def escena3_funciones(self):
        subtitulo, linea_subtitulo = self.crear_subtitulo("Obtención de las funciones de posición")

        bloque_a = self.crear_panel(
            "Vehículo A",
            BLUE,
            [r"\text{MRU}", r"x_A(t)=x_{0A}+v_A t", r"x_A(t)=0+25t", r"\boxed{x_A(t)=25t}"],
            ancho=3.5, alto=3.4, font_size=29
        ).move_to(LEFT * 2.6 + DOWN * 0.35)

        bloque_b = self.crear_panel(
            "Vehículo B",
            RED,
            [r"\text{MRUA}", r"x_B(t)=x_{0B}+v_{0B}t+\frac{1}{2}a_B t^2", r"x_B(t)=60-10t+\frac{1}{2}(4)t^2", r"\boxed{x_B(t)=60-10t+2t^2}"],
            ancho=4.5, alto=3.9, font_size=29
        ).move_to(RIGHT * 2.4 + DOWN * 0.35)

        bloque_c1 = self.crear_panel(
            "Vehículo C",
            GREEN,
            [r"a_C(t)=12-4t", r"v_C(t)=\int(12-4t)\,dt", r"v_C(t)=12t-2t^2+C_1", r"v_C(0)=0\Rightarrow C_1=0", r"\boxed{v_C(t)=12t-2t^2}"],
            ancho=5.3, alto=4.4, font_size=29
        ).move_to(DOWN * 0.35)

        bloque_c2 = self.crear_panel(
            "Integración para posición",
            GREEN,
            [r"x_C(t)=\int(12t-2t^2)\,dt", r"x_C(t)=6t^2-\frac{2}{3}t^3+C_2", r"x_C(0)=150\Rightarrow C_2=150", r"\boxed{x_C(t)=150+6t^2-\frac{2}{3}t^3}"],
            ancho=5.7, alto=4.0, font_size=29
        ).move_to(DOWN * 0.35)

        caja_resumen = RoundedRectangle(
            width=12.4,
            height=2.9,
            corner_radius=0.2,
            stroke_color=YELLOW,
            stroke_width=3,
            fill_color=YELLOW,
            fill_opacity=0.08
        ).move_to(DOWN * 0.65)

        titulo_resumen = Text(
            "Funciones de posición obtenidas",
            font_size=26,
            weight=BOLD,
            color=YELLOW
        ).move_to(caja_resumen.get_top() + DOWN * 0.35)

        resumen = VGroup(
            MathTex(r"x_A(t)=25t", font_size=32, color=BLUE),
            MathTex(r"x_B(t)=60-10t+2t^2", font_size=32, color=RED),
            MathTex(r"x_C(t)=150+6t^2-\frac{2}{3}t^3", font_size=32, color=GREEN)
        ).arrange(DOWN, buff=0.22).next_to(titulo_resumen, DOWN, buff=0.28)

        grupo_resumen = VGroup(caja_resumen, titulo_resumen, resumen)

        self.play(FadeIn(subtitulo, shift=UP * 0.2), Create(linea_subtitulo), run_time=1.0)
        self.play(FadeIn(bloque_a, shift=LEFT * 0.2), run_time=1.0)
        self.play(FadeIn(bloque_b, shift=RIGHT * 0.2), run_time=1.0)
        self.wait(2.4)

        self.play(FadeOut(bloque_a), FadeOut(bloque_b), run_time=1.0)

        self.play(FadeIn(bloque_c1, shift=UP * 0.2), run_time=1.2)
        self.wait(2.8)

        self.play(FadeOut(bloque_c1), run_time=0.9)
        self.play(FadeIn(bloque_c2, shift=UP * 0.2), run_time=1.2)
        self.wait(3.0)

        self.play(FadeOut(bloque_c2), run_time=1.0)
        self.play(FadeIn(grupo_resumen, shift=UP * 0.2), run_time=1.2)
        self.wait(3.0)

        self.play(FadeOut(grupo_resumen), FadeOut(subtitulo), FadeOut(linea_subtitulo), run_time=1.0)

    # =========================
    # Escena 4
    # =========================
    def escena4_cambio_direccion(self):
        subtitulo, linea_subtitulo = self.crear_subtitulo("Cambio de dirección de los vehículos")

        panel_b = self.crear_panel(
            "Vehículo B",
            RED,
            [
                r"v_B(t)=-10+4t",
                r"v_B(t)=0",
                r"-10+4t=0 \Rightarrow \boxed{t=2.5\,s}",
                r"x_B(2.5)=60-10(2.5)+2(2.5)^2",
                r"\boxed{x_B(2.5)=47.5\,m}"
            ],
            ancho=7.2,
            alto=4.7
        ).move_to(UP * 0.12)

        # corregido: más abajo
        panel_c = self.crear_panel(
            "Vehículo C",
            GREEN,
            [
                r"v_C(t)=12t-2t^2",
                r"v_C(t)=0",
                r"12t-2t^2=0 \Rightarrow t=0,\;\boxed{6\,s}",
                r"\text{El cambio real ocurre en } \boxed{t=6\,s}",
                r"x_C(6)=150+6(6)^2-\frac{2}{3}(6)^3",
                r"\boxed{x_C(6)=222\,m}"
            ],
            ancho=7.9,
            alto=5.8
        ).move_to(DOWN * 0.08)

        flecha_izq_b = Arrow(start=RIGHT * 1.1, end=LEFT * 1.1, buff=0, color=RED, stroke_width=8).move_to(DOWN * 2.0)
        flecha_der_b = Arrow(start=LEFT * 1.1, end=RIGHT * 1.1, buff=0, color=RED, stroke_width=8).move_to(DOWN * 2.0)
        etiqueta_izq_b = Text("izquierda", font_size=22, color=RED).next_to(flecha_izq_b, DOWN, buff=0.16)
        etiqueta_der_b = Text("derecha", font_size=22, color=RED).next_to(flecha_der_b, DOWN, buff=0.16)
        texto_b = Text("Se detiene y cambia de sentido", font_size=24, color=RED).next_to(etiqueta_der_b, DOWN, buff=0.16)

        flecha_der_c = Arrow(start=LEFT * 1.1, end=RIGHT * 1.1, buff=0, color=GREEN, stroke_width=8).move_to(DOWN * 2.0)
        flecha_izq_c = Arrow(start=RIGHT * 1.1, end=LEFT * 1.1, buff=0, color=GREEN, stroke_width=8).move_to(DOWN * 2.0)
        etiqueta_der_c = Text("derecha", font_size=22, color=GREEN).next_to(flecha_der_c, DOWN, buff=0.16)
        etiqueta_izq_c = Text("izquierda", font_size=22, color=GREEN).next_to(flecha_izq_c, DOWN, buff=0.16)
        texto_c = Text("Después de 6 s, invierte el sentido", font_size=24, color=GREEN).next_to(etiqueta_izq_c, DOWN, buff=0.16)

        self.play(FadeIn(subtitulo, shift=UP * 0.2), Create(linea_subtitulo), run_time=1.1)

        self.play(FadeIn(panel_b, shift=UP * 0.2), run_time=1.1)
        self.play(GrowArrow(flecha_izq_b), FadeIn(etiqueta_izq_b, shift=UP * 0.1), run_time=0.9)
        self.wait(2.6)

        self.play(
            ReplacementTransform(flecha_izq_b, flecha_der_b),
            FadeOut(etiqueta_izq_b),
            FadeIn(etiqueta_der_b, shift=UP * 0.1),
            run_time=1.1
        )
        self.play(FadeIn(texto_b, shift=UP * 0.1), run_time=0.8)
        self.wait(2.8)

        self.play(
            panel_b.animate.shift(LEFT * 2).set_opacity(0),
            flecha_der_b.animate.shift(LEFT * 2).set_opacity(0),
            etiqueta_der_b.animate.shift(LEFT * 2).set_opacity(0),
            texto_b.animate.shift(LEFT * 2).set_opacity(0),
            run_time=1.0
        )

        self.play(FadeIn(panel_c, shift=RIGHT * 0.4), run_time=1.1)
        self.play(GrowArrow(flecha_der_c), FadeIn(etiqueta_der_c, shift=UP * 0.1), run_time=0.9)
        self.wait(2.8)

        self.play(
            ReplacementTransform(flecha_der_c, flecha_izq_c),
            FadeOut(etiqueta_der_c),
            FadeIn(etiqueta_izq_c, shift=UP * 0.1),
            run_time=1.1
        )
        self.play(FadeIn(texto_c, shift=UP * 0.1), run_time=0.8)
        self.wait(3.0)

        self.play(
            FadeOut(panel_c),
            FadeOut(flecha_izq_c),
            FadeOut(etiqueta_izq_c),
            FadeOut(texto_c),
            FadeOut(subtitulo),
            FadeOut(linea_subtitulo),
            run_time=1.0
        )

    # =========================
    # Escena 5
    # =========================
    def escena5_velocidad_maxima(self):
        subtitulo, linea_subtitulo = self.crear_subtitulo("Velocidad máxima del vehículo C")

        panel_principal = self.crear_panel(
            "Cálculo del máximo",
            GREEN,
            [r"v_C(t)=12t-2t^2", r"a_C(t)=12-4t", r"a_C(t)=0", r"12-4t=0 \Rightarrow \boxed{t=3\,s}"],
            ancho=7.2,
            alto=4.7
        ).move_to(UP * 0.2)

        marcador_max = Text(
            "instante de velocidad máxima",
            font_size=24,
            color=YELLOW,
            weight=BOLD
        ).move_to(DOWN * 1.85)

        panel_evaluacion = self.crear_panel(
            "Evaluación de la velocidad",
            GREEN,
            [
                r"v_C(3)=12(3)-2(3)^2",
                r"v_C(3)=36-18",
                r"\boxed{v_C(3)=18\,m/s}",
                r"\text{Antes de } t=3\,s,\ \text{la velocidad aumenta}",
                r"\text{Después de } t=3\,s,\ \text{disminuye}"
            ],
            ancho=7.6,
            alto=5.3
        ).move_to(LEFT * 1.7 + DOWN * 0.05)

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 20, 5],
            x_length=3.2,
            y_length=2.4,
            axis_config={"include_ticks": False, "include_numbers": False, "color": GRAY_B}
        )

        grafica = axes.plot(lambda t: 12 * t - 2 * (t ** 2), x_range=[0, 6], color=GREEN)
        punto_max = Dot(axes.c2p(3, 18), color=YELLOW, radius=0.06)
        etiqueta_max = MathTex(r"(3,\ 18)", font_size=26, color=YELLOW).next_to(punto_max, UP, buff=0.12)
        label_t = Text("t", font_size=20, color=GRAY_A).next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        label_v = Text("v", font_size=20, color=GRAY_A).next_to(axes.y_axis.get_end(), UP, buff=0.1)

        mini_parabola = VGroup(axes, grafica, punto_max, etiqueta_max, label_t, label_v)
        mini_parabola.scale(0.95)
        mini_parabola.move_to(RIGHT * 4.05 + DOWN * 0.1)

        caja_final = RoundedRectangle(
            width=8.8,
            height=1.8,
            corner_radius=0.2,
            stroke_color=YELLOW,
            stroke_width=3,
            fill_color=YELLOW,
            fill_opacity=0.08
        ).move_to(DOWN * 0.35)

        resultado_final = MathTex(
            r"\boxed{v_{\max}=18\,m/s \;\text{ en }\; t=3\,s}",
            font_size=38,
            color=YELLOW
        ).move_to(caja_final.get_center())

        grupo_final = VGroup(caja_final, resultado_final)

        self.play(FadeIn(subtitulo, shift=UP * 0.2), Create(linea_subtitulo), run_time=1.1)
        self.play(FadeIn(panel_principal, shift=UP * 0.2), run_time=1.1)
        self.wait(2.6)

        self.play(FadeIn(marcador_max, shift=UP * 0.1), run_time=0.8)
        self.wait(2.0)

        self.play(FadeOut(panel_principal), FadeOut(marcador_max), run_time=1.0)

        self.play(FadeIn(panel_evaluacion, shift=UP * 0.2), run_time=1.0)
        self.play(Create(axes), run_time=0.9)
        self.play(Create(grafica), FadeIn(punto_max), FadeIn(etiqueta_max), FadeIn(label_t), FadeIn(label_v), run_time=1.1)
        self.wait(3.0)

        self.play(FadeOut(panel_evaluacion), FadeOut(mini_parabola), run_time=1.0)
        self.play(FadeIn(grupo_final, shift=UP * 0.2), run_time=1.2)
        self.wait(3.0)

        self.play(FadeOut(grupo_final), FadeOut(subtitulo), FadeOut(linea_subtitulo), run_time=1.0)

    # =========================
    # Escena 6
    # =========================
    def escena6_encuentro_ab(self):
        subtitulo, linea_subtitulo = self.crear_subtitulo("Encuentro crítico entre A y B")

        panel_ecuacion = self.crear_panel(
            "Igualando posiciones",
            YELLOW,
            [r"x_A(t)=x_B(t)", r"25t=60-10t+2t^2", r"2t^2-35t+60=0", r"t_1\approx\boxed{1.93\,s},\quad t_2\approx15.57\,s"],
            ancho=7.8,
            alto=4.7
        ).move_to(UP * 0.15)

        panel_aclaracion = self.crear_panel(
            "Interpretación física",
            BLUE,
            [r"\text{Existen dos intersecciones}", r"\text{El encuentro crítico es el primero}", r"\boxed{t\approx1.93\,s}"],
            ancho=6.8,
            alto=3.7
        ).move_to(DOWN * 0.15)

        panel_posicion = self.crear_panel(
            "Punto de encuentro",
            BLUE,
            [r"x_A(1.93)=25(1.93)", r"\boxed{x\approx48.25\,m}"],
            ancho=5.8,
            alto=3.2
        ).move_to(DOWN * 0.25)

        linea_base = Line(LEFT * 2.5, RIGHT * 2.5, color=GRAY, stroke_width=5).move_to(DOWN * 2.1)

        flecha_a = Arrow(
            start=[-2.0, -2.1, 0],
            end=[-0.45, -2.1, 0],
            buff=0,
            color=BLUE,
            stroke_width=7
        )

        flecha_b = Arrow(
            start=[2.0, -2.1, 0],
            end=[0.45, -2.1, 0],
            buff=0,
            color=RED,
            stroke_width=7
        )

        punto_encuentro = Dot(point=[0, -2.1, 0], color=YELLOW, radius=0.08)
        etiqueta_a = Text("A", font_size=24, color=BLUE, weight=BOLD).move_to([-1.25, -1.78, 0])
        etiqueta_b = Text("B", font_size=24, color=RED, weight=BOLD).move_to([1.25, -1.78, 0])
        texto_encuentro = Text("primer encuentro", font_size=22, color=YELLOW).move_to([0, -2.85, 0])

        visual_cruce = VGroup(
            linea_base, flecha_a, flecha_b, punto_encuentro,
            etiqueta_a, etiqueta_b, texto_encuentro
        )

        caja_final = RoundedRectangle(
            width=10.6,
            height=2.0,
            corner_radius=0.2,
            stroke_color=YELLOW,
            stroke_width=3,
            fill_color=YELLOW,
            fill_opacity=0.08
        ).move_to(DOWN * 0.55)

        resultado_final = MathTex(
            r"\boxed{A\ \text{alcanza a}\ B\ \text{en}\ t\approx1.93\,s,\ x\approx48.25\,m}",
            font_size=34,
            color=YELLOW
        ).move_to(caja_final.get_center())

        grupo_final = VGroup(caja_final, resultado_final)

        self.play(FadeIn(subtitulo, shift=UP * 0.2), Create(linea_subtitulo), run_time=1.1)
        self.play(FadeIn(panel_ecuacion, shift=UP * 0.2), run_time=1.1)
        self.wait(2.8)

        self.play(FadeOut(panel_ecuacion), run_time=1.0)

        self.play(FadeIn(panel_aclaracion, shift=UP * 0.2), run_time=1.0)
        self.wait(2.3)
        self.play(FadeOut(panel_aclaracion), run_time=0.9)

        self.play(FadeIn(panel_posicion, shift=UP * 0.2), run_time=1.0)
        self.wait(2.1)
        self.play(FadeOut(panel_posicion), run_time=0.9)

        self.play(Create(linea_base), run_time=0.8)
        self.play(GrowArrow(flecha_a), GrowArrow(flecha_b), FadeIn(etiqueta_a), FadeIn(etiqueta_b), run_time=1.0)
        self.play(FadeIn(punto_encuentro), FadeIn(texto_encuentro), run_time=0.8)
        self.wait(2.4)

        self.play(FadeOut(visual_cruce), run_time=1.0)
        self.play(FadeIn(grupo_final, shift=UP * 0.2), run_time=1.2)
        self.wait(3.0)

        self.play(FadeOut(grupo_final), FadeOut(subtitulo), FadeOut(linea_subtitulo), run_time=1.0)

    # =========================
    # Escena 7
    # =========================
    def escena7_retorno_c_distancia(self):
        subtitulo, linea_subtitulo = self.crear_subtitulo("Retorno de C y distancia entre A y B")

        panel_c = self.crear_panel(
            "Retorno del vehículo C",
            GREEN,
            [
                r"x_C(t)=150",
                r"150=150+6t^2-\frac{2}{3}t^3",
                r"0=t^2\left(6-\frac{2}{3}t\right)",
                r"t=0,\;\boxed{9\,s}",
                r"\text{El retorno real ocurre en } \boxed{t=9\,s}"
            ],
            ancho=7.8,
            alto=4.9
        ).move_to(UP * 0.1)

        # corregido: más separados
        panel_ab = self.crear_panel(
            "Posiciones en t = 9 s",
            BLUE,
            [
                r"x_A(9)=25(9)=225\,m",
                r"x_B(9)=60-10(9)+2(9)^2",
                r"x_B(9)=60-90+162",
                r"\boxed{x_B(9)=132\,m}"
            ],
            ancho=6.6,
            alto=4.25
        ).move_to(LEFT * 3.05 + DOWN * 0.02)

        panel_distancia = self.crear_panel(
            "Separación entre A y B",
            YELLOW,
            [
                r"d=\left|x_A-x_B\right|",
                r"d=\left|225-132\right|",
                r"\boxed{d=93\,m}"
            ],
            ancho=5.1,
            alto=3.35
        ).move_to(RIGHT * 3.35 + DOWN * 0.52)

        linea_base = Line(LEFT * 2.8, RIGHT * 2.8, color=GRAY, stroke_width=5).move_to(DOWN * 2.35)
        punto_b = Dot(point=[-1.0, -2.35, 0], color=RED, radius=0.09)
        punto_a = Dot(point=[1.6, -2.35, 0], color=BLUE, radius=0.09)

        etiqueta_b = Text("B", font_size=24, color=RED, weight=BOLD).next_to(punto_b, UP, buff=0.12)
        etiqueta_a = Text("A", font_size=24, color=BLUE, weight=BOLD).next_to(punto_a, UP, buff=0.12)

        segmento_distancia = DoubleArrow(
            start=[-1.0, -2.75, 0],
            end=[1.6, -2.75, 0],
            buff=0,
            color=YELLOW,
            stroke_width=6,
            tip_length=0.14
        )

        texto_distancia = Text("93 m", font_size=24, color=YELLOW, weight=BOLD).move_to([0.3, -3.02, 0])

        visual_final = VGroup(
            linea_base, punto_a, punto_b, etiqueta_a, etiqueta_b,
            segmento_distancia, texto_distancia
        )

        caja_final = RoundedRectangle(
            width=11.2,
            height=2.0,
            corner_radius=0.2,
            stroke_color=YELLOW,
            stroke_width=3,
            fill_color=YELLOW,
            fill_opacity=0.08
        ).move_to(DOWN * 0.45)

        resultado_final = MathTex(
            r"\boxed{\text{Cuando C regresa a }x=150,\ \text{la distancia entre A y B es }93\,m}",
            font_size=32,
            color=YELLOW
        ).move_to(caja_final.get_center())

        grupo_final = VGroup(caja_final, resultado_final)

        self.play(FadeIn(subtitulo, shift=UP * 0.2), Create(linea_subtitulo), run_time=1.1)
        self.play(FadeIn(panel_c, shift=UP * 0.2), run_time=1.1)
        self.wait(2.8)
        self.play(FadeOut(panel_c), run_time=1.0)

        self.play(FadeIn(panel_ab, shift=LEFT * 0.2), run_time=1.0)
        self.wait(2.2)

        self.play(FadeIn(panel_distancia, shift=RIGHT * 0.2), run_time=1.0)
        self.wait(2.3)

        self.play(Create(linea_base), run_time=0.8)
        self.play(FadeIn(punto_b), FadeIn(punto_a), FadeIn(etiqueta_b), FadeIn(etiqueta_a), run_time=0.8)
        self.play(Create(segmento_distancia), FadeIn(texto_distancia), run_time=1.0)
        self.wait(2.5)

        self.play(FadeOut(panel_ab), FadeOut(panel_distancia), FadeOut(visual_final), run_time=1.0)
        self.play(FadeIn(grupo_final, shift=UP * 0.2), run_time=1.2)
        self.wait(3.0)

        self.play(FadeOut(grupo_final), FadeOut(subtitulo), FadeOut(linea_subtitulo), run_time=1.0)

    # =========================
    # Escena 8
    # =========================
    def escena8_conclusiones(self):
        subtitulo, linea_subtitulo = self.crear_subtitulo("Conclusiones")
        subtitulo.set_color(YELLOW)

        caja = RoundedRectangle(
            width=10.8,
            height=5.4,
            corner_radius=0.2,
            stroke_color=YELLOW,
            stroke_width=3,
            fill_color=YELLOW,
            fill_opacity=0.06
        ).move_to(DOWN * 0.25)

        resultados = VGroup(
            MathTex(r"\bullet\ \ B\ \text{ cambia de dirección en } t=2.5\,s", font_size=30, color=RED),
            MathTex(r"\bullet\ \ C\ \text{ alcanza } v_{\max}=18\,m/s \text{ en } t=3\,s", font_size=30, color=GREEN),
            MathTex(r"\bullet\ \ A\ \text{ alcanza a } B \text{ en } t\approx1.93\,s", font_size=30, color=BLUE),
            MathTex(r"\bullet\ \ \text{Cuando } C \text{ regresa a } x=150,\ \text{la distancia entre } A \text{ y } B \text{ es } 93\,m", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        resultados.move_to(caja.get_center() + UP * 0.45)

        frase_final = VGroup(
            Text("La simulación confirma visualmente", font_size=24, color=WHITE),
            Text("los resultados analíticos del problema.", font_size=24, color=WHITE)
        ).arrange(DOWN, buff=0.12).move_to(caja.get_center() + DOWN * 1.75)

        linea_azul = Line(LEFT * 1.2, LEFT * 0.4, color=BLUE, stroke_width=6)
        linea_roja = Line(LEFT * 0.3, RIGHT * 0.3, color=RED, stroke_width=6)
        linea_verde = Line(RIGHT * 0.4, RIGHT * 1.2, color=GREEN, stroke_width=6)
        detalle_colores = VGroup(linea_azul, linea_roja, linea_verde).move_to(DOWN * 2.95)

        self.play(FadeIn(subtitulo, shift=UP * 0.2), Create(linea_subtitulo), run_time=1.0)
        self.play(Create(caja), run_time=1.0)

        for resultado in resultados:
            self.play(FadeIn(resultado, shift=LEFT * 0.15), run_time=0.7)

        self.play(FadeIn(frase_final, shift=UP * 0.15), run_time=1.0)
        self.play(Create(detalle_colores), run_time=0.8)
        self.wait(3.5)

        self.play(
            FadeOut(caja),
            FadeOut(resultados),
            FadeOut(frase_final),
            FadeOut(detalle_colores),
            FadeOut(subtitulo),
            FadeOut(linea_subtitulo),
            run_time=1.0
        )

    # =========================
    # Escena 9
    # =========================
    def escena9_simulacion_final(self):
        subtitulo, linea_subtitulo = self.crear_subtitulo("Simulación global del movimiento")

        eje = NumberLine(
            x_range=[0, 230, 10],
            length=11,
            include_numbers=False,
            include_ticks=True,
            color=GRAY
        ).move_to(DOWN * 0.8)

        marcas_texto = VGroup(
            Text("0 m", font_size=18, color=GRAY_A).next_to(eje.n2p(0), DOWN, buff=0.25),
            Text("60 m", font_size=18, color=GRAY_A).next_to(eje.n2p(60), DOWN, buff=0.25),
            Text("150 m", font_size=18, color=GRAY_A).next_to(eje.n2p(150), DOWN, buff=0.25),
            Text("225 m", font_size=18, color=GRAY_A).next_to(eje.n2p(225), DOWN, buff=0.25),
        )

        def xA(t):
            return 25 * t

        def xB(t):
            return 60 - 10 * t + 2 * t**2

        def xC(t):
            return 150 + 6 * t**2 - (2/3) * t**3

        t = ValueTracker(0)

        auto_a = always_redraw(
            lambda: self.crear_auto(BLUE).scale(0.82).move_to(eje.n2p(xA(t.get_value())) + UP * 0.32)
        )
        auto_b = always_redraw(
            lambda: self.crear_auto(RED).scale(0.82).move_to(eje.n2p(xB(t.get_value())) + UP * 0.32)
        )
        auto_c = always_redraw(
            lambda: self.crear_auto(GREEN).scale(0.82).move_to(eje.n2p(xC(t.get_value())) + UP * 0.32)
        )

        label_a = always_redraw(
            lambda: Text("A", font_size=22, weight=BOLD, color=BLUE).next_to(auto_a, UP, buff=0.10)
        )
        label_b = always_redraw(
            lambda: Text("B", font_size=22, weight=BOLD, color=RED).next_to(auto_b, UP, buff=0.10)
        )
        label_c = always_redraw(
            lambda: Text("C", font_size=22, weight=BOLD, color=GREEN).next_to(auto_c, UP, buff=0.10)
        )

        reloj_box = RoundedRectangle(
            width=2.3,
            height=0.9,
            corner_radius=0.15,
            stroke_color=YELLOW,
            stroke_width=2.5,
            fill_color=YELLOW,
            fill_opacity=0.08
        ).to_corner(UR).shift(LEFT * 0.2 + DOWN * 1.2)

        reloj_texto = Text("Tiempo", font_size=22, color=YELLOW, weight=BOLD).move_to(
            reloj_box.get_center() + UP * 0.16
        )

        reloj_valor = always_redraw(
            lambda: DecimalNumber(
                t.get_value(),
                num_decimal_places=2,
                font_size=24,
                color=WHITE
            ).move_to(reloj_box.get_center() + DOWN * 0.16)
        )

        reloj_s = always_redraw(
            lambda: Text("s", font_size=20, color=WHITE).next_to(reloj_valor, RIGHT, buff=0.08)
        )

        evento_box = RoundedRectangle(
            width=5.8,
            height=1.0,
            corner_radius=0.15,
            stroke_color=YELLOW,
            stroke_width=2.5,
            fill_color=YELLOW,
            fill_opacity=0.08
        ).to_corner(UL).shift(RIGHT * 0.3 + DOWN * 1.2)

        evento_titulo = Text(
            "Evento actual",
            font_size=22,
            color=YELLOW,
            weight=BOLD
        ).move_to(evento_box.get_center() + UP * 0.16)

        def texto_evento_actual():
            tv = t.get_value()
            if 1.8 <= tv <= 2.1:
                return "A alcanza a B"
            elif 2.4 <= tv <= 2.7:
                return "B cambia de dirección"
            elif 2.9 <= tv <= 3.2:
                return "C alcanza velocidad máxima"
            elif 5.9 <= tv <= 6.2:
                return "C cambia de dirección"
            elif 8.9 <= tv <= 9.2:
                return "C regresa a x = 150"
            else:
                return "Movimiento simultáneo"

        evento_texto = always_redraw(
            lambda: Text(
                texto_evento_actual(),
                font_size=21,
                color=WHITE
            ).move_to(evento_box.get_center() + DOWN * 0.18)
        )

        cierre = Text(
            "Verificación visual del modelo completo",
            font_size=24,
            color=YELLOW
        ).move_to(DOWN * 2.9)

        self.play(FadeIn(subtitulo, shift=UP * 0.2), Create(linea_subtitulo), run_time=1.0)
        self.play(Create(eje), FadeIn(marcas_texto), run_time=1.2)

        self.play(
            FadeIn(reloj_box),
            FadeIn(reloj_texto),
            FadeIn(evento_box),
            FadeIn(evento_titulo),
            run_time=0.8
        )

        self.play(
            FadeIn(auto_a), FadeIn(auto_b), FadeIn(auto_c),
            FadeIn(label_a), FadeIn(label_b), FadeIn(label_c),
            FadeIn(reloj_valor), FadeIn(reloj_s),
            FadeIn(evento_texto),
            run_time=1.0
        )

        self.play(FadeIn(cierre, shift=UP * 0.1), run_time=0.8)
        self.wait(0.8)

        self.play(t.animate.set_value(9), run_time=14, rate_func=linear)
        self.wait(2.0)

    # =========================
    # Render completo
    # =========================
    def construct(self):
        self.camera.background_color = "#0f1117"

        self.escena1_portada()
        self.escena2_datos()
        self.escena3_funciones()
        self.escena4_cambio_direccion()
        self.escena5_velocidad_maxima()
        self.escena6_encuentro_ab()
        self.escena7_retorno_c_distancia()
        self.escena8_conclusiones()
        self.escena9_simulacion_final()
