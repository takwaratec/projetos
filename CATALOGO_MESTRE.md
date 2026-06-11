# Catálogo Mestre do Ecossistema Takwara

> Gerado em: 2026-06-11
> Autor: Fabio Resck Takwara
> Propósito: Mapear todos os documentos, repositórios, DOIs e relações entre eles

---

## 1. Repositórios do Ecossistema

| Repositório | URL GitHub | URL Publicada | Finalidade |
|---|---|---|---|
| **Takwara-Tech** | `Resck/Takwara-Tech` | resck.github.io/Takwara-Tech | Site original de advocacia/blog, artigos COP30, calculadora de domos |
| **projetos** | `takwaratec/projetos` | takwaratec.github.io/projetos | Repositório técnico principal: documentação técnica, BNDES, P&D, anais |
| **Mulheres-Tecem-Amazonia** | `takwaratec/Mulheres-Tecem-Amazonia` | takwaratec.github.io/Mulheres-Tecem-Amazonia | Hub do consórcio UnB/UFRR/UFAC, dossiê BNDES completo |

---

## 2. Registros Zenodo

| DOI | Título | Tipo | Relação |
|---|---|---|---|
| **10.5281/zenodo.17225867** | Encruzilhadas Ambientais do Brasil — Relatório COP30 v1.0 | Publication / Report | **Collection/Parent** — site Takwara-Tech |
| **10.5281/zenodo.18827106** | Plataforma Amazônia Regenerativa v5.1 | Publication / Technical note | **isVersionOf** 17225867 — contém toda a série técnica |

### Observações sobre DOIs

- `zenodo.18827106` é o DOI usado por **todos os 5 boletins** em `01_TECNOLOGIA_TAKWARA` — cada um deveria ter seu próprio DOI
- `zenodo.17225867` (Takwara-Tech) não tem ligação explícita nos documentos com o conteúdo técnico de `projetos`
- **MQTF** não possui registro Zenodo próprio ainda
- O `.zenodo.json` no repositório `projetos` referencia o MQTF como `isVersionOf` → `18827106`, mas o título no Zenodo é "Plataforma Amazônia Regenerativa"

---

## 3. Estrutura de Documentos por Repositório

### 3.1 projetos (takwaratec/projetos)
**26.752 arquivos trackeado**s | **739 arquivos .md** | **Principal repositório de produção**

#### docs/ — Pastas estruturadas (247 .md)
| Pasta | .md files | Conteúdo |
|---|---|---|
| `00_GOVERNANCA` | 28 | Gestão de autoria, propriedade intelectual, matriz de correlação |
| `01_GOVERNANCA` | 3 | (versão anterior/reduzida) |
| `01_TECNOLOGIA_TAKWARA` | 13 (5 PT + 8 EN/ES) | **Boletins técnicos**: Solda Vegetal, Bioeconomia, Fitorremediação, Relatório Executivo, Tijolos Ecológicos |
| `02_PESQUISA_DESENVOLVIMENTO` | 32 | Relatórios P&D: biorrefinaria, PU Vegetal, SMGA, geodésicas, saneamento |
| `04_GESTAO_OPERACIONAL` | 4 | Gestão operacional |
| `05_ADVOCACY_COP30` | 6 | Dossiês estratégicos COP30 |
| `06_ANAIS_MEMORIA` | 18 | Documentos mestres (Plataforma v5.1), perfis de equipe, registros históricos |
| `07_BLOG_MEDIUM` | 69 | Arquivo completo de artigos publicados no Medium |
| `08_PROJETOS_ENGENHARIA` | 56 | Relatórios técnicos de equipamentos e patentes de tecnologia social |
| `09_DOSSIE_BNDES` | 14 | Formulários BNDES (consolidado, orçamento, migração C02) |
| `Arquivo Takwara` | **492** | **Arquivo legado** — versões antigas, documentos de referência, conteúdo não catalogado |
| `assets/`, `images/` | 0 | Mídia estática |

#### Root — Scripts e config (20+ arquivos)
| Arquivo | Função |
|---|---|
| `catalogador_takwara.py` | Catalogador de documentos |
| `final_organizer.py` | Organizador de arquivos |
| `final_sanitizer.py` / `final_sanitizer_pro.py` | Sanitizadores de metadados |
| `surgical_cataloger.py` | Catalogador cirúrgico (novo) |
| `RECONSTRUIR_ACERVO.py` | Script de reconstrução de acervo |
| `extract_refs.py` | Extrator de referências |
| `manual-git-zenodo.pdf` | Manual de operação Git/Zenodo |
| `manual-operacao-github.md` | Manual de operação GitHub |
| `MAPA_TEMATICO_WTF.md` | Mapa temático WTF |
| `gerar_mapa_tematico.py` | Gerador do mapa temático |

### 3.2 Takwara-Tech (Resck/Takwara-Tech)
**342 arquivos** | **101 arquivos .md** | **Site original de advocacia**

| Pasta | .md files | Conteúdo |
|---|---|---|
| `docs/A1. Tecnologias` | 12 | Tecnologias Takwara (versão blog) |
| `docs/A2. O Bambu` | 15 | Artigos sobre bambu |
| `docs/A2.a Personalidades` | 5 | Personalidades |
| `docs/A3. O PU Vegetal` | 2 | PU Vegetal |
| `docs/A4. Domos Geodésicos` | 4 | Domos geodésicos (inclui calculadora) |
| `docs/A6. COP30` | 9 | Artigos e denúncias COP30 |
| `docs/A7. Como Contribuir` | 4 | Como contribuir |

**⚠️ Arquivos com `#` no nome (espaços iniciais):** ~20 arquivos com problemas de nomenclatura (ex: `# A Trajetória da Degradação Nacional_ Das Promessas.md`) — provavelmente artefatos de exportação/conversão.

### 3.3 Mulheres-Tecem-Amazonia (takwaratec/Mulheres-Tecem-Amazonia)
**1.483 arquivos (branch main)** | **718 arquivos .md** | **Hub do consórcio**

| Pasta | .md files | Conteúdo |
|---|---|---|
| `docs/00_MODELO 1 - BNDES` | 5 | Modelo 1 BNDES |
| `docs/01_GOVERNANCA` | 78 | Governança completa (colaboradores, estratégia, orçamento, pareceres) |
| `docs/02_DIAGNOSTICO DE AREA` | 20 | Diagnóstico territorial |
| `docs/03_CIENTIFICO` | 1 | Científico |
| `docs/03_DOSSIE_BNDES` | 12 | Dossiê BNDES versão MQTF |
| `docs/03_ORCAMENTO_E_LOGISTICA` | 1 | Orçamento e logística |
| `docs/04_GESTAO_OPERACIONAL` | 75 | Gestão operacional, editais 2026 |
| `docs/04_PESQUISA_ANDAMENTO` | **523** | Pesquisas em andamento, acervo digital, resenhas técnicas |
| `docs/99_GOVERNANCA_IA` | 1 | Governança de IA |

**Nota:** Working tree limpo (main e gh-pages). Sem conteúdo local não commitado.

---

## 4. Sobreposições e Redundâncias

| Conteúdo | Onde aparece | Problema |
|---|---|---|
| **Boletins Técnicos** (Solda Vegetal, Bioeconomia, Fitorremediação, etc.) | `projetos/docs/01_TECNOLOGIA_TAKWARA/` + `dist_zenodo_v2.2.2/` | **Idênticos** — pastas sincronizadas, mas sem indicador de versão primária |
| **Dossiê BNDES** | `projetos/docs/09_DOSSIE_BNDES/` (Markdown) + `MQTF/docs/03_DOSSIE_BNDES/` (parcial) + `MQTF/03_CONSOLIDADO_BNDES_REVISADO_FINAL.md` (raiz) | Mesmo conteúdo em formatos diferentes, versões podem divergir |
| **Tecnologia Takwara** | `projetos/docs/01_TECNOLOGIA_TAKWARA/` (boletins) + `projetos/docs/Arquivo Takwara/01_TECNOLOGIA_CONSTRUTIVA/` (arquivo) + `Takwara-Tech/docs/A1. Tecnologias/` (blog) | Três versões do mesmo tema em níveis diferentes de maturidade |
| **Pesquisa PU Vegetal** | `projetos/docs/02_PESQUISA_DESENVOLVIMENTO/` (técnico) + `Takwara-Tech/docs/A3. O PU Vegetal/` (blog) | Sobreposição temática |
| **Conteúdo COP30** | `projetos/docs/05_ADVOCACY_COP30/` + `Takwara-Tech/docs/A6. COP30/` | Mesmo tema, públicos diferentes |

---

## 5. Documentos Locais sem Commit

### 5.1 projetos — 11 untracked + 1 modified

**Modificados (não commitados):**
| Arquivo | Status |
|---|---|
| `01_SOMBRA_AUDITORIA/04_PROJETO_WTF/03_PESQUISA_EM_ANDAMENTO/SONDA_DOCLING/00_INVENTARIO_CURADORIA_WTF.md` | Modificado |
| `catalogador_takwara.py` | Modificado |

**Deletados (D — removidos do working tree):**
~12 arquivos de imagem PNG (geração IA) em `01_SOMBRA_AUDITORIA/04_PROJETO_WTF/04_MIDIA/` — provavelmente removidos intencionalmente

**Novos (untracked):**
| Arquivo | Descrição |
|---|---|
| `final_organizer.py` | Script organizador |
| `final_sanitizer.py` | Script sanitizador |
| `final_sanitizer_pro.py` | Script sanitizador avançado |
| `surgical_cataloger.py` | Catalogador cirúrgico |
| `01_SOMBRA_AUDITORIA/00_GOVERNANCA/` | Nova pasta de governança |
| `01_SOMBRA_AUDITORIA/02_TECNICO/REVISAO_BIBLIOGRAFICA_TECNICA.md` | Revisão bibliográfica |
| `01_SOMBRA_AUDITORIA/04_PROJETO_WTF/01_GOVERNANCA/COMANDO_AGENTES_IA.md` | Comandos agentes IA |
| `01_SOMBRA_AUDITORIA/04_PROJETO_WTF/03_PESQUISA_EM_ANDAMENTO/TRANSCRIPT/...` | Transcrição raw |
| `01_SOMBRA_AUDITORIA/CLEAN_ROOM_STAGING/` | Staging |
| `01_SOMBRA_AUDITORIA/REPO_EXECUTIVO_2026/` | Repositório executivo |
| `dist_zenodo_v2.2.2/06_ANAIS_MEMORIA/perfis-equipe/TAK_plataforma-v5.1.md` | Arquivo extra no dist |

### 5.2 Takwara-Tech — 3 modified + 4 untracked

**Modificados:**
| Arquivo |
|---|
| `docs/Casa_Floresta_COP30.md` |
| `docs/Floresta_em_Pe-EN.md` |
| `docs/cop-da-verdade.md` |

**Novos (untracked):**
| Arquivo |
|---|
| `docs/A1. Tecnologias /Modulos gabarito.md` |
| `docs/BAncadas/` |
| `docs/Chapada Diamantina/` |
| `docs/Gabarito Metalon.txt` |
| `docs/Sem Título.html` |

### 5.3 MQTF
✅ Working tree limpo (main e gh-pages) — nada pendente

---

## 6. Problemas de Catalogação Identificados

### 6.1 Metadados
| Problema | Ocorrências | Severidade |
|---|---|---|
| `H.5281/zenodo.18827106` (campo inválido) | 10+ (todo frontmatter) | 🔴 Alta |
| `RR$` em vez de `R$` | 2 (cartilha bioeconomia) | 🟡 Média |
| `CPLI` em vez de `CLPI` | 1 (relatório executivo) | 🟡 Média |
| `Pu0026D` escapado | 1 (conexões estruturais) | 🟢 Baixa |

### 6.2 Nomenclatura
| Problema | Exemplos |
|---|---|
| Prefixos inconsistentes | `TAK_`, `RES_`, `WA_`, `_BIBLIOTECA_LEGADA_` |
| Arquivos com `#` no nome | `# A Trajetória...`, `#Artigo...` (Takwara-Tech) |
| Pastas com espaços | `A1. Tecnologias `, `A2.  O Bambu` (espaço duplo) |
| Nomes muito genéricos | `index.md` (em múltiplos lugares, sem desambiguação) |

### 6.3 Versionamento
| Problema |
|---|
| `dist_zenodo_v2.2.2/` é cópia exata de `docs/01_TECNOLOGIA_TAKWARA/` — sem indicador de qual é a primária |
| Arquivo extra no dist (`TAK_plataforma-v5.1.md`) que não está em `docs/` |
| Scripts de organização (final_organizer, surgical_cataloger) estão untracked |

---

## 7. Ações Recomendadas (Priorizadas)

| # | Ação | Repositório | Esforço |
|---|---|---|---|
| 1 | **Criar DOIs individuais no Zenodo** para cada boletim técnico | projetos | Médio |
| 2 | **Criar registro Zenodo para MQTF** | MQTF | Baixo |
| 3 | **Corrigir frontmatter** (remover H.5281, padronizar) | projetos | Baixo (batch) |
| 4 | **Commitar scripts untracked** (final_organizer, surgical_cataloger, etc.) | projetos | Baixo |
| 5 | **Resolver Arquivo Takwara** — catalogar 492 arquivos, mover para estrutura correta ou arquivar definitivamente | projetos | Alto |
| 6 | **Corrigir nomenclatura Takwara-Tech** (arquivos com #, espaços) | Takwara-Tech | Baixo |
| 7 | **Sincronizar docs/ ↔ dist_zenodo/ ou definir um como primário** | projetos | Baixo |
| 8 | **Consolidar dossiê BNDES** entre projetos e MQTF | Ambos | Médio |

---

*Este catálogo é um documento vivo. Atualize sempre que novos documentos forem adicionados ou DOIs forem criados.*
