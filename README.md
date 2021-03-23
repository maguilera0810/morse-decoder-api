# familify_test


Para probar en el loca es necesario tener instalado Pyhon3


pip install -r requirements.txt

Despues ejecutar los siguiens comandos
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python applications/morse/scripts/upload_code.py
python manage.py createsuperuser


las apis son las siguientes
http://mauss-morse-decoder.herokuapp.com

-Devuelve un listado de los codigos morse
    curl -X GET  "http://mauss-morse-decoder.herokuapp.com/api/get-codes" 

-Devuelve un listado de las palabras con mayor frecuencia
    curl -X GET  "http://mauss-morse-decoder.herokuapp.com/api/get-words" 

-Devuelve en codigo morse el valor del parametro test
    curl -X POST  "http://mauss-morse-decoder.herokuapp.com/api/translate/2morse" -d "{text:'HOLA MUNDO'}"

-Devuelve en alphanumerico el valor del parametro test
    curl -X POST  "http://mauss-morse-decoder.herokuapp.com/api/translate/2human" -d "{text:'.... --- .-.. .-   -- ..- -. -.. ---'}"

-Devuelve en codigo morse el valor del decodificado de  test
    curl -X POST  "http://mauss-morse-decoder.herokuapp.com/api/translate/bit2morse" -d "{text:'00000000110110110011100000111111001111110011111100000111011111111011101110000001100011111100000000011111100111111000001110110011111100000111111000111000001111110011001111000001111110001111110011111100000000'}"

-Devuelve en alphanumerico el valor del decodificado de  test
    curl -X POST  "http://mauss-morse-decoder.herokuapp.com/api/translate/bit2human" -d "{text:'00000000110110110011100000111111001111110011111100000111011111111011101110000001100011111100000000011111100111111000001110110011111100000111111000111000001111110011001111000001111110001111110011111100000000'}"

-el front para realizar las pruebas:
    https://maguilera0810.github.io/mauss-morse-decoder/

-repositorio del frontend
    https://github.com/maguilera0810/mauss-morse-decoder


-para ejecutar los test ejecutar:
    pytest