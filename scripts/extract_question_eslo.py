import os
import pandas as pd
import xml.etree.ElementTree as ET

questions = []
for file in os.listdir('../cleaned_eslo_entretien/'):
    file_path = os.path.join('../cleaned_eslo_entretien/', file)
    root = ET.parse(file_path).getroot()
    tags = [t for t in root.iter('Turn')]
    for i in range(len(tags)):
        tag = tags[i]
        text = tag.text
        try:
            for t in text.split('\n'):
                if '?' in t:
                    questions.append((tags[i-1].text, t))
        except:
            pass
df = pd.DataFrame(questions, columns=['previous_sentence', 'question'])
df.to_csv('cfpp.csv', sep=';')