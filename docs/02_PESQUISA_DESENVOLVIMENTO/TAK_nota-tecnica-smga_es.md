---
author:
- affiliation: Universidad de Brasilia / Núcleo Takwara
  name: Takwara, Fabio Resck
  orcid: 0000-0001-8815-3885
date: '2026-03-04'
10.5281/zenodo.18827106
10.5281/zenodo.18827106
keywords:
- monitoreo geoespacial
- biomasa
- bambú
- Guadua
- MRV
- GEDI
- Sentinel-2
- GBIF
- Amazonía
language: es
license: CC BY 4.0
series: Serie Técnica Plataforma Amazonía Regenerativa — Pesquisa y Desarrollo
subtitle: Arquitectura Técnica para el Inventario de Biomasa y MRV en Tiempo Real
title: 'Nota Técnica: Sistema de Monitoreo Geoespacial Automatizado (SMGA)'
translations:
  en: TAK_nota-tecnica-smga_en.md
  pt: TAK_nota-tecnica-smga.md
  es: TAK_nota-tecnica-smga_es.md
type: Boletín Técnico-Científico
version: '2.1'
---
# Nota Técnica: Sistema de Monitoreo Geoespacial Automatizado (SMGA)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.18827106-blue.svg)](https://doi.org/10.5281/zenodo.18827106)
[![Licencia: CC BY 4.0](https://img.shields.io/badge/Licencia-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![🇧🇷 PT](https://img.shields.io/badge/🇧🇷-Portugués-green)](./TAK_nota-tecnica-smga.md) [![🇺🇸 EN](https://img.shields.io/badge/🇺🇸-Inglés-blue)](./TAK_nota-tecnica-smga_en.md) [![🇪🇸 ES](https://img.shields.io/badge/🇪🇸-Español-orange)](./TAK_nota-tecnica-smga_es.md)
![Status](https://img.shields.io/badge/status-V2.1%20(Advocacy%205.1)-blue)
![Tipo](https://img.shields.io/badge/tipo-Boletín%20Técnico--Científico-teal)

---

## 1. Visão General y Justificación

El **Sistema de Monitoreo Geoespacial Automatizado (SMGA)** es el eje central de datos de la Plataforma Amazonía Regenerativa. Resuelve la brecha histórica de inventarios forestales independientes para el bambú nativo (*Guadua* spp.), proporcionando métricas auditables para la certificación de carbono (VERRA VM0044) y el monitoreo de la regeneración a escala regional.

## 2. Arquitectura Técnica (3 Capas)

### Capa 1: Ocurrencias Taxonómicas (Big Data)
Mapeo de registros georreferenciados históricos y actuales vía API REST:
- **GBIF & speciesLink**: Recolección automatizada de datos de herbario y observaciones de campo.
- **iNaturalist**: Validación comunitaria con evidencia fotográfica.

### Capa 2: Series Históricas y Sensoriamiento Remoto
Extracción de índices de vegetación y biomasa desde 1985:
- **Sentinel-2 & Landsat**: NDVI/NBR para la salud del bosque y detección de floración sincronizada.
- **GEDI (NASA/ISS)**: LiDAR espacial para la estimación directa de la altura del dosel y la biomasa aérea.

### Capa 3: Gobernanza y Transparencia (Blockchain-ready)
Integración de datos en un repositorio GitHub com hashes auditables, generando portales MkDocs automáticos para consulta pública.

## 3. Implementación Demostrativa Inmediata (Hoja de Ruta)

| Etapa | Acción | Plazo | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| **01** | Configuración del Repositorio y Scripts Python | Inmediato | Integración GBIF operativa |
| **02** | Extracción de AOI (Acre/Sudoeste Amazónico) | +48h | Mapa de densidad de *Guadua* spp. |
| **04** | Generación Automática de Informes MRV | +96h | PDF auditable para el Fondo Amazonía |

---
**APA:**
Takwara, F. R. (2026). *Nota Técnica: Sistema de Monitoreo Geoespacial Automatizado (SMGA)* (Versión 2.1). Boletín Técnico-Científico — Núcleo Takwara / Universidad de Brasilia. https://doi.org/10.5281/zenodo.18827106

---
**🎋 Takwara — Sustainable Technology and Sovereignty in the Amazon**
