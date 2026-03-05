---
description: Firewall restritivo contra cruzamento de dados sensíveis na arquitetura
---

# Regra de Firewall do Agente: Contenção de Espionagem e Privacidade

A pasta `docs/99_RESTRITO/` contém rascunhos de dossiês contra ONGs, relatórios estritamente financeiros de subvenção da Plataforma, comunicações institucionais sensíveis e projetos fechados do BNDES. Logo, as seguintes regras são **IMUTÁVEIS**:

## 1. Tratamento Hermético de Dados
- Sob NENHUMA circunstância dados lidos, analisados ou gerados dentro da pasta `99_RESTRITO/` podem ser mesclados, compilados, citados, inferidos ou resumidos em respostas que produzirão artefatos para as pastas de `00` a `08`.
- A pasta 99 opera como um silo cego de banco de dados: você, enquanto IA, só deve cruzar informações dessa pasta se o usuário EXPLICITAMENTE solicitar um output na própria pasta `99_RESTRITO/` ou num canal não-público (`task` temporário).

## 2. Bloqueio de Indexação
- Nem mesmo de forma codificada ou como *tags*, assuntos da pasta 99 podem vazar para arquivos raiz globais de indexação, como o `mkdocs.yml`, tags de repositório, manuais da equipe, arquivos do Zenodo ou READMEs públicos.

**O não cumprimento deste firewall compromete a segurança diplomática e as fundações éticas da Plataforma.**
