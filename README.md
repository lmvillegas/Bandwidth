# Bandwidth
Script para el monitoreo de Bandwidth en un equipo


__ Instalar python-3.8.5-amd64 en la laptop __


#.- instalar las depencias de Python 

	. pip install pandas matplotlib web.py

.- Descargar los archivos en la carpeta BandWidth y ubicarlos en C:\Bandwidth
.- Abrir Task Schelude e importar el Archivo Task_Scheduler_Log_speedTest.xml
	esto creara una tarea programada que se ejecutara cada media hora lo que permira realizar el escaneo de net BandWidth en el equipo configurado
.- una vez que se quieran ver los resultados es necesario ejecutar el server_to_web.py esto creara un servidor web ejecutandose desde http://localhost8080/bandwihtg donde se podran visualizar las graficas de las ulitimas 24 horas 



