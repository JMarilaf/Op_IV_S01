# Solemne 01 - Optativo Especialidad IV

Este repositorio cuenta con 2 scraping a diferentes sitios web.

¿Que tanto puede variar el precio de los vehículos usados? 
¿Cuáles son las marcas y modelos más económicos y costosos?
¿Cuál es la media que debe recorrer un vehículo anualmente?
¿Cuál es la relación entre automático, mecánico e híbrido?

1. Chile Autos: El archivo 'ChileAutos.py' tiene como objetivo guardar todos los vehículos usados que se encuentran en venta para tener una visualizacón de como varían los precios dependiendo de la marca, el año y el modelo, pero hay un problema con los registros, no existe precisión al guardar los datos. El año, marca, modelo y versión de los autos está todo guardado en un solo 'string', lo cuál dificulta la precisión para capturar los valores, el año es fácil, solo se deben tomar los primeros 4 caracteres del string, en cambio los demás datos varía el tamaño de los datos, por lo cuál se dificulta la separación de esta información. Con el precio no hay problema porque siempre está fijo, lo siguiente es la demás información, que no es estatica en la web, cambia de lugar dependiendo del vehículo, la captura de datos no es precisa. Si bien el scraping se cumple. es por todo lo anterior, que se decidio probar con otra página, otro rubro.


¿Cuantos eventos hay planificdos actualmente?
¿Qué tipo de eventos son los más y menos presentados?
¿Cuánto pueden variar los precios?

2. Puntoticket: La idea es obtener todos los eventos que se presentarán en el país, guardando el artista, el lugar, la comuna, el tipo de evento, imagen y url. Todo esto para tener una lista de panoramas de entretención a la cuál pueden optar las persoinas que deseen pasar un buen rato.

 
