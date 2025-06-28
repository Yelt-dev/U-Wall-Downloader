# U-Wall-Downloader

## 📦 Requisitos

- Python 3.7 o superior

## ✅ Instalación de dependencias y entorno virtual

1. Abre la terminal o CMD.
2. Crea un entorno virtual:

   ```bash
   python -m venv venv
   ```

3. Activa el entorno virtual:

   - Windows:

     ```bash
     venv\Scripts\activate
     ```

   - macOS / Linux:

     ```bash
     source venv/bin/activate
     ```

4. Instala dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuración

Crea un archivo `.env` con:

```
UNSPLASH_ACCESS_KEY=tu_api_key_de_unsplash
CATEGORY=paisajes
DOWNLOAD_FOLDER=imagenes
```

## 🚀 Uso manual

Con el entorno virtual activado, ejecuta:

```bash
python script.py
```

## 🔥 Lanzador automático

### Windows (`lanzar.bat`)

```
@echo off
call venv\Scripts\activate.bat
python script.py
```

Programa este archivo en el Programador de Tareas para ejecución diaria.

### macOS / Linux (`lanzar.sh`)

```
#!/bin/bash
source venv/bin/activate
python3 script.py
```

Hazlo ejecutable:

```bash
chmod +x lanzar.sh
```

Agrega a `cron` con:

```
0 9 * * * /ruta/al/lanzar.sh
```

## ⏰ Ejecución diaria

- **Windows:** Usar el Programador de Tareas con el `.bat`.
- **macOS / Linux:** Usar `cron` como se indica arriba.

## 📝 Notas

- Usa entorno virtual para evitar conflictos de dependencias globales.
- Log de imágenes guardadas en `downloaded.json`.
- El script verifica conexión a internet y muestra notificaciones locales.
