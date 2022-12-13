from music_analyzor import *
from music21 import *

class MusicGenerator(MusicAnalyzor):
    def __init__(self, note_object,num_bars):
        MusicAnalyzor.__init__(self, note_object, num_bars)
        self.Key = self.key_setting()
        self.Beats = self.rhythm_setting()
        self.ChordsPrg = self.chords_setting()
        print(self.Beats, self.ChordsPrg)

    def chords_generate(self):
        chords_lst=[]
        for j in range(4): #four 
            for i in range(1):
                chord = roman.RomanNumeral(self.ChordsPrg[j])
                chord.key = self.Key
                chord.duration.type = 'whole'
                chords_lst.append(chord)
        return chords_lst

    def melody_generate(self):
        '''generate melody_notes list based on key, chord progression and beats.'''
        cnt_notes_bar = [len(x) for x in self.Beats]
        _melody_notes = []
        for num_beat in range(len(self.Beats)):
            num_chord = num_beat//4
            rf = roman.RomanNumeral(self.ChordsPrg[num_chord], self.Key) # transfer roman numerals to chords based on key.
            chordNotes = rf.normalOrder # get the pitches of chords
            # randomly generate notes based on chords.
            _melody_notes.append(random.choices(chordNotes,k=cnt_notes_bar[num_beat]))
        print('_melody_notes',_melody_notes)
        melody_lst = []
        for num_melody in range(len(_melody_notes)):  
            itm= _melody_notes[num_melody]
            for num_itm in range(len(itm)):
                itm_melody = itm[num_itm]
                if len(itm) == 4: _type = '16th'
                elif len(itm) == 2: _type = 'eighth'
                elif len(itm) == 1: _type = 'quarter'
                if self.Beats[num_melody][num_itm] == '0':
                    _note = note.Rest(type = _type)
                else:
                    _note = note.Note(self.note_num[str(itm_melody)][0], type = _type)
                melody_lst.append(_note)
        return melody_lst

        # pc.show('midi')
    def mix_melody_chords(self):
        s = stream.Score()
        mm1 = tempo.MetronomeMark(number=88)
        # s.append(mm1)
        p1 = stream.Part()
        p1.append(mm1)
        chords_lst = self.chords_generate() # generate chords
        melody_lst = self.melody_generate() # generate melody
        for note in melody_lst:
            p1.append(note)
        p2 = stream.Part()
        p2.append(mm1)

        for num_chord in range(len(chords_lst)):
            # print(num_chord*2, chords_lst[num_chord])
            p2.insert(num_chord*4, chords_lst[num_chord])
        p2.show()
        s.insert(0,p1)
        s.insert(0,p2)
        return s