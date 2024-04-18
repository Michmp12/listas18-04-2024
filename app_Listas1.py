import os
sw = True
list_id = []
list_name = []
list_contact = []
list_e_mail = []

def fnt_limpiar():
    os.system('cls')
    print('Autor: Michell Mosquera')
    print('Fecha: 18 de abril del 2024\n\n')
    
    
def fnt_registrar(id, name, contact, e_mail):
    if id == '' or name == '' or contact == '' or e_mail == '':
        enter = input('\nError, debe de llenar todos los datos <ENTER>')
    else: 
        list_id.append(id)
        list_name.append(name)
        list_contact.append(contact)
        list_e_mail.append(e_mail)
        enter = input('\nRegistro exitoso <ENTER>')
                        
def fnt_selector(op):
    if op == '1':
        fnt_limpiar()
        id = input('Ingrese su ID: ')
        if id in list_id:
            enter = input('\nEsta persona ya se encuentra registrada <ENTER PARA CONTINUAR>')
        else:
            name = input('Ingrese su nombre: ')
            contact = input('Ingrese su contacto: ')
            e_mail = input('Ingrese su email: ')
            fnt_registrar(id, name, contact, e_mail)
    if op == '2':
        fnt_limpiar()
        for i in range(len(list_id)):
            print(f'{list_id[i]} {list_name[i]} {list_contact[i]} {list_e_mail[i]}')
        enter = input('\Presione <ENTER> para continuar')
        
    if op == '3':
        sw = False


while sw == True:
    fnt_limpiar()
    opcion = input('\n\n ----- MENÚ PRINCIPAL -----\n1. Regristar\n2.Consultar\n3.Salir\n.-> ')
    fnt_selector(opcion)
