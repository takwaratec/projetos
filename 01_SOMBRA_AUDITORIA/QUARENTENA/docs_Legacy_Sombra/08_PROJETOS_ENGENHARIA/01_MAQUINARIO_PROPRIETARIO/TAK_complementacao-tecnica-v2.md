# Relatório de Complementação Técnica: Portfólio Takwara

Este relatório detalha as reavaliações e acréscimos necessários para cada equipamento, integrando o feedback do usuário e dados técnicos extraídos da literatura científica que embasa o TRL (Technology Readiness Level) da plataforma.

---

## 1. Categorização e Simulação de Cenários

### 1.1 Modelo Urbano (Rio Branco-AC) vs. Comunitário
*   **Contexto Urbano:** Equipamentos robustos, alimentação monofásica estável, foco em alta produtividade para fornecimento regional.
*   **Contexto Comunitário:** Maquinário intercambiável, adaptado para limitações de carga elétrica. Foco em robustez e facilidade de manutenção (NR-12 simplificada).

---

## 2. Complementações por Equipamento

### 2.1 Tamboreador de Varas (Abrasão Térmica)
*   **Complementação Necessária:** 
    *   Simular dois tamanhos: 6m (Urbano) e 3m (Comunitário/Modular).
    *   Definir elemento abrasivo baseado na espécie de bambu (Guadua exige maior abrasão que Phyllostachys).
    *   **Potência Sugerida:** Motor monofásico de 1.5 a 3 CV com redutor de velocidade.

### 2.2 Misturador de Biocompósitos (Betoneira com Jato de PU)
*   **Complementação Necessária (Concepção):**
    *   O jato de PU deve ser do tipo **nevoeiro (mist)** para garantir cobertura sem escorrimento, dado que a quantidade de resina é mínima (20-25% em massa).
    *   **Mecanismo:** Aspersão pneumática com bico de largo espectro.
    *   **Análise de Falha:** Risco de polimerização precoce nas pás. Recomendado revestimento de polietileno de alta densidade (PEAD) ou Teflon nas zonas de contato.

### 2.3 Prensas e Conformação (Ajuste de Rota)
*   **Prensa de Tijolos:** 
    *   Adotar o modelo de **Pistão (similar à briquetadeira)**. 
    *   **Diferencial:** Não necessita de molde cassete para cura, apenas a conformação imediata.
    *   **Pressão:** Mínimo de 10 MPa (100 bar) para garantir a densidade necessária com aglutinação de PU/PET.
*   **Contenção para Painéis de PU Expansivo (PRIORIDADE):**
    *   Substitui a prensa OSB de alta pressão.
    *   **Estrutura:** Moldes tipo "sanduíche" com travamento mecânico manual.
    *   **Função:** Apenas conter a pressão de expansão do **Mamonex RD70**. Estrutura muito mais leve e barata para comunidades.

### 2.4 Solda Vegetal (União Estrutural)
*   **Complementação Necessária:**
    *   Definir protocolos de lixamento pré-injeção (aumento da área de contato superficial das fibras).
    *   **Parâmetro TRL:** Umidade do bambu deve ser obrigatoriamente **<12%** (conforme Cazella/Carvalho) para garantir a adesão química do isocianato às hidroxilas da celulose.

---

## 3. Parâmetros Extraídos da Literatura (Base TRL)

*   **Umidade Crítica:** 12% é o divisor de águas entre sucesso e falha na colagem.
*   **Compactação:** Para biocompósitos particulados (Lopes/Carvalho), a resistência mecânica é estritamente proporcional à densidade final (almejar >800 kg/m³ para painéis estruturais).
*   **Segurança Química:** Confirmar a ausência de isocianato livre após a cura total (24h-48h), conforme laudos Imperveg citados nas teses.

---

## 4. Próximos Passos (Standby OSB)

1.  **Suspensão temporária** dos estudos de Prensas OSB complexas (foco em CAPEX reduzido).
2.  **Detalhamento do Gabarito de Contenção** para Painéis Sanduíche (3x3m).
3.  **Simulação de cenários de motorização** customizáveis por localidade.

---
> **Status:** Próxima fase — Redação dos Memoriais com foco em Prensas de Baixa Pressão e Misturadores Monofásicos.
