# python 3.3

import os
import time
import sys


Anno_Mese = time.strftime("%Y_%m")
#print (Anno_Mese)
try:
    f_log = open ("c:\\temp\\" + Anno_Mese + "_delete_old_files.log",'a')
    #print (f_log.name)
except IOError:
    print ("Impossibile aprire il file di log")
    sys.exit(2)
    
f_log.write (time.asctime(time.localtime()))
f_log.write (" *****************************************************************************************\n")
f_log.write (time.asctime(time.localtime()))
f_log.write (" Inizio pulizia coppie di file idx e pdf\n")

### Leggo i parametri del file ini
try:
    f_ini = open("c:\\temp\\delete_old_files.ini",'r')
except IOError:
    f_log.write (time.asctime(time.localtime()))
    f_log.write (" 10 Errore nell'aprire il file ini delete_old_files.ini\n")
    sys.exit (2)
    
# Leggo i giorni 
for linea in f_ini:
    #print (linea,end='')
    base_linea = linea.split ("=")
    if base_linea[0] == "days":
        days = base_linea[1]
        days = days.rstrip('\n')
    #if base_linea[0] == "logfile_dir":
    #    logfile_dir = base_linea[1]
#print (days)
#print (logfile_dir)
f_ini.close()




# Riapro il file ini per leggere le directory
try:
    f_ini = open("c:\\temp\\delete_old_files.ini",'r')
    #print ("File ini",f_ini.name, "aperto..")
except:
    IOError
    f_log.write (time.asctime(time.localtime()))
    f_log.write (" 20 Errore nell'aprire il file ini delete_old_files.ini\n")
    sys.exit(2)

for linea in f_ini:
    #print (linea)
    base_linea = linea.split ("=")
    if base_linea[0] == "dir":
        #path = "c:\\temp"
        path = base_linea[1]
        path_new = path.replace ("\"","")
        path_new = path_new.replace ("\n","")
        f_log.write (time.asctime(time.localtime()))
        f_log.write (" Nuova Dir: " + str (path_new) + "\n")
        #print (path_new)
        
        os.chdir (path_new)
        f_log.write (time.asctime(time.localtime()))
        f_log.write (" Change Dir: " + str (os.path.abspath('.')) + "\n")
        #print (os.path.abspath('.'))

        now = time.time()
        #print (now)

        for f in os.listdir(path_new):
            #f = (os.path.join(path, f))
            #print ("File:", f)
            
            #print ("Now -7 gg: ", now - 7 * 86400)
            #print ("Differenza;", stato - now - 7 * 86400)

            if os.path.isfile(f):
                base = f.split (sep='.')
                #print (base[0])
                if base[1]=="idx":
                    stato = os.stat(f).st_mtime 
                    #print ("Stato File:",stato)
                    if  stato < (now - int(days) * 86400):  
                        #os.remove(os.path.join(path, f))
                        #print ("*****",f)
                        #base e' una lista
                        for f_pdf in os.listdir(path_new):
                            #print ("**" + str(f_pdf))
                            f_pdf_base = f_pdf.split (sep='.')
                            try:
                                if f_pdf_base[1] == "pdf":
                                    if f_pdf_base[0] == base[0]:
                                        print ("pdf trovato " + str(f_pdf_base) + "\n" )
                                        os.remove (f)
                                        f_log.write (time.asctime(time.localtime()))
                                        f_log.write (" Idx eliminato: " + str (os.path.abspath (f)) + "\n")
                                        os.remove (f_pdf)
                                        f_log.write (time.asctime(time.localtime()))
                                        f_log.write (" Pdf eliminato: " + str (os.path.abspath(f_pdf)) + "\n")
                                        continue
                                else:
                                    #print ("File non con estensione pdf...")
                                    continue
                            except:
                                print ("altro giro...\n")
                                continue
                            
                        #print (base[0],file = f_log)
                        
                        #if os.path.isfile (os.path.join(base[0],"pdf")): #& os.path.exists (base[0]+"idx"):
                        #    print (base[0], "cancellato")
                        
f_log.write (time.asctime(time.localtime()))
f_log.write (" Fine pulizia...\n")
f_ini.close()
f_log.close()
