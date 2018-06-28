from pydub import AudioSegment
from pydub.utils import make_chunks
import argparse


parser = argparse.ArgumentParser(description="makes chunks of .wav files")
parser.add_argument("-l", type=int, default=2000, help="length of chunks in ms (default: 2000ms)")
parser.add_argument('input_file', help="name of .wav file to splice")
parser.add_argument('output_file', help="name of outputfile(s)")

args = parser.parse_args()



myaudio = AudioSegment.from_file(args.input_file , "wav") #name that the chunk files will be given
chunk_length_ms = args.l # length of chunks in ms
chunks = make_chunks(myaudio, chunk_length_ms) 


#Export wav files
for i, chunk in enumerate(chunks):
    chunk_name = args.output_file + "{0}.wav".format(i)	#output name of chunks

    chunk.export(chunk_name, format="wav")
