import os
import eyed3


Str_Line = '_____________________________________________________________'
path ="C:/#_FP_APEX/#_DEV/#_Py_FP/Py_Test/Py_Music/Music_Files/"
path =".\Music_Files"


#/////////////////////////////////////////////////////////////////
      
#/////////////////////////////////////////////////////////////////
def fn_Replace(Str_Mp3):       
    print(Str_Line , "fn_Replace")
    print('\t ', Str_Mp3)
    
    Str_Mp3_2 = Str_Mp3
    
    #tags  = ["(Audio)", "[OFFICIAL VIDEO]", "(Official Video)", "(Official Music Video)", "(Official Audio)", "(Official Lyric Video)", " .mp3"]
    tags  = ["(Audio)", "[OFFICIAL VIDEO]", "(Official Video)", "(Official Music Video)", "(Official Audio)", "(Official Lyric Video)" , "(Official Visualizer)", "[OFFICIAL MUSIC VIDEO]", "(Lyric Video)"]
    
    for tag in tags:
        Str_Mp3_2 = Str_Mp3_2.replace(tag, '')
        #print('\t Str_New_FileName = ', Str_Mp3_2)
    


    Str_New_FileName = Str_Mp3_2
    Str_New_FileName = Str_New_FileName.replace(' .mp3', '.mp3')
    print('\t\t Str_New_FileName = ', Str_New_FileName)
     

    print('Str_Mp3              = ', Str_Mp3)
    print('Str_Mp3_2            = ', Str_Mp3_2)
    print('Str_New_FileName     = ', Str_New_FileName)

    
    '''
    print("something")
    wait = input("Press Enter to continue.")
    print("something")
    '''
 
    
    
    
    print('*************************************************')
    print('*                                               *')
    print('*                Rename Process                 *')
    print('*                                               *')
    print('*************************************************')
    
    os.rename(Str_Mp3,Str_New_FileName)
    
#/////////////////////////////////////////////////////////////////        
#/////////////////////////////////////////////////////////////////
def fn_MusicMp3(Str_Mp3):
    print(Str_Line , "fn_MusicMp3")
    print("Str_Mp3 = " , Str_Mp3)
    
    Str_4_Replace = ["(Audio)", "[OFFICIAL VIDEO]", "(Official Video)", "(Official Music Video)", "(Official Audio)", "(Official Lyric Video)", "(Official Visualizer)", "(Lyric Video)", "[OFFICIAL MUSIC VIDEO]", " .mp3"]
    if_Str_Contains = any(Str_4_Replace in Str_Mp3 for Str_4_Replace in Str_4_Replace)
    print('\t if_Str_Contains = ', if_Str_Contains)
    
    if if_Str_Contains == True:
        #print('\t !!!!!!!')
        fn_Replace(Str_Mp3)

    #------------------------------------------------    

        
         
 



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
    #----------------------------------------------

if __name__ == "__main__":
    main()    