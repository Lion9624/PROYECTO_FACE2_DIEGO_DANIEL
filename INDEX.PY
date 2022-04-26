from distutils import core
from email import message
from http import server
from logging import exception
from turtle import color
import pyodbc as sql
import smtplib
import datetime
from email.message import EmailMessage
message='hola recibiste este correo ya que perteneces a la ciudad de medellin y realizaste una compra en Face2'
subject="Compra en Face2"
message="subject : {}\n\n{}".format(subject,message)

try:
      conexion=sql.connect('DRIVER={SQL Server};SERVER=DIEGO123\SQLEXPRESS;DATABASE=Fase2;Trusted_Connection=yes;')
except Exception as Ex:
      print("Ocurrio un error al conectar a SQL : ",Ex)
    
      
def visualizar_datos():
      try:
            cursor=conexion.cursor()
            cursor.execute("Select * from Usuarios ")
            datos=cursor.fetchone()
            while datos:
                  print(datos,"\n")
                  datos=cursor.fetchone()
            cursor.close()
            conexion.close
      except Exception as Ex:
             print("Ocurrio un error al conectar a SQL : ",Ex)
      

def insertar_datos():
      try:
            cursor= conexion.cursor()
            nombre= input("Inserte el nombre del comprador: ")
            cedula= int(input("Ingrese la cédula del comprador: "))
            correo = input("Ingrese el correo electrónico del comprador: ")
            edad= int(input("Edad del comprador: "))
            ciudad = input("Ingrese la ciudad en la que se realiza la compra: ").lower()
            productos = int(input("Ingrese la cantidad de productos comprados: "))
            fecha = str(datetime.date.today())
            cursor.execute("INSERT INTO Usuarios (nombre, cedula, correo, edad, ciudad, productos,fecha_de_compra) values (?,?,?,?,?,?,?)", (nombre,cedula,correo,edad,ciudad,productos,fecha))
            cursor.commit()            
            cursor.close()
            if ciudad=="medellin":
                  server1=smtplib.SMTP('smtp.gmail.com','587')
                  server1.starttls()
                  server1.login('pepetoo123321@gmail.com','pepeto123456')
                  server1.sendmail('pepetoo123321@gmail.com',correo,message)                        
                  print("se envio el correo ")
      except Exception as ex:
            print(ex)


def main():
      try:
            bandera=True    
            while bandera==True:
                  try:
                        print("**********Menu Principal**********\n"
                        "********1.Ingresar Nueva Compra **\n"
                        "********2.Ver compras*************\n"
                        "********3.salir ******************\n")
                        opc=int(input("Selecciona una Opcion :"))
                        if opc==1:
                              insertar_datos()                              
                        elif opc==2:
                              visualizar_datos()
                        elif opc==3:
                              bandera=False
                        else :
                              print("DIGITA UNA OPCION VALIDA")
                  except Exception as Ex:
                        print("\nError, ingresa un valor numerico",Ex)
      except:    
            print("error") 


if __name__=='__main__':
      main()

