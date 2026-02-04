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

print(f'{konyvek=}')

