# Generador de Contactos Ficticios MECE

Este script genera contactos ficticios siguiendo la plantilla CSV de Go High Level y los principios MECE (Mutuamente Exclusivos, Colectivamente Exhaustivos).

## Características

- **Estructura MECE**: Cada categoría es independiente y cubre todos los sectores relevantes
- **Datos realistas**: Nombres, empresas y contactos que simulan datos reales
- **Formato compatible**: CSV con la misma estructura que el archivo original
- **Personalizable**: Configurable para generar cualquier cantidad de contactos

## Principios MECE implementados

### Mutuamente Exclusivos
- Cada sector de negocio es independiente
- Las etiquetas no se solapan entre categorías
- Los tipos de empresa son claramente diferenciables

### Colectivamente Exhaustivos
- Cubre todos los sectores de negocio principales
- Incluye diferentes tipos de empresa (autónomo, PYMES, grandes empresas)
- Abarca todos los estados de lead relevantes

## Sectores de negocio incluidos

1. **Alimentación**: Panaderías, carnicerías, pescaderías, etc.
2. **Servicios Profesionales**: Consultorías, asesorías, despachos
3. **Comercio**: Tiendas, establecimientos comerciales
4. **Salud**: Clínicas, farmacias, centros médicos
5. **Educación**: Academias, centros de formación, escuelas
6. **Tecnología**: Empresas de software, startups, consultoría IT
7. **Inmobiliaria**: Agencias, promotoras, gestoras
8. **Automoción**: Talleres, concesionarios, autoescuelas
9. **Servicios Legales**: Bufetes, despachos de abogados
10. **Finanzas**: Asesorías financieras, gestorías, consultoría fiscal

## Instalación y uso

### Requisitos
- Python 3.7 o superior
- No se requieren dependencias externas

### Ejecución
```bash
python generate_fake_contacts.py
```

### Uso interactivo
El script te preguntará cuántos contactos quieres generar. Por defecto genera 100.

### Salida
El script genera un archivo CSV con el formato:
```
contactos_ficticios_mece_YYYYMMDD_HHMMSS.csv
```

## Estructura del archivo generado

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| Contact Id | Identificador único | "a1b2c3d4e5f6g7h8i9j0" |
| First Name | Nombre | "Ana" |
| Last Name | Apellidos | "García Martínez" |
| Business Name | Nombre del negocio | "Panadería Ana" |
| Company Name | Nombre de la empresa | "García Consultores S.L." |
| Phone | Teléfono principal | "+34611111111" |
| Email | Correo principal | "ana.garcia@panaderia.com" |
| Created | Fecha de creación | "2024-06-01T10:00:00+02:00" |
| Last Activity | Última actividad | "2024-06-10T12:00:00+02:00" |
| Tags | Etiquetas separadas por comas | "sector-alimentación, pyme, comercio-local" |
| Additional Emails | Correos adicionales | "ana.garcia2@gmail.com" |
| Additional Phones | Teléfonos adicionales | "+34611111112" |

## Personalización

Puedes modificar el script para:
- Añadir nuevos sectores de negocio
- Cambiar las etiquetas disponibles
- Modificar los dominios de email
- Ajustar los prefijos telefónicos
- Personalizar los tipos de empresa

## Ejemplo de uso

```bash
$ python generate_fake_contacts.py
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

## Ventajas del enfoque MECE

1. **Clasificación clara**: Cada contacto pertenece a una categoría específica
2. **Sin duplicaciones**: Las etiquetas no se solapan
3. **Cobertura completa**: Todos los sectores están representados
4. **Escalabilidad**: Fácil añadir nuevas categorías sin conflictos
5. **Análisis eficiente**: Permite segmentación y análisis por categorías

## Licencia

Este script es de uso libre para fines educativos y comerciales.
