import os

for file in os.listdir('../eslo_entretien/'):
    file_path = os.path.join('../eslo_entretien/', file)
    with open(file_path,'r', encoding='cp1252') as f:
        content = f.readlines()
        for i in range(len(content)):
            if content[i].startswith(('<Sync','<Who','<Event')):
                content[i]=''
    with open(f"cleaned_{file_path.split('/')[-1]}",'w', encoding='utf8') as f:
        for c in content:
            f.write(c)