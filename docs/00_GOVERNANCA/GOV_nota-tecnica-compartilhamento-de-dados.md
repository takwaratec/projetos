---
author:
- affiliation: Universidade de Brasília / Núcleo Takwara
  name: Takwara, Fabio Resck
  orcid: 0000-0001-8815-3885
date: '2026-03-04'
10.5281/zenodo.18827106
language: pt-BR
license: CC BY 4.0
series: Governança de Dados
title: Política de Acesso Digital e Compartilhamento da Documentação
translations:
  en: GOV_nota-tecnica-compartilhamento-de-dados_en.md
  es: GOV_nota-tecnica-compartilhamento-de-dados_es.md
  pt: GOV_nota-tecnica-compartilhamento-de-dados.md
type: Governança
version: '2.0'
---

# Política de Acesso Digital e Compartilhamento

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.18827106-blue.svg)](https://doi.org/10.5281/zenodo.18827106)
[![Licença: CC BY 4.0](https://img.shields.io/badge/Licen%C3%A7a-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![🇧🇷 PT](https://img.shields.io/badge/🇧🇷-Português-green)](./GOV_nota-tecnica-compartilhamento-de-dados.md) [![🇺🇸 EN](https://img.shields.io/badge/🇺🇸-English-blue)](./GOV_nota-tecnica-compartilhamento-de-dados_en.md) [![🇪🇸 ES](https://img.shields.io/badge/🇪🇸-Español-orange)](./GOV_nota-tecnica-compartilhamento-de-dados_es.md)
![Status](https://img.shields.io/badge/status-V2.0%20(Advocacy%205.1)-blue)
[![🇧🇷 PT](https://img.shields.io/badge/🇧🇷-Português-green)](./GOV_nota-tecnica-compartilhamento-de-dados.md) [![🇺🇸 EN](https://img.shields.io/badge/🇺🇸-English-blue)](./GOV_nota-tecnica-compartilhamento-de-dados_en.md) [![🇪🇸 ES](https://img.shields.io/badge/🇪🇸-Español-orange)](./GOV_nota-tecnica-compartilhamento-de-dados_es.md)
![Status](https://img.shields.io/badge/status-V2.0%20(Advocacy%205.1)-blue)

---

## 1. Objetivo e princípios

Esta nota define como a documentação da Plataforma Amazônia Regenerativa (PAR) será compartilhada com parceiros técnicos, institucionais e financiadores, conciliando três requisitos:

- Proteção de conteúdo estratégico (projetos em elaboração, arranjos tecnológicos, modelos de negócio);
- Facilidade de acesso para parceiros que não são usuários avançados de TI;
- Aderência à lógica de transparência progressiva do projeto (documentos “vivos” vs. versões estáveis).

A estratégia adota **camadas de acesso** e **múltiplos formatos de entrega**, em vez de um único canal, para atender desde colaboradores de engenharia até gestores públicos de alto nível.

---

## 2. Camadas de acesso digital

### 2.1. Camada 0 – Pública (quando aplicável)

- **Conteúdo:** versões públicas já lançadas com DOI (ex.: Cartilha, Manual de Fitorremediação, Plataforma v5.1 quando publicada), notas de divulgação, resumos executivos sem informação sensível.
- **Canais:** Zenodo (coleção DOI), site institucional, e-mails oficiais de divulgação.
- **Perfil de acesso:** qualquer pessoa, sem autenticação.

### 2.2. Camada 1 – Restrita: GitHub + GitHub Pages privado

- **Conteúdo:** versão “viva” da documentação técnica (MkDocs), incluindo rascunhos de anexos, memorial técnico, SMGA, notas internas; documentação de engenharia, governança, modelos de dados, manuais operacionais ainda em teste.
- **Segurança:** site estático visível apenas a usuários autenticados no GitHub com permissão de leitura. Todo o histórico é versionado e auditável via Git.

### 2.3. Camada 2 – Restrita simplificada: PDFs e pacotes estáveis

- **Conteúdo:** “fotografias” estáveis dos documentos principais (PDF ou ZIP do site estático) por marco de projeto (Versões 1.0, 2.0, etc.).
- **Canais:** envio direto por e-mail (PDF/ZIP), compartilhamento via Drive/Nextcloud institucional com permissões de leitura.

---

## 3. Modelos de compartilhamento com tipos de parceiros

### 3.1. Parceiro tecnológico (ex.: Imperveg, Jesiel, fabricantes, laboratório)
- **Acesso principal:** Camada 1 (GitHub Pages privado) + acesso ao código/documentos no repositório.

### 3.2. Parceiro acadêmico/institucional (UnB, UFAC, Embrapa, institutos)
- **Acesso:** Núcleo técnico (Camada 1), Coordenação/direção (Camada 2 - PDFs).

### 3.3. Financiadores e avaliadores (BNDES, Fundo Amazônia, FAPs, bancos)
- **Acesso:** Dossiês formais submetidos em PDF (Camada 2).

---

## 4. Governança e revisões desta política

Esta nota será revisada sempre que houver mudança relevante nas políticas de acesso do GitHub ou na infraestrutura da Plataforma. Versões atualizadas serão mantidas no repositório de governança.

---

*Plataforma Amazônia Regenerativa — Série Técnica — Aplicabilidade Nacional*  
*Núcleo Takwara — Universidade de Brasília (UnB)*