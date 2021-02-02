import os
import pandas as pd
import xml.etree.ElementTree as ET

questions = []
for file in os.listdir('../cfpp/'):
    file_path = os.path.join('../cfpp/', file)
    root = ET.parse(file_path).getroot()
    tags = [t for t in root.iter('{http://www.tei-c.org/ns/1.0}seg')]
    # tags = [t for t in root.iter('seg')]
    print(tags)
    for i in range(len(tags)):
        tag = tags[i]
        text = tag.text
        print(text)
        if '?' in text:
            try:
                questions.append((tags[i-1].text, text))
            except:
                pass
df = pd.DataFrame(questions, columns=['previous_sentence', 'question'])
df.to_csv('cfpp.csv', sep=';')