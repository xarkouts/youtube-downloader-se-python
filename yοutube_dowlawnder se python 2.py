from pytube import YouTube
def dose_url():
    while(True):
        url=input("Δοσε το url του youtube βιντεο που θες να κατεβασις \n")
        if "www.youtube.com" in url and "watch?v=" in url:
             return url
            
        print("Το url που εισαγαται δεν ειναι youtube url \n Παρακαλο δοσε ενα youtube url")
def video( my_video):
     
     print("**********VIDEO TITLE********** ")
     print(my_video.title)
     print("**********TUBNAIL IMAGE********** ")
     print(my_video.thumbnail_url)
     print("**********DOWLAWND VIDEO********** ")
     for stream in my_video.streams:
       print(stream)       
     my_video=my_video.streams.get_highest_resolution()
     if my_video.download():
        print("EPITIXIA KATEBASMATOS VIDEO")         

def audio(my_video):
   
    print("**********VIDEO TITLE********** ")
    print(type(my_video.title))
    print("**********TUBNAIL IMAGE********** ")
    print(my_video.thumbnail_url)
    print("**********DOWLAWND VIDEO********** ")
    for stream in my_video.streams:
     print(stream)        
    my_video=my_video.streams.get_audio_only()

    if my_video.download(filename=f"audio only.mp3"):
     print("EPITIXIA KATEBASMATOS HXOY")
                            
    


def yutube_dowlawnd(url):
    
    while (True):
        ap=input(""" 
              ΠΛΗΚΤΟΛΟΓΙΣΕ 1 ΓΙΑ ΝΑ ΚΑΤΕΒΑΣΙΣ ΤΟ ΒΙΝΤΕΟ
              ΠΛΗΚΤΟΛΟΓΙΣΕ 2 ΓΙΑ ΝΑ ΚΑΤΕΒΑΣΙΣ ΤΟ ΤΟΝ ΗΧΟ
              ΠΛΗΚΤΟΛΟΓΙΣΕ 3 ΓΙΑ ΝΑ ΚΑΤΕΒΑΣΙΣ ΚΑΙ ΒΙΝΤΕΟ ΚΑΙ ΗΧΟ  
            """)
        if ap.isnumeric():
            ap=int(ap)
        if ap==1 or ap==2 or ap==3:
            break        
       
    try:
        my_video=YouTube(url)
       
        if(ap==1):
            video(my_video)
        if(ap==2):
         audio(my_video)
        if(ap==3):
         video(my_video)
         audio(my_video)            
    except:
        yutube_dowlawnd(dose_url())
    
    
       
            
    


    
    

   
yutube_dowlawnd(dose_url())
