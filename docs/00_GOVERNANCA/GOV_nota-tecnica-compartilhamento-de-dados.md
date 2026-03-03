# NOTA TÉCNICA
## Política de Acesso Digital e Compartilhamento da Documentação
### Plataforma Amazônia Regenerativa – Versão 1.0 – 03 mar. 2026

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

- **Conteúdo**: Versões públicas já lançadas com DOI (ex.: Cartilha, Manual de Fitorremediação, Plataforma v5.1 quando publicada), notas de divulgação, resumos executivos sem informação sensível.
- **Canais**:
    - Zenodo (coleção DOI);
    - Site institucional;
    - E-mails oficiais de divulgação.
- **Perfil de acesso**: Qualquer pessoa, sem autenticação.

**Uso**: Consolidação de reputação, citações acadêmicas, referência em editais e políticas públicas.

### 2.2. Camada 1 – Restrita: GitHub + GitHub Pages privado

- **Conteúdo**:
    - Versão “viva” da documentação técnica (MkDocs), incluindo rascunhos de anexos, memorial técnico, SMGA, notas internas;
    - Documentação de engenharia, governança, modelos de dados, manuais operacionais ainda em teste.
- **Infraestrutura**:
    - Organização GitHub dedicada (ex.: `amazonia-regenerativa`);
    - Repositório privado `docs-plataforma-amazonia-regenerativa`;
    - GitHub Pages configurado com **visibilidade privada** (“Only people with access to this repository”).
- **Segurança**:
    - O site estático só é visível a usuários autenticados no GitHub com permissão de leitura no repositório;
    - Todo o histórico é versionado e auditável via Git.

**Perfil de acesso**:
- Núcleo técnico ampliado (UnB, UFAC, Embrapa, Imperveg, Jesiel, parceiros estratégicos);
- 2–5 pessoas por instituição, com conta GitHub e acesso concedido (Read) ao repositório.

**Justificativa**:
- Viabiliza revisão técnica colaborativa com controle de versão;
- Evita exposição pública de conteúdos ainda em negociação com BNDES/Fundo Amazônia;
- Utiliza infraestrutura robusta, com controle de acesso nativo.


### 2.3. Camada 2 – Restrita simplificada: PDFs e pacotes estáveis

- **Conteúdo**:
    - “Fotografias” estáveis dos documentos principais (PDF ou ZIP do site estático) por marco de projeto:
        - Plataforma vX.Y;
        - Memorial Técnico vX.Y;
        - Cartilha vX.Y;
        - Manual de Fitorremediação vX.Y.
- **Canais**:
    - Envio direto por e‑mail (PDF/ZIP);
    - Compartilhamento via Drive/Nextcloud institucional com permissões de leitura;
    - Anexos em propostas formais.
- **Perfil de acesso**:
    - Gestores públicos, conselhos, jurídicos, comitês que não usam GitHub;
    - Parceiros que precisam de leitura, mas não de interação com o repositório.

**Justificativa**:
- Reduz barreira de entrada (não exige cadastro GitHub);
- Garante que decisões institucionais se baseiem em versões explícitas e datadas;
- Permite marca d’água (“Uso restrito – não divulgar”) quando necessário.


### 2.4. Camada 3 – Acesso excepcional (senha simples / ambiente temporário)

Quando houver necessidade de compartilhar rapidamente material ainda mais sensível com público heterogêneo (ex.: banca de avaliação externa, com prazo curto e sem tempo para criar contas GitHub):

- **Opção provisória**:
    - Construir uma cópia do site estático com proteção por senha (ex.: ferramenta tipo staticrypt) e hospedar em serviço de páginas estáticas;
    - Compartilhar link + senha em canal separado (ex.: e‑mail institucional).
- **Prazo**:
    - Acesso típico até a decisão do comitê (15–60 dias), seguido de desativação ou renovação de senha.

**Justificativa**:
- Mecanismo de contingência quando a exigência de cadastro GitHub se torna inviável;
- Não substitui as camadas 1 e 2, apenas as complementa em situações específicas.

---

## 3. Modelos de compartilhamento com tipos de parceiros

### 3.1. Parceiro tecnológico (ex.: Imperveg, Jesiel, fabricantes, laboratório)

- **Acesso principal**: Camada 1 (GitHub Pages privado) + acesso ao código/documentos relevantes no repositório.
- **Passos operacionais**:
    1. Solicitar lista de pessoas que atuarão tecnicamente (nome + e‑mail).
    2. Orientar criação de conta GitHub, se ainda não tiverem.
    3. Conceder acesso Read ao repositório `docs-plataforma-amazonia-regenerativa` (e Write apenas onde convier).
    4. Enviar o link do site privado como canal padrão de leitura.
- **Complemento**: PDFs das versões “oficiais” em anexos de contratos, NDAs, termos de cooperação.


### 3.2. Parceiro acadêmico/institucional (UnB, UFAC, Embrapa, institutos)

- **Acesso**:
    - Núcleo técnico: Camada 1;
    - Coordenação/direção: Camada 2 (PDFs).
- **Prática recomendada**:
    - Vincular os links privados a um termo simples de confidencialidade e uso restrito, quando o documento ainda não tiver DOI público.


### 3.3. Financiadores e avaliadores (BNDES, Fundo Amazônia, FAPs, bancos)

- **Acesso**:
    - Dossiês formais submetidos em PDF, usando os documentos “congelados” de cada fase (Camada 2);
    - Opcionalmente, fornecer acesso temporário Camada 3 para visualização da documentação viva, quando isso agregar transparência.
- **Justificativa**:
    - Evita dependência da infraestrutura de TI do avaliador;
    - Garante rastreabilidade de qual versão foi submetida.

---

## 4. Justificativas para uso do GitHub + Pages privado

1. **Rastreabilidade e versionamento**
    - Git registra cada alteração com autor, data e dif;
    - Facilita reconstruir histórico para auditorias, relatórios a financiadores e artigos científicos.
2. **Controle de acesso centralizado**
    - GitHub Pages privado respeita as permissões do repositório: quem não tem acesso GitHub não vê o site;
    - Elimina necessidade de reimplementar autenticação própria.
3. **Integração com automação (SMGA, MRV, builds)**
    - Repositórios já previstos para SMGA, scripts de MRV e documentação podem ser publicados automaticamente como site, reduzindo erro manual.
4. **Gradiente de abertura**
    - Documentos “estáveis” sob DOI podem migrar gradualmente da Camada 1 para a Camada 0, quando a estratégia institucional assim determinar.

---

## 5. Procedimento resumido para implantação

1. Criar ou confirmar a **Organização GitHub** da Plataforma.
2. Criar repositório privado `docs-plataforma-amazonia-regenerativa` com MkDocs.
3. Configurar GitHub Actions para buildar o site em `gh-pages`.
4. Em **Settings → Pages**, definir:
    - Source: branch `gh-pages`;
    - Visibility: **Private**.
5. Criar o time “Parceiros Técnicos” na organização e conceder **Read** a esse time.
6. Para cada instituição parceira, convidar 1–5 pessoas técnicas para o time.
7. Definir rotina de exportação trimestral/semestral de PDFs (Camada 2) com numeração de versão e data.

---

## 6. Governança e revisões desta política

- Esta nota será revisada sempre que:
    - Houver mudança relevante nas políticas de acesso do GitHub;
    - A Plataforma iniciar uso de novo hospedeiro ou esquema de autenticação (ex.: Cloudflare Access);
    - Novos parceiros exigirem formatos específicos (ex.: repositórios institucionais).
- Versões atualizadas da política serão mantidas no repositório de governança da Plataforma e, quando apropriado, anexadas a acordos de cooperação e NDAs.

---

Esta Política de Acesso Digital pode ser anexada como “ANEXO – Política de Compartilhamento e Confidencialidade Digital da Documentação” em termos de parceria com Imperveg e demais colaboradores estratégicos.

<div align="center">⁂</div>
