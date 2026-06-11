import os, glob, PyPDF2
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions

# --- Configurações ---
SOURCE_DIR = "/Users/fabiotakwara/Documents/BAMBUBR"
DEST_DIR = "01_SOMBRA_AUDITORIA/04_PROJETO_WTF/03_PESQUISA_EM_ANDAMENTO/SONDA_DOCLING"

FILTRO_CIENCIA = [
    "bambu", "bamboo", "guadua", "timber", "bio-based", "biopolimero", "biopolymer", 
    "polyurethane", "poliuretano", "castor oil", "mamona", "imperveg", "amazonia", 
    "amazon", "regenerative", "bioeconomy", "geodesic", "geodesica", "dome", "test",
    "ensaio", "resistencia", "takwara", "unb", "report", "relatorio", "article", "thesis"
]

def avaliar_pdf(caminho):
    try:
        with open(caminho, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            texto = reader.pages[0].extract_text().lower()
            return any(termo in texto for termo in FILTRO_CIENCIA)
    except: return False

def disparar_sonda_curadoria():
    converter = DocumentConverter() # Usaremos o modo padrão, mais rápido
    pdfs = glob.glob(os.path.join(SOURCE_DIR, "**/*.pdf"), recursive=True)
    os.makedirs(DEST_DIR, exist_ok=True)
    
    # Criamos um arquivo mestre de inventário
    inventario_path = os.path.join(DEST_DIR, "00_INVENTARIO_CURADORIA_WTF.md")
    
    print(f"📡 Iniciando Mapeamento de Curadoria: {len(pdfs)} arquivos.")

    with open(inventario_path, "a", encoding="utf-8") as f_inv:
        f_inv.write(f"# 🗂️ Inventário de Curadoria - Tecnologia Takwara\n\n")

        for path in pdfs:
            if avaliar_pdf(path):
                nome = os.path.basename(path)
                print(f"📍 Localizado: {nome}")
                try:
                    # Extração rápida apenas para entender o tema
                    result = converter.convert(path)
                    resumo_curto = result.document.export_to_markdown()[:500] # Pega só o início
                    
                    # Escreve no índice mestre
                    f_inv.write(f"## 📄 {nome}\n")
                    f_inv.write(f"- **📍 Localização Original:** `{path}`\n")
                    f_inv.write(f"- **🔍 Prévia do Conteúdo:** {resumo_curto}...\n")
                    f_inv.write(f"- **⚠️ Status de Tabela:** Requer curadoria Gemini (Layout Complexo)\n")
                    f_inv.write(f"---\n\n")
                    
                    print(f"✅ Indexado: {nome}")
                except Exception as e:
                    f_inv.write(f"## 📄 {nome} (ERRO NA INDEXAÇÃO)\n")
                    f_inv.write(f"- **📍 Localização:** `{path}`\n")
                    f_inv.write(f"- **❌ Erro:** {str(e)[:100]}\n---\n\n")

if __name__ == "__main__":
    disparar_sonda_curadoria()