# WAAT-2018
Repository del Corso WAAT AA-2017-18 

## Installazione


1. da _Pycharm_ aprire il menù *VCS*->*Checkout From Version Control*->*GitHub*
2. selezionare _Auth Type_->*password* e inserire le credenziali del vostro account su GitHub 
3. inserire *https://github.com/SteTicca/Gruppo1*  nel campo *Git Reposistory Url*

oppure da terminale (per utenti esperti):

```git

    git clone https://github.com/SteTicca/Gruppo1
    
```

Scaricato il repository, assicurarsi di avere creato il *VirtualEnv* per il progetto.
File -> Settings -> Project Interpreter.
- Premere sull'ingranaggio a destra del campo per selezionare il _Python Interpreter_.
- Selezionare _Add Local_.
- *NB* Assicurarsi in inserire la cartella corretta nel campo _Location_ e premere invio.


oppure da terminale (per utenti esperti):
- Aprire il terminale di _PyCharm_ ed eseguire il seguente comando.

```bash
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
```
Il file requirements.txt contiene la lista di tutte le librerie che serviranno durante le
esercitazioni come ad esempio *nltk*, *numpy* etc.
