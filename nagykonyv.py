konyvek = []
with open('2023/Forrasok/02_feladat/konyvek.txt', 'r',encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        #nev;szulEv;halEv;nemzetiseg;cim;helyezes
        nev = adatok[0]
        szulEv = int(adatok[1])
        halEv = int(adatok[2]) if adatok[2] != "" else 2005
        nemzetiseg = adatok[3]
        cim = adatok[4]
        helyezes = int(adatok[5])
        konyv = {
            'név': nev,
            'szul_Ev': szulEv,
            'hal_Ev': halEv,
            'nemzetiségek': nemzetiseg,
            'cím': cim,
            'helyezés': helyezes
        }
        konyvek.append(konyv)

# 3.2.feladat
print(f"3.2.feladat: Az állományban {len(konyvek)} adatai szerepelnek.")

#3.3.feladat
magyar_konyvek = []
for konyv in konyvek:
    if konyv["nemzetiségek"] == 'magyar':
        magyar_konyvek.append(konyv)

print(len(magyar_konyvek))

legjobb_konyv = magyar_konyvek[0]
for konyv in magyar_konyvek:
    if konyv['helyezés'] < legjobb_konyv['helyezés']:
        legjobb_konyv = konyv

print(f" 3.3.feladat: A legjobb helyezést elért magyar könyv: {legjobb_konyv['név']}: {legjobb_konyv['cím']}")

#3.4.feladat
nemet_iro = False
for konyv in konyvek:
    if konyv["nemzetiségek"] == 'német':
        nemet_iro = True

if nemet_iro:
        print("3.4.feladat: A listában szerepel német író könyve.")
else:
        print("3.4.feladat: A listában nem szerepel német író könyve.")

#3.5.feladat
idosebb_mint_90 = []
for konyv in konyvek:
    if (konyv['hal_Ev'] - konyv['szul_Ev'] > 90):
        idosebb_mint_90.append(konyv['név'])

print("3.5. feladat: 90 évesnél idősebb írók:")
for iro in idosebb_mint_90:
    print("\t"+ iro)