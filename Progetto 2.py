#----------------------------------------SOFTWARE PER LA GESTIONE DI DATI MEDICI--------------------------
"""Descrizione:
Il seguente programma si occupa di gestire controlli medici di un centro di analisi mediche, permettendo all'utente che lo utilizza
di velocizzare le normali procedure di gestione dei dati, dei referti medici e delle analisi svolte dal personale sanitario"""

import numpy as np

#Definisce i dati dei pazienti attraverso una classe e stampa i dati con il metodo scheda_personale
class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, età, peso, analisi_effettuate=None):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.età = int(età)
        self.peso = float(peso)
        self.risultati_analisi = np.array([])

        if analisi_effettuate is None:
            self.analisi_effettuate = []
        else:
            self.analisi_effettuate = analisi_effettuate


    def aggiungi_analisi(self, tipo, valore):
        nuova_analisi = Analisi(tipo, float(valore))
        self.analisi_effettuate.append(nuova_analisi)
        self.risultati_analisi = np.append(self.risultati_analisi, valore)

#Definisce il metodo per generare la scheda medica del paziente       
    def scheda_personale(self):
        testo = f"\nPAZIENTE: {self.cognome.upper()} {self.nome.upper()}\n"
        testo += f"C.F: {self.codice_fiscale}\n"
        testo += f"Età: {self.età} anni \n"
        testo += f"Peso: {self.peso} kg \n"

        if not self.analisi_effettuate:
            testo += "Nessun dato presente"
        else:
            testo += f"\n------RISULTATI ANALISI-------\n"
            testo += f"\nAnalisi effettuate: ({len(self.analisi_effettuate)})\n"
            
            for a in self.analisi_effettuate:
                testo += f"\n{a.tipo_di_analisi}: {a.risultato:.1f} -> {a.valuta()}\n"
                
        return testo 
    
    def statistiche_analisi(self):
        if len(self.risultati_analisi) == 0:
            return "Nessun dato presente"
        return(f"Media dei valori: {np.mean(self.risultati_analisi): .1f}\n"
               f"Valore Max: {np.max(self.risultati_analisi): .1f}\n"
               f"Valore min: {np.min(self.risultati_analisi): .1f}\n"
               f"Deviazione standard: {np.std(self.risultati_analisi): .1f}")


#Crea la classe Medico per visualizzare tutte le operazioni sanitarie eseguite e stampa le info sulle visite effettuate 
   
class Medico:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        print(f"\nIl seguente Medico: {self.cognome} {self.nome}\nspecializzato in: {self.specializzazione}\nha visitato il paziente: \n {paziente.scheda_personale()}")

#Crea la classe Analisi per mostrare i risultati delle analisi effettuate, con valori basati su una scala generale

class Analisi:
    def __init__(self,tipo_di_analisi, risultato):
        self.tipo_di_analisi = tipo_di_analisi
        self.risultato = risultato

#Definisce il risultato delle analisi in base ad un range(si utilizza un dizionario per stabilire il tipo d'esame con i rispettivi valori max/min)
    
    def valuta(self):
        ranges = {"Glicemia": (70,99),
                  "Colesterolo": (0,100),
                  "Trigliceridi": (0,150),
                  "Emoglobina": (12,16)
                }
        tipo= self.tipo_di_analisi
        if tipo not in ranges:
            return "Range di riferimento non definito"
        min_val, max_val = ranges[self.tipo_di_analisi]

        if self.risultato < min_val:
            return "Valore Basso"
        elif self.risultato > max_val:
            return "Valore troppo Alto"
        else:
            return "Valore nella norma"
        

#TEST DEL PROGRAMMA CON DATI DI PAZIENTI E MEDICI    

def main():
    print("---------CENTRO DI ANALISI MEDICHE-----------\n")

medici=[
    Medico("Luca", "Ascoli", "Cardiologia"), 
    Medico("Laura", "Neri", "Endocrinologia") ,
    Medico("Anna", "Verdi", "Laboratorio")]



pazienti = []

p1 = Paziente("Mario", "Rossi", "RSSMRA70A01F205L", 42, 68.5)
p1.aggiungi_analisi("Glicemia", 94)
p1.aggiungi_analisi("Colesterolo", 218)
p1.aggiungi_analisi("Trigliceridi", 142)
pazienti.append(p1)


p2 = Paziente("Mauro", "Bianchi", "BNCHMR34B02M201Z", 38, 54.9)
p2.aggiungi_analisi("Glicemia", 108)
p2.aggiungi_analisi("Colesterolo", 170)
p2.aggiungi_analisi("Trigliceridi", 130)
pazienti.append(p2)

p3 = Paziente("Luca", "Conti", "CNTLCU92P15L219K", 33, 78.0)
p3.aggiungi_analisi("Glicemia", 82)
p3.aggiungi_analisi("Colesterolo", 172)
p3.aggiungi_analisi("Trigliceridi", 210)
pazienti.append(p3)

p4 = Paziente("Alessandro", "Romano", "RMNLSS75M10H501R", 47, 62.0)
p4.aggiungi_analisi("Glicemia", 89)
p4.aggiungi_analisi("Colesterolo", 205)
p4.aggiungi_analisi("Trigliceridi", 138)
pazienti.append(p4)

p5 = Paziente("Giuseppe", "Ferrari", "FRRGPEU85B22H501Z", 39, 90.0)
p5.aggiungi_analisi("Glicemia", 100)
p5.aggiungi_analisi("Colesterolo", 185)
p5.aggiungi_analisi("Trigliceridi", 165)
pazienti.append(p5)

#Stampa le schede e le statistiche delle analisi di ogni paziente

for p in pazienti:
    print (f"\n:---DATI PAZIENTE---:\n {p.scheda_personale()}\n")

    print(f"---STATISTICHE---\n{p.statistiche_analisi()}\n")

#Esempio di visite effettuate
medici[0].visita_paziente(pazienti[0])
print()
medici[1].visita_paziente(pazienti[1])
print()
medici[2].visita_paziente(pazienti[2])

if __name__ == "__main__":
    main()






