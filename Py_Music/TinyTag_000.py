'''
Created on May 25, 2022

@author: Fabian Ponce
'''
import os
from tinytag import TinyTag

###############################################################
##
##    https://pypi.org/project/tinytag/
##
###############################################################

Str_Line = '_____________________________________________________________'
path ="C:/#_FP_APEX/#_DEV/#_Py_FP/Py_Test/Py_Music/Music_Files/"
path =".\Music_Files"
path =".\Music_Files"


#/////////////////////////////////////////////////////////////////      
#/////////////////////////////////////////////////////////////////        
#/////////////////////////////////////////////////////////////////
def fn_MusicMp3(Str_Mp3):
    print(Str_Line , "fn_MusicMp3")
    print("Str_Mp3 = " , Str_Mp3)
    
    
    tag = TinyTag.get(Str_Mp3, encoding='gbk')
    
    
    Str_album    =   tag.album         # album as string
    Str_albumartist    =   tag.albumartist   # album artist as string
    Str_artist    =   tag.artist        # artist name as string
    Str_audio_offset    =   tag.audio_offset  # number of bytes before audio data begins
    Str_bitrate    =   tag.bitrate       # bitrate in kBits/s
    Str_comment    =   tag.comment       # file comment as string
    Str_composer    =   tag.composer      # composer as string 
    Str_disc    =   tag.disc          # disc number
    Str_disc_total    =   tag.disc_total    # the total number of discs
    Str_duration    =   tag.duration      # duration of the song in seconds
    Str_filesize    =   tag.filesize      # file size in bytes
    Str_genre    =   tag.genre         # genre as string
    Str_samplerate    =   tag.samplerate    # samples per second
    Str_title    =   tag.title         # title of the song
    Str_track    =   tag.track         # track number as string
    Str_track_total    =   tag.track_total   # total number of tracks as string
    Str_year    =   tag.year          # year or data as string
    
    
    print('    Str_album            = ',     Str_album    )
    print('    Str_albumartist      = ',     Str_albumartist     )
    print('    Str_artist           = ',     Str_artist     )
    print('    Str_audio_offset     = ',     Str_audio_offset     )
    print('    Str_bitrate          = ',     Str_bitrate    )
    print('    Str_comment          = ',     Str_comment    )
    print('    Str_composer         = ',     Str_composer   )
    print('    Str_disc             = ',     Str_disc    )
    print('    Str_disc_total       = ',     Str_disc_total    )
    print('    Str_duration         = ',     Str_duration    )
    print('    Str_filesize         = ',     Str_filesize    )
    print('    Str_genre            = ',     Str_genre    )
    print('    Str_samplerate       = ',     Str_samplerate    )
    print('    Str_title            = ',     Str_title    )
    print('    Str_track            = ',     Str_track    )
    print('    Str_track_total      = ',     Str_track_total    )
    print('    Str_year             = ',     Str_year)
    
    tag.title = 'HOLA'
    TinyTag.tag.save()

    


        
         
 



def fn_SubDirectory():
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
            fn_MusicMp3(name)
        else:
            print('No es mp3') 
    
    
    
#####================================================================================
#####================================================================================

def main():
    print(Str_Line , "main")
    #----------------------------------------------
    fn_SubDirectory()
    print('\n\t\t DONE...')
    #----------------------------------------------

if __name__ == "__main__":
    main()    