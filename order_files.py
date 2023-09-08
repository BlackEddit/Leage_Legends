import os
import shutil ##utilidad de shell que te permite mover archivos, copiarlos, y hacer muchas otras cosas

# Crear las carpetas ADC y SUP si no existen
if not os.path.exists('ADC'):
    os.makedirs('ADC')

if not os.path.exists('SUP'):
    os.makedirs('SUP')

# Lista de campeones ADC y SUP (añade más según tu conocimiento)
adc_champs = ['Ashe', 'Jhin', 'Caitlyn']
sup_champs = ['Thresh', 'Leona', 'Lulu']

# Mover los archivos a sus respectivas carpetas
for filename in os.listdir('.'):
    if filename.endswith('.json'):
        champ_name = filename.split('.')[0]
        if champ_name in adc_champs:
            shutil.move(filename, f'ADC/{filename}')
        elif champ_name in sup_champs:
            shutil.move(filename, f'SUP/{filename}')