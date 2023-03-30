# Predicción de Salarios en STEM en EE.UU

---------------------------------------------

![stem](https://github.com/SantiRiccardi/STEM-Salary-Prediction/blob/main/img/STEM.jpg)


## **Introducción**
**¿Qué son las carreras STEM?** <br>

El término STEM es el acrónimo de los términos en inglés Science, Technology, Engineering and Mathematics (Ciencia, Tecnología, Ingeniería y Matemáticas). Por tanto, las carreras STEM son todas las que incluyen habilidades y conocimientos en alguna de estas disciplinas.<br>

**¿Cuáles son las carreras STEM con más salidas laborales?**

El auge de las nuevas tecnologías y el volumen de datos que se gestiona está creciendo a gran velocidad. Por eso, se precisan profesionales que puedan responder a la demanda actual generada, así como que sean capaces de adaptarse a las demandas del futuro. 

Uno de los campos que más profesionales STEM requerirá en el futuro es el de la digitalización. De hecho, la Unión Europea estima que el 45% de los empleos en 2022 estarán relacionados con el ámbito digital, según datos del estudio Empleabilidad y Talento Digital 2020.

En este sentido, el informe InfoJobs-Esade 2020 Estado del Mercado Laboral en España revela que las dos carreras con más oportunidades profesionales son Ingeniería Informática e Ingeniería de Telecomunicaciones. De ahí que carreras relacionadas con la informática, la ciberseguridad, el desarrollo software, el desarrollo de experiencia de usuario (UX), el análisis y la ciencia de datos, el Internet de las Cosas (IoT) o la inteligencia artificial (IA) y la robótica, así como las implicadas en la automatización de procesos, sean cada vez más demandadas. 

## **Objetivo**
El objetivo principal del Proyecto es el de Predecir el Salario de las carreras STEM basado en características como la educación, años de experiencia, genero, entre otras. Dicha predicción se obtiene a través de la creación de una Aplicación Web realizada con Streamlit, en la cual el usuario solo deberá ingresar sus datos y así obtener de manera inmediata una prediccion del salario que le correspondería de acuerdo a la información cargada. 

## **Estructura de Carpetas**
### [src](/src)
* data
    + raw: los datasets en crudo de datos necesarios para empezar con el análisis y el modelo. 
    + processed: datos ya limpios que son los utilizados en el entrenamiento del modelo.
* utils: todos los modulos y funciones auxiliares creados para el desarrollo del proyecto.
* notebooks: notebooks de limpieza, procesado, EDA y modelos de Machine Learning.
    + project_resume.ipynb: notebook limpio donde resumas los pasos que has seguido en el proyecto y sirva como memoria del proyecto.
* train.py: entrenamiento del modelo.
* model: guarda aquí tus modelos ya entrenados y listos para poner en producción. 

### [app](/app)


## ¿Qué problema o necesidad vamos a resolver? ¿Podemos solucionarlo con ML?
La mayoría de las paginas webs que nos ofrecen datos reales sobre salarios solo nos predicen, de acuerdo al tipo de trabajo que nos interesa saber, un rango genérico basado en miles de datos cargados por distintos usuarios con distintas características laborales. Es por eso, que la creación de la siguiente webb app nos proporciona una prediccion mucho mas personalizada, certera y acorde a cada tipo de persona y trabajo que desee en el area STEM. 

## ¿Qué solución aporta tu modelo de ML?
Ofrece una aproximación de las 10 carreras mas demandadas en STEM cuyas empreesas radiquen en EE.UU, pais en donde se concentran las companias mas poderosas y de mayor tasa de empleabilidad. A través de la carga de datos personales, el usuario puede obtener una aproximación de su salario de acuerdo a su educacion, genero, años de experiencia, entre otras.

## ¿Qué modelos has probado?
Se pusieron a prueba 9 Modelos. 
Se realizo 4 tipos de Escalados.
Se Optimizaron los Hiperparamétros de los 2 mejores modelos.
Tambien se intentaron metodos como Reduccion de Dimension, lo cual no dio buenos resultados.


## ¿Qué resultados y conclusiones has obtenido?
Se necesitaría un dataset con mayor volúmen. Pero los datos tambien nos arrojaron que existe Oversampling, lo cuál puede ser la causa principal de las bajas métricas ya que hay un desbalanceo de clases en las variables categóricas como es el caso del title.

## ¿Cuáles han sido las variables de mayor impacto?
Aquellas con mayor correlación fueron: los años de experiencia, el level senior, region west y software engineering manager. 

## ¿Qué decisiones o acciones te permiten llevar a cabo tu modelo? 
Puede ayudar a los usuarios a tratar de entender que requisitos son los que más peso tienen a la hora de obtener un mejor salario. A su vez, sirve como guía para su formación profesional. 

## ¿Qué consecuencias tiene en negocio?
En la búsqueda de empleo, cada usuario ya puede contar a priori con el monto que debería recibir. A su vez, brinda información sobre en que aspectos las companias hacen foco a la hora de contratar, es decir, que características son las más relevantes. Si bien no se llego a introducir en la webb app, en la seccion de explore, el usuario tendrá la posibilidad de visualizar las características mas relevantes que son requeridas lo cual brinda también valiosa informacíon para aquellos usuarios que tienen pensado introducirse en alguna de las carreras de esta industria.
