# Simulación de cinemática con Manim

Proyecto de Física del primer semestre de la Universidad Mayor de San Simón.
Representa el movimiento de tres vehículos en una pista recta y desarrolla los
cálculos con una animación en español de nueve secciones.

## Modelo físico

Se utiliza el sistema internacional: tiempo en segundos, posición en metros,
velocidad en m/s y aceleración en m/s². El sentido positivo es hacia la derecha.

| Vehículo | Movimiento | Posición |
| --- | --- | --- |
| A | Movimiento rectilíneo uniforme | `xA(t) = 25t` |
| B | Movimiento rectilíneo uniformemente acelerado | `xB(t) = 60 − 10t + 2t²` |
| C | Aceleración variable: `aC(t) = 12 − 4t` | `xC(t) = 150 + 6t² − (2/3)t³` |

La simulación final cubre de **0 a 9 segundos**. El desarrollo muestra:

- B cambia de dirección a los **2,5 s**, en **47,5 m**.
- C alcanza su velocidad máxima de **18 m/s** a los **3 s**.
- C cambia de dirección a los **6 s**, en **222 m**.
- A y B se encuentran primero a los **1,926327968… s**, en **48,1581992… m**.
  En pantalla se redondea a **1,93 s y 48,16 m**. El segundo encuentro matemático
  ocurre a los **15,573672… s**, fuera del intervalo de la simulación final.
- C regresa a su posición inicial a los **9 s**. Entonces A y B están separados
  por **93 m**.

La velocidad de C es una magnitud con signo: su máximo es 18 m/s. No debe
confundirse con la rapidez máxima; a los 9 s su velocidad es −54 m/s y su rapidez
es 54 m/s.

## Instalación

Versión de referencia: **Python 3.12 y Manim Community 0.19.0**. El archivo
`requirements.txt` fija la dependencia directa; no es un bloqueo completo de
todas las dependencias transitivas.

En Debian/Ubuntu, instala las herramientas del sistema:

```bash
sudo apt-get update
sudo apt-get install -y python3-dev python3-venv build-essential pkg-config \
  libcairo2-dev libpango1.0-dev ffmpeg dvisvgm \
  texlive-latex-base texlive-latex-extra texlive-fonts-recommended
```

Crea un entorno virtual desde la carpeta del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Las fórmulas se generan con `MathTex`, por lo que LaTeX y `dvisvgm` son necesarios.
En Windows o macOS, consulta la [instalación oficial de Manim](https://docs.manim.community/en/stable/installation.html)
para preparar las dependencias correspondientes. Los comandos del sistema
anteriores son específicos para Debian/Ubuntu.

## Generar el video

Ejecuta desde la carpeta principal, con el entorno virtual activado:

```bash
# Video completo en baja calidad, útil para comprobar cambios
python -m manim -ql simulacion_cinematica.py ProyectoCompleto

# Video en calidad alta
python -m manim -qh simulacion_cinematica.py ProyectoCompleto
```

Los resultados se guardan en `media/videos/simulacion_cinematica/` dentro de la
subcarpeta de calidad correspondiente. `media/` está excluido de Git. Para abrir
el resultado automáticamente en una computadora con reproductor gráfico, añade
`-p`, por ejemplo `python -m manim -pql simulacion_cinematica.py ProyectoCompleto`.
En un servidor sin escritorio, omite `-p`.

El archivo original sin extensión se renombró a `simulacion_cinematica.py` para
que el cargador de Manim pueda reconocerlo. La escena sigue llamándose
`ProyectoCompleto`.

## Pruebas

Las pruebas físicas no requieren instalar Manim:

```bash
python3 -m unittest discover -s tests -v
```

Cubren condiciones iniciales, ambos encuentros, precisión de la posición,
cambios de dirección, velocidad máxima, retorno de C y separación entre A y B.
También comparan la velocidad con la derivada numérica de la posición.

GitHub Actions ejecuta las pruebas físicas y un renderizado de baja resolución
de la escena completa. Las pruebas numéricas no sustituyen revisar visualmente
el video: comprueba legibilidad y composición cuando cambies el diseño.

## Organización

```text
simulacion_cinematica.py     Escena ProyectoCompleto, paneles y animaciones
cinematica.py                Funciones físicas sin dependencia de Manim
requirements.txt             Versión de Manim Community
tests/test_cinematica.py      Pruebas del modelo físico
.github/workflows/pruebas.yml Pruebas físicas y renderizado de comprobación
```

Las funciones de posición de `cinematica.py` se utilizan directamente en la
simulación final para evitar tener copias independientes del modelo. Las
fórmulas de los paneles explicativos conservan su desarrollo original.

## Cambios de mantenimiento

- Se corrigió la posición del encuentro: antes se multiplicaba por el tiempo
  ya redondeado y se mostraba 48,25 m. Ahora se calcula primero y se redondea al final.
- Se retiraron objetos que permanecían invisibles tras una transición.
- Se mantienen las nueve secciones, colores, diseño y duraciones originales.
  La corrección numérica cambia únicamente las expresiones del punto de encuentro.

Desarrollo mantenido con asistencia de IA. Los resultados físicos corresponden
al modelo ideal descrito, sin colisiones, tamaños reales de vehículos ni fricción.
