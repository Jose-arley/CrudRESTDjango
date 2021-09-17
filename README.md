# Creacion de un CRUD Completo con API REST


## usuario administrativo : Pruebas, password 12345
  
1. Clone repositorio:  
  
```console  
$ git clone +
```  
  
2. Instale el archivo requirements:  
  
```console  
$ pip install -r requirements.txt  
```  
  
3. Actualice la BBDD :   
   
```console  
$ python manage.py makemigrations   
$ python manage.py migrate   
```  
   
4. Ejecute la app:   
  
```console   
$ python manage.py runserver  
```   
##ejemplo de creaciòn de usurio usando Postman
#url del servicio:http://127.0.0.1:8000/api/Developers-items
{
	"first_name":"jose",
	"last_name": "briceño",
	"Documente_number": "1060742472"
	"Language_Develop": "Python",
	"Experience": "2 años",
	"email": "random@gmail.com",
	"years": 28
}

