import numpy as np

def laagste_verbruik_uren(prijzen, n):
    """
    Berekent de beste aaneengesloten uren met de laagste gemiddelde procentuele waarde.
    
    :param prijzen: Lijst met prijzen per uur (24 waarden)
    :param n: Aantal aaneengesloten uren dat geoptimaliseerd moet worden
    :return: (beste_start_uur, beste_eind_uur, laagste_gemiddelde)
    """
    # Procentuele waarden berekenen
    max_prijs = max(prijzen)
    procentuele_waarden = [(p / max_prijs) * 100 for p in prijzen]
    
    # Sliding window om de laagste aaneengesloten periode te vinden
    min_gemiddelde = float('inf')
    beste_start = 0
    
    for i in range(25 - aantal_uren):  # Loop over mogelijke startpunten
        huidig_gemiddelde = np.mean(procentuele_waarden[i:i + n])
        
        if huidig_gemiddelde < min_gemiddelde:
            min_gemiddelde = huidig_gemiddelde
            beste_start = i
    
    beste_eind = beste_start + aantal_uren - 1
    return beste_start, beste_eind, min_gemiddelde

def uren_onder_waarde(prijzen, procent_drempel):
    """
    Berekent het aantal uren waarbij de prijs onder een bepaald percentage van het gemiddelde ligt.
    
    :param prijzen: Lijst met prijzen per uur (24 waarden)
    :param procent_drempel: Percentage van het gemiddelde waar de prijs onder moet liggen
    :return: Aantal uren onder de drempel
    """
    gemiddelde_prijs = np.mean(prijzen)
    drempel_waarde = (procent_drempel / 100) * gemiddelde_prijs
    
    uren_onder = sum(1 for p in prijzen if p < drempel_waarde)
    
    return uren_onder

# Voorbeeld: 24 willekeurige prijzen en een venster van 6 uur
prijzen_per_uur = [10, 8, 6, 4, 7, 20, 25, 30, 28, 18, 16, 14, 12, 10, 8, 6, 5, 7, 9, 13, 17, 19, 21, 23]
procent_drempel = 60  # Drempelwaarde als percentage van het gemiddelde

aantal_uren = uren_onder_waarde(prijzen_per_uur, procent_drempel)
beste_start, beste_eind, laagste_gemiddelde = laagste_verbruik_uren(prijzen_per_uur, aantal_uren)


print(f"Beste uren voor laag verbruik: {beste_start}:00 - {beste_eind}:00 met een gemiddelde waarde van {laagste_gemiddelde:.2f}%")
print(f"Aantal uren onder {procent_drempel}% van het gemiddelde: {aantal_uren}")
