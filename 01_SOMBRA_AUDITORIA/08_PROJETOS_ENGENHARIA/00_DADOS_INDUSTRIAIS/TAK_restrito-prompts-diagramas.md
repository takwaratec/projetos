# Arquivo Restrito: Inteligência Industrial e Prompts Takwara

Este documento contém informações de cunho estratégico e técnico-criativo (Prompts de IA e Mapas Mentais) que foram removidos dos memoriais públicos para garantir a privacidade da tecnologia industrial.

---

## T02 - Biorrefinaria

### Mapa Mental de Fluxo (Mermaid)
```mermaid
graph TD
    %% Estilos de alto contraste
    classDef hardware fill:#333,stroke:#fff,stroke-width:2px,color:#fff;
    classDef sujo fill:#b91c1c,stroke:#000,stroke-width:4px,color:#fff,font-weight:bold;
    classDef vapor fill:#1d4ed8,stroke:#000,stroke-width:4px,color:#fff,font-weight:bold;
    classDef limpo fill:#15803d,stroke:#000,stroke-width:4px,color:#fff,font-weight:bold;

    subgraph CARREGAMENTO [Alimentação]
        A[<b>Bambu Estrutural 6m</b>]:::hardware --> C_A[<b>Câmara A (Tratamento)</b>]:::hardware
        B[<b>Biomassa Residual</b>]:::hardware --> R_P[<b>Reator de Pirólise</b>]:::sujo
    end

    subgraph IGNICAO [Coração Térmico]
        G_IGN((<b>Ignitor a Gás/Manual</b>)):::sujo --> B_RS[<b>Queimador Rocket Stove</b>]:::sujo
        B_RS -->|Chama Turbulenta| C[<b>Riser (Aorta Térmica)</b>]:::sujo
        R_P -->|Gases Não-Condensáveis| B_RS
    end

    subgraph VAPOR [Circuito de Tratamento]
        E[(<b>Mix H2O + EP</b>)]:::vapor --> F{<b>Serpentina externa no Riser</b>}:::vapor
        C -.->|Transferência de Calor| F
        F -->|<b>Vapor Flash</b>| G([<b>Banda de Vapor</b>]):::vapor
        G --> C_A
    end

    subgraph PIROLISE [Universo Sujo]
        R_P -->|Fumaça Pesada| H[<b>Chaminé Suja</b>]:::sujo
        H --> I[<b>Condensador Inclinado</b>]:::sujo
        I -->|Destilação| J[(<b>Extrato Pirolenhoso</b>)]:::sujo
        I -->|Retorno de Gases| K{<b>Corta-Chamas ISO 16852</b>}:::sujo
        K -->|Realimentação| B_RS
    end

    subgraph SECAGEM [Universo Limpo]
        L((<b>Ar Atmosférico</b>)):::limpo --> M[<b>Jaqueta de Vácuo</b>]:::limpo
        B_RS -.->|Calor Residual| M
        M -->|Exaustão Induzida| N([<b>Câmara B (Secagem)</b>]):::limpo
    end
```

### Prompt Mestre (T02)
> **Prompt em Inglês (Otimizado para LLMs e Geradores de Imagem):**
> *"Industrial isometric 3D render, highly detailed, photorealistic. A community biomass biorefinery plant in an Amazonian setting. On the right, two massive 6-meter-long horizontal cylindrical steel tanks stacked parallel, resembling brushed metal autoclaves with large round ship-like hatch doors and thick flanges. The top tank has a red metallic pipe (steam band) connected to its dome. On the lower left side, a stark, shorter, and much thicker vertical reactor (pyrolysis retort) rests on a masonry base with a visible dark horizontal funnel (Rocket Stove) glowing fiercely with orange fire inside. A shiny slanted steel pipe (condenser) cascades down from the thick reactor towards the ground, dripping dark green oil into a siphon. The overall aesthetic is clean brushed steel, precise industrial instrumentation, steampunk biological machinery, soft natural daylight piercing through a heavy canopy, Unreal Engine 5 render, sharp focus, 8k resolution."*

---

## T03 - Frangueira

### Prompt IA (T03 Industrial)
> **Prompt (EN):** Technical 3D render of an "Industrial Bamboo Rotisserie". A heavy-duty steel rack holding 12 bamboo culms in parallel, rotating simultaneously. Driven by a powerful gear reducer and individual pulleys. Integrated forced air heating vents at the base. High-gloss green resin finish on the bamboo. Engineering blueprint aesthetic mixed with hyper-realistic 3D rendering. Ultra-sharp focus on the gear and chain assembly.

---

## T04 - Misturador

### Prompt IA (T04)
> **Prompt (EN):** Technical 3D render of a "Waterproof Bio-Composite Mixer". A horizontal stainless steel drum rotating on a heavy-duty chassis. Internal view shows a pneumatic spray lance emitting a fine mist of green resin over shredded bamboo fibers. Visible external adjustable gland seals on the main shaft. Amazonian solar-powered workshop setting, hyper-realistic, engineering precision.

---

## T05 - Prensa Cassetes

### Prompt IA (T05)
> **Prompt (EN):** Technical 3D render of a "Modular Cassette Press" (T05). A rugged steel frame with a powerful vertical hydraulic piston. Interior view shows a "cassette" mold being swapped out. Bamboo composite bricks stacked nearby. Focus on the hydraulic gauges and the exchangeable mold mechanism. Amazonian bio-factory setting, 8k, professional engineering visual.

---

## T06 - Gabarito Universal

### Prompt IA (T06)
> **Prompt (EN):** Technical studio photo of a "Takwara Universal Jig Skeleton". A central vertical steel frame with multiple articulated arms holding bamboo poles on both front and back sides. Two different bamboo structures (a bike frame and a triangular truss) are being assembled simultaneously on the same machine. Clear 360-degree access to all joints. Industrial bio-factory aesthetic, bright lighting, high-tech tools. 8k resolution.

---

## T07 - Prensa Sanduíche

### Prompt IA (T07)
> **Prompt (EN):** Technical 3D render of a "Bamboo OSB Sandwich Press". A large horizontal flat-bed steel table. A bamboo composite board is being pressed. Massive industrial weights are placed on top to contain resin expansion. The scene is set in a spacious bio-factory. 8k, realistic metal and bamboo fiber textures, sharp engineering focus.

---

## Tamboreador

### Prompt IA
> **Prompt (EN):** Photorealistic ultra-detailed 3D render of a "Takwara Bamboo Thermal Tumbler". A massive 6-meter perforated carbon steel drum rotating on heavy-duty rollers. Visible belt drive system with red-painted cast iron pulleys. A large industrial dust cyclone connected via metallic ducts. Soft morning sunlight filtering through an Amazonian workshop, illuminating a fine cloud of golden bamboo dust being sucked into the system. Textures: oxidized welds, brushed steel, oily transmission belts. Analogue pressure gauges and a manual switchboard on the side. 8k resolution, cinematic lighting, engineering masterpiece aesthetic.
