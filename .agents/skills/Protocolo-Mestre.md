---
title: Protocolo-Mestre (Meta-Skill)
description: Roteador principal de domínio. Analisa o contexto e carrega multiplas Skills (Ex: Ciência + Advocacy) simultaneamente.
---

# Meta-Skill: Protocolo-Mestre de Roteamento

Este documento funciona como a **Mesa de Som (Mixer)** das habilidades da Inteligência Artificial. Ele impede que o Agente atue "cego" usando apenas uma lente acadêmica ou apenas uma lente militante, quando o projeto exige as duas.

## Instrução de Triangulação de Domínio
Sempre que o Agente for acionado para criar, revisar ou documentar na Plataforma Amazônia Regenerativa, ele deve cruzar automaticamente as matrizes abaixo de acordo com a pasta ou o comando invocado:

### 1. Cruzamento: Ciência + Advocacy (Dossiês e Artigos)
**Quando usar:** Quando operar nas pastas `05_ADVOCACY_COP30`, `07_BLOG_MEDIUM`, ou acionar os comandos `/triage`, `/publicar_advocacy`.
**Ação do Agente:** 
- Carregar a **Advocacy Skill** (para o tom combativo e denúncia do lobby).
- Carregar a **Research Skill** e **Technology Skill** (para embasar a denúncia com a ciência de materiais do PU/Bambu, evitando discurso vazio).

### 2. Cruzamento: Engenharia + Governança (Memoriais Técnicos)
**Quando usar:** Quando operar nas pastas `01_TECNOLOGIA_TAKWARA`, `02_PESQUISA_DESENVOLVIMENTO` ou acionar `/doi-sync`.
**Ação do Agente:** 
- Carregar a **Technology Skill** e **Management Skill** (para descritivos estruturais, como Biorrefinaria ou Geodésicas).
- Carregar a **Governance Skill** (para padronização, autoria, financiabilidade e licenças).
- *A Advocacy Skill é silenciada aqui*, mantendo a Persona do Autor como estritamente institucional/científica.

### 3. Cruzamento Singular: Preservação Histórica
**Quando usar:** Pasta `06_ANAIS_MEMORIA`.
**Ação do Agente:** Carregar exclusivamente a **Annals Skill**.

## O Ponto Cego (Gatilho de Segurança)
Se o usuário pedir algo ambíguo ("Escreva um texto sobre bambu"), o Agente deve **PARAR** e exigir do usuário: *"Autor, este documento deve ser roteado pelo eixo da Ciência (documento técnico) ou do Advocacy (denúncia/blog)?"*
