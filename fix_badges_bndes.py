import os
import re

folders = [
    'docs/09_DOSSIE_BNDES',
    '01_SOMBRA_AUDITORIA/09_DOSSIE_BNDES'
]

def get_badges_and_header(filename, lang):
    basename = os.path.basename(filename)
    base = basename.replace('_en.md', '.md').replace('_es.md', '.md')
    name_no_ext = base.replace('.md', '')
    
    dirname = os.path.dirname(filename)
    has_en = os.path.exists(os.path.join(dirname, name_no_ext + '_en.md'))
    has_es = os.path.exists(os.path.join(dirname, name_no_ext + '_es.md'))
    
    pt_link = f"({name_no_ext}.md)" if lang != "pt" else "(#)"
    en_link = f"({name_no_ext}_en.md)" if lang != "en" else "(#)"
    es_link = f"({name_no_ext}_es.md)" if lang != "es" else "(#)"
    
    trans_badges = f"[![🇧🇷 PT](https://img.shields.io/badge/🇧🇷-Português-green)]{pt_link}"
    if has_en:
        trans_badges += f" [![🇺🇸 EN](https://img.shields.io/badge/🇺🇸-English-blue)]{en_link}"
    if has_es:
        trans_badges += f" [![🇪🇸 ES](https://img.shields.io/badge/🇪🇸-Español-orange)]{es_link}"
        
    version_badge = "![Versão](https://img.shields.io/badge/versão-v2.0-blue)"
    if lang == "en":
        version_badge = "![Version](https://img.shields.io/badge/version-v2.0-blue)"
    elif lang == "es":
        version_badge = "![Versión](https://img.shields.io/badge/versión-v2.0-blue)"
        
    status_badge = "![Status](https://img.shields.io/badge/status-Ativo-blue)"
    if lang == "en":
        status_badge = "![Status](https://img.shields.io/badge/status-Active-blue)"
    elif lang == "es":
        status_badge = "![Status](https://img.shields.io/badge/status-Activo-blue)"
        
    license_badge = "[![Licença: CC BY 4.0](https://img.shields.io/badge/Licen%C3%A7a-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)"
    if lang == "en":
        license_badge = "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)"
    elif lang == "es":
        license_badge = "[![Licencia: CC BY 4.0](https://img.shields.io/badge/Licencia-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)"

    badges = f"""[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.18827106-blue.svg)](https://doi.org/10.5281/zenodo.18827106)
{license_badge}
{status_badge}
{version_badge}

---

{trans_badges}
"""
    return badges

for folder in folders:
    if not os.path.exists(folder):
        continue
    for f in os.listdir(folder):
        if f.endswith('.md'):
            path = os.path.join(folder, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # 1. Remove Antigravity line
            content = re.sub(r'\n\*\*Auditado por:\*\* Antigravity \(IA Takwara\)', '', content)
            content = re.sub(r'\n\*\*Audited by:\*\* Antigravity \(Takwara AI\)', '', content)
            
            # 2. Remove old badges block
            # Match from [![DOI] down to the translation badges and the following ---
            content = re.sub(r'\[!\[DOI\].*?\n---\n+\[!\[🇧🇷 PT\].*?\n---\n+', '', content, flags=re.DOTALL)
            # Remove any stray --- right after header
            content = re.sub(r'\n---\n(?=\n##|$)', '\n', content)
            
            lang = "pt"
            if f.endswith('_en.md'):
                lang = "en"
            elif f.endswith('_es.md'):
                lang = "es"
                
            badges = get_badges_and_header(path, lang)
            
            # Insert badges right before the first Markdown header ## or after the frontmatter/title
            # Find the first '## ' or '---'
            # ACTUALLY, let's find the first empty line after the title block and insert there, followed by ---
            split_idx = content.find('\n\n')
            if split_idx != -1:
                # But some files might have ## at the start or title block #... \n **...** \n
                # Let's search for the first ## to insert before it
                h2_match = re.search(r'\n## ', content)
                if h2_match:
                    insert_pos = h2_match.start()
                    new_content = content[:insert_pos].strip() + "\n\n" + badges + "\n---\n" + content[insert_pos:]
                else:
                    new_content = content.strip() + "\n\n" + badges + "\n---\n"
            else:
                new_content = badges + "\n---\n" + content
                
            new_content = re.sub(r'\n{3,}', '\n\n', new_content)

            with open(path, 'w', encoding='utf-8') as file:
                file.write(new_content)
