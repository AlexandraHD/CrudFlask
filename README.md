# CrudFlask
--------------------------  ENGLISH  -----------------------

-----------------------------------------  CRUDWebFlask  ---------------------------------------
With this project I pretend to create a web app in which a user can register their name, a message,
and choose between some pets. When the user sends the info, their name and message are shown on
the same window, as a list. On another tab, the user can search for their code and will see the
pet that was assigned according to their selection.

*** Database ***
The database has 3 tables: Users, Pets, and Matches.

Users has 3 fields: id_user, name, message.
Pets has 3 fields: id_pet, type, photo.
Match has 2 fields: id_user, id_pet.

*** Navbar ***
The navbar has 3 tabs: Home, Users, and Match.

Home: Main page that shows what the app does and how to use it.
Users: Page in which the user can find a form to register their name and message.
	Also, it will show a list with the user's code, name, and message.
Matches: Page in which the user will find a searching barr to search for their code, choose an
	animal, and see the assigned pet.

*** Edit ***
In order to edit the info submitted, you can clic on the code assigned. You will be redirected to
other page to change the info. On this page, you will see your code, name, and message. However,
only name and message can be changed.


--------------------------  ESPAÑOL  -----------------------

-----------------------------------------  CRUDWebFlask  ---------------------------------------

En este proyecto se quiere crear una pagina web en la que un usuario pueda registrar su nombre,
un mensaje y elegir entre mascotas. Cuando el usuario envía la información, su nombre y mensaje
se muestran en la misma ventana, en un listado. Y en otra pestaña, el usuario puede buscar su
código, y verá la mascota que se le ha asignado de acuerdo a sus preferencias.


*** Base de datos ***
La base de datos contiene 3 tablas: Users, Pets y Matches.

Users tiene los campos: id_user, name, message.
Pets tiene los campos: id_pet, type, photo.
Match tiene los campos: id_user, id_pet.

*** Barra de navegación ***
La barra de navegación cuenta con 3 pestañas: Home, Users y Match.

Home: Página principal en la que se muestra al usuario lo que hace la página web y cómo se usa.
Users: Página en la que el usuario encontrará un formulario para registrar su nombre y mensaje. 
	También mostrará una lista con el codigo, nombre y los mensajes de los usuarios.
Matches: Página en la que el usuario econtrará una barra para realizar la búsqueda de su código, 
	elegir el animal de su preferencia y ver la mascota asignada.

*** Editar ***
Para editar la información proporcionada, puede hacer clic sobre el código que se le asignó. 
Va a ser redirigido a otra página para editar su informacion. En esta página verá su código, 
nombre y mensaje. Sin embargo, solo nombre y mensaje pueden ser editados.
