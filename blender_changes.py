import sys
import bpy

argv = sys.argv
if "--" in argv:
    argv = argv[argv.index("--") + 1:]  # get all args after "--"
    
    print(argv)
    
    
    geo_name = argv[0]
    tex_name = argv[1]
    
    #tex_name = '23b.JPG'
    #geo_name = 'Object_0033.abc'
    
    if not tex_name:
        print("no texture")
        exit()
    
    if not geo_name:
        print("no geometry")
        exit()
    
    subject = bpy.data.objects['sculpture']
    subj_material = bpy.data.materials['sculpt']
    subj_image = bpy.data.images['sacha']

    subj_image.filepath = '//images/'+tex_name

    #bpy.ops.view3d.snap_cursor_to_center()
    bpy.ops.wm.alembic_import(filepath='//sculpts/'+geo_name)
    newSubject = bpy.context.selected_objects[0]
    newSubject.data.materials.append(subj_material)


    bpy.data.objects.remove(subject,do_unlink=True)
    newSubject.name = 'sculpture'
    
    bpy.context.scene.render.filepath = '//out/'+geo_name+'_'+tex_name+'/#####.jpg'
    bpy.ops.file.pack_all()
    bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
