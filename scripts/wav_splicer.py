#todo: take filenames as arguments


from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file("########.wav" , "wav") # change to name of file you want segmented
chunk_length_ms = 1000 # length of chunks in ms
chunks = make_chunks(myaudio, chunk_length_ms) 

#Export wav files

for i, chunk in enumerate(chunks):
    chunk_name = "#######{0}.wav".format(i)	#output name of chunks

    chunk.export(chunk_name, format="wav")