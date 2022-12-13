from music_analyzor import *
from music21 import *
from music21 import chord

# color refer: https://xdevs.com/guide/color_serial/

class MusicGenerator(MusicAnalyzor):
    def __init__(self, note_object,num_bars):
        MusicAnalyzor.__init__(self, note_object, num_bars)
        self.Key = self.key_setting()
        print("{0}rhythm beats{1} \nstart...".format('\033[1m','\033[0m'))
        self.Beats = self.rhythm_setting()
        print("finished...\n {2}{3}{4}".format('\033[1m','\033[0m','\033[94m',str(self.Beats),'\033[0m'))
        print("{0}chords progression{1} \nstart...".format('\033[1m','\033[0m'))
        self.ChordsPrg = self.chords_setting()
        print("finished...\n {2}{3}{4}".format('\033[1m','\033[0m','\033[92m',str(self.ChordsPrg),'\033[0m'))

    def chords_generate(self):
        chords_lst=[]
        for j in range(4): #four 
            for i in range(2):
                _chord = roman.RomanNumeral(self.ChordsPrg[j])
                _chord= " ".join([str(p) for p in _chord.pitches])
                # change from RomanNumeral to origin chords
                crd = chord.Chord(_chord)
                crd.key = self.Key
                crd.duration.type = 'half'
                chords_lst.append(crd)
        return chords_lst

    def melody_generate(self):
        '''generate melody_notes list based on key, chord progression and beats.'''
        print("{0}melody{1} \nstart...".format('\033[1m','\033[0m'))
        cnt_notes_bar = [len(x) for x in self.Beats]
        _melody_notes = []
        for num_beat in range(len(self.Beats)):
            num_chord = num_beat//4
            rf = roman.RomanNumeral(self.ChordsPrg[num_chord], self.Key) # transfer roman numerals to chords based on key.
            chordNotes = rf.normalOrder # get the pitches of chords
            _melody_notes.append(random.choices(chordNotes,k=cnt_notes_bar[num_beat])) # randomly generate notes based on chords.

        melody_lst = []
        # set beats
        for num_melody in range(len(_melody_notes)):  
            itm= _melody_notes[num_melody]
            # type of the note beat
            if len(itm) == 4: _type = '16th' # Sixteenth note type
            elif len(itm) == 2: _type = 'eighth' # Eighth note type
            elif len(itm) == 1: _type = 'quarter' # Quarter note type
            for num_itm in range(len(itm)):
                itm_melody = itm[num_itm]
                # combine to note.Note
                if self.Beats[num_melody][num_itm] == '0':
                    _note = note.Rest(type = _type) # Rest note
                else:
                    _note = note.Note(self.note_num[str(itm_melody)][0], type = _type) # Pitch note
                melody_lst.append(_note)
        print("finished...\n{2} {3}{4} ".format('\033[1m','\033[0m','\033[93m',str(melody_lst),'\033[0m'))
        return melody_lst

    def mix_melody_chords(self):
        s = stream.Score()
        mm1 = tempo.MetronomeMark(number=88)
        # create melody part of the score
        p_melody = stream.Part()
        p_melody.append(mm1)
        chords_lst = self.chords_generate() # generate chords
        melody_lst = self.melody_generate() # generate melody
        for note in melody_lst:
            p_melody.append(note)
        # create chords part of the score
        p_chords = stream.Part()
        p_chords.append(mm1)
        for num_chord in range(len(chords_lst)):
            p_chords.insert(num_chord*2, chords_lst[num_chord])
        # mix the melody and chords
        s.insert(0,p_melody)
        s.insert(0,p_chords)
        return s