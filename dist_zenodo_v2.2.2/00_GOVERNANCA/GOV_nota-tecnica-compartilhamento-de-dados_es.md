---
author:
- affiliation: Universidade de Brasília / Núcleo Takwara
  name: Takwara, Fabio Resck
  orcid: 0000-0001-8815-3885
date: '2026-03-04'
doi: 10.5281/zenodo.18882784
language: es
license: CC BY 4.0
series: Gobernanza de Datos
title: Política de Acceso Digital y Uso Compartido de la Documentación
translations:
  en: GOV_nota-tecnica-compartilhamento-de-dados_en.md
  es: GOV_nota-tecnica-compartilhamento-de-dados_es.md
  pt: GOV_nota-tecnica-compartilhamento-de-dados.md
type: Gobernanza
version: '2.1'
---

# Política de Acceso Digital y Uso Compartido

**Serie:** Gobernanza **Versión:** 2.0 | **Data:** 2026-03-04 | **Autor:** Fabio Takwara | **Licencia:** CC BY 4.0 | **DOI:** 10.5281/zenodo.18882784

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.18882784-blue.svg)](https://doi.org/10.5281/zenodo.18882784)
[![Licencia: CC BY 4.0](https://img.shields.io/badge/Licencia-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![🇧🇷 PT](https://img.shields.io/badge/🇧🇷-Portugués-green)](./GOV_nota-tecnica-compartilhamento-de-dados.md) [![🇺🇸 EN](https://img.shields.io/badge/🇺🇸-Inglés-blue)](./GOV_nota-tecnica-compartilhamento-de-dados_en.md) [![🇪🇸 ES](https://img.shields.io/badge/🇪🇸-Español-orange)](./GOV_nota-tecnica-compartilhamento-de-dados_es.md)
![Status](https://img.shields.io/badge/status-V2.0%20(Advocacy%205.1)-blue)

---

## 1. Objetivo y Principios

Esta nota define cómo se compartirá la documentación de la Plataforma Amazonía Regenerativa (PAR) con socios técnicos, institucionales y financistas, conciliando tres requisitos:

- Protección de contenido estratégico (proyectos en elaboración, arreglos tecnológicos, modelos de negocio);
- Facilidad de acceso para socios que no son usuarios avanzados de TI;
- Adhesión a la lógica de transparencia progresiva del proyecto (documentos “vivos” vs. versiones estables).

La estrategia adopta **capas de acceso** y **múltiples formatos de entrega**, en lugar de un único canal, para atender desde colaboradores de ingeniería hasta gestores públicos de alto nivel.

---

## 2. Capas de Acceso Digital

### 2.1. Capa 0 – Pública (cuando sea aplicable)

- **Contenido:** versiones públicas ya lanzadas con DOI (ej.: Cartilla, Manual de Fitorremediación, Plataforma v5.1 cuando se publique), notas de divulgación, resúmenes ejecutivos sin información sensible.
- **Canales:** Zenodo (colección DOI), sitio web institucional, correos electrónicos oficiales de divulgación.
- **Perfil de acceso:** cualquier persona, sin autenticación.

### 2.2. Capa 1 – Restringida: GitHub + GitHub Pages privado

- **Contenido:** versión “viva” de la documentación técnica (MkDocs), incluidos borradores de anexos, memoria técnica, SMGA, notas internas; documentación de ingeniería, gobernanza, modelos de datos, manuales operativos aún en prueba.
- **Seguridad:** sitio estático visible solo para usuarios autenticados en GitHub con permiso de lectura. Todo el historial está versionado y es auditable vía Git.

### 2.3. Capa 2 – Restringida simplificada: PDFs y Paquetes Estables

- **Contenido:** “fotografías” estables de los documentos principales (PDF o ZIP del sitio estático) por hito del proyecto (Versiones 1.0, 2.0, etc.).
- **Canales:** envío directo por correo electrónico (PDF/ZIP), uso compartido a través de Drive/Nextcloud institucional con permisos de lectura.

---

## 3. Modelos de Uso Compartido con Tipos de Socios

### 3.1. Socio tecnológico (ej.: Imperveg, Jesiel, fabricantes, laboratorio)
- **Acceso principal:** Capa 1 (GitHub Pages privado) + acceso al código/documentos en el repositorio.

### 3.2. Socio académico/institucional (UnB, UFAC, Embrapa, institutos)
- **Acceso:** Núcleo técnico (Capa 1), Coordinación/dirección (Capa 2 - PDFs).

### 3.3. Financistas y evaluadores (BNDES, Fondo Amazonia, FAPs, bancos)
- **Acceso:** Dossiers formales presentados en PDF (Capa 2).

---

## 4. Gobernanza y Revisiones de esta Política

Esta nota se revisará siempre que haya un cambio relevante en las políticas de acceso de GitHub o en la infraestructura de la Plataforma. Las versiones actualizadas se mantendrán en el repositorio de gobernanza.

---

*Plataforma Amazonía Regenerativa — Serie Técnica — Aplicabilidad Nacional*  
*Núcleo Takwara — Universidad de Brasília (UnB)*
