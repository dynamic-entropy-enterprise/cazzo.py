# Cazzo.py
disegna cazzi su command line

# Motivazione
te gusta er pipo

# Installazione
cazzo.py dipende dai seguenti programmi
 - `clear` (per sistemi unix)
 - `cls` (per sistemi windows)
 
dovrebbero essere presintallati 

dopo essersi assicurati che i programmi siano presenti clonare la repo

# Utilizzo
`cazzo.py` può disegnare cazzi di lunghezza fissa o variabile a seconda del numero di  argomenti passati in command line

## Lunghezza fissa
nella directory della repo, girare
```bash
python cazzo.py <length>
```
disegna un cazzo di lunghezza `<length>`

## Lunghezza variabile
nella directory della repo, girare
```bash
python cazzo.py <min-length> <max-length>
```
diesgna un cazzo la cui lunghezza varia tra `<min-length>` e `<max-length>` nel tempo, si può specificare il tempo in cui il cazzo si allunga/accorcia di un'unità specificando
```bash
python cazzo.py <min-length> <max-length> <time(millis)>
```

# TODO
 - parametrizzare la larghezza del cazzo
 - permettere tipi diversi di cazzo (es. circonciso, non circonciso)
 - file di config per il cazzo
 - opzione per far partire "ho litigato con mia moglie" di Gianni Celeste ogni volta che giri lo script
