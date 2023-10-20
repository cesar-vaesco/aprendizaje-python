### Entorno virtual Python

- Un entorno virtual es un entorno Python en el que el intérprete Python, las bibliotecas y los scripts instalados en él están aislados de los instalados en otros entornos virtuales, y (por defecto) cualquier biblioteca instalada en un «sistema» Python, es decir, uno que esté instalado como parte de tu sistema operativo.
- Un entorno virtual es un árbol de directorios que contiene archivos ejecutables de Python y otros archivos que indican que es un entorno virtual.

#### Crear un entorno vitual
- En la terminal o cmd situandose donde se creo el entorno virtual digitar el siguiente script: 
    - python -m venv nombre_entorno
        - Ejemplo: -->> python -m venv 19-databases
    - El anterior script genera el entorno virtual
#### Activar el entorno virtual
- En la terminal o cmd situandose donde se creo el entorno virtual digitar el siguiente script:
    - .\nombre_entorno\Scripts\
        - Ejemplo: -->   .\19-databases\Scripts\activate
    - El anterior "script" activa el entorno virtual
#### Desactivar el entorno virtual 
- En la terminal o cmd situandose donde se creo el entorno virtual digitar el siguiente script:
    - deactivate
        - Ejemplo: (19-databases) @cesar ➜ python_curso git(main) deactivate  
    - El anterior "script" desactiva el entorno virtual


