#!/usr/bin/python


import sys
import cv2
import string
from os import listdir
from os.path import isfile, join
import numpy as np
import random

labels = ['Apuleia', 'Aspidosperma', 'Astronium', 'Byrsonima', 'Calophyllum', 'Cecropia', 'Cedrelinga', 'Cochlospermum', 'Combretum', 'Copaifera' ]

PATHSRC = '.'
PATHDST = './tr'
LISTA = '/Users/lesoliveira/Dropbox/carvao/lista.txt'

PATCHSIZE = 256
PATCHS = 40

def getlabel(img_path):

	name =  img_path.split(' ')
	print name
	#print name
	#label_name = './labels/' + name[0] + '.inf'
	#fp = open(label_name)
	#line = fp.readline()
	#label = line.split('|')
	#fp.close
	return name[0]




def createPatches(img_path, img_name, label, seq, flista):


	fname = img_path + '/' +  img_name
	print fname
	img = cv2.imread(fname, 0) ;
	   
	h, w =  img.shape
	h= 950
	
	for i in range(PATCHS):
		print w, h
		x = random.randrange(0, w-PATCHSIZE)
		y = random.randrange(0, h-PATCHSIZE)
	   
		new_img = img[y:y+PATCHSIZE, x:x+PATCHSIZE] # Crop from x, y, w, h

		nfname =  ("%s/%s_%03d_%03d.tif" % (PATHDST, label, seq, i))
		print nfname
		cv2.imwrite(nfname, new_img)
		
		#if (label == 'B'):
		#lst =  ("%s_%03d.tif 0\n" % (label, i))
		#print lst
		#else:
		#	lst =  ("%s_%03d_%03d.tif 1\n" % (label, seq, i))
	   
		#flista.write(lst)


   

####################################
#### MAIN
####################################

if __name__ == "__main__":

	if len(sys.argv) != 1:
		sys.exit(" - Usage: createPath")

	seq = 0
	
	## arquivo para salvar a lista com imagens e labels.
	lname = LISTA
	flista = open( lname, "w")
	j = 0
	oldlabel = ''

	onlyfiles = [ f for f in listdir(PATHSRC) if isfile(join(PATHSRC,f)) ]
	for i in onlyfiles:
		
		print i
		tipo = i.split('.')
		if tipo[1] == 'tif':
			
			label = getlabel(i)
			
			if (j == 1):
				oldlabel = label
			
			print 'Label and OldLabel--------'
			print j, label, oldlabel
			
			if(label != oldlabel):
				seq = 0
				oldlabel = label
	

		
			createPatches( PATHSRC, i, label, seq, flista)
			seq = seq + 1
			
			#print 'croping ', i, label
			#img = './tif/' + i
			#crop( i, img, label );
		j = j +1	
	flista.close()
	


