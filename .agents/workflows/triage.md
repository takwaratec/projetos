---
description: Avalia, higieniza e classifica materiais brutos em Markdown estruturado
---

# Workflow: `/triage`

Este fluxo de trabalho automatiza a entrada de dados brutos (PDFs, links de notícias, rascunhos) no acervo, aplicando as regras de redação, tom autoral e higiene cibernética antes de mesclar o conhecimento à Plataforma.

## Uso
**Para o usuário:** No chat, envie `/triage [link ou nome do arquivo na /tmp]`. Informe rapidamente o propósito (ex: "matéria sobre o PL 123", "artigo científico sobre PU").

## Passo a Passo para o Agente:
1. **Leitura Cautelosa:** Extraia o texto do(s) arquivo(s) ou links indicados. Use o subagente web, se o link estiver bloqueado por Cloudflare ou Paywall simples.
2. **Análise de Persona e Tom:** 
    - Decida qual será a categoria final baseando-se no tema.
    - Se for um Dossiê/Opinião política: Adeque ao "Fabio Takwara Militante" (Advocacy 5.1 Redação - Seção 4).
    - Se for insumo científico/memorial: Adeque ao "Fabio Takwara Cientista".
3. **Draft Seguro (Higiene de Ativos):**
    - Escreva o conteúdo redigido Markdown limpo (`.md`) no diretório temporário (`/tmp/triage_resultado.md`). Não coloque na pasta definitiva ainda!
    - Remova todas as marcas características de IAs (`Gerado por...`, `Em conclusão...`, `Aqui está...`).
    - Exclua ligações quebradas e âncoras tipo `\[^n]`.
4. **Alerta de Revisão:** 
    - Utilize o comando de notificar usuário apresentando um resumo analítico de 2 a 3 pontos abordados no documento triado.
    - Peça aprovação final para mover o arquivo da `tmp/` para a respectiva pasta (ex: `07_BLOG_MEDIUM`, `05_ADVOCACY_COP30`, etc).
