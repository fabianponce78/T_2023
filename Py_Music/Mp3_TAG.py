import os
import eyed3


Str_Line = '_____________________________________________________________'
path ="C:/#_FP_APEX/#_DEV/#_Py_FP/Py_Test/Py_Music/Music_Files/"
path =".\Music_Files"
#path = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Py_Music\Music_Files\Chris Cornell'



#/////////////////////////////////////////////////////////////////
def fn_Get_Genre(Str_Mp3):
    print(Str_Line , "fn_Get_Genre")
    print("Str_Mp3 = " , Str_Mp3)
    
    audio=eyed3.load(Str_Mp3)    
    Str_Title = audio.tag.title
    Str_Artist = audio.tag.artist
    Str_Album = audio.tag.album
    Str_Album_Artist = audio.tag.album_artist
    Str_Composer = audio.tag.composer    
    Str_genre = audio.tag.genre
    
    if Str_genre is None:
        print('\t Str_genre is None')
        val_Str = input("\t Enter your value: ")    ###---------
        print(val_Str)                              ###---------
        
        file = eyed3.load(Str_Mp3)
        file.initTag()
        file.tag.title = val_Str                    ###---------
        #---------------------------------------------
        file.tag.title = Str_Title
        file.tag.artist = Str_Artist
        file.tag.album = Str_Album
        file.tag.album_artist = Str_Album
        file.tag.composer = Str_Composer
        
        file.tag.genre = val_Str                    ###---------
        
        
        #---------------------------------------------
        file.tag.save()


#/////////////////////////////////////////////////////////////////
def fn_Get_Title(Str_Mp3):
    print(Str_Line , "fn_Get_Title")
    print("Str_Mp3 = " , Str_Mp3)
    
    audio=eyed3.load(Str_Mp3)    
    Str_Title = audio.tag.title
    Str_Artist = audio.tag.artist
    Str_Album = audio.tag.album
    Str_Album_Artist = audio.tag.album_artist
    Str_Composer = audio.tag.composer    
    
    if Str_Title is None:
        print('\t Str_Title is None')
        val_Str_Title = input("\t Enter your value: ")
        print(val_Str_Title)
        
        file = eyed3.load(Str_Mp3)
        file.initTag()
        file.tag.title = val_Str_Title
        #---------------------------------------------
        file.tag.title = val_Str_Title
        file.tag.artist = Str_Artist
        file.tag.album = Str_Album
        file.tag.album_artist = Str_Album
        file.tag.composer = Str_Composer
        
        #---------------------------------------------
        file.tag.save()
        
#/////////////////////////////////////////////////////////////////
def fn_Get_Album(Str_Mp3):
    print(Str_Line , "fn_Get_Album")
    print("Str_Mp3 = " , Str_Mp3)
    
    audio=eyed3.load(Str_Mp3)    
    Str_Album = audio.tag.album
    
    if Str_Album is None:
        print('\t Album is None')
        val_Str_Album = input("\t Enter your value: ")
        print(val_Str_Album)
        
        file = eyed3.load(Str_Mp3)
        file.initTag()
        file.tag.album = val_Str_Album
        file.tag.album_artist = val_Str_Album
        file.tag.save()
        
#/////////////////////////////////////////////////////////////////        
#/////////////////////////////////////////////////////////////////
def fn_02_MusicMp3(Str_Mp3):
    print(Str_Line , "fn_MusicMp3")
    print("Str_Mp3 = " , Str_Mp3)
    
    audio=eyed3.load(Str_Mp3)
    
    Str_Title = audio.tag.title
    Str_Artist = audio.tag.artist
    Str_Album = audio.tag.album
    Str_Album_Artist = audio.tag.album_artist
    Str_Composer = audio.tag.composer
    Str_genre = audio.tag.genre

    
    print("\t Title:", Str_Title)
    print("\t Artist:", Str_Artist)
    print("\t Album:", Str_Album)
    print("\t Album artist:", Str_Album_Artist)
    print("\t Composer:",Str_Composer)
    
    print("\t Str_genre:", Str_genre)

    #print("Publisher:",audio.tag.publisher)
    #print("Genre:",audio.tag.genre.name)

    #------------------------------------------------
    if Str_Album is None:
        print('Album is None')
        fn_Get_Album(Str_Mp3)
    else:
        print("Album:", len(Str_Album)  )
    #------------------------------------------------
    
    #------------------------------------------------
    if Str_Title is None:
        print('Str_Title is None')
        fn_Get_Title(Str_Mp3)
    else:
        print("Str_Title:", len(Str_Title)  )
    #------------------------------------------------
    
    #------------------------------------------------
    if Str_genre is None:
        print('Str_genre is None')
        fn_Get_Genre(Str_Mp3)
    else:
        #print("Str_genre:", len(Str_genre)  )
        print(".")
    #------------------------------------------------        


        
         
 



def fn_01_SubDirectory():
    print(Str_Line , "fn_SubDirectory")
    #we shall store all the file names in this list
    filelist = []
    
    for root, dirs, files in os.walk(path):
        for file in files:
            #append the file name to the list
            filelist.append(os.path.join(root,file))
    
    #print all the file names
    for name in filelist:
        #print(name)
        is_Mp3 = name.find('.mp')
        if (is_Mp3>2):
            #print('___',     name.find('.mp') )
            fn_02_MusicMp3(name)
        else:
            print('No es mp3') 
    
    
    
#####================================================================================
#####================================================================================

def main():
    print(Str_Line , "main")
    #----------------------------------------------
    fn_01_SubDirectory()
    print('\n\t\t DONE...')
    #----------------------------------------------

if __name__ == "__main__":
    main()    