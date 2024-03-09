#############################################################################################################
#############################################################################################################
# Formatiert Discogs-Tracklists ; for AGB
		# Sucht Songs/title aus der Tracklist der Album_HTML-File und schreibt sie in TXT-File
		# ==> Extrahiert ebenso die Tracklist aus Sampler_HTML-Files, allerdings KEINE artists
		# ==> Funktioniert nur für ReleaseEntry-HTMLs, noch nicht für MasterEntry-HTMLs
#############################################################################################################
#############################################################################################################

import os
import glob
import re
import html



### Pfad/Quell-File : im Programm-/Arbeits-Ordner ##############################

path = os.getcwd()


### HTML-File finden ###########################################################

files = glob.glob(path + "/*")
ext_list = ['.htm', '.html']

for i in files:
    if os.path.splitext(i)[1] in ext_list:
        work_file = i
        print('work_file : \n')
        print(work_file)


### HTML-File durchsuchen ######################################################

f = open(work_file,"r", encoding="utf-8")

### Kompletter File-Inhalt als String(/Liste) 

text = f.read()
f.close()


#####  Variable "text" in neue Liste aufteilen, Elemente auf target_words durchsuchen, Elemente einkürzen
##########################################################################################################

html_list = text.split('><')

title_list = []

for i in html_list:
    if re.search('span.+trackTitle_.+', i):
        title_esc = i.split('>')[1].split('<')[0]                       # Den ersten Split nochmals splitten, jeweils angesprochen über Indizes der durch split() entstehenden Listen
        #print(title_esc)
        title = html.unescape(title_esc)				# converts HTML-EscapeCharacters to String
        #print(title)
        title_list.append(title)
        #break


##### Ergebnisse im richtigen Format in TXT schreiben
########################################################################

print('\n\ntitle_list: \n')

end_format = open("end_format.txt","w")

for cnt, i in enumerate(title_list, start=1):
	if cnt != len(title_list):					# if nicht letzter_SongTitel
		end_format.write(i)
		end_format.write(' ; \n')
		print(cnt, i)
	else:
		end_format.write(i)
		print(cnt, i)
		
end_format.close()

print('\n\nAnzahl der ermittelten Songs  : ', len(title_list))


##### geschriebene TXT in (EDITOR-)PROZESS-FENSTER öffnen (Inhalt zum kopieren bereit), nach_Frage wieder SCHLIEßEN & LÖSCHEN
##############################################################################################################################

###  ÖFFNEN  ###
import subprocess
OpenIt = subprocess.Popen(['notepad.exe', 'end_format.txt'])

###  USER_INPUT  ###
del_f = input("\n\nEditor-Fenster wird nun geschlossen und die .txt-Datei gelöscht. \n\
Soll die .htm-/.html-Datei ebenfalls gelöscht werden? \nEingabe  :  ENTER  =  Ja \n\t  n+ENTER  =  Nein\n")

###  SCHLIEßEN  ###
OpenIt.terminate()

###  LÖSCHEN  ###
import os
os.remove("end_format.txt")

if del_f == '':
	os.remove(work_file)
