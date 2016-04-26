## Przygotowanie
* Python 3.5.1 [link](https://www.python.org/downloads/)

## Pobranie projektu

Uruchamiasz Windows PowerShell. Przechodzisz to wybranego folderu. W moim przypadki D:\PYTHON\test.
wpisujesz `git init` i następnie `git pull https://github.com/zatto84/zalien.git`.

## Instalacja virtualenvy

W PowerShell `pip install virtualenv`

## Uruchomienie virtual envy

Za pomocą powershell wpisujesz ` virtualenv.exe envy`

## Przejście do środowiska wirtualnego

Z konsoli `\envy\Scripts\activate`

## Instalacja zależności 

Przejdź do folderu test i wpisz konsoli `pip install -r .\requirements.txt`
Jeden z plików może się nie pobrać automatycznie. Jeżeli tak się stanie to zainstaluj go ręcznie. `pip install git+https://github.com/nwcell/psycopg2-windows.git@win64-py34#egg=psycopg2`
[Dla innych wersji ](https://github.com/nwcell/psycopg2-windows)

## Dodawanie zależności

**Jeżeli z jakiegoś powodu dodasz coś do wirtualki nie zapomnij dodać tego do pliku requirements.txt**

W tym celu będąc w folderze test musisz wpisać `pip freeze > .\requirements.txt`
