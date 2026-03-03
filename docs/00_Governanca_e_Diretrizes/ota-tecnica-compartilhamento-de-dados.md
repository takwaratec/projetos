<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Sim, por favor, crie essa nota técnica de compartilhamento com as justificativas cabíveis e os modelos de compartilhamento associados.

NOTA TÉCNICA
Política de Acesso Digital e Compartilhamento da Documentação
Plataforma Amazônia Regenerativa – Versão 1.0 – 03 mar. 2026[^1][^2]

***

## 1. Objetivo e princípios

Esta nota define como a documentação da Plataforma Amazônia Regenerativa (PAR) será compartilhada com parceiros técnicos, institucionais e financiadores, conciliando três requisitos:

- proteção de conteúdo estratégico (projetos em elaboração, arranjos tecnológicos, modelos de negócio);
- facilidade de acesso para parceiros que não são usuários avançados de TI;
- aderência à lógica de transparência progressiva do projeto (documentos “vivos” vs. versões estáveis).[^2]

A estratégia adota **camadas de acesso** e **múltiplos formatos de entrega**, em vez de um único canal, para atender desde colaboradores de engenharia até gestores públicos de alto nível.[^2]

***

## 2. Camadas de acesso digital

### 2.1. Camada 0 – Pública (quando aplicável)

- Conteúdo: versões públicas já lançadas com DOI (ex.: Cartilha, Manual de Fitorremediação, Plataforma v5.1 quando publicada), notas de divulgação, resumos executivos sem informação sensível.[^3][^2]
- Canais:
    - Zenodo (coleção DOI);
    - site institucional;
    - e-mails oficiais de divulgação.[^3][^2]
- Perfil de acesso: qualquer pessoa, sem autenticação.

Uso: consolidação de reputação, citações acadêmicas, referência em editais e políticas públicas.

### 2.2. Camada 1 – Restrita: GitHub + GitHub Pages privado

- Conteúdo:
    - versão “viva” da documentação técnica (MkDocs), incluindo rascunhos de anexos, memorial técnico, SMGA, notas internas;
    - documentação de engenharia, governança, modelos de dados, manuais operacionais ainda em teste.[^4][^2]
- Infraestrutura:
    - Organização GitHub dedicada (ex.: `amazonia-regenerativa`);
    - repositório privado `docs-plataforma-amazonia-regenerativa`;
    - GitHub Pages configurado com **visibilidade privada** (“Only people with access to this repository”).[^5][^1]
- Segurança:
    - o site estático só é visível a usuários autenticados no GitHub com permissão de leitura no repositório;
    - todo o histórico é versionado e auditável via Git.[^5]

Perfil de acesso:

- Núcleo técnico ampliado (UnB, UFAC, Embrapa, Imperveg, Jesiel, parceiros estratégicos);
- 2–5 pessoas por instituição, com conta GitHub e acesso concedido (Read) ao repositório.

Justificativa:

- viabiliza revisão técnica colaborativa com controle de versão;
- evita exposição pública de conteúdos ainda em negociação com BNDES/Fundo Amazônia;
- utiliza infraestrutura robusta, com controle de acesso nativo.[^1][^5]


### 2.3. Camada 2 – Restrita simplificada: PDFs e pacotes estáveis

- Conteúdo:
    - “fotografias” estáveis dos documentos principais (PDF ou ZIP do site estático) por marco de projeto:
        - Plataforma vX.Y;
        - Memorial Técnico vX.Y;
        - Cartilha vX.Y;
        - Manual de Fitorremediação vX.Y.[^4][^2][^3]
- Canais:
    - envio direto por e‑mail (PDF/ZIP);
    - compartilhamento via Drive/Nextcloud institucional com permissões de leitura;
    - anexos em propostas formais.
- Perfil de acesso:
    - gestores públicos, conselhos, jurídicos, comitês que não usam GitHub;
    - parceiros que precisam de leitura, mas não de interação com o repositório.

Justificativa:

- reduz barreira de entrada (não exige cadastro GitHub);
- garante que decisões institucionais se baseiem em versões explícitas e datadas;
- permite marca d’água (“Uso restrito – não divulgar”) quando necessário.


### 2.4. Camada 3 – Acesso excepcional (senha simples / ambiente temporário)

Quando houver necessidade de compartilhar rapidamente material ainda mais sensível com público heterogêneo (ex.: banca de avaliação externa, com prazo curto e sem tempo para criar contas GitHub):

- Opção provisória:
    - construir uma cópia do site estático com proteção por senha (ex.: ferramenta tipo staticrypt) e hospedar em serviço de páginas estáticas;[^6]
    - compartilhar link + senha em canal separado (ex.: e‑mail institucional).
- Prazo:
    - acesso típico até a decisão do comitê (15–60 dias), seguido de desativação ou renovação de senha.

Justificativa:

- mecanismo de contingência quando a exigência de cadastro GitHub se torna inviável;
- não substitui as camadas 1 e 2, apenas as complementa em situações específicas.

***

## 3. Modelos de compartilhamento com tipos de parceiros

### 3.1. Parceiro tecnológico (ex.: Imperveg, Jesiel, fabricantes, laboratório)

- Acesso principal: **Camada 1 (GitHub Pages privado)** + acesso ao código/documentos relevantes no repositório.[^1][^5]
- Passos operacionais:

1. Solicitar lista de pessoas que atuarão tecnicamente (nome + e‑mail).
2. Orientar criação de conta GitHub, se ainda não tiverem.
3. Conceder acesso Read ao repositório `docs-plataforma-amazonia-regenerativa` (e Write apenas onde convier).
4. Enviar o link do site privado como canal padrão de leitura.
- Complemento: PDFs das versões “oficiais” em anexos de contratos, NDAs, termos de cooperação.[^2][^4]


### 3.2. Parceiro acadêmico/institucional (UnB, UFAC, Embrapa, institutos)

- Acesso:
    - Núcleo técnico: Camada 1;
    - Coordenação/direção: Camada 2 (PDFs).
- Prática recomendada:
    - vincular os links privados a um termo simples de confidencialidade e uso restrito, quando o documento ainda não tiver DOI público.[^2]


### 3.3. Financiadores e avaliadores (BNDES, Fundo Amazônia, FAPs, bancos)

- Acesso:
    - Dossiês formais submetidos em PDF, usando os documentos “congelados” de cada fase (Camada 2);
    - opcionalmente, fornecer acesso temporário Camada 3 para visualização da documentação viva, quando isso agregar transparência.[^7][^4]
- Justificativa:
    - evita dependência da infraestrutura de TI do avaliador;
    - garante rastreabilidade de qual versão foi submetida.

***

## 4. Justificativas para uso do GitHub + Pages privado

1. **Rastreabilidade e versionamento**
    - Git registra cada alteração com autor, data e dif;
    - facilita reconstruir histórico para auditorias, relatórios a financiadores e artigos científicos.[^4]
2. **Controle de acesso centralizado**
    - GitHub Pages privado respeita as permissões do repositório: quem não tem acesso GitHub não vê o site;
    - elimina necessidade de reimplementar autenticação própria.[^5][^1]
3. **Integração com automação (SMGA, MRV, builds)**
    - Repositórios já previstos para SMGA, scripts de MRV e documentação podem ser publicados automaticamente como site, reduzindo erro manual.[^4]
4. **Gradiente de abertura**
    - Documentos “stáveis” sob DOI podem migrar gradualmente da Camada 1 para a Camada 0, quando a estratégia institucional assim determinar.[^3][^2]

***

## 5. Procedimento resumido para implantação

1. Criar ou confirmar a **Organização GitHub** da Plataforma.[^8]
2. Criar repositório privado `docs-plataforma-amazonia-regenerativa` com MkDocs.
3. Configurar GitHub Actions para buildar o site em `gh-pages`.
4. Em **Settings → Pages**, definir:
    - Source: branch `gh-pages`;
    - Visibility: **Private**.[^1][^5]
5. Criar o time “Parceiros Técnicos” na organização e conceder **Read** a esse time.
6. Para cada instituição parceira, convidar 1–5 pessoas técnicas para o time.
7. Definir rotina de exportação trimestral/semestral de PDFs (Camada 2) com numeração de versão e data.[^2]

***

## 6. Governança e revisões desta política

- Esta nota será revisada sempre que:
    - houver mudança relevante nas políticas de acesso do GitHub;[^8]
    - a Plataforma iniciar uso de novo hospedeiro ou esquema de autenticação (ex.: Cloudflare Access);[^9]
    - novos parceiros exigirem formatos específicos (ex.: repositórios institucionais).
- Versões atualizadas da política serão mantidas no repositório de governança da Plataforma e, quando apropriado, anexadas a acordos de cooperação e NDAs.[^2]

---

Esta Política de Acesso Digital pode ser anexada como “ANEXO – Política de Compartilhamento e Confidencialidade Digital da Documentação” em termos de parceria com Imperveg e demais colaboradores estratégicos.

<div align="center">⁂</div>

[^1]: https://docs.github.com/pt/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site

[^2]: paste.txt

[^3]: manual-fitorremediacao-credito-carbono.md

[^4]: memorial-tecnico-biorrefinaria-de-bambu-5.1.md

[^5]: https://github.blog/changelog/2021-01-21-access-control-for-github-pages/

[^6]: https://github.com/squidfunk/mkdocs-material/discussions/5875

[^7]: Plataforma-Amazonia-Regenerativa-v5.1.md

[^8]: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits

[^9]: https://www.featurebase.app/blog/readthedocs-alternatives

