from music_generator import *
from music21 import *
def main():
    tmp = MusicGenerator(note_object=[['C','D','G'],'1/1'],num_bars = 4)
    _mld = tmp.mix_melody_chords()
    _mld.show()
    _mld.write('midi', fp='file.mid')
    _mld.write('musicxml.png',fp = 'score.png')
    print(_mld)

if __name__ == "__main__":
    main()