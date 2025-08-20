# 🎯 Generador de Contactos Ficticios MECE

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)](https://github.com/ricardopenalver/fake-contacts-generator)

Este script genera contactos ficticios siguiendo la plantilla CSV de Go High Level y los principios **MECE** (Mutuamente Exclusivos, Colectivamente Exhaustivos).

## ✨ Características

- **🏗️ Estructura MECE**: Cada categoría es independiente y cubre todos los sectores relevantes
- **🎭 Datos realistas**: Nombres, empresas y contactos que simulan datos reales
- **📊 Formato compatible**: CSV con la misma estructura que el archivo original
- **⚙️ Personalizable**: Configurable para generar cualquier cantidad de contactos
- **🚀 Sin dependencias**: Solo utiliza la biblioteca estándar de Python

## 🎯 Principios MECE implementados

### Mutuamente Exclusivos
- ✅ Cada sector de negocio es independiente
- ✅ Las etiquetas no se solapan entre categorías
- ✅ Los tipos de empresa son claramente diferenciables

### Colectivamente Exhaustivos
- ✅ Cubre todos los sectores de negocio principales
- ✅ Incluye diferentes tipos de empresa (autónomo, PYMES, grandes empresas)
- ✅ Abarca todos los estados de lead relevantes

## 🏢 Sectores de negocio incluidos

| Sector | Ejemplos | Etiquetas |
|--------|----------|-----------|
| **Alimentación** | Panaderías, carnicerías, pescaderías | `sector-alimentación`, `pyme`, `comercio-local` |
| **Servicios Profesionales** | Consultorías, asesorías, despachos | `servicios-profesionales`, `consultoría`, `asesoría` |
| **Comercio** | Tiendas, establecimientos comerciales | `comercio`, `retail`, `pyme` |
| **Salud** | Clínicas, farmacias, centros médicos | `sector-salud`, `sanidad`, `bienestar` |
| **Educación** | Academias, centros de formación, escuelas | `educación`, `formación`, `enseñanza` |
| **Tecnología** | Empresas de software, startups, consultoría IT | `tecnología`, `innovación`, `digital` |
| **Inmobiliaria** | Agencias, promotoras, gestoras | `inmobiliaria`, `construcción`, `real-estate` |
| **Automoción** | Talleres, concesionarios, autoescuelas | `automoción`, `transporte`, `vehículos` |
| **Servicios Legales** | Bufetes, despachos de abogados | `servicios-legales`, `jurídico`, `legal` |
| **Finanzas** | Asesorías financieras, gestorías, consultoría fiscal | `finanzas`, `fiscal`, `contabilidad` |

## 🚀 Instalación y uso

### Requisitos
- Python 3.7 o superior
- No se requieren dependencias externas

### Instalación rápida
```bash
# Clonar el repositorio
git clone https://github.com/ricardopenalver/fake-contacts-generator.git
cd fake-contacts-generator

# Ejecutar el script
python3 generate_fake_contacts.py
```

### Uso interactivo
```bash
python3 generate_fake_contacts.py
```

El script te preguntará cuántos contactos quieres generar. Por defecto genera 100.

### Salida
El script genera un archivo CSV con el formato:
```
contactos_ficticios_mece_YYYYMMDD_HHMMSS.csv
```

## 📊 Estructura del archivo generado

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `Contact Id` | Identificador único | `"a1b2c3d4e5f6g7h8i9j0"` |
| `First Name` | Nombre | `"Ana"` |
| `Last Name` | Apellidos | `"García Martínez"` |
| `Business Name` | Nombre del negocio | `"Panadería Ana"` |
| `Company Name` | Nombre de la empresa | `"García Consultores S.L."` |
| `Phone` | Teléfono principal | `"+34611111111"` |
| `Email` | Correo principal | `"ana.garcia@panaderia.com"` |
| `Created` | Fecha de creación | `"2024-06-01T10:00:00+02:00"` |
| `Last Activity` | Última actividad | `"2024-06-10T12:00:00+02:00"` |
| `Tags` | Etiquetas separadas por comas | `"sector-alimentación, pyme, comercio-local"` |
| `Additional Emails` | Correos adicionales | `"ana.garcia2@gmail.com"` |
| `Additional Phones` | Teléfonos adicionales | `"+34611111112"` |

## 🎨 Personalización

Puedes modificar el script para:
- ➕ Añadir nuevos sectores de negocio
- 🏷️ Cambiar las etiquetas disponibles
- 📧 Modificar los dominios de email
- 📱 Ajustar los prefijos telefónicos
- 🏢 Personalizar los tipos de empresa

## 📝 Ejemplo de uso

```bash
$ python3 generate_fake_contacts.py
Generador de Contactos Ficticios MECE
=====================================
¿Cuántos contactos quieres generar? (por defecto 100): 50
Generados 10 contactos...
Generados 20 contactos...
Generados 30 contactos...
Generados 40 contactos...
Generados 50 contactos...
Archivo 'contactos_ficticios_mece_20241219_143022.csv' generado exitosamente con 50 contactos únicos.

Archivo generado: contactos_ficticios_mece_20241219_143022.csv
Los contactos siguen los principios MECE:
- Mutuamente Exclusivos: Cada categoría es independiente
- Colectivamente Exhaustivos: Cubren todos los sectores relevantes
```

## 🎯 Ventajas del enfoque MECE

1. **📋 Clasificación clara**: Cada contacto pertenece a una categoría específica
2. **🚫 Sin duplicaciones**: Las etiquetas no se solapan
3. **🌍 Cobertura completa**: Todos los sectores están representados
4. **📈 Escalabilidad**: Fácil añadir nuevas categorías sin conflictos
5. **📊 Análisis eficiente**: Permite segmentación y análisis por categorías

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor:

1. 🍴 Haz un fork del proyecto
2. 🌿 Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push a la rama (`git push origin feature/AmazingFeature`)
5. 🔄 Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Ricardo Peñalver García**

- 📧 Email: [ricardopenalver@icloud.com](mailto:ricardopenalver@icloud.com)
- 🌐 LinkedIn: [Ricardo Peñalver García](https://linkedin.com/in/ricardopenalver)
- 🐙 GitHub: [@ricardopenalver](https://github.com/ricardopenalver)

## ⭐ ¿Te gustó el proyecto?

Si este proyecto te ha sido útil, ¡considera darle una estrella en GitHub! ⭐

---

**Nota**: Este script es de uso libre para fines educativos y comerciales.
