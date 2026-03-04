---
author:
- affiliation: Universidade de Brasília / Núcleo Takwara
  name: Takwara, Fabio Resck
  orcid: 0000-0001-8815-3885
date: '2026-03-04'
doi: 10.5281/zenodo.18827106
language: en
license: CC BY 4.0
series: Data Governance
title: Digital Access and Documentation Sharing Policy
translations:
  en: GOV_nota-tecnica-compartilhamento-de-dados_en.md
  es: GOV_nota-tecnica-compartilhamento-de-dados_es.md
  pt: GOV_nota-tecnica-compartilhamento-de-dados.md
type: Governance
version: '2.0'
---

# Digital Access and Sharing Policy

**Series:** Governance **Version:** 2.0 | **Date:** 2026-03-04 | **Author:** Fabio Takwara | **License:** CC BY 4.0 | **DOI:** 10.5281/zenodo.18827106

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.18827106-blue.svg)](https://doi.org/10.5281/zenodo.18827106)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![🇧🇷 PT](https://img.shields.io/badge/🇧🇷-Portuguese-green)](./GOV_nota-tecnica-compartilhamento-de-dados.md) [![🇺🇸 EN](https://img.shields.io/badge/🇺🇸-English-blue)](./GOV_nota-tecnica-compartilhamento-de-dados_en.md) [![🇪🇸 ES](https://img.shields.io/badge/🇪🇸-Spanish-orange)](./GOV_nota-tecnica-compartilhamento-de-dados_es.md)
![Status](https://img.shields.io/badge/status-V2.0%20(Advocacy%205.1)-blue)

---

## 1. Objective and Principles

This note defines how documentation of the Regenerative Amazon Platform (PAR) will be shared with technical, institutional partners, and funders, reconciling three requirements:

- Protection of strategic content (projects under preparation, technological arrangements, business models);
- Ease of access for partners who are not advanced IT users;
- Adherence to the project's progressive transparency logic ("live" documents vs. stable versions).

The strategy adopts **access layers** and **multiple delivery formats**, instead of a single channel, to serve everyone from engineering collaborators to high-level public managers.

---

## 2. Digital Access Layers

### 2.1. Layer 0 – Public (when applicable)

- **Content:** public versions already released with DOI (e.g., Handbook, Phytoremediation Manual, Platform v5.1 when published), dissemination notes, executive summaries without sensitive information.
- **Channels:** Zenodo (DOI collection), institutional website, official dissemination emails.
- **Access Profile:** anyone, without authentication.

### 2.2. Layer 1 – Restricted: GitHub + Private GitHub Pages

- **Content:** "live" version of the technical documentation (MkDocs), including draft annexes, technical memorial, SMGA, internal notes; engineering documentation, governance, data models, operational manuals still under testing.
- **Security:** static site visible only to authenticated GitHub users with read permission. Full history is versioned and auditable via Git.

### 2.3. Layer 2 – Restricted Simplified: PDFs and Stable Packages

- **Content:** stable "photographs" of the main documents (PDF or ZIP of the static site) by project milestone (Versions 1.0, 2.0, etc.).
- **Channels:** direct email delivery (PDF/ZIP), sharing via institutional Drive/Nextcloud with read permissions.

---

## 3. Sharing Models with Types of Partners

### 3.1. Technological Partner (e.g., Imperveg, Jesiel, manufacturers, laboratory)
- **Primary Access:** Layer 1 (Private GitHub Pages) + access to code/documents in the repository.

### 3.2. Academic/Institutional Partner (UnB, UFAC, Embrapa, institutes)
- **Access:** Technical core (Layer 1), Coordination/direction (Layer 2 - PDFs).

### 3.3. Funders and Evaluators (BNDES, Amazon Fund, FAPs, banks)
- **Access:** Formal dossiers submitted in PDF (Layer 2).

---

## 4. Governance and Policy Revisions

This note will be revised whenever there is a relevant change in GitHub access policies or Platform infrastructure. Updated versions will be maintained in the governance repository.

---

*Regenerative Amazon Platform — Technical Series — National Applicability*  
*Takwara Nucleus — University of Brasília (UnB)*
