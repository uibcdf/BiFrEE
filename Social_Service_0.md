# Drat del Servicio Social

# Posibles títulos

- Desarrollo de una librería de Open Source para el cálculo de la constante de afinidad de
  complejos proteícos.
- Calculo de la energía libre de unión entre biomoléculas mediante la mecánica molecular y el GBSA
- Cálculo de la constante de afinidad o disociación entre biomoléculas
- Abordajes MM/GB(PB)SA para el cálculo de la energía libre de unión entre biomoléculas

NOTA: ESTE DOCUMENTO DEBE GENERALIZARSE AL CASO PROTEINA-PROTEINA, PROTEINA-LIGANDO, PROTEINA-DNA,
...

# Introducción

Con esta herramienta podríamos por ejemplo predecir aquellas mutaciones del virus en la spike que
incrementaran la afinidad de dicha proteína por su receptor, con el consiguiente incremento de la
capacidad infectiva (creo que hay un paper de esto -lo tengo que buscar-).
Tambien se puede usar para el tema de anticuerpos.

A mi me interesa particularmente el tema protein-peptide para el proyecto de rosendo.

# Unidad didáctica

## Objetivos

- Elaboración de jupyter notebooks como documento resumen que será colgado en web de librería.
- Elaboración de slides para charla.

## Contenidos

El alumno debe, mediante el estudio guiado de la bibliografía científica, generar un discurso coherente, consistente y autocontenido, a modo de unidad didáctica, que contenga las respuestas a las siguientes cuestiones:

- Qué significa la energía libre? Qué relación tiene la energía libre de un estado termodinámico con la
  probabilidad de que este estado suceda?
- Qué es el peso de Boltzmann de un estado termodinámico?
- Qué relación hay entre la distribución de probabilidad de
  Boltzman de los estados de un sistema y la energía libre de Gibbs? y la energía libre de Helmholtz? En qué circunstancias?
- Qué significa función de partición de un estado termodinámico? Qué relación tiene con la probabilidad de que dicho estado suceda?
- Es lo mismo calcular la energía libre de unión de dos biomoléculas que las constantes de afinidad o de disociación?
- En una interpretación termodinámica (trabajo o calor) qué significado tienen los conceptos: diferencia de energía libre entre dos estados, variación de la energía libre entre dos estados, energía libre absoluta y energía libre relativa. Y en una interpretación de mecánica estadística (probabilidad)?
- Qué significado tienen los puntos anteriores para un proceso de unión/des-unión de un sistema
  compuesto por dos moléculas que interaccionan?
- Nos dice algo la energía libre de unión sobre la cinética de la reacción A+B <-> AB? De donde se
  deriva y qué significa la condición de balance detallado? Qué interpretación tiene como teorema de Bayes?
- Qué es un ciclo termodinámico? A qué llamamos rama de un ciclo termodinámico? Cuantas ramas puede
  tener un ciclo termodinámico?
- El método MM/GBSA es un "método de punto final" (end-point) para la predicción de la energía libre de unión. ¿Qué significa "método de punto final"?¿Qué otros métodos de punto final conocemos?¿Qué diferencias hay con los "métodos de camino" (pathway) para el mismo fín?
- En qué consisten los métodos MM/PBSA y MM/GBSA para el cálculo de energía libre de unión de dos
  biomoléculas?
- Según la literatura científica, son los abordajes MM/PBSA y MM/GBSA comparables en el cálculo de constantes de afinidad de dímeros protéicos?
- Qué es el método de solvente implícito GB? qué diferencias tiene con el PB?
- Qué información relevante puede darnos el cálculo de la variación de la energía libre de unión
  cuando se realizan mutaciones puntuales en la interfase?
- Cómo se define la interfase de interacción de un dímero? Qué son los hot-spots? Hay distintas
  jerarquías en el grado de implicación de un aminoácido en la estabilidad de la interacción
  proteína-proteína? Podemos encontrar aminoácidos distantes de la interfase con una participación
  relevante en la estabilidad de un dímero?
- Puede calcularse el grado de contribución a la estabilidad de un dímero de un aminoácido con el
  método MM/GBSA?
- Qué otros métodos teórico-computacionales hemos desarrollado para el cálculo de la energía libre
  de unión de dos biomoléculas (proteína-proteína, proteína-DNA, proteína-Ligando)?
- Puede el método MM/GBSA, o el MM/PBSA, calcular la contribución a la energía libre de unión por
  residuo o por parejas de residuos?
- ¿Qué importancia tiene la exploración del espacio conformacional del receptor y el ligando, sólos,
  como monómeros, en los métodos MM/PBSA y MM/GBSA?
- Para qué confiarías en un método como MM/PBSA o MM/GBSA: ¿Para obtener valores absolutos fiables
  de la constante de afinidad de un sistema receptor-ligando?¿O para decidir si un ligando es más
afín que otro frente a un mismo receptor? ¿Por qué?
- Dado el método MM/GBSA, o MM/PBSA, ¿Existen variaciones en su ejecución?¿Que significa, por
  ejemplo, llevar a cabo el método MM/PBSA mediante el protocolo estandard de un única
trayectoria?¿Qué otras variaciones conoces y con la intención de mejorar qué estimación han sido
diseñadas?
- Hoy en día contamos con abordajes teórico-computacionales más fiables o precisos para el cálculo
  de la afinidad de un receptor y un ligando. ¿Puedes mencionar alguno? ¿Qué motivos hay para seguir
usando MM/PBSA o MM/GBSA y en qué contextos?
- Qué métodos experimentales tenemos medir la energía libre de unión de un receptor y un ligando.
  Dicho de otra manera, con qué experimentos debemos validar nuestros métodos
teórico-computacionales de predicción de la afinidad de un ligando con un receptor?
- ¿Qué otras variaciones o estrategias se te ocurren, o conoces de la literatura, para mejorar el
  cálculo de la energía libre de solvatación del receptor, ligando y complejo -para dos de las
ramas del ciclo termodinámico-?
- ¿Qué otras variaciones conoces o se te ocurren para calcular el término entrópico de la
  diferencia de energía libre de unión en vacio del receptor y el ligando -una de las ramas del
ciclo termodinámico-?¿Por qué es más adecuado estimar la diferencia de energía libre en vacio?
- ¿Pueden estos métodos ser usados para calcular la estabilidad de un monómero que se encuentra
  plegado debido a su asociación con iones?
-¿Por qué calculamos la diferencia de energía libre de las ramas de solvatación con modelos de solvente implicito si sabemos
hacerlo con solvente explícito?¿Por qué resolvemos estas ramas con un método de punto final si
podemos hacerlo con un método de camino?
- Hay algún conjunto de sistemas receptor-ligando (protein-proteín, protein-ligand y
  protein-nucleic acids) en la comunidad recurrentemente usado en la literatura para el testeo y
benchmarking de estos métodos y sus variaciones?
- Qué es la entropia conformacional? Qué métodos conoces para estimarla?

# Librería

- No hay librería que automatice el flujo de trabajo para OpenMM. Si lo hay con gromacs, amber,
  namd y charmm.
- Elaboración de documentación en web


# Milestones

- Charla en el 3 mes con slides de unidad didáctica.
- Charla en el 6 mes con extensión de unidad didáctica a herramientas desarrolladas en la librería.

# Entregables

- Documento en Latex (unidades didácticas) con anexo de slides de las charlas.
- Librería en GitHub, donde se puede seguir la implementación así como las discusiones.
- Deployment de la librería.
- Documentación de la librería en web.
- Reporte del tutor de actividades adicionales como la asistencia a seminarios del laboratorio.

# Obligaciones Adicionales

- Asistencia a seminarios virtuales del laboratorio sobre el trabajo realizado por los investigadores y estudiantes del laboratorio.
- Asistencia a talleres virtuales sobre cuestiones de interés para su formación. 

# Calendario
- 240 horas para la unidad didáctica en el primer trimestre
- 240 horas para la elaboración de la librería en el segundo trimestre

# Qué aprendera el alumno

## El contexto científico del proyecto

- Herramientas y estratégias de búsqueda de bibliografía científica.
- Herramientas de gestión biobliográfica.
- Se hará uso de la librería OpenMM para llevar a cabo una pequeña simulación de dinámica molecular con la que demostrar el uso de la librería implementada. La función de este experimento no será la investigación, sino simplemente el obtener una o varias trayectorias sobre las que demostrar que la librería obtiene el ensemble relevante de modelos farmacofóricos.

## El trabajo en un laboratorio computacional de investigación

- Linux.
- Python y librerías científicas.
- Conda y Anaconda.
- Git, control de versiones.
- GitHub, desarrollo en colaboración de herramientas científicas.
- Jupyter lab and notebooks.
- Latex.
- Deployment of packages with conda.
- Creación de documentación científica con sphinx.
- Lenguages decorados: Markdown y rst.

