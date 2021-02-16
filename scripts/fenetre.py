import os
import pandas as pd
import xml.etree.ElementTree as ET

questions = []
for file in os.listdir('../cleaned_eslo_entretien/'):
    file_path = os.path.join('../cleaned_eslo_entretien/', file)
    # print(file_path)
    root = ET.parse(file_path).getroot()
#     all_descendants = list(root.iter('Turn'))
#     print(all_descendants[30:40])
#     print([elem.tag for elem in root.iter()])
    tags = [t for t in root.iter('Turn')]
#     print(tags)
    for i in range(5, len(tags)-5):
        tag = tags[i]
        text = tag.text
#         print(len(text))
        try:
            for t in text.split('\n'):
                if '?' in t and t!='?':
                    context_p = ''
                    context_n = ''
                    for o in range(5):
                        context_p += tags[i-o-1].text
                        context_n += tags[i+o+1].text
                    questions.append((context_p, t, context_n))
        except:
            pass

df = pd.DataFrame(questions, columns=['previous_5_turn', 'question', 'next_5_turn'])
df.to_csv('eslo_repas_fenetre.csv', sep=';')