import os 
from glob import glob 
import re  

def tag(line): 
    return line.split()[0].strip() 
def value (line): 
    return line.split('-')[-1].strip()  

def get_value(file,TAG): 
    AA = []
    for line in file: 
        if len(line.strip())==0: 
            continue 
        elif line.split()[0].strip()==TAG: 
            AA.append( re.findall(r'-(.*)',line)[0].strip()) 
    if len(AA)!=0: 
        return AA
    else:return  [''] 
    
allfiles = glob("RIS/*.ris") 
        

for file in allfiles: 
    f = open(file,'r',errors="ignore").readlines() 
    
    name = int(os.path.splitext(os.path.basename(file))[0])+1
    print(name)
    
    date = get_value(f, 'DA') [0]
    if date !='': 
        year,month,day=date.split('/')
    else: 
        year = get_value(f,'Y1')
        month = '01'
        day = '01'
    fout = f"{year}-{month}-{day}-paper-title-number-{name}.md" 
    
    
    with open(fout,'w') as ff :
         ff.write('---\n')
         title = get_value(f,'T1')[0] 
         ff.write(f"title: \"{title}\"\n")
         authors = get_value(f,'AU') 
         aut_names = ";".join(authors) 
         ff.write(f"authors: \"{aut_names}\"\n") 
         ff.write(f"collection: publications\ncategory: manuscripts\n")
         url = get_value(f,'UR')[0] 
         ff.write(f"permalink: {url}\n")
         
  
         
         ff.write(f"date: {year}-{month}-{day}\n")
        
         vanue = get_value(f,'JF')[0]
         if vanue == "": 
             vanue = get_value(f,'T2') [0]
         ff.write(f"venue: {vanue}\n")
         
         page_i = get_value(f,'SP')[0] 
         page_f = get_value(f,'EP') [0]
         volume = get_value(f,'VL') [0]
         issue = get_value(f,'IS') [0]
         DOI = get_value(f,'DO')[0]
         pdfurl=f"'https://majabed.github.io/jabedlab/files/paper{name}.pdf'"
         ff.write(f"paperurl: {pdfurl}\n")
         
         
         ff.write(f"citation: '{aut_names} {title}. <i>{vanue}<\i> {year}, {volume}({issue}),{page_i}-{page_f}. DOI:{DOI}.'\n") 
         ff.write('---\n')
         
         abstract = get_value(f,'AB')[0] 
         if abstract =='': 
             abstract = get_value(f,'N2')[0]

         ff.write('\n') 
         ff.write(abstract)
         ff.write('\n')  
        
#%% 
