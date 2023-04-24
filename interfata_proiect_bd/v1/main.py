from tkinter import *
from PIL import ImageTk,Image
import cx_Oracle
# query='insert into ingrediente (id_ingredient,nume_ingredient,cantitate)values (null,\'Canepa\',10)'
# cursor.execute(query)
# conn.commit()
# query = 'insert into formula (esenta_id_parfum,ingrediente_id_ingredient,procent)values (2000,3000,15)'
# query = 'insert into ambalaje (esenta_id_parfum,id_ambalaj,stoc,pret,gramaj)values (2000,null,100,123,75)'
# query = 'insert into cereri (distribuitor_id_distribuitor,ambalaje_id_ambalaj,gramaj,nr_bucati,data)values (100,1007,100,20,sysdate)'
# query = 'insert into distribuitor (id_distribuitor,nume_distr)values (null,\'Iulius Mall\')'
#  query = 'insert into formula (esenta_id_parfum,ingrediente_id_ingredient,procent)values (2000,3010,15)'
# cursor.execute(query)
# conn.commit()
ascunde=0

win = Tk()
clicked1 = StringVar(win)
textDepasire = Label(win, text="Nu exista cantitatea dorita:")
def adaugaPoze(win):
   image1 = Image.open("background_cos.jpeg")
   test = ImageTk.PhotoImage(image1)
   label1 = Label(win,image=test)
   label1.image = test
   label1.place(x=0, y=3,relheight=1,relwidth=1)


class Cos:
   def __int__(self):
      self.coduri_ambalaje=[]
      self.pret=[]
      self.cantitate=[]
      self.total=0
      self.gramaj=[]
      self.coduri_parfum=[]
      self.nume_parfumuri=[]
      self.stocuri_ambalaje=[]
      self.id_ingredient=[]
      self.stocuri_ingrediente=[]
      self.text=None
   def set_coduri_ambalaje(self,n):
      self.coduri_ambalaje=n
   def set_nume_parfumuri(self,n):
      self.nume_parfumuri=n
   def set_coduri_parfum(self, n):
      self.coduri_parfum = n
   def set_pret(self, n):
      self.pret = n
   def set_cantitate(self, n):
      self.cantitate = n
   def set_total(self,n):
      self.total=n
   def set_gramaj(self,n):
      self.gramaj=n
   def set_stocuri_ambalaje(self,n):
      self.stocuri_ambalaje = n
   def set_id_ingredient(self,n):
      self.id_ingredient = n
   def set_stocuri_ingrediente(self,n):
      self.stocuri_ingrediente = n
class Client:
   def __init__(self):
      self.nume_distribuitor=None
      self.nume_parfum=None
      self.gramaj=None
      self.nr_bucati=None
      self.gramaj_disponibil=['']
      self.cod_ambalaj=None
      self.pret=None
      self.nr_comanda=None
   def set_nume_distribuitor(self,n):
      self.nume_distribuitor=n
   def set_nume_parfum(self, n):
      self.nume_parfum = n
   def set_gramaj(self, n):
      self.gramaj = n
   def set_nr_bucati(self,n):
      self.nr_bucati=n
   def set_gramaje_disponibile(self,n):
      self.gramaj_disponibil=n
   def set_nr_comanda(self,n):
      self.nr_comanda=n



def evaluare_nr_bucati(event):
   nr=nr_bucati.get()
   client.set_nr_bucati(nr)
   Label(win, text="x").place(relx=2.5 / 10, rely=7 / 10)
   Label(win, text=str(client.nr_bucati) ).place(relx=3.5 / 10, rely=7 / 10)
   Label(win, text="="+str(int(client.nr_bucati)*int(client.pret))).place(relx=4.5 / 10, rely=7 / 10)

def evaluare_nr_comanda(event):
   nr=nr_comanda.get()
   client.set_nr_comanda(nr)

####JOIN######
def evaluare_nume_parfum(event):
   nume_parfum=clicked.get()
   nume_parfum=nume_parfum[2:len(nume_parfum)-3]
   client.set_nume_parfum(nume_parfum)
   cursor.execute('select id_parfum from esenta where nume_parfum=\''+str(client.nume_parfum)+'\'')
   rows = cursor.fetchall()
   rows=str(rows)
   rows=rows[2:len(rows)-3]
   client.cod_parfum=rows
   cursor.execute('select gramaj from ambalaje where esenta_id_parfum=\'' + str(client.cod_parfum) + '\'')
   rows = cursor.fetchall()
   vect=[]
   for i in rows:
      i = str(i)
      i=i[1:len(i)-2]
      vect.append(i)
   if not vect:
      vect.append("nu avem niciun produs disponibil")
   client.set_gramaje_disponibile(vect)
   create_gramaje()

def create_gramaje():
   clicked1.set("select a weight")
   gramaj = OptionMenu(win, clicked1, *client.gramaj_disponibil, command=evaluare_gramaj)
   gramaj.place(relx=2.5 / 10, rely=4.5 / 10)


def evaluare_gramaj(event):
   gramaj=clicked1.get()
   client.set_gramaj(gramaj)
   adauga_pret()
   client.gramaj_disponibil.clear()

def evaluare_nume_distribuitor(event):
   nume=nume_distribuitor.get()
   client.set_nume_distribuitor(nume)

####JOIN######
#adauga pret jos
def adauga_pret():
   cursor.execute('select id_ambalaj from ambalaje where esenta_id_parfum=' + str(client.cod_parfum) + 'and gramaj='+str(client.gramaj)+'')
   rows = cursor.fetchall()
   rows=str(rows)
   rows=rows[2:len(rows)-3]
   client.cod_ambalaj=rows
   cursor.execute(
      'select pret from ambalaje where id_ambalaj=' + str(client.cod_ambalaj) + '')
   row = cursor.fetchall()
   row = str(row)
   row = row[2:len(row) - 3]
   client.pret=row
   Label(win, text=str(client.pret)+"   RON").place(relx=1 / 10, rely=7 / 10)

def verificare_stocuri():
         print(cos.stocuri_ambalaje)
         if client.cod_ambalaj in cos.coduri_ambalaje:
            print("se afla")
            index = cos.coduri_ambalaje.index(client.cod_ambalaj)
            print(index)
            print(cos.stocuri_ambalaje)
            if(int(client.nr_bucati)>int(cos.stocuri_ambalaje[index])):
               return 1
            cos.stocuri_ambalaje[index] =int(cos.stocuri_ambalaje[index]) - int(client.nr_bucati)
            ingrediente = []
            cursor.execute(
               'select ingrediente_id_ingredient from formula where esenta_id_parfum=' + str(client.cod_parfum) + '')
            rows = cursor.fetchall()
            for i in rows:
               i = str(i)
               i = i[1:len(i) - 2]
               i = int(i)
               ingrediente.append(i)

            cursor.execute(
                  'select procent from formula where esenta_id_parfum=' + str(client.cod_parfum) + '')
            rows = cursor.fetchall()
            procente = []
            for i in rows:
               i = str(i)
               i = i[1:len(i) - 2]
               i=int(i)
               procente.append(i)
            for i in range(0, len(ingrediente)):
               if ingrediente[i] in cos.id_ingredient:
                  index = cos.id_ingredient.index(ingrediente[i])
                  if float(client.nr_bucati) * float(client.gramaj) * float(float(procente[i])/100) > float(
                          cos.stocuri_ingrediente[index]):
                     return 1
                  cos.stocuri_ingrediente[index] = float(cos.stocuri_ingrediente[index]) - float(client.nr_bucati) * float(
                     client.gramaj) * float(float(procente[i])/100)
               else:
                  cursor.execute(
                     'select cantitate from ingrediente where id_ingredient=' + str(ingrediente[i]) + '')
                  rows = cursor.fetchall()
                  rows = str(rows)
                  rows = rows[2:len(rows) - 3]
                  cantitate = rows
                  if float(client.nr_bucati)*float(client.gramaj)*float(float(procente[i])/100)>float(cantitate):
                     return 1
                  cos.stocuri_ingrediente.append(
                     float(cantitate) - float(client.nr_bucati) * float(client.gramaj) * float(float(procente[i])/100))
                  cos.id_ingredient.append(ingrediente[i])
         else:
            print("produsul nu se afla deja in cos")
            cursor.execute(
               'select stoc from ambalaje where id_ambalaj=' + str(client.cod_ambalaj) + '')
            stoc_ambalaj_total = cursor.fetchall()
            stoc_ambalaj_total = str(stoc_ambalaj_total)
            stoc_ambalaj_total = stoc_ambalaj_total[2:len(stoc_ambalaj_total) - 3]
            if (int(client.nr_bucati) > int(stoc_ambalaj_total)):
               return 1
            cos.coduri_ambalaje.append(client.cod_ambalaj)
            cos.stocuri_ambalaje.append(int(stoc_ambalaj_total) - int(client.nr_bucati))

            ingrediente = []
            cursor.execute(
               'select ingrediente_id_ingredient from formula where esenta_id_parfum=' + str(client.cod_parfum) + '')
            rows = cursor.fetchall()
            for i in rows:
               i = str(i)
               i = i[1:len(i) - 2]
               i = float(i)
               ingrediente.append(i)

            cursor.execute(
               'select procent from formula where esenta_id_parfum=' + str(client.cod_parfum) + '')
            rows = cursor.fetchall()
            procente = []
            for i in rows:
               i = str(i)
               i = i[1:len(i) - 2]
               procente.append(i)
            for i in range (0,len(ingrediente)):
               if ingrediente[i] in cos.id_ingredient :
                  index = cos.id_ingredient.index(ingrediente[i])
                  if float(client.nr_bucati)*float(client.gramaj)*float(float(procente[i])/100)>float(cos.stocuri_ingrediente[index]):
                     return 1
                  cos.stocuri_ingrediente[index]=float(cos.stocuri_ingrediente[index])-float(client.nr_bucati)*float(client.gramaj)*float(float(procente[i])/100)
               else:
                  cursor.execute(
                     'select cantitate from ingrediente where id_ingredient=' + str(ingrediente[i]) + '')
                  rows = cursor.fetchall()
                  rows = str(rows)
                  rows = rows[2:len(rows) - 3]
                  cantitate=rows
                  if float(client.nr_bucati)*float(client.gramaj)*float(float(procente[i])/100)>float(cantitate):
                     return 1
                  cos.stocuri_ingrediente.append(float(cantitate)-float(client.nr_bucati)*float(client.gramaj)*float(float(procente[i])/100))
                  cos.id_ingredient.append(ingrediente[i])

         return 0

def adauga_in_cos():
   if(verificare_stocuri()==0):
      cos.pret.append(client.pret)
      cos.coduri_parfum.append(client.cod_parfum)
      cos.cantitate.append(client.nr_bucati)
      cos.gramaj.append(client.gramaj)
      cos.nume_parfumuri.append(client.nume_parfum)
      total=0
      for i in range (0,len(cos.nume_parfumuri)):
         total=total+int(cos.cantitate[i])*int(cos.pret[i])
         inaltime=i/2+3.1
         cos.text=Label(win, text= str(cos.nume_parfumuri[i])+ "---->"+str(cos.cantitate[i])+"x"+ str(cos.pret[i]) + "   RON").place(relx=6.75/ 10,rely=inaltime / 10)
      cos.set_total(total)
      text =Label(win, text="TOTAL:").place(
      relx = 6.75 / 10, rely = 7.5 / 10)
      Label(win,
            text=str(cos.total)+"   RON").place(
         relx= 7.75/ 10, rely=7.5 / 10)

def refa_int():
   adaugaPoze(win)
   # nume distribuitor
   Label(win, text="Nume Distribuitor").place(relx=1 / 10, rely=2.5 / 10)
   nume_distribuitor = Entry(win, width=30, borderwidth=5)
   nume_distribuitor.bind("<Return>", evaluare_nume_distribuitor)
   nume_distribuitor.place(relx=2.5 / 10, rely=2.5 / 10)

   # nume parfum
   clicked = StringVar(win)
   clicked.set("Select an perfume")
   Label(win, text="Nume parfum").place(relx=1 / 10, rely=3.5 / 10)
   cursor.execute('select nume_parfum from esenta')
   row = cursor.fetchall()
   nume_parfum = OptionMenu(win, clicked, *row, command=evaluare_nume_parfum)
   nume_parfum.place(relx=2.5 / 10, rely=3.4 / 10)
   # gramaj
   Label(win, text="Gramaj").place(relx=1 / 10, rely=4.5 / 10)

   # nr_bucati
   Label(win, text="Nr bucati").place(relx=1 / 10, rely=5.5 / 10)
   nr_bucati = Entry(win, width=30, borderwidth=5)
   nr_bucati.bind("<Return>", evaluare_nr_bucati)
   nr_bucati.place(relx=2.5 / 10, rely=5.5 / 10)

   # nr comanda
   Label(win, text="Nr comanda").place(relx=0.5 / 10, rely=9 / 10)
   nr_comanda = Entry(win, width=3, borderwidth=5)
   nr_comanda.bind("<Return>", evaluare_nr_comanda)
   nr_comanda.place(relx=1.5 / 10, rely=9 / 10)
   AddButton = Button(win, width=15, text="Add", fg="black", command=adauga_in_cos).place(relx=4 / 10, rely=8 / 10)
   CommandButton = Button(win, width=15, text="Cancel", command=anulare).place(relx=0.75 / 10, rely=8 / 10)
   CommandButton = Button(win, width=15, text="Cancel the order", command=anulareComanda).place(relx=2 / 10,
                                                                                                rely=9 / 10)
   CommandButton = Button(win, text="Send the order", command=send_order).place(relx=8.5 / 10, rely=9 / 10)
def send_order():
   cursor.execute(
      'select id_distribuitor from distribuitor where nume_distr=\'' + str(client.nume_distribuitor) + '\'')
   rows = cursor.fetchall()
   #daca exista numele il prelucram luam id ul
   if rows:
      rows = str(rows)
      rows = rows[2:len(rows) - 3]
   #daca nu exista numele il adaugam in distribuitori si luam id_ul lui
   else:
      query = 'insert into distribuitor (id_distribuitor,nume_distr) values (null,\''+str(client.nume_distribuitor) +'\')'
      cursor.execute(query)
      conn.commit()
      cursor.execute(
         'select id_distribuitor from distribuitor where nume_distr=\'' + str(client.nume_distribuitor) + '\'')
      rows = cursor.fetchall()
      rows = str(rows)
      rows = rows[2:len(rows) - 3]
   cursor.execute(
      'select max(nr_comanda) from cereri')
   nr_comanda = cursor.fetchall()
   nr_comanda=str(nr_comanda)
   nr_comanda=nr_comanda[2:len(nr_comanda)-3]
   nr_comanda = int(nr_comanda) + 1
   for i in range (0,len(cos.nume_parfumuri)):
      query = 'insert into cereri (nr_comanda,distribuitor_id_distribuitor,ambalaje_id_ambalaj,nr_bucati,data)values (' +str(nr_comanda)+','+ str(
            rows) + ',' + str(cos.coduri_ambalaje[i]) + ',' + str(cos.cantitate[i]) + ',sysdate)'
      cursor.execute(query)
      query = 'update ambalaje set stoc=' + str(cos.stocuri_ambalaje[i]) + 'where id_ambalaj=' + str(
            cos.coduri_ambalaje[i]) + ''
      cursor.execute(query)
   for j in range(0, len(cos.stocuri_ingrediente)):
      query = 'update ingrediente set cantitate=' + str(
            cos.stocuri_ingrediente[j]) + 'where id_ingredient=' + str(
            cos.id_ingredient[j]) + ''
      cursor.execute(query)
   conn.commit()
   cos.coduri_ambalaje.clear()
   cos.pret.clear()
   cos.cantitate.clear()
   cos.total = 0
   cos.gramaj = []
   cos.coduri_parfum.clear()
   cos.nume_parfumuri.clear()
   cos.stocuri_ambalaje.clear()
   cos.id_ingredient.clear()
   cos.stocuri_ingrediente.clear()
   client.nume_distribuitor = None
   client.nume_parfum = None
   client.gramaj = None
   client.nr_bucati = None
   client.gramaj_disponibil.clear()
   client.cod_ambalaj = None
   client.pret = None
   client.nr_comanda = None
   refa_int()
def anulare():
   index=cos.coduri_ambalaje.index(client.cod_ambalaj)
   if(cos.cantitate[index]==client.nr_bucati):
      cos.cantitate.pop(index)
      cos.coduri_ambalaje.pop(index)
      cos.total=int(cos.total)-int(client.nr_bucati)*int(client.pret)
      cos.pret.pop(index)
      cos.gramaj.pop(index)
      cos.coduri_parfum.pop(index)
      cos.nume_parfumuri.pop(index)
      cos.stocuri_ambalaje.pop(index)

def anulareComanda():
   query='select nr_comanda from cereri'
   cursor.execute(query)
   conn.commit()
   nr = cursor.fetchall()
   nr_comenzi=[]
   for i in nr:
      i=str(i)
      i=i[1:-2]
      nr_comenzi.append(i)
   if client.nr_comanda in nr_comenzi:
      cursor.execute('select nr_comanda from cereri c, distribuitor d where c.distribuitor_id_distribuitor=d.id_distribuitor and nume_distr=\''+client.nume_distribuitor+'\'')
      nr=cursor.fetchall()
      nr_n=[]
      for i in nr:
         i=str(i)
         i=i[1:-2]
         nr_n.append(i)
      if client.nr_comanda in nr_n:
         cursor.execute('select a.stoc from ambalaje a, cereri c where a.id_ambalaj=c.ambalaje_id_ambalaj and c.nr_comanda='+client.nr_comanda)
         conn.commit()
         stoc = cursor.fetchall()
         cursor.execute(
            'select c.nr_bucati from ambalaje a, cereri c where a.id_ambalaj=c.ambalaje_id_ambalaj and c.nr_comanda=' + client.nr_comanda)
         conn.commit()
         nr_bucati_com=cursor.fetchall()
         cursor.execute(
            'select c.ambalaje_id_ambalaj from ambalaje a, cereri c where a.id_ambalaj=c.ambalaje_id_ambalaj and c.nr_comanda=' + client.nr_comanda)
         conn.commit()
         id_ambalaje = cursor.fetchall()
         id_ambalaje_n=[]
         nr_bucati_com_n=[]
         stoc_n=[]
         gramaje=[]
         for i in id_ambalaje:
            i = str(i)
            i = i[1:-2]
            id_ambalaje_n.append(i)
            cursor.execute('select gramaj from ambalaje where id_ambalaj=' + i)
            row=cursor.fetchall()
            row=str(row)
            row=row[2:-3]
            gramaje.append(row)

         id_parfum=[]
         for i in id_ambalaje_n:
            cursor.execute(
            'select a.esenta_id_parfum from ambalaje a, cereri c where a.id_ambalaj=c.ambalaje_id_ambalaj and id_ambalaj='+i+'and c.nr_comanda='+client.nr_comanda)
            row=cursor.fetchall()
            row=str(row)
            row=row[2:-3]
            id_parfum.append(row)
         for i in nr_bucati_com:
            i = str(i)
            i = i[1:-2]
            nr_bucati_com_n.append(i)
         j=0
         for i in stoc:
            i=str(i)
            i=i[1:-2]
            stoc_n.append(i)
            stoc_nou=int(i)+int(nr_bucati_com_n[j])
            cursor.execute('merge into ambalaje using cereri on (ambalaje.id_ambalaj=cereri.ambalaje_id_ambalaj) when matched then update set ambalaje.stoc='+str(stoc_nou)+' where cereri.nr_comanda='+str(client.nr_comanda)+'and ambalaje.id_ambalaj='+str(id_ambalaje_n[j]))
         for parfum in id_parfum:
            cursor.execute('select procent from formula where esenta_id_parfum=' + parfum)
            row = cursor.fetchall()
            procente = []
            for it in row:
               it=it = str(it)
               it = it[1:-2]
               procente.append(it)
            cursor.execute('select ingrediente_id_ingredient from formula where esenta_id_parfum='+ parfum)
            row = cursor.fetchall()
            ingrediente=[]
            for i in row:
               i=str(i)
               i=i[1:-2]
               ingrediente.append(i)
            index = 0
            for i in ingrediente:
               cursor.execute('select cantitate from ingrediente where id_ingredient='+i)
               row = cursor.fetchall()
               row=str(row)
               row=row[2:-3]
               cantitate_noua=int(row)+int(nr_bucati_com_n[id_parfum.index(parfum)])*int(procente[index])*int(gramaje[id_parfum.index(parfum)])
               index+=1
               cursor.execute('update ingrediente set cantitate='+str(cantitate_noua)+'where id_ingredient='+i)
            j+=1
         cursor.execute('delete from cereri where nr_comanda='+str(client.nr_comanda))
         conn.commit()



   conn.commit()
if __name__ == '__main__':
   #creeare fereastra
   client=Client()
   cos=Cos()
   cos.set_coduri_ambalaje([])
   cos.set_coduri_parfum([])
   cos.set_pret([])
   cos.set_cantitate([])
   cos.set_gramaj([])
   cos.set_nume_parfumuri([])
   cos.set_stocuri_ambalaje([])
   cos.set_id_ingredient([])
   cos.set_stocuri_ingrediente([])
   win.geometry("1200x900")
   win.title("Votre parfumerie préférée")
   adaugaPoze(win)
   #conectare
   user = 'bd001'
   password = 'oana2106*'
   cx_Oracle.init_oracle_client(
      lib_dir=r"C:\Users\Oana\Documents\an 3\tema_bd\instantclient-basic-windows.x64-21.7.0.0.0dbru\instantclient_21_7")
   dsn_tns = cx_Oracle.makedsn('bd-dc.cs.tuiasi.ro', '1539', service_name='orcl')
   conn = cx_Oracle.connect(user=user, password=password, dsn=dsn_tns)
   cursor = conn.cursor()

   #nume distribuitor
   Label(win, text="Nume Distribuitor").place(relx=1 / 10, rely=2.5 / 10)
   nume_distribuitor= Entry(win, width=30, borderwidth=5)
   nume_distribuitor.bind("<Return>", evaluare_nume_distribuitor)
   nume_distribuitor.place(relx=2.5 / 10, rely=2.5 / 10)

   #nume parfum
   clicked = StringVar(win)
   clicked.set("Select an perfume")
   Label(win, text="Nume parfum").place(relx=1 / 10, rely=3.5 / 10)
   cursor.execute('select nume_parfum from esenta')
   row = cursor.fetchall()
   nume_parfum = OptionMenu(win,clicked,*row,command=evaluare_nume_parfum)
   nume_parfum.place(relx=2.5 / 10, rely=3.4 / 10)
   #gramaj
   Label(win, text="Gramaj").place(relx=1 / 10, rely=4.5 / 10)

   #nr_bucati
   Label(win, text="Nr bucati").place(relx=1 / 10, rely=5.5 / 10)
   nr_bucati = Entry(win, width=30, borderwidth=5)
   nr_bucati.bind("<Return>", evaluare_nr_bucati)
   nr_bucati.place(relx=2.5 / 10, rely=5.5 / 10)

   # nr comanda
   Label(win, text="Nr comanda").place(relx=0.5 / 10, rely=9 / 10)
   nr_comanda = Entry(win, width=3, borderwidth=5)
   nr_comanda.bind("<Return>", evaluare_nr_comanda)
   nr_comanda.place(relx=1.5 / 10, rely=9 / 10)
   AddButton = Button(win, width=15, text="Add", fg="black",command=adauga_in_cos).place(relx=4 / 10, rely=8 / 10)
   CommandButton = Button(win, width=15, text="Cancel",command=anulare).place(relx=0.75 / 10, rely=8 / 10)
   CommandButton = Button(win, width=15, text="Cancel the order",command=anulareComanda).place(relx=2 / 10, rely=9 / 10)
   CommandButton = Button(win, text="Send the order", command=send_order).place(relx=8.5 / 10, rely=9 / 10)
   win.mainloop()

