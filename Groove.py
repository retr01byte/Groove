import playsound
import glob
import os


print(r'''
     _________         .    .
    (..       \_    ,  |\  /|
     \       O  \  /|  \ \/ /
      \______    \/ |   \  / 
         vvvv\    \ |   /  |
         \^^^^  ==   \_/   |
         `\_   ===    \.  |
        / /\_   \ /      |
        |/   \_  \|      /
              \________/
	''')


list_music = []
fil = []
path = os.getcwd()

_file_ = ('.mp3')
print('[+] lendo arquivos de audio na pasta: {}\n'.format(path))
for file in glob.glob('*'):
	if file.endswith(_file_):
		base_name = os.path.basename(file)
		print('\t' + base_name)
		fil.append(base_name)
		list_music.append(os.path.abspath(file))


for name, music in zip(fil, list_music):
	print('\n[+] reproduzindo [{}]'.format(name, list_music))
	try:
		playsound.playsound(music)
	except KeyboardInterrupt:
		print('[-] Musica interrompida.')
		break