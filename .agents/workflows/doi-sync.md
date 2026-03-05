---
description: Sincronizador de Identificadores Persistentes (DOI) em Lote via Zenodo
---

# Workflow: `/doi-sync`

Como a Plataforma consolida diversos documentos soltos sob o *Master DOI da Plataforma 5.1* ou emite sub-DOIs modulares na base do Sistema Takwara, esse workflow tira o peso manual da checagem.

## Ação do Agente
Sempre que acionado, siga o processo:
1. Revise se o master DOI registrado em seu `system_prompt_takwara.txt` confere com o último registro validado.
2. Varra os cabeçalhos YAML (Frontmatter) de arquivos como relatórios mestres, memoriais técnicos e manuais.
3. Use script automatizado (Python/sed) se necessário, para garantir que as seções `doi: ...` de todos aqueles arquivos pontuais espelhem a identificação mestra da Coleção de V.2.0 (ex: 10.5281/zenodo.18827106, quando configurado ser o master).
4. Sincronize/substitua as insígnias estáticas geradas (`[![DOI]...]`) por todo o código para apontarem ao número correto.
5. Produza um diff de resumo reportando as alterações das versões.
