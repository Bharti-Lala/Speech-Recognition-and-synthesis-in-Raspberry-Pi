import os
#from pocketsphinx import AudioFile, get_model_path, get_data_pa
from wit import Wit

'''model_path = get_model_path()
data_path = get_data_path()'''



os.system("jack_control start")
os.system("sudo amixer cset numid=3 1")
os.system("arecord -D plughw:1,0 -d 10 temp.wav")
#os.system("python noise_out.py")
os.system("sox temp.wav -n noiseprof noise.prof")
os.system("sox temp.wav temp1.wav noisered noise.prof 0.21")
os.system("sox temp1.wav -n noiseprof noise.prof")
os.system("sox temp1.wav temp2.wav noisered noise.prof 0.21")
#os.system("sox temp2.wav temp3.wav silence -l 1 0.1 1% -1 2.0 1%")
#os.system("sox temp2.wav --bits 16 --encoding signed-integer --endian little temp.raw")

client = Wit('FWRGIL5Q5KD3MOINSZ3TNT5M26GTM543')
resp = None
with open('temp.wav','rb') as f:
    resp = client.speech(f,None,{'Content-Type': 'audio/wave'})
print ('You said:'+str(resp))

'''config = {
    'verbose': False,
    'audio_file': os.path.join(data_path, '/home/bharti/Desktop/temp.raw'),
    'buffer_size': 4096,
    'no_search': False,
    'full_utt': False,
    'hmm': os.path.join(model_path, 'en-us'),
    'lm': os.path.join(model_path, 'en-us.lm.bin'),
    'dict': os.path.join(model_path, 'cmudict-en-us.dict')
}

audio = AudioFile(**config)
for phrase in audio:
    print(phrase)'''

