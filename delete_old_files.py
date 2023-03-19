import os, time, sys

### Leggo i parametri del file ini
try:
    f_ini = open("delete_old_files.ini",'r')
    #print ("File ini",f_ini.name, "aperto..")
except IOError:
    print ("Impossibile aprire il file ini: delete_old_files.ini ")
    sys.exit (2)
    
for linea in f_ini:
    #print (linea,end='')
    base_linea = linea.split ("=")
    if base_linea[0] == "days":
        days = base_linea[1]
        days = days.rstrip('\n')
    #if base_linea[0] == "logfile_dir":
    #    logfile_dir = base_linea[1]

f_ini.close()

#print (days)
#print (logfile_dir)

Anno_Mese = time.strftime("%Y_%m")
#print (Anno_Mese)
try:
    log_file = open ("delete_old_files_"+Anno_Mese+".log",'a')
    #print (log_file.name)
except IOError:
    print ("Impossibile aprire il file di log")
    sys.exit(2)
    
#print (time.asctime(time.localtime()),"Inizio pulizia coppie di file idx e pdf più vecchi di",days,"giorni...", file = log_file)
print (time.asctime(time.localtime()),"Inizio pulizia coppie di file idx e pdf - almeno",days,"giorni...", file = log_file)

try:
    f_ini = open("delete_old_files.ini",'r')
    #print ("File ini",f_ini.name, "aperto..")
except:
    IOError
    print ("Impossibile aprire il file ini")
    sys.exit(2)


for linea in f_ini:
    #print (linea)
    base_linea = linea.split ("=")
    if base_linea[0] == "dir":
        #path = "c:\\temp"
        path = base_linea[1]
        path_new = path.replace ("\"","")
        path_new = path_new.replace ("\n","")
        #print (path_new)
        
        os.chdir (path_new)
        #print (os.path.abspath('.'))

        now = time.time()
        #print (now)

        for f in os.listdir(path_new):
            #f = (os.path.join(path, f))
            #print ("File:", f)
            
            #print ("Now -7 gg: ", now - 7 * 86400)
            #print ("Differenza;", stato - now - 7 * 86400)

            if os.path.isfile(f):
                stato = os.stat(f).st_mtime 
                #print ("Stato File:",stato)
                base = f.split (sep='.')
                #print (base[0])
                if base[1]=="idx":
                    if  stato < (now - int(days) * 86400):  
                        #os.remove(os.path.join(path, f))
                        print ("*****",f)
                        #base è una lista
                        for f_pdf in os.listdir(path_new):
                            f_pdf_base = f_pdf.split (sep='.')
                            if f_pdf_base[1] == "pdf":
                                if f_pdf_base[0] == base[0]:
                                    os.remove (f)
                                    print ("idx eliminato: ",os.path.abspath (f),file = log_file)
                                    os.remove (f_pdf)
                                    print ("pdf eliminato: ",os.path.abspath(f_pdf),file = log_file)
                                    continue
                        #print (base[0],file = log_file)
                        
                        #if os.path.isfile (os.path.join(base[0],"pdf")): #& os.path.exists (base[0]+"idx"):
                        #    print (base[0], "cancellato")
                        

print (time.asctime(time.localtime()),"Fine pulizia...", file = log_file)

f_ini.close()
log_file.close()
