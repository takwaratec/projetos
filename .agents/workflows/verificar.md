---
description: Protocolo de Verificação Independente de Fontes (PVI)
---

Este workflow deve ser invocado sempre que um documento de alto impacto for criado ou revisado, garantindo a legitimidade documental.

1. **Origens de Dados**:
   - **Científica**: Teses da UnB, UFPA, USP e artigos indexados.
   - **Legal/Gov**: Diário Oficial (DOU), Portais de Transparência, Tribunais (TCU/STF).
   - **Histórica**: Acervo Takwara (Arquivo Fabio Takwara) e Legado Chierice.
   - **Coleção**: Master DOI Zenodo (`10.5281/zenodo.18827106`).

2. **Passos de Validação**:
   - [ ] **DOI Check**: Verifique se o documento ou a referência está no Zenodo.
   - [ ] **Neutralidade**: Busque fontas de mídia independente vs. mídia estatal para o mesmo fato.
   - [ ] **Status de Inércia**: Se o documento trata de Advocacy, execute o Protocolo V.I. do workflow `/denúncia`.
   - [ ] **Rigor de Citação**: Use o formato ABNT/APA conforme definido no `docs/05_ADVOCACY_COP30/OPS_artigos-criticos.md`.

3. **Automação**:
   - Ao detectar um link externo, o assistente deve buscar por metadados de validade (Data de acesso, autoridade da fonte).

// turbo
**Comando Sugerido**: "/verificar [diretório]" - Aplica a Política de Verificação Independente ao diretório especificado, cruzando com o Acervo e fontes externas.
