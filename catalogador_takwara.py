import os, glob
try:
    from Cocoa import NSURL
    from Quartz import PDFDocument
except ImportError:
    print('❌ Erro: Execute primeiro: pip3 install pyobjc-framework-Cocoa pyobjc-framework-Quartz')
    exit()

origens = [

    '01_SOMBRA_AUDITORIA/04_PROJETO_WTF/01_GOVERNANCA/01_COLABORADORES/Bibliografia_Equipe/relacionadas'
    
]


destino = '01_SOMBRA_AUDITORIA/04_PROJETO_WTF/03_PESQUISA_EM_ANDAMENTO/TRANSCRIPT/AMAZONIA_GESTORAS'
os.makedirs(destino, exist_ok=True)


print(f'🚀 Iniciando Coleta Transversal...')

for raiz in origens:
    arquivos = glob.glob(os.path.join(raiz, '**/*.pdf'), recursive=True)
    for p in arquivos:
        nome_base = os.path.basename(p).replace(' ', '_')
        txt_saida = os.path.join(destino, f'RAW_{nome_base}.txt')
        
        if os.path.exists(txt_saida): continue

        url = NSURL.fileURLWithPath_(os.path.abspath(p))
        doc = PDFDocument.alloc().initWithURL_(url)
        texto = doc.string() if doc else ''
        
        if texto and len(texto.strip()) > 50:
            with open(txt_saida, 'w', encoding='utf-8') as f:
                f.write(texto)
            print(f'✅ Transcrito: {nome_base}')
        else:
            print(f'⚠️  Imagem/Vazio: {nome_base}')

print('\n✨ Processo finalizado. Verifique a pasta AMAZONIA_GESTORAS')