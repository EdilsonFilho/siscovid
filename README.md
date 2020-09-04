# PROJETO SISCOVID
Criando o ambiente e o projeto:

## Para a API
### usei VSCode
-importante verficar as extensoes e configurar o interpretador do projeto. Usei python 3.6.9

### criando o diretorio e encapsulando com virtualenv
```
mkdir siscovid
cd siscovid
virtualenv venv --python=python3
source venv/bin/activate
```

### instalando o django
```
pip install django
django-admin startproject siscovid
```

### entrando no projeto
```cd siscovid```
```python manage.py```

(para rodar o servidor que pode ser acessado em localhost:8000)

### iniciando a aplicação
`python mange.py startapp siscovid`
-criei na model os campos que desejo

-fui em settigns e fiz :

			installed_Apps  add 'scheduling'
			
			language: pt-br
			
python manage.py migrate
`python manage.py makemigrations`

(vai aparecer o __initial__)


`pyton manege.py migrate` (aplica a estrutura no banco de dados)

`python manage.py createsuperuser` (criando super usuario)
-pus as credenciais pedidas
-Para verificar subi o servidor e verifiquei se tudo estava ok, Done!

-Fui no admin.py e:
	 add from .models import scheduling
(com isso eu pude ter a capicidade de add registros, para alimentar dados na API)

Como é uma API, queremos gerar rotas e disponibilizar como JSON

-Fui em views e :

	'from .models import scheduling'
	
(e criei os metodos necessários)

-em urls.py add os paths das views

-e add: from scheduling.views etc....

### instalando rest_framework
`pip install djangorestframework`
-colocar em settings >> installed_apps o `rest_framework` 

[veja mais sobre django resframework aqui](https://www.django-rest-framework.org/)

-Usei insomnia para fazer teste usando as rotas que criei, com servidor em operacao. Tudo ok!

-o proprio django restframework ja me permite testar também as rotas, por exemplo GET, POST etc.

### Ainda na aplicação
-Desenvolvi a aplicação, usando a ideia de serializer etc. 


### Endpoints importantes
```
GET http://localhost:8000/scheduling/
POST http://localhost:8000/scheduling/create
PUT http://localhost:8000/scheduling/<id>/
```
  
### Para testar
-Usei Insomnia

-Criei um projeto chamado "medico",mas na verdade é um sistema em Python para cadastro e login de usuarios que usam as rotas listadas acima.








