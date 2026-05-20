Conservar los ultimos 10 reportes y de cada dia dejar el reporte con el maximo porcentaje de avance para descartar al maximo pruebas fallidas. Ajustar reports.json para que no se descuadre respecto a las carpetas de los reportes.

Si en el archivo reports.json progressPercent esta nulo se debe recalcular usando el archivo summary.json que esta dentro de cada carpeta de reporte respectiva.

Se deben borrar las carpetas sobrantes de repositorio que no esten referenciadas en el archivo reports.json