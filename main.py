from music_generator import *
from music21 import *
import os
def main():
    tmp = MusicGenerator(note_object=[['C','G','B'],'1/2'],num_bars = 4)
    _mld = tmp.mix_melody_chords()
    # _mld.show()
    tm1 = time.time()
    print("{0}outputs:{1} start writing...".format('\033[1m','\033[0m'),end="")
    fp_output = ['file.mid','score-1.png','score.musicxml']
    for fp in fp_output:
        if os.path.exists(fp):
            os.remove(fp)
    _mld.write('midi', fp='file.mid')
    tm2 = time.time()
    print("{2}s...{0}midi{1} finished writing...".format('\033[1m','\033[0m',str(round(tm2-tm1,5))),end='')
    _mld.write('musicxml.png',fp = 'score.png')
    tm3 = time.time()
    print("{0}s...{1}png {2} finished writing ".format(str(round(tm3-tm1,5)),'\033[1m','\033[0m'))

if __name__ == "__main__":
    main()
