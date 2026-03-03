
NOTA TÉCNICA
Política de Acesso Digital e Compartilhamento da Documentação
Plataforma Amazônia Regenerativa – Versão 1.0 – 03 mar. 2026[^1][^2]

***

## 1. Objetivo e princípios

Esta nota define como a documentação da Plataforma Amazônia Regenerativaelimine do texto (PAR) será compartilhada com parceiros técnicos, institucionais e financiadores, conciliando três requisitos:

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

Plataforma Amazônia Regenerativa  
Série Técnica – Aplicabilidade Nacional  
Núcleo Takwara – Universidade de Brasília (UnB)  

Título: Política de Acesso Digital e Compartilhamento da Documentação  
Tipo de documento: Nota Técnica Interna  
Versão: 1.0  
Data: 03 de março de 2026  
Autor responsável: Takwara, Fabio Resck (Núcleo Takwara/UnB)  
Revisão institucional: Universidade de Brasília – Parceiros Técnicos (UFAC, Embrapa, Imperveg)  

***

MEMORANDO TÉCNICO DE ENCAMINHAMENTO
Plataforma Amazônia Regenerativa – Orçamento Consolidado e Pendências Críticas
Versão 1.0 – 03 mar. 2026[^1][^2]

***

## 1. Objeto do memorando

Este memorando sintetiza o estado atual do orçamento consolidado da Plataforma Amazônia Regenerativa (PAR) e explicita as principais pendências a serem tratadas em conjunto com a Universidade de Brasília (UnB) para viabilizar a consolidação do dossiê técnico‐financeiro a ser submetido ao BNDES/Fundo Amazônia e instrumentos correlatos.[^2][^1]

***

## 2. Síntese do orçamento consolidado (48 meses)

- Valor global estimado: ~R\$ 19 milhões em 48 meses, combinando CAPEX, OPEX, licenciamento, certificações e capital de giro.[^1]
- CAPEX: ~R\$ 4,25 milhões (biorrefinaria, UBPs, linha de compósitos, domos, adequações civis e instalações).[^2][^1]
- OPEX: ~R\$ 16,77 milhões (RH completo com encargos, logística, insumos, certificações, P\&D, monitoramento e comunicação).[^1]
- Estrutura em tranches:
    - Tranche 1 – Núcleo de menor risco: biorrefinaria, UBPs, piloto BSM/BER e SMGA inicial.
    - Tranche 2 – Escalonamento: compósitos bambu–PU, domos-estufa, cursos pagos e consolidação de saneamento.
    - Tranche 3 – Consolidação: saneamento como mercado âncora, créditos de carbono (VM0044 + padrão social) e replicação regional.[^2][^1]

O cenário-base permanece ancorado na unidade de biorrefinaria/bioenergia, operando com Guadua spp. e resíduos agroextrativistas, sem depender de saneamento, PET ou créditos de carbono para atingir o ponto de equilíbrio.[^1][^2]

***

## 3. Pontos positivos já consolidados

1. Encargos trabalhistas e RH

- Encargos CLT ajustados (≈65%) e incorporados integralmente ao orçamento de pessoal técnico e operacional, com custo total da equipe da ordem de R\$ 8,5 milhões/48 meses.[^1]
- Estrutura de RH alinhada ao desenho dos núcleos (máquinas, regenerativas/PU, arquitetura, bioeconomia/gênero/governança, saneamento, operação local).[^2][^1]

2. Logística e frota

- Revisão do OPEX de frota (combustível, manutenção, seguros, licenciamento) para ~R\$ 1,53 milhão, compatível com a realidade logística amazônica.[^1]
- Inclusão de frete CIF Acre, locação/compartilhamento de máquinas pesadas e custos de deslocamento aéreo/fluvial/rodoviário em linha com cenários de estresse de diesel.[^2][^1]

3. Licenciamento, normas e segurança

- Itens específicos para PMFS, CAR, licenciamento ambiental (LP/LI/LO), NR‑13, AVCB, SST (PGR, PCMSO, LTCAT, planos de emergência e incêndio).[^2]
- Conformidade declarada com ABNT NBR 16828 (bambu), NR‑13 (caldeiras/vasos) e RES. CONAMA 382/2006 (emissões).[^2]

4. Certificação de carbono

- Custos de certificação Verra VM0044 (biochar) dimensionados na faixa de R\$ 350–600 mil, incluindo elaboração de PDD, validação/verificação e MRV básico.[^3][^2]
- Créditos de carbono tratados como “upside”, não como condição de viabilidade do cenário-base.[^3][^2]

5. P\&D, documentação e SMGA

- Reserva explícita de P\&D (≈7,5% do OPEX) para ajustes tecnológicos (BSMBER, PU vegetal, maquinário Jesiel, SMGA).[^1][^2]
- Inclusão do Sistema de Monitoramento Geoespacial Automatizado (SMGA) como anexo e item orçamentário classificado em “documentação técnica, testes, laudos e certificações”.[^2]

***

## 4. Pendências críticas a serem tratadas com a UnB

### 4.1. Contrapartida financeira e econômica

Situação

- A contrapartida potencial (horas técnicas, documentos já produzidos com DOI, protótipos Jesiel/Takwara, comodato de área/galpão, apoio Imperveg, UFAC/Embrapa, viagens e Fase 0 Domo Voador) está descrita qualitativamente, mas ainda não consolidada como pacote quantitativo (R\$) fechado.[^4][^1]

Pendências

- Definir faixa de contrapartida alvo (10–20% do valor total) em alinhamento com o edital final do BNDES/Fundo Amazônia.[^1]
- Valorizar em R\$ os ativos de contrapartida:
    - Propriedade intelectual/documentos (Plataforma v5.1, Memorial Técnico, Cartilha e Manual de Fitorremediação, todos com DOI).[^4][^3][^1]
    - Infraestruturas e comodatos (galpão, terrenos, laboratórios parceiros).[^1]
    - Horas técnicas já realizadas (UnB, Núcleo Takwara, UFAC, Embrapa, Imperveg, Jesiel).[^2][^1]
- Identificar e engajar ao menos um cofinanciador público/estadual (FAPAC, SEBRAE‑AC, governo do Acre) para reforço da contrapartida.[^1]


### 4.2. Modelagem econômico-financeira (VPL, TIR, payback)

Situação

- A estrutura de modelo já está descrita (unidades de negócio, cenários base/otimista/estresse, análise de sensibilidade), com preços e volumes indicativos por produto/serviço.[^2][^1]
- Os indicadores quantitativos (VPL, TIR, payback, DSCR) ainda não foram calculados em planilha auditável ou script.[^1][^2]

Pendências

- A UnB (ou equipe designada) deve rodar o modelo financeiro completo, por unidade de negócio e consolidado, e alimentar o Memorial com:
    - VPL, TIR, payback e ponto de equilíbrio para:
        - i) Biorrefinaria/bioenergia;
        - ii) Bioconstrução/compósitos;
        - iii) Saneamento/bioinsumos.[^1]
    - Cenários de estresse específicos (atraso em saneamento, não escala do PET, choques de frete, não materialização de mercados de carvão ativado).[^2][^1]


### 4.3. Preços de mercado no Acre – calibração empírica

Situação

- Preços de referência (briquetes, biochar, colmo tratado, extrato pirolenhoso, contratos de saneamento, cursos) baseiam-se em literatura, benchmarks de outros estados e experiência acumulada, mas ainda carecem de calibração local sistemática.[^1]

Pendências

- Conduzir um pequeno estudo de mercado com 3–5 entrevistas por segmento no Acre:
    - Queimadores intensivos (padarias, cerâmicas, frigoríficos, agroindústrias).
    - Serrarias, movelarias, marcenarias (para bambu tratado).
    - Prefeituras e serviços de saúde (serviços de saneamento ecológico e filtros).
    - Potenciais compradores de cursos e imersões (órgãos públicos, ONGs, universidades locais).[^1]
- Ajustar os preços unitários e volumes projetados no modelo conforme resultados.[^1]


### 4.4. Padrão de certificação de carbono e rota de implementação

Situação

- O pacote conceitual indica VM0044 (VERRA – biochar) e recomenda Plan Vivo como padrão social prioritário para pequenos produtores, com possibilidade de Social Carbon como add‑on brasileiro.[^3]
- Não há ainda uma decisão formal sobre combinação de padrões, nem definição de papéis (quem faz PDD, quem é VVB preferencial).[^3]

Pendências

- Deliberação UnB + parceiros sobre a combinação de padrões:
    - Ex.: Plan Vivo (restauração + meios de vida) + VM0044 (biochar) + Social Carbon (co‑benefícios).[^3]
- Definir:
    - Responsável pela elaboração do(s) PDD(s);
    - VVBs prioritários;
    - Cronograma indicativo (início da linha de base, 1ª validação, 1ª verificação).


### 4.5. Formalização jurídica da contrapartida e parcerias

Situação

- Modelos de carta de intenção, estatuto de associação, arranjo de SPE e governança híbrida já estão redigidos em nível conceitual e de minuta.
- Ainda não há laudos de avaliação de ativos e cartas com valores numéricos explícitos para fins de contrapartida.[^1]

Pendências

- Elaborar, para cada parceiro-chave (prefeitura, universidade, Imperveg, UFAC/Embrapa, governo do Acre):
    - Minutas de carta de compromisso com indicação de valor econômico estimado (R\$) da contrapartida.
    - Laudos de avaliação de IP e de equipamentos/infraestrutura (para uso junto ao BNDES).


### 4.6. Linha do tempo jurídico–financeira integrada

Situação

- Todos os instrumentos regulatórios e jurídicos necessários estão listados (PMFS, CAR, LP/LI/LO, SPE, CLPI, PSA, ARTs/RRTs), mas ainda sem um Gantt unificado e vinculado às tranches.

Pendências

- Construir uma linha do tempo integrada (jurídica + financeira), evidenciando:
    - Marcos críticos de submissão ao BNDES/Fundo Amazônia.
    - Marcos “gate” de desembolso de cada tranche (ex.: SPE constituída, PMFS protocolado, CLPI concluído, LP concedida).


### 4.7. Fase 0 (Domo Voador) – contabilização como contrapartida

Situação

- Fase 0 (Domo Voador) está desenhada como dispositivo de articulação territorial pré-financiamento, com financiamento híbrido (recursos do projeto + vagas pagas + contrapartida própria).
- Ainda falta amarração contábil clara para registrar essas despesas como contrapartida no pacote BNDES/Fundo Amazônia.

Pendências

- Detalhar:
    - Quais custos da Fase 0 serão apresentados como contrapartida (viagens, estrutura, horas técnicas, bolsas).
    - Quais comprovantes (notas, diárias, contratos) serão arquivados e como serão laudadamente valorados.


### 4.8. Reconciliação numérica final

Situação

- Pequenas divergências de arredondamento entre subtotais de tabelas (por fase e por categoria) podem permanecer após a consolidação atual.[^1]

Pendências

- Rodada final de auditoria interna (linha a linha) do orçamento consolidado, ajustando:
    - Somatórios por categoria (RH, CAPEX, OPEX, certificações, P\&D, reservas).
    - Somatórios por fase/tranche.[^1]

***

## 5. Proposta de próximos passos (agenda conjunta UnB – Plataforma)

1. Oficina de alinhamento UnB–Plataforma (on-line, 3–4 horas):
    - Revisar o pacote de contrapartida.
    - Tomar decisão preliminar sobre padrões de certificação de carbono.
    - Definir responsáveis por modelagem financeira e estudo de mercado local.
2. Entregas técnicas prioritárias (30–45 dias):
    - Modelo financeiro rodado com VPL, TIR, payback e cenários.
    - Relatório sucinto de mercado Acre (preços/volumes).
    - Rascunho da linha do tempo jurídico–financeira.
    - Minutas de cartas de compromisso de contrapartida com valores.
3. Consolidação do dossiê para submissão (60–90 dias):
    - Orçamento “congelado” com reconciliação numérica.
    - Anexos técnicos (Memorial, SMGA, Fitorremediação, Cartilha) vinculados como base metodológica.

***


Plataforma Amazônia Regenerativa – Tecnologia do Bambu para a Soberania Amazônica  
Documento interno de uso restrito – Não circular fora da rede de parceiros sem autorização prévia por escrito da coordenação da Plataforma.  

Licença padrão para documentos internos: CC BY-NC-ND 4.0 (salvo indicação em contrário no corpo do documento ou anexo específico).  

Contato institucional:  
Núcleo Takwara – Universidade de Brasília  
E-mail: takwaratec@gmail.com 
Website técnico (repositório principal / GitHub Pages privado, quando aplicável).