from distutils import core
from email import message
from http import server
from logging import exception
from turtle import color
import pyodbc as sql
import smtplib
from email.message import EmailMessage
message='hola recibiste este correo ya que perteneces a la ciudad de medellin'
subject="Compra en Face2"
message="subject : {}\n\n{}".format(subject,message)
try:
    Conexion=sql.connect('DRIVER={SQL Server};SERVER=DIEGO123\SQLEXPRESS;DATABASE=Fase2;Trusted_Connection=yes;')
except Exception as Ex:
      print("Ocurrio un error al conectar a SQL : ",Ex)
      
def insertar_datos():
      try:
            cursor=Conexion.cursor()
            cursor.execute("Select * from Usuarios ")
            datos=cursor.fetchone()
            while datos:
                  print(datos,"\n")
                  datos=cursor.fetchone()
            cursor.close()
            Conexion.close
      except Exception as Ex:
             print("Ocurrio un error al conectar a SQL : ",Ex)


try :
    bandera=True
    
    while bandera==True:
        try:
            print("**********Menu Principal**********\n"
                  "********1.Ingresar Nueva Compra **\n"
                  "********2.Ver compras*************\n"
                  "********3.salir ******************\n")

            opc=int(input("Selecciona una Opcion :"))
            if opc==1:
                  
                  if ciudad=="medellin":
                        server1=smtplib.SMTP('smtp.gmail.com','587')
                        server1.starttls()
                        server1.login('pepetoo123321@gmail.com','pepeto123456')
                        server1.sendmail('pepetoo123321@gmail.com',correo,message)
                        
                        print("se envio el correo ")
                        
            elif opc==2:
                 insertar_datos()
            elif opc==3:
                  bandera=False
            else :
                  print("DIGITA UNA OPCION VALIDA")
        except Exception as Ex:
            print("\nError, ingresa un valor numerico",Ex)
      
except:    
    print("error")

