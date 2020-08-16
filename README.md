# Bandwidth
Script para el monitoreo de Bandwidth en un equipo


***Instalar python-3.8.5-amd64 en la laptop***	


***Instalar las depencias de Python***

	>pip install pandas matplotlib web.py

# Instalar la app desde git
Para Realizar la instalacion desde GitHub es procedimiento es muy sencillo.
Debes considerar tener instalador git en la maquina anfitrion 

- Abrir un CMD desde C:\ 
- ejecutar el comando 
    >git clone https://github.com/lmvillegas/Bandwidth.git

# Importacion de la Tarea en Task Scheduler

Ya con esto tendras el software en tu maquina ahora solo falta crear la tarea en el **Task Schedule** 
para que se ejecute con una frecuencia de 30 min.
- Abrir el Task Scheduler desde el menu de actions encontraran un boton de import Task 
- al darle clic sobre ese boton nos pedira un archivo xml el cual se encuentra en la ruta C:\Bandwidth 
- Importar el Archivo Task_Scheduler_Log_speedTest.xml

Con estos pasos ya tendremos la tarea creada y en ejecucion de nuestro scritp 

# Instalacion Tradicional
Para el proceso de instalacion manual descargan el paquete en formato .zip
- copiar el contenido del directorio de Bandwidth en C:\
- La ruta final del app debe ser C:\Bandwidth para que la importacion del Task Scheduler encaje perfectamente.

[Realizar las actividades de Importacion de la Tarea en Task Scheduler](#importacion-de-la-tarea-en-task-scheduler)

@lmvillegas :+1: est� listo para ponerlo en Marcha! :shipit: