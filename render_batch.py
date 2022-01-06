import os

batch_dir = 'batches/'
files = os.listdir(batch_dir)

for f in files:
    os.system('blender -b '+batch_dir+f+' -a')
    fname = f.split('.')[0]
    os.system('ffmpeg -framerate 25 -i '+batch_dir+'out/'+fname+'/%05d.png -c:v libx264 -pix_fmt yuv420p ~/gdrive/projects.active/anton.Sculptures/out/sp/'+fname+'.mp4')
