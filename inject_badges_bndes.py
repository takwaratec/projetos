import os
import re

folders = [
    'docs/09_DOSSIE_BNDES',
    '01_SOMBRA_AUDITORIA/09_DOSSIE_BNDES'
]

def get_badges(filename, lang):
    base = filename.replace('_en.md', '.md').replace('_es.md', '.md')
    name_no_ext = base.replace('.md', '')
    
    # Check if translations exist for this file
    has_en = os.path.exists(os.path.join(os.path.dirname(filename), name_no_ext + '_en.md'))
    has_es = os.path.exists(os.path.join(os.path.dirname(filename), name_no_ext + '_es.md'))
    
    pt_link = f"({name_no_ext}.md)" if lang != "pt" else "(#)"
    en_link = f"({name_no_ext}_en.md)" if lang != "en" else "(#)"
    es_link = f"({name_no_ext}_es.md)" if lang != "es" else "(#)"
    
    trans_badges = f"[![🇧🇷 PT](https://img.shields.io/badge/🇧🇷-Português-green)]{pt_link}"
    if has_en:
        trans_badges += f" [![🇺🇸 EN](https://img.shields.io/badge/🇺🇸-English-blue)]{en_link}"
    if has_es:
        trans_badges += f" [![🇪🇸 ES](https://img.shields.io/badge/🇪🇸-Español-orange)]{es_link}"
        
    if lang == "pt":
        return f"""[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.18827106-blue.svg)](https://doi.org/10.5281/zenodo.18827106)
[![Licença: CC BY 4.0](https://img.shields.io/badge/Licen%C3%A7a-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Status](https://img.shields.io/badge/status-Ativo-blue)

---

{trans_badges}
"""
    elif lang == "en":
        return f"""[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.18827106-blue.svg)](https://doi.org/10.5281/zenodo.18827106)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Status](https://img.shields.io/badge/status-Active-blue)

---

{trans_badges}
"""
    elif lang == "es":
        return f"""[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.18827106-blue.svg)](https://doi.org/10.5281/zenodo.18827106)
[![Licencia: CC BY 4.0](https://img.shields.io/badge/Licencia-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Status](https://img.shields.io/badge/status-Activo-blue)

---

{trans_badges}
"""

for folder in folders:
    if not os.path.exists(folder):
        continue
    for f in os.listdir(folder):
        if f.endswith('.md'):
            path = os.path.join(folder, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                
            if '10.5281/zenodo.18827106' in content and 'img.shields.io' in content:
                continue # Already has badges
                
            lang = "pt"
            if f.endswith('_en.md'):
                lang = "en"
            elif f.endswith('_es.md'):
                lang = "es"
                
            badges = get_badges(path, lang)
            
            # Find the first '---' to insert before it
            parts = content.split('---', 1)
            if len(parts) > 1:
                new_content = parts[0] + badges + "\n---\n" + parts[1].lstrip('-').lstrip()
            else:
                new_content = parts[0] + "\n" + badges + "\n---\n"
                
            with open(path, 'w', encoding='utf-8') as file:
                file.write(new_content)
