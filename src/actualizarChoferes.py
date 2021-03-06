src/actualizarViaje.py                                                                              0000664 0001752 0001752 00000000000 13573612654 020613  0                                                                                                    ustar   rodrigo.villalba                rodrigo.villalba                                                                                                                                                                                                       src/api/                                                                                            0000775 0000060 0001757 00000000000 13573521677 012430  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/api/user/                                                                                       0000775 0000060 0001757 00000000000 13573712111 013367  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/api/user/__init__.py                                                                            0000775 0000000 0001757 00000000000 13563664232 015236  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              src/api/user/__pycache__/                                                                           0000775 0000000 0001757 00000000000 13573722054 015342  5                                                                                                    ustar   root                            developer                                                                                                                                                                                                              src/api/user/__pycache__/__init__.cpython-36.pyc                                                    0000775 0000060 0001757 00000000227 13563664415 022004  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
�h�]    �               @   s   d S )N� r   r   r   �D/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                             src/api/user/__pycache__/registrar.cpython-36.pyc                                                   0000644 0000060 0000060 00000001747 13572677752 021500  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
��]�  �               @   s�   d dl mZ d dl mZ d dlmZ d dlmZ d dlmZ d dlm	Z	 dZ
dZee
e�Zejee
 d	gd
�eedd� ���ZdS )�    )�request)�	Blueprint)�require_api_token)�content_type_json)�Persona)�ClienteZ	registrarz/ucar/usuario/�POST)�methodsc           
   C   sn   yRt tj� �} tj� jtj| d k�}|j� rJtf | �}|j	�  ddd�S ddd�S    ddd�S ddd�S )	N�email�okzusuario creado)�status�message�errorzEmail no admitido!zError de conexion!zusuario no creado)
�dictr   �get_jsonr   �select�wherer
   �existsr   �save)�data�query�new� r   �E/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/registrar.py�usuario_registrar   s    



r   N)�flaskr   r   Zapi.utilr   r   �orm.model.ucar.personar   �orm.model.client.clienter   ZINDEX�PATH�__name__�index_usuario_registrar�router   r   r   r   r   �<module>   s   
                         src/api/user/__pycache__/identificar.cpython-36.pyc                                                 0000644 0000060 0000060 00000002037 13573520721 021730  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
ʡ�]�  �               @   s�   d dl mZ d dlmZ d dl mZ d dlmZ d dlmZ d dlmZ d dl	m
Z
 dZd	Zeee�Zejee d
gd�eedd� ���ZdS )�    )�request)�Select)�	Blueprint)�update_user_conn)�require_api_token)�content_type_json)�PersonaZidentificarz/ucar/usuario/�POST)�methodsc              C   s�   t d �} ylttj� �}tjtjtjtj�j	tj|d ktj|d k@ �} | j
� rrt| d jg� d| d j� d�S W n   ddd�S ddd�S )	N�email�passwordr   �ok)�status�message�errorz	pg selectz&El usuario no se encuentra registrado!)r   �dictr   �get_jsonr   �select�idr   r   �where�existsr   )�query�data� r   �G/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/identificar.py�usuario_identificar   s    
r   N)�flaskr   �peeweer   r   �api.utilr   r   r   �orm.model.ucar.personar   �INDEX�PATH�__name__�index_usuario_identificar�router   r   r   r   r   �<module>   s   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 src/api/user/__pycache__/listar.cpython-36.pyc                                                      0000644 0000060 0000060 00000001350 13564701436 020746  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
��]g  �               @   sf   d dl mZ d dl mZ d dlmZ d dlmZ dZdZeee	�Z
e
jee dgd�ed	d
� ��ZdS )�    )�jsonify)�	Blueprint)�require_api_token)�Personazlistar/z/ucar/usuario/�GET)�methodsc           	   C   sF   g } y(t j� }x|j� D ]}| j|� qW W n   ddd�S t| �S )N�errorzError de conexion!)�status�message)r   �select�dicts�appendr   )�data�query�result� r   �B/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/listar.py�usuario_listar   s    
r   N)�flaskr   r   �api.utilr   �orm.model.ucar.personar   �INDEX�PATH�__name__�index_usuario_listar�router   r   r   r   r   �<module>   s   
                                                                                                                                                                                                                                                                                        src/api/user/__pycache__/crear_reserva.cpython-36.pyc                                               0000644 0000060 0000060 00000001732 13573350604 022274  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
���]F  �               @   s�   d dl mZ d dl mZ d dlmZ d dlmZ d dlmZ d dlm	Z	 d dl
mZ d dlmZ d	Zd
Zeee�Zejee dgd�eedd� ���ZdS )�    )�request)�	Blueprint)�Select)�require_api_token)�content_type_json)�ViajeReservado)�Persona)�update_user_connZreservarz/ucar/reserva/�POST)�methodsc           	   C   sL   y6t tj� �} tf | �}t| d g� |j�  ddd�S    ddd�S d S )N�fk_persona_id�okzViaje Reservado!)�status�message�errorzNo existe el usuario!)�dictr   �get_jsonr   r	   �save)�data�new� r   �I/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/crear_reserva.py�viaje_reservar   s    

r   N)�flaskr   r   �peeweer   �api.utilr   r   �orm.model.ucar.viaje_reservador   �orm.model.ucar.personar   r	   �INDEX�PATH�__name__�index_reserva_reservar�router   r   r   r   r   �<module>   s   
                                      src/api/user/__pycache__/eliminar_reserva.cpython-36.pyc                                            0000644 0000000 0000000 00000001601 13573332617 022267  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3
���]  �               @   s~   d dl mZ d dl mZ d dlmZ d dlmZ d dlmZ d dlm	Z	 dZ
dZee
e�Zejee
 d	gd
�edd� ��ZdS )�    )�request)�	Blueprint)�Select)�require_api_token)�content_type_json)�ViajeReservadoz	cancelar/z/ucar/viaje/�GET)�methodsc            
   C   sN   y8t j� jt jtjjd�k�j� r,ddd�S ddd�S W n   ddd�S d S )NZid_viaje�okzViaje Cancelado!)�status�message�errorzEl viaje no existe!zBad Request!)r   �delete�where�idr   �args�get�execute� r   r   �L/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/eliminar_reserva.py�viaje_reservar   s     
r   N)�flaskr   r   �peeweer   �api.utilr   r   �orm.model.ucar.viaje_reservador   �INDEX�PATH�__name__�index_reserva_cancelar�router   r   r   r   r   �<module>   s   
                                                                                                                               src/api/user/__pycache__/listar_reservas.cpython-36.pyc                                             0000644 0000060 0000060 00000001574 13565365174 022676  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
7�]�  �               @   s�   d dl mZ d dl mZ d dl mZ d dlmZ d dlmZ d dlmZ d dl	m
Z
 dZd	Zeee e�Zejee d
gd�edd� ��ZdS )�    )�request)�jsonify)�	Blueprint)�Select)�require_api_token)�content_type_json)�ViajeReservadozlistar/z/ucar/reserva/�GET)�methodsc           	   C   sJ   y4g } t jt j�}x|j� D ]}| j|� qW t| �S    ddd�S d S )N�errorzError de conexion!)�status�message)r   �select�id�dicts�appendr   )Z	respuesta�query�result� r   �K/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/listar_reservas.py�reserva_listar   s    r   N)�flaskr   r   r   �peeweer   �api.utilr   r   �orm.model.ucar.viaje_reservador   �INDEX�PATH�__name__�index_reserva_listar�router   r   r   r   r   �<module>   s                                                                                                                                       src/api/user/__pycache__/subir_foto.cpython-36.pyc                                                  0000644 0000060 0000060 00000002523 13573276472 021635  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
w{�]Z  �               @   s�   d dl mZ d dl mZ d dlmZ d dlmZ d dlmZ d dlm	Z	 d dlm
Z
 d dlZd	Zd
Zeee e�Zejee dgd�eedd� ���ZdS )�    )�request)�	Blueprint)�Select)�require_api_token)�content_type_json)�Persona)�update_user_connNZsubirz/foto/�POST)�methodsc              C   s�   y�t tj� �} tj� jtj| d k�}|j� r�t| d g� t	dd�}|j
| d � |j�  tjdddt| d � g� tjddt| d � g� dd	d
�S ddd
�S W n   ddd
�S d S )NZuserIdz5/opt/rh/httpd24/root/var/www/ucar/html/env2/fotos/aux�wZimgDataz=/opt/rh/httpd24/root/var/www/ucar/html/env2/scripts/decode.shz2/opt/rh/httpd24/root/var/www/ucar/html/env2/fotos/z=/opt/rh/httpd24/root/var/www/ucar/html/env2/scripts/rename.sh�okzFoto Subida!)�status�message�errorzEsa persona no existe!zError Interno)�dictr   �get_jsonr   �select�where�id�existsr   �open�write�close�sub�run�str)�data�queryZfoto� r   �F/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/subir_foto.py�	SubirFoto   s    

r    )�flaskr   r   �peeweer   �api.utilr   r   �orm.model.ucar.personar   r   �
subprocessr   �INDEX�PATH�__name__�index_foto_subir�router    r   r   r   r   �<module>   s                                                                                                                                                                                src/api/user/__pycache__/get_user_by_email.cpython-36.pyc                                           0000644 0000000 0000000 00000001637 13573332617 022427  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3
���]�  �               @   s~   d dl mZ d dl mZ d dl mZ d dlmZ d dlmZ d dlm	Z	 dZ
dZee
e�Zejee
 d	gd
�edd� ��ZdS )�    )�request)�jsonify)�	Blueprint)�require_api_token)�Persona)�Selectzdatos/z/ucar/usuario/�GET)�methodsc           
   C   sn   g } yLt j� jt jtjjd�k�}|rDx&|j� D ]}| j|� q0W n
ddd�S W n   ddd�S t	| d �S )N�email�errorzEsa Persona no existe!)�status�messagezError de conexion!r   )
r   �select�wherer
   r   �args�get�dicts�appendr   )�data�query�result� r   �M/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/get_user_by_email.py�usuario_datos   s    
r   N)�flaskr   r   r   �api.utilr   �orm.model.ucar.personar   �peeweer   �INDEX�PATH�__name__�index_usuario_datos�router   r   r   r   r   �<module>   s   
                                                                                                 src/api/user/__pycache__/recuperar_cuenta.cpython-36.pyc                                            0000644 0000060 0000060 00000002464 13564713712 023006  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
���]Z  �               @   s�   d dl mZ d dlmZ d dlmZ d dlmZ d dlmZ d dl	m
Z
 d dl	mZ d dl	mZ d d	lmZ d
ZdZeee�Zeeejee dgd�dd� ���ZdS )�    )�search)�uuid1)�md5)�request)�	Blueprint)�ucar_sendemail)�require_api_token)�content_type_json)�Personaz
recuperar/z/ucar/usuario/�GET)�methodsc              C   s�   t jjd�} | r�tjtj�jtj| k�}|j� r�d}t	|| �r�t
t� �dd� }tjtjt|j� �j� i�jtj| k�j� }|r�t| d|� �� ddd�S d	d
d�S d	dd�S d	dd�S d	dd�S )N�emailz-^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$r   �   z	password �okzemail enviado)�status�message�errorzerror al actualizarzemail no validozemail no encontradozfalta parametro)r   �args�getr
   �select�password�wherer   �existsr   �strr   �updater   �encode�	hexdigest�executer   )�data�query�regex�pw� r"   �L/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/recuperar_cuenta.py�usuario_recuperar_cuenta   s    
,



r$   N)�rer   �uuidr   �hashlibr   �flaskr   r   �api.utilr   r   r	   �orm.model.ucar.personar
   �INDEX�PATH�__name__�index_recuperar_cuenta�router$   r"   r"   r"   r#   �<module>   s   
                                                                                                                                                                                                            src/api/user/__pycache__/actualizar_perfil.cpython-36.pyc                                           0000644 0000060 0000060 00000002216 13573722054 023151  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
!��]L  �               @   sv   d dl mZ d dl mZ d dlmZ d dlmZ d dlmZ dZdZ	eee
�Zeje	e dgd	�eed
d� ���ZdS )�    )�request)�	Blueprint)�require_api_token)�content_type_json)�PersonaZ
actualizarz/ucar/perfil/�POST)�methodsc              C   s�   y�t tj� �} tj� jtj| d k�}|j� r�| d dkrrtj| d | d | d | d d�jtj| d k�j	� }n<tj| d | d | d | d | d d	�jtj| d k�j	� }d
dd�S ddd�S    ddd�S d S )N�id�password� �nombre�apellido�email�institucion)r   r   r   r   )r   r   r   r   r
   �okzPerfil Modificado!)�status�message�errorzEsa persona no existe!zError de conexion!)
�dictr   �get_jsonr   �select�wherer	   �exists�update�execute)�data�queryZnrows� r   �M/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/actualizar_perfil.py�actualizar_perfil   s(    " 

r   N)�flaskr   r   �api.utilr   r   �orm.model.ucar.personar   �INDEX�PATH�__name__�index_perfil_actualizar�router   r   r   r   r   �<module>   s   
                                                                                                                                                                                                                                                                                                                                                                                  src/api/user/__pycache__/registrar_vehiculo.cpython-36.pyc                                          0000644 0000060 0000060 00000002017 13573623771 023356  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
!%�]�  �               @   s�   d dl mZ d dl mZ d dlmZ d dlmZ d dlmZ d dlmZ dZ	dZ
ee
e	 e�Zeje
e	 d	gd
�eedd� ���ZdS )�    )�request)�	Blueprint)�update_user_conn)�require_api_token)�content_type_json)�Vehiculo�	registrarz/ucar/vehiculo/�POST)�methodsc           
   C   s�   yjt tj� �} tj� jtj| d k�jd�}|j� rFtj	f | �j
�  ntf | �j�  t| d g� ddd�S    ddd�S ddd�S )	N�	fkPersona�   �okzVehiculo registrado)�status�message�errorzError al guardarzUsuario no encontrado)�dictr   �get_jsonr   �select�wherer   �limit�exists�update�execute�saver   )�data�query� r   �N/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/registrar_vehiculo.py�vehiculo_registrar   s    

r   N)�flaskr   r   �api.utilr   r   r   �orm.model.ucar.vehiculor   �INDEX�PATH�__name__�index_vehiculo_registrar�router   r   r   r   r   �<module>   s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    src/api/user/__pycache__/editar_itinerario.cpython-36.pyc                                           0000644 0000060 0000060 00000001651 13573337260 023151  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
���]  �               @   s�   d dl mZ d dl mZ d dlmZ d dlmZ d dlmZ d dlm	Z	 d dlm
Z
 dZd	Zeee e�Zejee d
gd�eedd� ���ZdS )�    )�request)�	Blueprint)�Select)�require_api_token)�content_type_json)�
Itinerario)�update_user_connZeditarz/ucar/itinerario/�POST)�methodsc           	   C   sL   y6t tj� �} tf | �}t| d g� |j�  ddd�S    ddd�S d S )N�
fk_persona�okzItinerario Guardado!)�status�message�errorzNo existe el usuario!)�dictr   �get_jsonr   r   �save)�data�new� r   �M/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/editar_itinerario.py�editar_itinerario   s    

r   N)�flaskr   r   �peeweer   �api.utilr   r   �orm.model.ucar.itinerarior   r   �INDEX�PATH�__name__�index_editar_itinerario�router   r   r   r   r   �<module>   s                                                                                          src/api/user/__pycache__/usuario_solicitar_viaje.cpython-36.pyc                                     0000644 0000060 0000060 00000001771 13573521156 024374  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
O��]  �               @   s�   d dl mZ d dl mZ d dlmZ d dlmZ d dlmZ d dlZd dlmZ d dl	m
Z
 d	Zd
Zeee e�Zejee dgd�eedd� ���ZdS )�    )�request)�	Blueprint)�update_user_conn)�require_api_token)�content_type_jsonN)�date)�ColaDePedidosZ	solicitarz/ucar/usuario/viaje/�POST)�methodsc              C   sP   t tj� �} tj� jd�| d< tjj� | d< d| d< tf | �}|j	�  ddd�S )	Nz%d/%m/%Y�fecha�horazno atendido�estado�okzSolicitud Agregada a la cola!)�status�message)
�dictr   �get_jsonr   �today�strftime�datetime�nowr   �save)�data�new� r   �S/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/usuario_solicitar_viaje.py�UsuarioSolicitarViaje   s    
r   )�flaskr   r   �api.utilr   r   r   r   r   �orm.model.ucar.cola_de_pedidosr   �INDEX�PATH�__name__�index_usuario_solicitar_viaje�router   r   r   r   r   �<module>   s          src/api/user/__pycache__/pasajero_verificar_viaje.cpython-36.pyc                                    0000644 0000060 0000060 00000006277 13573702551 024500  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
a��]T  �               @   s�   d dl mZ d dlZd dlmZ d dlmZ d dlmZ d dlm	Z	 d dl
mZ d dl
mZ d d	l
mZ d d
lmZ d dlmZ d dlZd dlZdZdZeee�Zejee dgd�eedd� ���Zdd� Zdd� Zdd� Zdd� Zdd� ZdS )�    )�loadsN)�request)�Select)�	Blueprint)�jsonify)�update_user_conn)�require_api_token)�content_type_json)�
Itinerario)�MatchZ	verificarz/ucar/pasajero/viaje/�POST)�methodsc              C   s&  d} dg}t |�}t| |�}d}� x�|D ]�}||k�r|| d jd�}|| d jd�}d|d |d |d |d d	�}tj� jtj|d
 ktj|d k@ tj|d k@ tj	|d k@ �}	|	j
� �rxN|	D ]@}
|
j}t|�|d< t� }|
j|_d|_d|_d|_|j�  |S W ndS |d }q(W d S )NgH1����L@g i��I9@�'-57.647976859562334,-25.285515826523806�&-57.63543469077945,-25.324514646565376r   �,�   �TRUE)�	respuesta�longitudInicio�latitudInicio�longitudFin�
latitudFinr   r   r   r   �idChoferz-57.647976859562334z-25.285515826523806ZatentidozAlgo salio mal�H1����L�� i��I9�)r   r   )r   r   )�genRtLst�minRoute�splitr
   �select�where�latitudOrig�longitudOrig�
latitudDst�longitudDst�exists�fk_persona_id�strr   �fk_chofer_id�latitud�longitud�estado�save)�posicion�coordenadas�rutas�Min�i�rutaZinicioVZfinVr   �query�resultr   �new� r5   �T/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/pasajero_verificar_viaje.py�BuscarChofer   s4    

 (

r7   c             C   s.   g }x$| D ]}|j t|d |d �� q
W |S )Nr   r   )�append�	getPuntos)r-   r.   Zparr5   r5   r6   r   9   s    
r   c             C   s�   t ttjd| |g�dd��}d}g }xv|d d d d d D ]Z}|j|d d	 d |d d	 d
 f� x.|d D ]"}|j|d	 d |d	 d
 f� qrW q>W |S )Nz;/opt/rh/httpd24/root/var/www/ucar/html/env2/scripts/curl.shzUTF-8)�encodingr   Z	matchingsZlegsZstepsZmaneuver�locationr   Zintersections)r   r&   �sub�check_outputr8   )ZinicioZfinZdiccionarior0   �puntos�step�intersectionr5   r5   r6   r9   ?   s    &&r9   c             C   sX   g }x|D ]}|j t| |�� q
W t|�}d}x$|D ]}||krH|| S |d }q4W d S )Nr   r   )r8   �dist�min)r,   r>   �
distancias�puntor/   r0   �	distanciar5   r5   r6   �rtCmpI   s    

rF   c             C   s2   t j| d |d  d | d |d  d  �}|S )Nr   �   r   )�math�sqrt)�a�bZdistancer5   r5   r6   rA   T   s    .rA   c       	      C   sz   g }x|D ]}|j t| |�� q
W g }x|D ]}|j t| |�� q,W t|�}d}x$|D ]}||krj|| S |d }qVW d S )Nr   r   )r8   rF   rA   rB   )	r,   r.   r>   r1   rC   rD   r/   r0   rE   r5   r5   r6   r   X   s    


r   )�jsonr   �
subprocessr<   �flaskr   �peeweer   r   r   �api.utilr   r   r	   �orm.model.ucar.itinerarior
   �orm.model.ucar.matchr   �timerH   �INDEX�PATH�__name__�index_pasajero_verificar_viaje�router7   r   r9   rF   rA   r   r5   r5   r5   r6   �<module>   s.   
#
                                                                                                                                                                                                                                                                                                                                 src/api/user/__pycache__/pasajero_solicitar_viaje.cpython-36.pyc                                    0000644 0000060 0000060 00000002312 13573537636 024513  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
M��]�  �               @   s�   d dl mZ d dl mZ d dlmZ d dlmZ d dlmZ d dlZd dlmZ d dl	m
Z
 d	Zd
Zeee e�Zejee dgd�eedd� ���ZdS )�    )�request)�	Blueprint)�update_user_conn)�require_api_token)�content_type_jsonN)�date)�ColaDePedidosZ	solicitarz/ucar/pasajero/viaje/�POST)�methodsc           
   C   s�   y�t tj� �} tj� jtj| d ktjdk@ �}|j� rBddd�S t	j
� jd�| d< tjj� | d< d| d	< tf | �}|j�  d
dd�S W n   ddd�S d S )N�fk_persona_idzno atendido�errorzYa tiene un pedido de viaje!)�status�messagez%d/%m/%Y�fecha�hora�estado�okzSolicitud Agregada a la cola!zNo existe el usuario!)�dictr   �get_jsonr   �select�wherer   r   �existsr   �today�strftime�datetime�now�save)�data�query�new� r    �T/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/pasajero_solicitar_viaje.py�PasajeroSolicitarViaje   s    "

r"   )�flaskr   r   �api.utilr   r   r   r   r   �orm.model.ucar.cola_de_pedidosr   �INDEX�PATH�__name__�index_pasajero_solicitar_viaje�router"   r    r    r    r!   �<module>   s                                                                                                                                                                                                                                                                                                                         src/api/user/__pycache__/listar_vehiculo.cpython-36.pyc                                             0000644 0000060 0000060 00000001755 13573630251 022651  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
�0�]F  �               @   s�   d dl mZ d dl mZ d dl mZ d dlmZ d dlmZ d dlmZ d dlm	Z	 dZ
d	Zeee
 e�Zejee
 d
gd�edd� ��ZdS )�    )�jsonify)�request)�	Blueprint)�update_user_conn)�require_api_token)�content_type_json)�Vehiculozlistar/z/ucar/vehiculo/�GET)�methodsc           
   C   sv   g } yVt j� jt jtjjd�k�jd�}|j� rXx|j	� D ]}| j
|� q:W t| d �S W n   ddd�S ddd�S )N�id�   r   �errorzError de conexion!)�status�messagezEl usuario no existe)r   �select�where�	fkPersonar   �args�get�limit�exists�dicts�appendr   )�data�query�row� r   �K/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/listar_vehiculo.py�vehiculo_listar   s    "
r   N)�flaskr   r   r   �api.utilr   r   r   �orm.model.ucar.vehiculor   �INDEX�PATH�__name__�index_vehiculo_listar�router   r   r   r   r   �<module>   s                      src/api/user/__pycache__/choferesCercanos.cpython-36.pyc                                            0000644 0000060 0000060 00000005061 13573656306 022734  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
�\�]
  �               @   s�   d dl mZ d dlZd dlmZ d dlmZ d dlmZ d dlm	Z	 d dl
mZ d dl
mZ d d	l
mZ d d
lmZ d dlZd dlZdZdZeee e�Zejee dgd�eedd� ���Zdd� Zdd� Zdd� Zdd� Zdd� ZdS )�    )�loadsN)�request)�Select)�	Blueprint)�jsonify)�update_user_conn)�require_api_token)�content_type_json)�Persona�	verificarz/ucar/chofer/viaje/�POST)�methodsc              C   s\   d
} dg}t |�}t| |�}d}x6|D ].}||krLt| d �t| d �d�S |d }q&W d S )NgH1����L@g i��I9@�'-57.647976859562334,-25.285515826523806�&-57.63543469077945,-25.324514646565376r   �   )�longitud�latitud�H1����L�� i��I9�)r   r   )r   r   )�genRtLst�minRoute�str)�posicion�coordenadas�rutas�Min�i�ruta� r   �L/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/choferesCercanos.py�BuscarChofer   s    

r    c             C   s.   g }x$| D ]}|j t|d |d �� q
W |S )Nr   r   )�append�	getPuntos)r   r   Zparr   r   r   r   "   s    
r   c             C   s�   t ttjd| |g�dd��}d}g }xv|d d d d d D ]Z}|j|d d	 d |d d	 d
 f� x.|d D ]"}|j|d	 d |d	 d
 f� qrW q>W |S )Nz;/opt/rh/httpd24/root/var/www/ucar/html/env2/scripts/curl.shzUTF-8)�encodingr   Z	matchingsZlegsZstepsZmaneuver�locationr   Zintersections)r   r   �sub�check_outputr!   )ZinicioZfinZdiccionarior   �puntos�step�intersectionr   r   r   r"   (   s    &&r"   c             C   sX   g }x|D ]}|j t| |�� q
W t|�}d}x$|D ]}||krH|| S |d }q4W d S )Nr   r   )r!   �dist�min)r   r'   �
distancias�puntor   r   �	distanciar   r   r   �rtCmp2   s    

r/   c             C   s2   t j| d |d  d | d |d  d  �}|S )Nr   �   r   )�math�sqrt)�a�bZdistancer   r   r   r*   =   s    .r*   c       	      C   sz   g }x|D ]}|j t| |�� q
W g }x|D ]}|j t| |�� q,W t|�}d}x$|D ]}||krj|| S |d }qVW d S )Nr   r   )r!   r/   r*   r+   )	r   r   r'   r   r,   r-   r   r   r.   r   r   r   r   A   s    


r   )�jsonr   �
subprocessr%   �flaskr   �peeweer   r   r   �api.utilr   r   r	   �orm.model.ucar.personar
   �timer1   �INDEX�PATH�__name__�index_chofer_verificar_viaje�router    r   r"   r/   r*   r   r   r   r   r   �<module>   s,   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                               src/api/user/__pycache__/conductor_viajes.cpython-36.pyc                                            0000644 0000060 0000060 00000001774 13573705532 023024  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
��]r  �               @   s�   d dl mZ d dl mZ d dl mZ d dlmZ d dlmZ d dlmZ d dlm	Z	 dZ
d	Zeee
 e�Zejee
 d
gd�eedd� ���ZdS )�    )�request)�	Blueprint)�jsonify)�update_user_conn)�require_api_token)�content_type_json)�Match�listarz/ucar/conductor/pedidos/�POST)�methodsc           
   C   sh   yLt tj� �} tj� jtj| d ktjdk@ �jd�}|j	� rJt
|d �S W n   ddd�S ddd�S )	N�	fk_choferzno atentido�   r   �errorzerror de conexion)�status�messagezusuario no encontrado)�dictr   �get_jsonr   �select�wherer   �estado�limit�existsr   )�data�query� r   �L/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/user/conductor_viajes.py�conductor_listar_viajes   s    (
r   N)�flaskr   r   r   �api.utilr   r   r   �orm.model.ucar.matchr   �INDEX�PATH�__name__�index_conductor_listar_viajes�router   r   r   r   r   �<module>   s       src/api/user/listar.py                                                                              0000775 0000000 0001757 00000001147 13564701404 015004  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import jsonify
from flask import Blueprint
from api.util import require_api_token
from orm.model.ucar.persona import Persona

INDEX = 'listar/'
PATH = '/ucar/usuario/'
index_usuario_listar = Blueprint(INDEX, __name__)

@index_usuario_listar.route(PATH + INDEX, methods=['GET'])
@require_api_token
def usuario_listar():
    data = []
    try:
        query = Persona.select()
        for result in query.dicts():
            data.append(result)
    except:
        return {"status":"error","message":"Error de conexion!"}
    return jsonify(data)
                                                                                                                                                                                                                                                                                                                                                                                                                         src/api/user/identificar.py                                                                         0000775 0000000 0001757 00000001743 13573520712 015772  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from peewee import Select
from flask import Blueprint
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.persona import Persona

INDEX = 'identificar'
PATH = '/ucar/usuario/'
index_usuario_identificar = Blueprint(INDEX, __name__)

@index_usuario_identificar.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def usuario_identificar():
	query = Select(None)
	try:
		data = dict(request.get_json())
		query = Persona.select(Persona.id, Persona.email, Persona.password)\
			.where((Persona.email == data['email']) & (Persona.password == data['password']))
		if query.exists():
			update_user_conn([query[0].id])
			return {'status':'ok','message': f'{query[0].id}'}
	except:
		return {"status":"error","message":"pg select"}
	return {'status':'error','message':'El usuario no se encuentra registrado!'}
                             src/api/user/recuperar_cuenta.py                                                                    0000775 0000000 0001757 00000002532 13564713631 017041  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              from re import search
from uuid import uuid1
from hashlib import md5
from flask import request
from flask import Blueprint
from api.util import ucar_sendemail
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.persona import Persona

INDEX = 'recuperar/'
PATH = '/ucar/usuario/'
index_recuperar_cuenta = Blueprint(INDEX, __name__)

@require_api_token
@content_type_json
@index_recuperar_cuenta.route(PATH + INDEX, methods=['GET'])
def usuario_recuperar_cuenta():
    data = request.args.get('email')
    if data:
        query = Persona.select(Persona.password).where(Persona.email == data)
        if query.exists():
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if search(regex, data):
                pw = str(uuid1())[0:5]
                query = (Persona.update({Persona.password: md5(pw.encode()).hexdigest()}).where(Persona.email == data).execute())
                if query:
                    ucar_sendemail(data, f'password {pw}')
                    return {'status':'ok', 'message' : 'email enviado'}
                return {'status':'error', 'message' : 'error al actualizar'}
            return {'status':'error', 'message' : 'email no valido'}
        return {'status':'error', 'message' : 'email no encontrado'}
    return {'status':'error', 'message' : 'falta parametro'}                                                                                                                                                                      src/api/user/registrar_vehiculo.py                                                                  0000775 0000000 0001757 00000001772 13573622441 017415  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.vehiculo import Vehiculo

INDEX = 'registrar'
PATH = '/ucar/vehiculo/'
index_vehiculo_registrar = Blueprint(PATH + INDEX, __name__)

@index_vehiculo_registrar.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def vehiculo_registrar():
    try:
        data = dict(request.get_json())
        query = Vehiculo.select().where(Vehiculo.fkPersona == data['fkPersona']).limit(1)
        if query.exists():
            Vehiculo.update(**data).execute()
        else:
            Vehiculo(**data).save()
        update_user_conn([data['fkPersona']])
        return {'status':'ok', 'message':'Vehiculo registrado'}
    except:
        return {'status':'error', 'message':'Error al guardar'}
    return {'status':'ok', 'message':'Usuario no encontrado'}      src/api/user/get_user_by_email.py                                                                   0000775 0000000 0001757 00000001372 13573302276 017170  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import jsonify
from flask import Blueprint
from api.util import require_api_token
from orm.model.ucar.persona import Persona
from peewee import Select
INDEX = 'datos/'
PATH = '/ucar/usuario/'
index_usuario_datos = Blueprint(INDEX, __name__)

@index_usuario_datos.route(PATH + INDEX, methods=['GET'])
@require_api_token
def usuario_datos():
	data = []
	try:
		query = Persona.select().where(Persona.email == request.args.get("email"))
		if query:
			for result in query.dicts():
				data.append(result)
		else:
			return {"status":"error","message":"Esa Persona no existe!"}
	except:
		return {"status":"error","message":"Error de conexion!"}
	return jsonify(data[0])
                                                                                                                                                                                                                                                                      src/api/user/editar_itinerario.py                                                                   0000775 0000000 0001757 00000001435 13573337244 017212  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from peewee import Select
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.itinerario import Itinerario
from api.util import update_user_conn

INDEX = 'editar'
PATH = '/ucar/itinerario/'
index_editar_itinerario = Blueprint( PATH + INDEX, __name__)

@index_editar_itinerario.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def editar_itinerario():
	try:	
		data = dict(request.get_json())
		new = Itinerario(**data)
		update_user_conn([data['fk_persona']])
		new.save()
		return {"status" : "ok", "message" : "Itinerario Guardado!"}
	except:
		return {"status" : "error", "message" : "No existe el usuario!"}
                                                                                                                                                                                                                                   src/api/user/pasajero_verificar_viaje.pyM                                                           0000775 0000000 0001757 00000003522 13573602464 020644  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from peewee import Select
from flask import jsonify
from flask import Blueprint
import datetime 
from datetime import date 
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.persona import Persona
from orm.model.ucar.cola_de_pedidos import ColaDePedidos
from orm.model.ucar.viaje import Viaje
from orm.model.ucar.itinerario import Itinerario
import time

dias["lunes"] = 0
dias["martes"] = 1
dias["miercoles"] = 2
dias["jueves"] = 3
dias["viernes"] = 4 
dias["sabado"] = 5
dias["domingo"] = 6

INDEX = 'verificar'
PATH = '/ucar/pasajero/viaje/'
index_pasajero_verificar_viaje = Blueprint(INDEX, __name__)

@index_pasajero_verificar_viaje.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def verificar_viaje():
	try:
#Aca se recibe el id y se controla si hay algun viaje para ese pasajero, de ser asi
# se le responde true y la informacion del viaje, si no se le responde false y el resto vacio
		data = dict(request.get_json())
		respuesta["respuesta"] = "FALSE"
		respuesta["message"] = "Viaje Expirado!"
		i = 0
		queryList=[]
		while i < 59 :
			query = ColaDePedidos.select.where(
				(ColaDePedidos.fk_persona_id==data["id"]) & 
				(ColaDePedidos.estado=="no atendido") & 
				(ColaDePedidos.fecha==datetime.datetime.now()) &
				((ColaDePedidos.hora.to_timestamp()) < (datetime.datetime.now().timestamp() - 60))
				)
			if query.exists():
				for result in query.dicts():
					queryList.append(result)
				queryDict = jsonify(queryList)	
				respuesta["idChofer"] = queryDict["fk_chofer_id"]
				query2 =
				
	
				return respuesta 
			time.sleep(1)
			i=i+1
		return respuesta	
	except :
		return {"status":"error","message":"El usuario no se encuentra registrado!"}
                                                                                                                                                                              src/api/user/listar_reservas.py                                                                     0000775 0000000 0001757 00000001341 13565033436 016716  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import jsonify
from flask import Blueprint
from peewee import Select
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.viaje_reservado import ViajeReservado

INDEX = 'listar/'
PATH = '/ucar/reserva/'
index_reserva_listar = Blueprint(PATH + INDEX, __name__)

@index_reserva_listar.route(PATH + INDEX, methods=['GET'])
@require_api_token
def reserva_listar():
	try:	
		respuesta = []
		query = ViajeReservado.select(ViajeReservado.id)	
		for result in query.dicts():
			respuesta.append(result)
		return jsonify(respuesta)
	except:
		return {"status" : "error", "message" : "Error de conexion!"}
                                                                                                                                                                                                                                                                                               src/api/user/listar_vehiculo.py                                                                     0000664 0001752 0001752 00000001506 13573630235 022427  0                                                                                                    ustar   rodrigo.villalba                rodrigo.villalba                                                                                                                                                                                                       #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import jsonify
from flask import request
from flask import Blueprint
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.vehiculo import Vehiculo

INDEX = 'listar/'
PATH = '/ucar/vehiculo/'
index_vehiculo_listar = Blueprint(PATH + INDEX, __name__)

@index_vehiculo_listar.route(PATH + INDEX, methods=['GET'])
@require_api_token
def vehiculo_listar():
	data = []
	try:
		query = Vehiculo.select().where(Vehiculo.fkPersona == request.args.get("id")).limit(1)
		if query.exists():
			for row in query.dicts():
				data.append(row)
			return jsonify(data[0]) 
	except:
		return {"status":"error","message":"Error de conexion!"}
	return {"status":"error","message":"El usuario no existe"}
	                                                                                                                                                                                          src/api/user/pasajero_verificar_viaje.py.Orig                                                       0000775 0000000 0001757 00000001607 13573526110 021421  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from peewee import Select
from flask import Blueprint
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.persona import Persona
import time

INDEX = 'verificar'
PATH = '/ucar/pasajero/viaje/'
index_pasajero_verificar_viaje = Blueprint(INDEX, __name__)

@index_pasajero_verificar_viaje.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def verificar_viaje():
	try:
#Aca se recibe el id y se controla si hay algun viaje para ese pasajero, de ser asi
# se le responde true y la informacion del viaje, si no se le responde false y el resto vacio
		time.sleep(30)
		return {"respuesta":"TRUE","message":"Viaje Encontrado!"}
	except :
		return {"status":"error","message":"El usuario no se encuentra registrado!"}
                                                                                                                         src/api/user/registrar.py                                                                           0000775 0000000 0001757 00000001612 13572677725 015526  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.persona import Persona
from orm.model.client.cliente import Cliente

INDEX = 'registrar'
PATH = '/ucar/usuario/'
index_usuario_registrar = Blueprint(INDEX, __name__)

@index_usuario_registrar.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def usuario_registrar():
	try:
		data = dict(request.get_json())
		query = Cliente.select().where(Cliente.email == data['email'])
		if query.exists():
			new = Persona(**data)
			new.save()
			return {"status":"ok","message":"usuario creado"}
		return {'status':'error', 'message':'Email no admitido!'}
	except:
		return {'status':'error','message':'Error de conexion!'}
	return {'status':'error','message':'usuario no creado'}
                                                                                                                      src/api/user/actualizar_perfil.py                                                                   0000775 0000000 0001757 00000002514 13573722041 017205  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
#from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.persona import Persona

INDEX = 'actualizar'
PATH = '/ucar/perfil/'
index_perfil_actualizar = Blueprint(INDEX, __name__)

@index_perfil_actualizar.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def actualizar_perfil():
	try:
		data = dict(request.get_json())
		query = Persona.select().where(Persona.id == data['id'])
		if query.exists():
			#update_user_conn([data['userId']])
			if data['password'] == "":
				nrows = (Persona.update(
						nombre=data['nombre'],
						apellido=data['apellido'],
						email=data['email'],
						institucion=data['institucion']).where(Persona.id == data['id']).execute())
			else:			
				nrows = (Persona.update(
						nombre=data['nombre'],
						apellido=data['apellido'],
						email=data['email'],
						institucion=data['institucion'],
						password=data['password']).where(Persona.id == data['id']).execute())	
			#update_user_conn([data['id']])
			return {"status":"ok","message":"Perfil Modificado!"}
		return {'status':'error', 'message':'Esa persona no existe!'}
	except:
		return {'status':'error','message':'Error de conexion!'}
                                                                                                                                                                                    src/api/user/subir_foto.py                                                                          0000775 0000000 0001757 00000002532 13573275567 015700  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from peewee import Select
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.persona import Persona
from api.util import update_user_conn
import subprocess as sub
INDEX = 'subir'
PATH = '/foto/'
index_foto_subir = Blueprint( PATH + INDEX, __name__)

@index_foto_subir.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def SubirFoto():
	try:	
		data = dict(request.get_json())
		query = Persona.select().where(Persona.id == data['userId'])
		if query.exists():
			update_user_conn([data['userId']])
			foto = open("/opt/rh/httpd24/root/var/www/ucar/html/env2/fotos/aux","w")
			foto.write(data['imgData'])
			foto.close()
			sub.run(["/opt/rh/httpd24/root/var/www/ucar/html/env2/scripts/decode.sh","/opt/rh/httpd24/root/var/www/ucar/html/env2/fotos/aux","/opt/rh/httpd24/root/var/www/ucar/html/env2/fotos/" + str(data['userId'])])
			sub.run(["/opt/rh/httpd24/root/var/www/ucar/html/env2/scripts/rename.sh","/opt/rh/httpd24/root/var/www/ucar/html/env2/fotos/" + str(data['userId'])])
			return {"status" : "ok", "message" : "Foto Subida!"}
		else:	
			return {"status" : "error", "message" : "Esa persona no existe!"}
	except:
		return {"status" : "error", "message" : "Error Interno"}
                                                                                                                                                                      src/api/user/pasajero_solicitar_viaje.py                                                            0000775 0000000 0001757 00000002246 13573537515 020554  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
import datetime
from datetime import date
from orm.model.ucar.cola_de_pedidos import ColaDePedidos
INDEX = 'solicitar'
PATH = '/ucar/pasajero/viaje/'
index_pasajero_solicitar_viaje = Blueprint(PATH + INDEX, __name__)

@index_pasajero_solicitar_viaje.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def PasajeroSolicitarViaje():
	try:    
		data = dict(request.get_json())
		query = ColaDePedidos.select().where((ColaDePedidos.fk_persona_id==data["fk_persona_id"]) & (ColaDePedidos.estado=="no atendido") )
		if query.exists() :
			return {"status" : "error", "message" :"Ya tiene un pedido de viaje!"}
		else :
			data["fecha"] = date.today().strftime("%d/%m/%Y")
			data["hora"] = datetime.datetime.now()
			data["estado"] = "no atendido"
			new = ColaDePedidos(**data)
			new.save()
			return {"status" : "ok", "message" : "Solicitud Agregada a la cola!"}
	except:
		return {"status" : "error", "message" : "No existe el usuario!"}
                                                                                                                                                                                                                                                                                                                                                          src/api/user/conductor_viajes.py                                                                    0000664 0001752 0001752 00000001562 13573704750 022602  0                                                                                                    ustar   rodrigo.villalba                rodrigo.villalba                                                                                                                                                                                                       #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from flask import jsonify
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.match import Match

INDEX = 'listar'
PATH = '/ucar/conductor/pedidos/'
index_conductor_listar_viajes = Blueprint(PATH + INDEX, __name__)

@index_conductor_listar_viajes.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def conductor_listar_viajes():
	try:
		data = dict(request.get_json())
		query = Match.select().where((Match.fk_chofer == data['fk_chofer']) & (Match.estado == 'no atentido')).limit(1)
		if query.exists():
			return jsonify(query[0])
	except:
		return {'status':'error', 'message':'error de conexion'}
	return {'status':'error', 'message':'usuario no encontrado'}                                                                                                                                              src/api/user/pasajero_verificar_viaje.py                                                            0000755 0001754 0001754 00000007124 13573702541 024630  0                                                                                                    ustar   cristobal.barreto               cristobal.barreto                                                                                                                                                                                                      #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from json import loads
import subprocess as sub
from flask import request
from peewee import Select
from flask import Blueprint
from flask import jsonify
from api.util import update_user_conn
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.itinerario import Itinerario
from orm.model.ucar.match import Match 
import time
import math

INDEX = 'verificar'
PATH = '/ucar/pasajero/viaje/'
index_pasajero_verificar_viaje = Blueprint(INDEX, __name__)

@index_pasajero_verificar_viaje.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def BuscarChofer():
	#Posicion del Pasajero 
	posicion=(-57.647976859562334,-25.285515826523806) #TODO conseguir de la base de datos
	#Lista de Choferes Online
	coordenadas=[("-57.647976859562334,-25.285515826523806","-57.63543469077945,-25.324514646565376")] #TODO conseguir de la base de datos
	rutas = genRtLst(coordenadas)
	Min = minRoute(posicion,rutas)
	i=0
	for ruta in rutas:
		if ruta == Min:
			inicioV=coordenadas[i][0].split(",")
			finV=coordenadas[i][1].split(",")
			respuesta ={ "respuesta":"TRUE","longitudInicio":inicioV[1],"latitudInicio":inicioV[0],"longitudFin":finV[1],"latitudFin":finV[0]} 
			query = Itinerario.select().where(
							(Itinerario.latitudOrig == respuesta["latitudInicio"]) &
							(Itinerario.longitudOrig == respuesta["longitudInicio"]) &
							(Itinerario.latitudDst == respuesta["latitudFin"]) &
							(Itinerario.longitudDst == respuesta["longitudFin"]) 
							)
			if query.exists():
				for result in query:
					idChofer = result.fk_persona_id
					respuesta["idChofer"] = str(idChofer)
					#match = { "fk_chofer_id" : idChofer , "latitud" : "-57.647976859562334" , "longitud" : "-25.285515826523806"  , "estado" : "atentido" }
					new = Match()
					new.fk_chofer_id = result.fk_persona_id
					new.latitud = "-57.647976859562334"
					new.longitud = "-25.285515826523806"
					new.estado = "atentido"
					new.save()
					return respuesta
			else:
				return "Algo salio mal"
		i=i+1
def genRtLst(coordenadas):
    rutas=[]
    for par in coordenadas:
        rutas.append(getPuntos(par[0],par[1]))
    return rutas
#Retorna los puntos que conforman una ruta a travez del punto inicial y el punto final
def getPuntos(inicio,fin):
    diccionario=loads(str(sub.check_output(["/opt/rh/httpd24/root/var/www/ucar/html/env2/scripts/curl.sh",inicio,fin]),encoding="UTF-8"))
    i = 0
    puntos = []
    for step in diccionario["matchings"][0]["legs"][0]["steps"]:
        puntos.append((step["maneuver"]["location"][0],step["maneuver"]["location"][1]))
        for intersection in step["intersections"]:
            puntos.append((intersection["location"][0],intersection["location"][1]))
    return puntos
#Retorna el punto mas cercano a la posicion dada (un punto a una ruta)
def rtCmp(posicion,puntos):
    distancias=[]
    for punto in puntos:
       distancias.append(dist(posicion,punto)) 
    Min =  min(distancias)
    i = 0
    for distancia in distancias:
        if distancia == Min:
            return puntos[i]
        i = i + 1
#Distancia de un punto a, a un punto b
def dist( a , b ):
    distance = math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    return distance
#Retorna la ruta mas cercana
def minRoute(posicion,rutas):
    puntos = []
    for ruta in rutas:
        puntos.append(rtCmp(posicion,ruta))
    distancias=[]
    for punto in puntos:
       distancias.append(dist(posicion,punto)) 
    Min =  min(distancias)
    i = 0
    for distancia in distancias:
        if distancia == Min:
            return rutas[i]
        i = i + 1
                                                                                                                                                                                                                                                                                                                                                                                                                                            src/api/user/crear_reserva.py                                                                       0000775 0000000 0001757 00000001506 13573337374 016343  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from peewee import Select
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.viaje_reservado import ViajeReservado
from orm.model.ucar.persona import Persona
from api.util import update_user_conn

INDEX = 'reservar'
PATH = '/ucar/reserva/'
index_reserva_reservar = Blueprint(INDEX, __name__)

@index_reserva_reservar.route(PATH + INDEX, methods=['POST'])
@require_api_token
@content_type_json
def viaje_reservar():
	try:	
		data = dict(request.get_json())
		new = ViajeReservado(**data)
		update_user_conn([data['fk_persona_id']])
		new.save()
		return {"status" : "ok", "message" : "Viaje Reservado!"}
	except:
		return {"status" : "error", "message" : "No existe el usuario!"}
                                                                                                                                                                                          src/api/user/eliminar_reserva.py                                                                    0000775 0000000 0001757 00000001416 13573301642 017034  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import request
from flask import Blueprint
from peewee import Select
from api.util import require_api_token
from api.util import content_type_json
from orm.model.ucar.viaje_reservado import ViajeReservado
INDEX = 'cancelar/'
PATH = '/ucar/viaje/'
index_reserva_cancelar = Blueprint(INDEX, __name__)

@index_reserva_cancelar.route(PATH + INDEX, methods=['GET'])
@require_api_token
def viaje_reservar():
	try:	
		if  ViajeReservado.delete().where(ViajeReservado.id == request.args.get("id_viaje") ).execute():
			return { "status" : "ok", "message" : "Viaje Cancelado!"}
		else :
			return { "status" : "error", "message" : "El viaje no existe!"}
	except:
		return { "status" : "error", "message" : "Bad Request!"}
                                                                                                                                                                                                                                                  src/api/__init__.py                                                                                 0000775 0000060 0001757 00000000000 13563664232 014524  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/api/__pycache__/                                                                                0000775 0000060 0001757 00000000000 13573623771 014636  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/api/__pycache__/__init__.cpython-36.pyc                                                         0000775 0000060 0001757 00000000222 13563664415 021021  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
�h�]    �               @   s   d S )N� r   r   r   �?/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                                  src/api/__pycache__/util.cpython-36.pyc                                                             0000644 0000060 0000060 00000004152 13573623771 017457  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
��]  �               @   sP   d dl mZ d dl mZ d dlmZ dZdZdd� Zdd	� Zd
d� Z	dd� Z
dS )�    )�Flask)�request)�wrapsZ*JbslEJwMnd7fcfrtqcyT_O4MgTWQ1bau1XtdGhWGXwZyNPnZACTchuDwdHagc                s   t � �� fdd��}|S )Nc                 sT   t jjd�rJt jjd�rJt jjd�}t jjd�}|tkrJ|tkrJ� | |�S ddd�S )NzX-Auth-Tokenz	X-User-Id�errorz!You must be logged in to do this.)�status�message)r   �headers�has_key�get�UCAR_API_USER_ID�UCAR_API_AUTH_TOKEN)�args�kwargs�token�user)�func� �;/opt/rh/httpd24/root/var/www/ucar/html/env2/src/api/util.py�check_token
   s    
z&require_api_token.<locals>.check_token)r   )r   r   r   )r   r   �require_api_token	   s    r   c                s   t � �� fdd��}|S )Nc                 s   t jr� | |�S ddd�S )Nr   zContent-Type: application/json)r   r   )r   �is_json)r   r   )r   r   r   �check   s    
z content_type_json.<locals>.check)r   )r   r   r   )r   r   �content_type_json   s    r   c             C   s�   ddl m} ddlm} ddlm} |� }d|d< | |d< d|d	< |j||d
�� |ddd�}|j�  |j|d d� |j	|d |d |j
� � |j�  d S )Nr   )�SMTP)�MIMEMultipart)�MIMETextzso2tphids2018@gmail.comZFromZTozucar: recuperar cuentaZSubject�plainzsmtp.gmail.comiK  )�host�portZny4Rla7h0t3P)Zsmtplibr   Zemail.mime.multipartr   Zemail.mime.textr   �attachZstarttls�loginZsendmail�	as_string�quit)�tor   r   r   r   �msg�serverr   r   r   �ucar_sendemail   s    r&   c              G   sT   ddl m } ddlm} x6| D ].}|j� jd�}|j|d�j|j|k�j�  qW d S )Nr   )�datetime)�Personaz%d-%m-%Y %H:%M:%S)�conexion)	r'   �orm.model.ucar.personar(   �now�strftime�update�where�id�execute)Zuser_idr'   r(   r/   r+   r   r   r   �update_user_conn-   s
    
r1   N)�flaskr   r   �	functoolsr   r   r   r   r   r&   r1   r   r   r   r   �<module>   s                                                                                                                                                                                                                                                                                                                                                                                                                         src/api/util.py                                                                                     0000775 0000060 0001757 00000003406 13573615673 013765  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import Flask
from flask import request
from functools import wraps

UCAR_API_AUTH_TOKEN = 'JbslEJwMnd7fcfrtqcyT_O4MgTWQ1bau1XtdGhWGXw'
UCAR_API_USER_ID = 'yNPnZACTchuDwdHag'

def require_api_token(func):
    @wraps(func)
    def check_token(*args, **kwargs):
        if request.headers.has_key('X-Auth-Token') and request.headers.has_key('X-User-Id'):
            token = request.headers.get('X-Auth-Token')
            user = request.headers.get('X-User-Id')
            if user in UCAR_API_USER_ID and token in UCAR_API_AUTH_TOKEN:
                return func(*args, **kwargs)
        return {"status":"error","message":"You must be logged in to do this."}
    return check_token

def content_type_json(func):
    @wraps(func)
    def check(*args, **kwargs):
        if request.is_json:
            return func(*args, **kwargs)
        return {"status": "error","message":"Content-Type: application/json"}
    return check

def ucar_sendemail(to, message):
    from smtplib import SMTP
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart()
    msg['From'] = 'so2tphids2018@gmail.com'
    msg['To'] = to
    msg['Subject'] = "ucar: recuperar cuenta"
    msg.attach(MIMEText(message, 'plain'))

    server = SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(msg['From'], 'ny4Rla7h0t3P')
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

def update_user_conn(*user_id):
    from datetime import datetime
    from orm.model.ucar.persona import Persona

    for id in user_id:
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        Persona.update(conexion = now).where(Persona.id == id).execute()

                                                                                                                                                                                                                                                          src/index.py                                                                                        0000775 0000060 0001757 00000004644 13573721607 013346  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from sys import argv
from flask import Flask
from orm.create.ucar import create_tables
from api.user.registrar import index_usuario_registrar
from api.user.identificar import index_usuario_identificar
from api.user.listar import index_usuario_listar
from api.user.crear_reserva import index_reserva_reservar
from api.user.eliminar_reserva import index_reserva_cancelar
from api.user.listar_reservas import index_reserva_listar
from api.user.subir_foto import index_foto_subir
from api.user.get_user_by_email import index_usuario_datos
from api.user.recuperar_cuenta import index_recuperar_cuenta
from api.user.actualizar_perfil import index_perfil_actualizar
from api.user.registrar_vehiculo import index_vehiculo_registrar
from api.user.editar_itinerario import index_editar_itinerario 
from api.user.pasajero_solicitar_viaje import index_pasajero_solicitar_viaje
from api.user.pasajero_verificar_viaje import index_pasajero_verificar_viaje
from api.user.listar_vehiculo import index_vehiculo_listar
from api.user.conductor_viajes import index_conductor_listar_viajes
#from orm.model.ucar.itinerario import Itinerario

app = Flask(__name__)
app.register_blueprint(index_usuario_registrar)
app.register_blueprint(index_usuario_identificar)
app.register_blueprint(index_usuario_listar)
app.register_blueprint(index_reserva_reservar)
app.register_blueprint(index_reserva_cancelar)
app.register_blueprint(index_reserva_listar)
app.register_blueprint(index_foto_subir)
app.register_blueprint(index_usuario_datos)
app.register_blueprint(index_recuperar_cuenta)
app.register_blueprint(index_perfil_actualizar)
app.register_blueprint(index_vehiculo_registrar)
app.register_blueprint(index_editar_itinerario)
app.register_blueprint(index_pasajero_solicitar_viaje)
app.register_blueprint(index_pasajero_verificar_viaje)
app.register_blueprint(index_vehiculo_listar)
app.register_blueprint(index_conductor_listar_viajes)

if __name__ == '__main__':
    if len(argv) == 2:
        if argv[1] == '--init-db':
            create_tables()

    '''
    new = Itinerario()
    new.latitudOrig = '-57.647976859562334'
    new.longitudOrig = '-25.285515826523806'
    new.latitudDst = '-57.63543469077945'
    new.longitudDst  = '-25.324514646565376'
    new.dia = 'lunes'
    new.fecha = '10-12-2019'
    new.horaEntrada = '10:01'
    new.horaSalida = '12:01'
    new.fk_persona = '2'
    new.save()
    '''
    
    app.run()
                                                                                            src/orm/                                                                                            0000775 0000060 0001757 00000000000 13563664116 012447  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/conn/                                                                                       0000775 0000060 0001757 00000000000 13563664116 013404  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/conn/conn_ucar.json                                                                         0000775 0000060 0001757 00000000170 13563661372 016250  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              {
    "database":"ucar",
    "user":"ucar_api",
    "password":"#7h3m4573r!.",
    "host":"127.0.0.1",
    "port":5432
}                                                                                                                                                                                                                                                                                                                                                                                                        src/orm/conn/__init__.py                                                                            0000775 0000060 0001757 00000000000 13563661372 015507  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/conn/base.py                                                                                0000775 0000060 0001757 00000000211 13563661372 014666  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              from peewee import Model
from orm.conn.db import pg_conn

class BaseModel(Model):
    class Meta:
        database = pg_conn('conn_ucar')                                                                                                                                                                                                                                                                                                                                                                                       src/orm/conn/db.py                                                                                  0000775 0000060 0001757 00000002014 13563663653 014350  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from os import path
from json import load
from peewee import PostgresqlDatabase

# función		:   pg_conn()
# parametros	:	archivo de conexión
# utilidad		: 	lee el archivo de configuracíon de la bd la
#                   cual contiene los parametros de conexión,
#                   utiliza los mismos para definir la conexión.
# retorno		:   instancia de conexión a la base de datos
# detalles		: 	ninguno
def pg_conn(jsonfile):
    # obtiene la dirección del directorio del script actual
    current_file_dir = path.dirname(__file__)
    # concatenación del nombre del archivo cfg
    # y su ubicación (directorio actual)
    cfg = path.join(current_file_dir, jsonfile + '.json')
    # manejo de archivos
    with open(cfg) as f:
        # se lee todo el contenido
        # del archivo json, se almacena
        # en data en forma de diccionario {clave:valor}
        data = dict(load(f))
    # retorno de instancia de conexión
    return PostgresqlDatabase(**data)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    src/orm/conn/__pycache__/                                                                           0000775 0000060 0001757 00000000000 13563664116 015614  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/conn/__pycache__/__init__.cpython-36.pyc                                                    0000775 0000060 0001757 00000000227 13563664116 022005  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
�b�]    �               @   s   d S )N� r   r   r   �D/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/conn/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                             src/orm/conn/__pycache__/db.cpython-36.pyc                                                          0000775 0000060 0001757 00000001013 13563664116 020625  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
�g�]  �               @   s0   d dl mZ d dlmZ d dlmZ dd� ZdS )�    )�path)�load)�PostgresqlDatabasec          
   C   sD   t jt�}t j|| d �}t|��}tt|��}W d Q R X tf |�S )Nz.json)r   �dirname�__file__�join�open�dictr   r   )ZjsonfileZcurrent_file_dirZcfg�f�data� r   �>/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/conn/db.py�pg_conn   s
    

r   N)�osr   �jsonr   Zpeeweer   r   r   r   r   r   �<module>   s   	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     src/orm/conn/__pycache__/base.cpython-36.pyc                                                        0000775 0000060 0001757 00000001045 13563664116 021157  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
�b�]�   �               @   s,   d dl mZ d dlmZ G dd� de�ZdS )�    )�Model)�pg_connc               @   s   e Zd ZG dd� d�ZdS )�	BaseModelc               @   s   e Zd Zed�ZdS )zBaseModel.Meta�	conn_ucarN)�__name__�
__module__�__qualname__r   �database� r
   r
   �@/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/conn/base.py�Meta   s   r   N)r   r   r   r   r
   r
   r
   r   r      s   r   N)�peeweer   �orm.conn.dbr   r   r
   r
   r
   r   �<module>   s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              src/orm/model/                                                                                      0000775 0000060 0001757 00000000000 13563661372 013550  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/model/ucar/                                                                                 0000775 0000060 0001757 00000000000 13573714440 014476  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/model/ucar/__init__.py                                                                      0000775 0000000 0001757 00000000000 13563661372 016340  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              src/orm/model/ucar/match.py                                                                         0000664 0001752 0001752 00000001205 13573675067 021437  0                                                                                                    ustar   rodrigo.villalba                rodrigo.villalba                                                                                                                                                                                                       #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import AutoField
from peewee import CharField
from peewee import DateField
from peewee import FloatField
from peewee import TimeField
from peewee import ForeignKeyField
from datetime import datetime
from orm.conn.base import BaseModel
from orm.model.ucar.persona import Persona

class Match(BaseModel):
	id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
	fk_chofer = ForeignKeyField(null=False,model=Persona,field=Persona.id)	#Chofer
	latitud = CharField(null=False)	
	longitud = CharField(null=False)
	estado = CharField(null=False, default='no atendido')
                                                                                                                                                                                                                                                                                                                                                                                           src/orm/model/ucar/__pycache__/                                                                     0000775 0000000 0001757 00000000000 13573714453 016446  5                                                                                                    ustar   root                            developer                                                                                                                                                                                                              src/orm/model/ucar/__pycache__/__init__.cpython-36.pyc                                              0000775 0000060 0001757 00000000235 13563664116 023101  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
�b�]    �               @   s   d S )N� r   r   r   �J/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/ucar/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                       src/orm/model/ucar/__pycache__/persona.cpython-36.pyc                                               0000644 0000000 0000000 00000001625 13573615136 021515  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3
%�]�  �               @   sh   d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dlmZ d dlmZ G dd	� d	e�Z	d
S )�    )�Model)�	AutoField)�	CharField)�BooleanField)�DateTimeField)�datetime)�	BaseModelc               @   sz   e Zd Zeddd�Zeddd�Zeddd�Zedddd�Zeddd�Z	eddd�Z
eddej� jd�d�Zeddd	�Zd
S )�PersonaFT)�null�primary_key��   )r
   �
max_length)r
   �uniquer   z%d-%m-%Y %H:%M:%S)r
   �formats�default)r
   r   N)�__name__�
__module__�__qualname__r   �idr   ZnombreZapellido�emailZinstitucion�passwordr   r   �now�strftimeZconexionr   Z	conductor� r   r   �I/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/ucar/persona.pyr	   
   s   r	   N)
�peeweer   r   r   r   r   r   Zorm.conn.baser   r	   r   r   r   r   �<module>   s                                                                                                              src/orm/model/ucar/__pycache__/base.cpython-36.pyc                                                  0000775 0000060 0001757 00000001006 13563661372 022252  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
)�]�   �               @   s,   d dl mZ d dlmZ G dd� de�ZdS )�    )�Model)�pg_connc               @   s   e Zd ZG dd� d�ZdS )�	BaseModelc               @   s   e Zd Zed�ZdS )zBaseModel.MetaZ	conn_ucarN)�__name__�
__module__�__qualname__r   �database� r	   r	   �!/root/ucar/orm/model/ucar/base.py�Meta   s   r   N)r   r   r   r   r	   r	   r	   r
   r      s   r   N)�peeweer   Zorm.conn.dbr   r   r	   r	   r	   r
   �<module>   s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             src/orm/model/ucar/__pycache__/viaje_reservado.cpython-36.pyc                                       0000644 0000000 0000000 00000001743 13573271752 023221  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3
�s�]#  �               @   s�   d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d d	l	m
Z
 d d
lmZ G dd� de
�ZdS )�    )�Model)�	AutoField)�	CharField)�
FloatField)�BooleanField)�	DateField)�	TimeField)�ForeignKeyField)�	BaseModel)�Personac               @   sh   e Zd Zeddd�Zedd�Zedd�Zedd�Zedd�Z	e
ddd�Zeddd�Zedeejd�Zd	S )
�ViajeReservadoFT)�null�primary_key)r   z%d-%m-%Y)r   �formatsz%H:%M)r   �model�fieldN)�__name__�
__module__�__qualname__r   �idr   ZlatitudOrigZlongitudOrigZ
latitudDstZlongitudDstr   �fechar   Zhorar	   r   �
fk_persona� r   r   �Q/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/ucar/viaje_reservado.pyr      s   



r   N)�peeweer   r   r   r   r   r   r   r	   �orm.conn.baser
   �orm.model.ucar.personar   r   r   r   r   r   �<module>   s                                src/orm/model/ucar/__pycache__/vehiculo.cpython-36.pyc                                              0000644 0000000 0000000 00000001504 13572672277 021670  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3
vr�]d  �               @   s\   d dl mZ d dl mZ d dl mZ d dl mZ d dlmZ d dlmZ G dd� de�Z	d	S )
�    )�	AutoField)�	CharField)�IntegerField)�ForeignKeyField)�	BaseModel)�Personac               @   sf   e Zd Zeddd�Zeddeejd�Zeddd�Z	eddd�Z
eddd�Zedddd�Zedd�Zd	S )
�VehiculoFT)�null�primary_key)r	   �unique�model�field��   )r	   �
max_length)r	   r   r   )r	   N)�__name__�
__module__�__qualname__r   �idr   r   Z	fkPersonar   ZmarcaZmodelo�colorZchapar   Zasiento� r   r   �J/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/ucar/vehiculo.pyr   	   s   r   N)
�peeweer   r   r   r   �orm.conn.baser   �orm.model.ucar.personar   r   r   r   r   r   �<module>   s                                                                                                                                                                                               src/orm/model/ucar/__pycache__/itinerario.cpython-36.pyc                                            0000644 0000000 0000000 00000002031 13573714453 022205  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3
 ��]�  �               @   s�   d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d d	l	m
Z
 d d
lmZ G dd� de
�ZdS )�    )�	AutoField)�	CharField)�IntegerField)�DateTimeField)�	DateField)�
FloatField)�	TimeField)�ForeignKeyField)�	BaseModel)�Personac               @   s|   e Zd Zeddd�Zeddd�Zeddd�Zeddd�Zeddd�Z	eddd�Z
eddd�Zeddd�Zedeejd�Zd	S )
�
ItinerarioFT)�null�primary_key��   )r   �
max_lengthz%H:%M)r   �formats)r   �model�fieldN)�__name__�
__module__�__qualname__r   �idr   ZlatitudOrigZlongitudOrigZ
latitudDstZlongitudDstZdiar   ZhoraEntradaZ
horaSalidar	   r   Z
fk_persona� r   r   �L/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/ucar/itinerario.pyr      s   r   N)�peeweer   r   r   r   r   r   r   r	   �orm.conn.baser
   �orm.model.ucar.personar   r   r   r   r   r   �<module>   s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          src/orm/model/ucar/__pycache__/viaje.cpython-36.pyc                                                 0000644 0000000 0000000 00000001776 13573615136 021153  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3
U�]�  �               @   s�   d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dlmZ d dlm	Z	 d d	l
mZ G d
d� de	�ZdS )�    )�	AutoField)�	CharField)�	DateField)�
FloatField)�	TimeField)�ForeignKeyField)�datetime)�	BaseModel)�Personac               @   s�   e Zd Zeddd�Zeddej� jd�d�Z	e
ddej� jd�d�Zedeejd�Zedeejd�Zedd�Zedd�Zedd	d
�ZdS )�ViajeFT)�null�primary_keyz%d-%m-%Y)r   �formats�defaultz%H:%M:%S)r   �model�field)r   Zcompleto)r   r   N)�__name__�
__module__�__qualname__r   �idr   r   �now�strftime�fechar   �horar   r
   Z	fk_choferZfk_pasajeror   ZlatitudZlongitudr   Zestado� r   r   �G/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/ucar/viaje.pyr      s   

r   N)�peeweer   r   r   r   r   r   r   �orm.conn.baser	   �orm.model.ucar.personar
   r   r   r   r   r   �<module>   s     src/orm/model/ucar/__pycache__/cola_de_pedidos.cpython-36.pyc                                       0000644 0000000 0000000 00000002103 13573550614 023132  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3
��]�  �               @   s�   d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d d	l	m
Z
 d d
lmZ G dd� de
�ZdS )�    )�	AutoField)�	CharField)�IntegerField)�DateTimeField)�	DateField)�
FloatField)�	TimeField)�ForeignKeyField)�	BaseModel)�Personac               @   s�   e Zd Zeddd�Zedd�Zedd�Zedd�Zedd�Z	e
ddd�Zeddd�Zeddd	�Zedeejd
�Zedeejd
�ZdS )�ColaDePedidosFT)�null�primary_key)r   z%d-%m-%Y)r   �formatsz%H:%M��   )r   �
max_length)r   �model�fieldN)�__name__�
__module__�__qualname__r   �idr   �latitudOrig�longitudOrig�
latitudDst�longitudDstr   �fechar   �horaZestador	   r   �
fk_persona�	fk_chofer� r    r    �Q/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/ucar/cola_de_pedidos.pyr      s   



r   N)�peeweer   r   r   r   r   r   r   r	   �orm.conn.baser
   �orm.model.ucar.personar   r   r    r    r    r!   �<module>   s                                                                                                                                                                                                                                                                                                                                                                                                                                                                src/orm/model/ucar/__pycache__/match.cpython-36.pyc                                                 0000644 0000000 0000000 00000001525 13573675213 021143  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3
7z�]�  �               @   s�   d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dl mZ d dlmZ d dlm	Z	 d d	l
mZ G d
d� de	�ZdS )�    )�	AutoField)�	CharField)�	DateField)�
FloatField)�	TimeField)�ForeignKeyField)�datetime)�	BaseModel)�Personac               @   sH   e Zd Zeddd�Zedeejd�Zedd�Z	edd�Z
eddd�ZdS )	�MatchFT)�null�primary_key)r   �model�field)r   zno atendido)r   �defaultN)�__name__�
__module__�__qualname__r   �idr   r
   �	fk_choferr   �latitud�longitud�estado� r   r   �G/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/ucar/match.pyr      s
   

r   N)�peeweer   r   r   r   r   r   r   �orm.conn.baser	   �orm.model.ucar.personar
   r   r   r   r   r   �<module>   s                                                                                                                                                                              src/orm/model/ucar/persona.py                                                                       0000775 0000000 0001757 00000001675 13573614445 016273  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import Model
from peewee import AutoField
from peewee import CharField
from peewee import BooleanField
from peewee import DateTimeField
from datetime import datetime
from orm.conn.base import BaseModel

class Persona(BaseModel):
    id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
    nombre = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    apellido = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    email = CharField(null=False, unique=True, max_length=255) # VARCHAR(255), UNIQUE, NOT NULL
    institucion = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    password = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    conexion = DateTimeField(null=True, formats='%d-%m-%Y %H:%M:%S', default=datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    conductor = BooleanField(null=True, default=False)                                                                   src/orm/model/ucar/cola_de_pedidos.py                                                               0000775 0000000 0001757 00000001670 13573547034 017713  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import AutoField
from peewee import CharField
from peewee import IntegerField
from peewee import DateTimeField
from peewee import DateTimeField
from peewee import DateField
from peewee import FloatField
from peewee import TimeField
from peewee import ForeignKeyField
from orm.conn.base import BaseModel
from orm.model.ucar.persona import Persona

class ColaDePedidos(BaseModel):
	id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
	latitudOrig = CharField(null=False)	
	longitudOrig = CharField(null=False)
	latitudDst = CharField(null=False)	
	longitudDst = CharField(null=False)
	fecha = DateField(null=True,formats='%d-%m-%Y')
	hora = TimeField(null=True,formats='%H:%M')
	estado = CharField(null=True,max_length=255)
	fk_persona = ForeignKeyField(null=False,model=Persona,field=Persona.id)
	fk_chofer = ForeignKeyField(null=True,model=Persona,field=Persona.id)
                                                                        src/orm/model/ucar/viaje_reservado.py                                                               0000775 0000000 0001757 00000001443 13573271672 017766  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import Model
from peewee import AutoField
from peewee import CharField
from peewee import FloatField
from peewee import BooleanField
from peewee import DateField
from peewee import TimeField
from peewee import ForeignKeyField  
from orm.conn.base import BaseModel
from orm.model.ucar.persona import Persona

class ViajeReservado(BaseModel):
	id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
	latitudOrig = FloatField(null=False)	
	longitudOrig = FloatField(null=False)
	latitudDst = FloatField(null=False)	
	longitudDst = FloatField(null=False)
	fecha = DateField(null=False,formats='%d-%m-%Y')
	hora = TimeField(null=False,formats='%H:%M')
	fk_persona = ForeignKeyField(null=False,model=Persona,field=Persona.id)
                                                                                                                                                                                                                             src/orm/model/ucar/vehiculo.py                                                                      0000775 0000000 0001757 00000001544 13572671166 016437  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import AutoField
from peewee import CharField
from peewee import IntegerField
from peewee import ForeignKeyField
from orm.conn.base import BaseModel
from orm.model.ucar.persona import Persona

class Vehiculo(BaseModel):
    id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
    fkPersona = ForeignKeyField(null=False, unique=True, model=Persona, field=Persona.id) # FK, one-to-one, Persona->Vehiculo
    marca = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    modelo = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    color = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    chapa = CharField(null=False, unique=True, max_length=255) # VARCHAR(255), NOT NULL, UNIQUE
    asiento = IntegerField(null=False) # INTEGER, NOT NULL                                                                                                                                                            src/orm/model/ucar/viaje.py                                                                         0000775 0000000 0001757 00000001626 13573614525 015715  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import AutoField
from peewee import CharField
from peewee import DateField
from peewee import FloatField
from peewee import TimeField
from peewee import ForeignKeyField
from datetime import datetime
from orm.conn.base import BaseModel
from orm.model.ucar.persona import Persona

class Viaje(BaseModel):
	id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
	fecha = DateField(null=False, formats='%d-%m-%Y', default=datetime.now().strftime("%d-%m-%Y"))
	hora = TimeField(null=False, formats='%H:%M:%S', default=datetime.now().strftime("%H:%M:%S"))
	fk_chofer = ForeignKeyField(null=False,model=Persona,field=Persona.id)	#Chofer
	fk_pasajero = ForeignKeyField(null=False,model=Persona,field=Persona.id) #Pasajero
	latitud = FloatField(null=False)	
	longitud = FloatField(null=False)
	estado = CharField(null=False, default='completo')                                                                                                          src/orm/model/ucar/itinerario.py                                                                    0000775 0000000 0001757 00000001670 13573714440 016760  0                                                                                                    ustar   root                            developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import AutoField
from peewee import CharField
from peewee import IntegerField
from peewee import DateTimeField
from peewee import DateTimeField
from peewee import DateField
from peewee import FloatField
from peewee import TimeField
from peewee import ForeignKeyField
from orm.conn.base import BaseModel
from orm.model.ucar.persona import Persona

class Itinerario(BaseModel):
	id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
	latitudOrig = CharField(null=False, max_length=255)	
	longitudOrig = CharField(null=False, max_length=255)
	latitudDst = CharField(null=False, max_length=255)	
	longitudDst = CharField(null=False, max_length=255)
	dia = CharField(null=False, max_length=255)
	horaEntrada = TimeField(null=False,formats='%H:%M')
	horaSalida = TimeField(null=False,formats='%H:%M')
	fk_persona = ForeignKeyField(null=False,model=Persona,field=Persona.id)
                                                                        src/orm/model/client/                                                                               0000775 0000060 0001757 00000000000 13563663742 015031  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/model/client/__init__.py                                                                    0000775 0000060 0001757 00000000000 13563661372 017130  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/model/client/__pycache__/                                                                   0000775 0000060 0001757 00000000000 13563664116 017235  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/model/client/__pycache__/__init__.cpython-36.pyc                                            0000775 0000060 0001757 00000000237 13563664116 023427  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
�b�]    �               @   s   d S )N� r   r   r   �L/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/client/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                     src/orm/model/client/__pycache__/cliente.cpython-36.pyc                                             0000775 0000060 0001757 00000001061 13563664116 023307  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
�g�]t  �               @   sD   d dl mZ d dl mZ d dl mZ d dlmZ G dd� de�ZdS )�    )�Model)�	AutoField)�	CharField)�	BaseModelc               @   s&   e Zd Zeddd�Zedddd�ZdS )�ClienteFT)�null�primary_key��   )r   �unique�
max_lengthN)�__name__�
__module__�__qualname__r   �idr   �email� r   r   �K/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/client/cliente.pyr      s   r   N)�peeweer   r   r   �orm.conn.baser   r   r   r   r   r   �<module>   s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  src/orm/model/client/cliente.py                                                                     0000775 0000060 0001757 00000000564 13563663742 017036  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import Model
from peewee import AutoField
from peewee import CharField
from orm.conn.base import BaseModel

class Cliente(BaseModel):
    id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
    email = CharField(null=False, unique=True, max_length=255) # VARCHAR(255), UNIQUE, NOT NULL
                                                                                                                                            src/orm/model/__init__.py                                                                           0000775 0000060 0001757 00000000000 13563661372 015652  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/model/__pycache__/                                                                          0000775 0000060 0001757 00000000000 13563664116 015757  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/model/__pycache__/__init__.cpython-36.pyc                                                   0000775 0000060 0001757 00000000230 13563664116 022142  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
�b�]    �               @   s   d S )N� r   r   r   �E/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                            src/orm/create/                                                                                     0000775 0000060 0001757 00000000000 13573334700 013704  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/create/__init__.py                                                                          0000775 0000060 0001757 00000000000 13563661372 016015  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/create/__pycache__/                                                                         0000775 0000060 0001757 00000000000 13573662171 016122  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/create/__pycache__/__init__.cpython-36.pyc                                                  0000775 0000060 0001757 00000000231 13563664116 022306  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
�b�]    �               @   s   d S )N� r   r   r   �F/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/create/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                           src/orm/create/__pycache__/ucar.cpython-36.pyc                                                      0000644 0000060 0000060 00000001610 13573662171 020714  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
5d�]�  �               @   sx   d dl mZ d dlmZ d dlmZ d dlmZ d dlm	Z	 d dl
mZ d dlmZ d dlmZ d d	lmZ d
d� ZdS )�    )�pg_conn)�Persona)�Cliente)�Vehiculo)�
Itinerario)�ViajeReservado)�Viaje)�ColaDePedidos)�Matchc              C   s:   t tttttttg} td�}|j	�  |j
| � |j�  d S )NZ	conn_ucar)r   r   r   r   r   r   r	   r
   r   �connect�create_tables�close)ZTABLES�db� r   �B/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/create/ucar.pyr      s
    
r   N)Zorm.conn.dbr   Zorm.model.ucar.personar   Zorm.model.client.clienter   Zorm.model.ucar.vehiculor   Zorm.model.ucar.itinerarior   Zorm.model.ucar.viaje_reservador   Zorm.model.ucar.viajer   Zorm.model.ucar.cola_de_pedidosr	   Zorm.model.ucar.matchr
   r   r   r   r   r   �<module>   s                                                                                                                           src/orm/create/ucar.py                                                                              0000775 0000060 0001757 00000001245 13573662065 015225  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from orm.conn.db import pg_conn
from orm.model.ucar.persona import Persona
from orm.model.client.cliente import Cliente
from orm.model.ucar.vehiculo import Vehiculo
from orm.model.ucar.itinerario import Itinerario
from orm.model.ucar.viaje_reservado import ViajeReservado
from orm.model.ucar.viaje import Viaje
from orm.model.ucar.cola_de_pedidos import ColaDePedidos
from orm.model.ucar.match import Match

def create_tables():
    TABLES = [Persona, Cliente, ViajeReservado, Vehiculo, Itinerario, Viaje, ColaDePedidos, Match]
    db = pg_conn('conn_ucar')
    db.connect()
    db.create_tables(TABLES)
    db.close()
                                                                                                                                                                                                                                                                                                                                                           src/orm/__init__.py                                                                                 0000775 0000060 0001757 00000000000 13563661372 014552  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/__pycache__/                                                                                0000775 0000060 0001757 00000000000 13563664116 014657  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/orm/__pycache__/__init__.cpython-36.pyc                                                         0000775 0000060 0001757 00000000222 13563664116 021043  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
�b�]    �               @   s   d S )N� r   r   r   �?/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                                  src/__pycache__/                                                                                    0000755 0000060 0000060 00000000000 13573721776 013305  5                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 src/__pycache__/index.cpython-36.pyc                                                                0000644 0000060 0000060 00000003334 13573721776 017045  0                                                                                                    ustar   apache                          apache                                                                                                                                                                                                                 3
���]�	  �               @   s�  d dl mZ d dlmZ d dlmZ d dlmZ d dlm	Z	 d dl
mZ d dlmZ d dlmZ d d	lmZ d d
lmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dl m!Z! d dl"m#Z# d dl$m%Z% ee&�Z'e'j(e� e'j(e	� e'j(e� e'j(e� e'j(e� e'j(e� e'j(e� e'j(e� e'j(e� e'j(e� e'j(e� e'j(e� e'j(e� e'j(e!� e'j(e#� e'j(e%� e&dk�r�e)e�dk�r�ed dk�r�e�  e'j*�  dS )�    )�argv)�Flask)�create_tables)�index_usuario_registrar)�index_usuario_identificar)�index_usuario_listar)�index_reserva_reservar)�index_reserva_cancelar)�index_reserva_listar)�index_foto_subir)�index_usuario_datos)�index_recuperar_cuenta)�index_perfil_actualizar)�index_vehiculo_registrar)�index_editar_itinerario)�index_pasajero_solicitar_viaje)�index_pasajero_verificar_viaje)�index_vehiculo_listar)�index_conductor_listar_viajes�__main__�   �   z	--init-dbN)+�sysr   Zflaskr   Zorm.create.ucarr   Zapi.user.registrarr   Zapi.user.identificarr   Zapi.user.listarr   Zapi.user.crear_reservar   Zapi.user.eliminar_reservar	   Zapi.user.listar_reservasr
   Zapi.user.subir_fotor   Zapi.user.get_user_by_emailr   Zapi.user.recuperar_cuentar   Zapi.user.actualizar_perfilr   Zapi.user.registrar_vehiculor   Zapi.user.editar_itinerarior   Z!api.user.pasajero_solicitar_viajer   Z!api.user.pasajero_verificar_viajer   Zapi.user.listar_vehiculor   Zapi.user.conductor_viajesr   �__name__�appZregister_blueprint�len�run� r   r   �8/opt/rh/httpd24/root/var/www/ucar/html/env2/src/index.py�<module>   sP   
















                                                                                                                                                                                                                                                                                                    src/trash/                                                                                          0000775 0000060 0001757 00000000000 13563722201 012761  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/app2.py                                                                                   0000775 0000060 0001757 00000004734 13563116676 014225  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              #! /opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import Flask
from flask import escape
from flask import request
from flask import jsonify
from peewee import Select
from functools import wraps
from orm.model.ucar.persona import Persona

app = Flask(__name__)

UCAR_API_AUTH_TOKEN = 'JbslEJwMnd7fcfrtqcyT_O4MgTWQ1bau1XtdGhWGXw'
UCAR_API_USER_ID = 'yNPnZACTchuDwdHag'

# https://stackoverflow.com/questions/32510290/how-do-you-implement-token-authentication-in-flask
def require_api_token(func):
    @wraps(func)
    def check_token(*args, **kwargs):
        if request.headers.has_key('X-Auth-Token') and request.headers.has_key('X-User-Id'):
            token = request.headers.get('X-Auth-Token')
            user = request.headers.get('X-User-Id')
            if user in UCAR_API_USER_ID and token in UCAR_API_AUTH_TOKEN:
                return func(*args, **kwargs)
        return {"status":"error","message":"You must be logged in to do this."}
    return check_token

def content_type_json(func):
    @wraps(func)
    def check(*args, **kwargs):
        if request.is_json:
            return func(*args, **kwargs)
        return {"status": "error","message":"Content-Type: application/json"}
    return check

@app.route('/ucar/info', methods=['GET'])
def info():
    return {'status':'ok','message':'v1'}

@app.route('/ucar/usuario/registrar', methods=['POST'])
@require_api_token
@content_type_json
def usuario_registrar():
    try:
        data = dict(request.get_json())
        new = Persona(**data)
        new.save()
    except:
        return {"status":"error","message":"pg insert"}
    return {'status':'ok','message':'usuario creado'}

@app.route('/ucar/usuario/identificar', methods=['POST'])
@require_api_token
@content_type_json
def usuario_identificar():
    query = Select(None)
    try:
        data = dict(request.get_json())
        query = Persona.select(Persona.email, Persona.password)\
                .where((Persona.email == data['email']) | (Persona.password == data['password']))
    except:
        return {"status":"error","message":"pg select"}
    if not query.exists():
        return {'status':'ok','message':'usuario identificado'}
    return {'status':'error','message':'usuario no identificado'}

@app.route('/ucar/usuario/listar', methods=['GET'])
@require_api_token
def usuario_listar():
    data = []
    query = Persona.select()
    for result in query.dicts():
        data.append(result)
    return jsonify(data)

if __name__ == '__main__':
    app.run()
                                    src/trash/app.py                                                                                    0000775 0000060 0001757 00000005603 13563201611 014117  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              #! /opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import Flask
from flask import escape
from flask import request
from flask import jsonify
from peewee import Select
from functools import wraps
from orm.model.ucar.persona import Persona
from html import unescape
import json

app = Flask(__name__)

UCAR_API_AUTH_TOKEN = 'JbslEJwMnd7fcfrtqcyT_O4MgTWQ1bau1XtdGhWGXw'
UCAR_API_USER_ID = 'yNPnZACTchuDwdHag'



f = open('/opt/rh/httpd24/root/var/www/ucar/html/env2/src/hola', 'a')
f.write("holaaaaaaaa")
# https://stackoverflow.com/questions/32510290/how-do-you-implement-token-authentication-in-flask
def require_api_token(func):
    @wraps(func)
    def check_token(*args, **kwargs):
        if request.headers.has_key('X-Auth-Token') and request.headers.has_key('X-User-Id'):
            token = request.headers.get('X-Auth-Token')
            user = request.headers.get('X-User-Id')
            if user in UCAR_API_USER_ID and token in UCAR_API_AUTH_TOKEN:
                return func(*args, **kwargs)
        return {"status":"error","message":"You must be logged in to do this."}
    return check_token

def content_type_json(func):
    @wraps(func)
    def check(*args, **kwargs):
        if request.is_json:
            return func(*args, **kwargs)
        return {"status": "error","message":"Content-Type: application/json"}
    return check

@app.route('/ucar/info', methods=['GET'])
def info():
    return {'status':'ok','message':'v1'}

@app.route('/ucar/usuario/registrar', methods=['POST'])
@require_api_token
@content_type_json
def usuario_registrar():
    try:
        data = dict(request.get_json())
        new = Persona(**data)
        new.save()
    except:
        return {"status":"error","message":"pg insert"}
    return {'status':'ok','message':'usuario creado'}

@app.route('/ucar/usuario/identificar', methods=['POST'])
@require_api_token
@content_type_json
def usuario_identificar():
    try:
        '''
        var_email = str(request.data).replace('b\'', '').split('&')[0].replace('email=','')
        f.write('hola \n')
        f.write(str(request.headers))
        f.write(str(request.data))
        f.write(request.values)
        f.write(request.data['email'] + "\n")
        f.write(str(request.get_json()) + "\n")
        '''

        query = Persona.select(Persona.email, Persona.password)\
                .where((Persona.email == request.json['email']) & (Persona.password == request.json['password']))
    except:
        return {"status":"error","message":"pg select"}
    if query.exists():
        return {'status':'ok','message':'usuario identificado'}
    return {'status':'error','message':'usuario no identificado'}

@app.route('/ucar/usuario/listar', methods=['GET'])
@require_api_token
def usuario_listar():
    data = []
    query = Persona.select()
    for result in query.dicts():
        data.append(result)
    return jsonify(data)

if __name__ == '__main__':
    app.run()
                                                                                                                             src/trash/index.py                                                                                  0000775 0000060 0001757 00000000347 13563303222 014447  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              #! /opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import Flask, escape, request
import peewee

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Alv xdxdxd!'

if __name__ == '__main__':
	app.run()
                                                                                                                                                                                                                                                                                         src/trash/orm/                                                                                      0000775 0000060 0001757 00000000000 13562550074 013564  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/conn/                                                                                 0000775 0000060 0001757 00000000000 13563277270 014526  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/conn/conn_ucar.json                                                                   0000775 0000060 0001757 00000000170 13562550074 017364  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              {
    "database":"ucar",
    "user":"ucar_api",
    "password":"#7h3m4573r!.",
    "host":"127.0.0.1",
    "port":5432
}                                                                                                                                                                                                                                                                                                                                                                                                        src/trash/orm/conn/__init__.py                                                                      0000775 0000060 0001757 00000000000 13562550074 016623  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/conn/__pycache__/                                                                     0000775 0000060 0001757 00000000000 13563123213 016721  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/conn/__pycache__/__init__.cpython-36.pyc                                              0000775 0000060 0001757 00000000227 13563123213 023112  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
<��]    �               @   s   d S )N� r   r   r   �D/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/conn/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                             src/trash/orm/conn/__pycache__/db.cpython-36.pyc                                                    0000775 0000060 0001757 00000001013 13563123213 021732  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
<��]�  �               @   s0   d dl mZ d dlmZ d dlmZ dd� ZdS )�    )�path)�load)�PostgresqlDatabasec          
   C   sD   t jt�}t j|| d �}t|��}tt|��}W d Q R X tf |�S )Nz.json)r   �dirname�__file__�join�open�dictr   r   )ZjsonfileZcurrent_file_dirZcfg�f�data� r   �>/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/conn/db.py�pg_conn   s
    

r   N)�osr   �jsonr   �peeweer   r   r   r   r   r   �<module>   s   	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     src/trash/orm/conn/__pycache__/__init__.cpython-35.pyc                                              0000775 0000060 0001757 00000000203 13562550074 023113  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              
!�]    �               @   s   d  S)N� r   r   r   �0/var/www/ucar/html/env2/src/orm/conn/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                                                 src/trash/orm/conn/__pycache__/db.cpython-35.pyc                                                    0000775 0000060 0001757 00000001032 13562550074 021742  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              
$�]�  �               @   s@   d  d l  m Z d  d l m Z d  d l m Z d d �  Z d S)�    )�path)�load)�PostgresqlDatabasec          
   C   sW   t  j t � } t  j | |  d � } t | � � } t t | � � } Wd  QRXt | �  S)Nz.json)r   �dirname�__file__�join�open�dictr   r   )ZjsonfileZcurrent_file_dirZcfg�f�data� r   �*/var/www/ucar/html/env2/src/orm/conn/db.py�pg_conn   s
    r   N)�osr   �jsonr   �peeweer   r   r   r   r   r   �<module>   s   	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      src/trash/orm/conn/db.py                                                                            0000775 0000060 0001757 00000002015 13563277270 015466  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              #! /opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from os import path
from json import load
from peewee import PostgresqlDatabase

# función		:   pg_conn()
# parametros	:	archivo de conexión
# utilidad		: 	lee el archivo de configuracíon de la bd la
#                   cual contiene los parametros de conexión,
#                   utiliza los mismos para definir la conexión.
# retorno		:   instancia de conexión a la base de datos
# detalles		: 	ninguno
def pg_conn(jsonfile):
    # obtiene la dirección del directorio del script actual
    current_file_dir = path.dirname(__file__)
    # concatenación del nombre del archivo cfg
    # y su ubicación (directorio actual)
    cfg = path.join(current_file_dir, jsonfile + '.json')
    # manejo de archivos
    with open(cfg) as f:
        # se lee todo el contenido
        # del archivo json, se almacena
        # en data en forma de diccionario {clave:valor}
        data = dict(load(f))
    # retorno de instancia de conexión
    return PostgresqlDatabase(**data)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   src/trash/orm/model/                                                                                0000775 0000060 0001757 00000000000 13562550074 014664  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/model/ucar/                                                                           0000775 0000060 0001757 00000000000 13563277364 015627  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/model/ucar/__init__.py                                                                0000775 0000060 0001757 00000000000 13562550074 017720  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/model/ucar/__pycache__/                                                               0000775 0000060 0001757 00000000000 13563123213 020016  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/model/ucar/__pycache__/__init__.cpython-36.pyc                                        0000775 0000060 0001757 00000000235 13563123213 024206  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
<��]    �               @   s   d S )N� r   r   r   �J/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/ucar/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                       src/trash/orm/model/ucar/__pycache__/persona.cpython-36.pyc                                         0000775 0000060 0001757 00000001242 13563123213 024115  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
<��]�  �               @   sD   d dl mZ d dl mZ d dl mZ d dlmZ G dd� de�ZdS )�    )�Model)�	AutoField)�	CharField)�	BaseModelc               @   sV   e Zd Zeddd�Zeddd�Zeddd�Zedddd�Zeddd�Z	eddd�Z
dS )�PersonaFT)�null�primary_key��   )r   �
max_length)r   �uniquer
   N)�__name__�
__module__�__qualname__r   �idr   ZnombreZapellido�emailZinstitucion�password� r   r   �I/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/ucar/persona.pyr      s   r   N)�peeweer   r   r   Zorm.model.ucar.baser   r   r   r   r   r   �<module>   s                                                                                                                                                                                                                                                                                                                                                                 src/trash/orm/model/ucar/__pycache__/base.cpython-36.pyc                                            0000775 0000060 0001757 00000001053 13563123213 023360  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
<��]�   �               @   s,   d dl mZ d dlmZ G dd� de�ZdS )�    )�Model)�pg_connc               @   s   e Zd ZG dd� d�ZdS )�	BaseModelc               @   s   e Zd Zed�ZdS )zBaseModel.MetaZ	conn_ucarN)�__name__�
__module__�__qualname__r   �database� r	   r	   �F/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/ucar/base.py�Meta   s   r   N)r   r   r   r   r	   r	   r	   r
   r      s   r   N)�peeweer   Zorm.conn.dbr   r   r	   r	   r	   r
   �<module>   s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        src/trash/orm/model/ucar/__pycache__/__init__.cpython-35.pyc                                        0000775 0000060 0001757 00000000211 13562550074 024207  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              
!�]    �               @   s   d  S)N� r   r   r   �6/var/www/ucar/html/env2/src/orm/model/ucar/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                                           src/trash/orm/model/ucar/__pycache__/persona.cpython-35.pyc                                         0000775 0000060 0001757 00000001315 13562550074 024125  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              
^�]�  �               @   sZ   d  d l  m Z d  d l  m Z d  d l  m Z d  d l m Z Gd d �  d e � Z d S)�    )�Model)�	AutoField)�	CharField)�	BaseModelc               @   s�   e  Z d  Z e d d d d � Z e d d d d � Z e d d d d � Z e d d d d d d � Z e d d d d � Z	 e d d d d � Z
 d S)	�Persona�nullF�primary_keyT�
max_length��   �uniqueN)�__name__�
__module__�__qualname__r   �idr   ZnombreZapellido�emailZinstitucion�password� r   r   �5/var/www/ucar/html/env2/src/orm/model/ucar/persona.pyr      s   r   N)�peeweer   r   r   Zorm.model.ucar.baser   r   r   r   r   r   �<module>   s                                                                                                                                                                                                                                                                                                                      src/trash/orm/model/ucar/__pycache__/base.cpython-35.pyc                                            0000775 0000060 0001757 00000001066 13562550074 023373  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              
N�]�   �               @   s:   d  d l  m Z d  d l m Z Gd d �  d e � Z d S)�    )�Model)�pg_connc               @   s#   e  Z d  Z Gd d �  d � Z d S)�	BaseModelc               @   s   e  Z d  Z e d � Z d S)zBaseModel.MetaZ	conn_ucarN)�__name__�
__module__�__qualname__r   �database� r	   r	   �2/var/www/ucar/html/env2/src/orm/model/ucar/base.py�Meta   s   r   N)r   r   r   r   r	   r	   r	   r
   r      s   r   N)�peeweer   Zorm.conn.dbr   r   r	   r	   r	   r
   �<module>   s                                                                                                                                                                                                                                                                                                                                                                                                                                                                             src/trash/orm/model/ucar/base.py                                                                    0000775 0000060 0001757 00000000305 13563277326 017112  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              #! /opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import Model
from orm.conn.db import pg_conn

class BaseModel(Model):
    class Meta:
        database = pg_conn('conn_ucar')
                                                                                                                                                                                                                                                                                                                           src/trash/orm/model/ucar/persona.py                                                                 0000775 0000060 0001757 00000001264 13563277364 017656  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              #! /opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from peewee import Model
from peewee import AutoField
from peewee import CharField
from orm.model.ucar.base import BaseModel

class Persona(BaseModel):
    id = AutoField(null=False, primary_key=True) # SERIAL, PK, NOT NULL
    nombre = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    apellido = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    email = CharField(null=False, unique=True, max_length=255) # VARCHAR(255), UNIQUE, NOT NULL
    institucion = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
    password = CharField(null=False, max_length=255) # VARCHAR(255), NOT NULL
                                                                                                                                                                                                                                                                                                                                            src/trash/orm/model/client/                                                                         0000775 0000060 0001757 00000000000 13562550074 016142  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/model/client/__init__.py                                                              0000775 0000060 0001757 00000000000 13562550074 020244  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/model/__init__.py                                                                     0000775 0000060 0001757 00000000000 13562550074 016766  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/model/__pycache__/                                                                    0000775 0000060 0001757 00000000000 13563123213 017064  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/model/__pycache__/__init__.cpython-36.pyc                                             0000775 0000060 0001757 00000000230 13563123213 023247  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
<��]    �               @   s   d S )N� r   r   r   �E/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/model/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                            src/trash/orm/model/__pycache__/__init__.cpython-35.pyc                                             0000775 0000060 0001757 00000000204 13562550074 023257  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              
!�]    �               @   s   d  S)N� r   r   r   �1/var/www/ucar/html/env2/src/orm/model/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                                                src/trash/orm/create/                                                                               0000775 0000060 0001757 00000000000 13562550074 015027  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/create/__init__.py                                                                    0000775 0000060 0001757 00000000000 13562550074 017131  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/create/ucar.py                                                                        0000775 0000060 0001757 00000000425 13562550074 016337  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              from os import path
from site import addsitedir
addsitedir(path.abspath(path.join(path.dirname(__file__), '..')))

from conn.db import pg_conn
from model.ucar.persona import Persona

TABLES = [Persona]

db = pg_conn('conn_ucar')
db.connect()
db.create_tables(TABLES)
db.close()                                                                                                                                                                                                                                           src/trash/orm/__init__.py                                                                           0000775 0000060 0001757 00000000000 13562550074 015666  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/__pycache__/                                                                          0000775 0000060 0001757 00000000000 13563123213 015764  5                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              src/trash/orm/__pycache__/__init__.cpython-36.pyc                                                   0000775 0000060 0001757 00000000222 13563123213 022150  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              3
<��]    �               @   s   d S )N� r   r   r   �?/opt/rh/httpd24/root/var/www/ucar/html/env2/src/orm/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                                  src/trash/orm/__pycache__/__init__.cpython-35.pyc                                                   0000775 0000060 0001757 00000000176 13562550074 022167  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              
!�]    �               @   s   d  S)N� r   r   r   �+/var/www/ucar/html/env2/src/orm/__init__.py�<module>   s                                                                                                                                                                                                                                                                                                                                                                                                      src/trash/ucar-db-setup.py                                                                          0000775 0000060 0001757 00000000345 13562551467 016030  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              #!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from orm.conn.db import pg_conn
from orm.model.ucar.persona import Persona

TABLES = [Persona]

db = pg_conn('conn_ucar')
db.connect()
db.create_tables(TABLES)
db.close()
                                                                                                                                                                                                                                                                                           src/ucar.wsgi                                                                                       0000775 0000060 0001757 00000000411 13563675420 013476  0                                                                                                    ustar   apache                          developer                                                                                                                                                                                                              #! /opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/opt/rh/httpd24/root/var/www/ucar/html/env2/src')
from index import app as application
application.secret_key = '12345'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       