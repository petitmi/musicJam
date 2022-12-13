from music_generator import *
from music21 import *
import os
def main():
    tmp = MusicGenerator(note_object=[['C','D','G'],'1/1'],num_bars = 4)
    _mld = tmp.mix_melody_chords()
    # _mld.show()
    fp_output = ['file.mid','score-1.png','score.musicxml']
    print(os.getcwd())
    for fp in fp_output:
        if os.path.exists(fp):
            os.remove(fp)
    _mld.write('midi', fp='file.mid')
    _mld.write('musicxml.png',fp = 'score.png')
    print("{0} {1} {2} finished writing ".format('\033[1m',str(fp),'\033[0m'))

if __name__ == "__main__":
    main()
