from ValidaUser import ValidaUser
from ValidaPass import ValidaPass

usuario = raw_input('ingrese usuario: ')
contra = raw_input('ingrese contrasena: ')

if ValidaUser(usuario) == True and ValidaPass(contra) == True:
    print 'datos correctos'
else:
    print 'datos incorrectos'
