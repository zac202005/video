import schedule
import time
from moviepy.editor import ImageClip, TextClip, CompositeVideoClip, AudioFileClip
from gtts import gTTS

def creer_video():
    print("Génération de la vidéo en cours...")
    
    # 1. Créer la voix off
    texte = "Voici votre vidéo automatique de 11 heures !"
    tts = gTTS(text=texte, lang='fr')
    tts.save("audio.mp3")
    
    # 2. Créer le clip vidéo (exemple avec une image et du texte)
    # Note : Assurez-vous d'avoir ImageMagick installé pour les TextClip
    audio = AudioFileClip("audio.mp3")
    img_clip = ImageClip("background.jpg").set_duration(audio.duration)
    
    txt_clip = TextClip(texte, fontsize=70, color='white').set_duration(audio.duration)
    txt_clip = txt_clip.set_position('center')
    
    video = CompositeVideoClip([img_clip, txt_clip])
    video.set_audio(audio)
    
    # 3. Exporter
    nom_fichier = f"video_{time.strftime('%Y%m%d_%H%M')}.mp4"
    video.write_videofile(nom_fichier, fps=24)
    print(f"Vidéo terminée : {nom_fichier}")

# --- PLANIFICATION ---
# Planifier à 11h00
schedule.every().day.at("11:00").do(creer_video)

# Planifier à 16h00
schedule.every().day.at("16:00").do(creer_video)

print("Programme d'automatisation lancé...")

while True:
    schedule.run_pending()
    time.sleep(60) # Vérifie chaque minute
