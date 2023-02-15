from img_work import *
from audio_work import *


ans = input('Полюбуемся красивыми видами? (Да/Нет)  ')
sans = input('Добавить фоном музыку? (Да/Нет)  ')
if ans.lower() == "да" and sans.lower() == 'да':
    img_open('ural_m.jpg')
    music('music.wav')
elif ans.lower() == "да" and sans.lower() == 'нет':      
    img_open('ural_m.jpg')
else:
    print('Ну нет, так нет.')
    
