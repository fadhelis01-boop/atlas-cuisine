import re
def parse_tome3(path='/mnt/user-data/outputs/BIBLE_TOME3_REFERENTIEL_INGREDIENTS.md'):
    rows={}
    sec=''
    for line in open(path,encoding='utf-8'):
        if line.startswith('## '): sec=line.strip()
        if not line.startswith('|'): continue
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells)<5 or cells[0] in('Nom','Colonne','---') or set(cells[0])<=set('-: '): continue
        name=re.sub(r'\*\*|^✅\s*','',cells[0]).strip()
        al,de,dispo=cells[1],cells[2],cells[3]
        if not re.match(r'^(🟢|🟡|🟠|🔴|—)',dispo): continue
        sure=set();maybe=set()
        for tok in re.split(r'[,\s]+',al.replace('—','')):
            m=re.match(r'^(GL|CR|OE|PO|AR|SO|LA|FC|CE|MO|SE|SU|LU|MM)(\?)?$',tok)
            if m: (maybe if m.group(2) else sure).add(m.group(1))
        d={}
        t=re.sub(r'\*\*','',de)
        if re.search(r'PORC\?',t): d['pork']='possible'
        elif re.search(r'PORC',t): d['pork']='certain'
        if re.search(r'ALC~',t): d['alcohol']='trace'
        if re.search(r'(?<![~])ALC(?![~])',t): d['alcohol']='certain'
        if 'ANIM' in t: d['animal']='certain' if 'ANIM?' not in t else 'possible'
        rows[name]={'allergens':sure,'maybe':maybe,'derivs':d,'dispo':dispo[0],'section':sec,'raw_derivs':de}
    return rows
if __name__=='__main__':
    R=parse_tome3(); print(len(R),"lignes parsées")
    import sys
    for q in ['poulet','olive','citron','oignon','ail','gingembre','curcuma','safran','coriandre','persil','huile','moutarde','citron vert','ghee','lentilles','cumin','tomate','garam','spaghetti','pâtes','guanciale','pancetta','pecorino','parmesan','œuf','poivre','sel','paleron','bœuf','lardons','vin rouge','carotte','champignon','bouquet','thym','laurier','vinaigre','concentré','nouilles','crevette','sauce de poisson','germes','cacahu','tamarin','sucre','piment','aubergine','courgette','poivron','basilic','farine','levure','eau','lait','beurre','rhum','magret','dinde','jus de raisin','harissa','paprika','cébette','tofu','bouillon','jus de citron']:
        hits=[n for n in R if q.lower() in n.lower()]
        print(f"{q!r}: {hits[:7]}")
