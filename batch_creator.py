import os
import shutil

geo_dir = 'sculpts/'
img_dir = 'images/'
master_blend = 'anton.SachaJafri_System_ZERO_7k.blend'

geos = os.listdir(geo_dir)
imgs = os.listdir(img_dir)

#for i in range(0,len(geos)):
for i in range(0,9):
    newName = geos[i].split('.')[0]+'_'+imgs[i].split('.')[0]+'.blend'
    shutil.copyfile(master_blend,newName)
    os.system('blender -b '+newName+' -- '+geos[i]+' '+imgs[i])
    #os.system('blender -b '+newName+' -o //previews/'+newName.split(".")[0]+'_ -f 3600')
    #os.remove(newName.split(".")[0]+".blend1")
    shutil.move(newName,'batches/')
