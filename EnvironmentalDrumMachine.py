from pyo.lib.players import SfPlayer
from pyo import Server
from time import sleep
from pydub import AudioSegment
from pydub.playback import play

import os
import json
from pprint import pprint

import warnings
warnings.filterwarnings("ignore")

class EnvironmentalDrumMachine(object):
    """
    This is the EDM main class. It contains all the necessary methods to play with the application.

    Args:
        BPM (int): Beats per minute of the loop
        loops (int): Number of loops of the drum pattern to be played

    Attributes:
        BPM (int): Beats per minute of the loop
        loops (int): Number of loops of the drum pattern to be played

        DRUM_KIT_PATH (str): relative path to the drum kit folder
        DRUM_PATTERNS_PATH (str): relative path to the drum pattern folders

    """
    def __init__(self, BPM=160, loops=4):

        self.BPM = BPM
        self.loops = loops

        self.DRUM_KIT_PATH = './kit'  # Change name if needed, insert here your sounds
        self.DRUM_PATTERNS_PATH = './patterns'  # Add JSON-based patterns in this folder

    def get_settings(self):
        """
        Basically a function to retrieve the settings of the actual EDM
        """
        return {
            'BPM': self.BPM,
            'loops': self.loops,
            'DRUM_KIT_PATH': self.DRUM_KIT_PATH,
            'DRUM_PATTERNS_PATH': self.DRUM_PATTERNS_PATH,
        }

    def play(self, drum_kit, pattern, measure_length, syncope=False):
        """
        This function plays the selected pattern with the selected drum machine
        Args:
            drum_kit (dict): created drum kit by the user
            pattern (dict): pattern or drum loop to play
            measure_length (int): relative length of th selected pattern
            syncope (bool): flag to select whether the pattern should be played syncopated or not
        """
        sleep_time = (1 / (self.BPM / 60)) / 2

        # Initialize server
        s = Server().boot()
        s.start()

        bar_counter = 0
        measure_counter = 0
        if not syncope:
            # Go over all the loops
            while measure_counter < self.loops:
                bar_counter += 1
                # Go over all the measures
                if bar_counter > measure_length:
                    bar_counter = 1
                    measure_counter += 1
                players = []
                for instrument, beats in pattern.items():
                    if bar_counter in beats:
                        # Play in stereo!
                        players.append(SfPlayer(drum_kit[instrument], speed=1, loop=False).out(chnl=[0]))
                        players.append(SfPlayer(drum_kit[instrument], speed=1, loop=False).out(chnl=[1]))

                # Wait to reproduce the next note (computed with the BPM)
                sleep(sleep_time)
        else:
            # Syncope counter
            syncop_count = 2
            while measure_counter < self.loops:
                bar_counter += 1
                if bar_counter > measure_length:
                    bar_counter = 1
                    measure_counter += 1
                players = []
                for instrument, beats in pattern.items():
                    if bar_counter in beats:
                        players.append(SfPlayer(drum_kit[instrument], speed=1, loop=False).out(chnl=[0]))
                        players.append(SfPlayer(drum_kit[instrument], speed=1, loop=False).out(chnl=[1]))

                # Syncopate notes by elongating by 2 half of the notes
                if syncop_count % 2 == 0:
                    sleep(sleep_time * 2)
                else:
                    sleep(sleep_time)
                syncop_count += 1

    def get_pattern(self, pattern_name):
        """
        This function retrieves a certain JSON-based pattern from the patter folder
        Args:
            pattern_name (str): the name of the parsed pattern

        Return:
            pattern (dict): dict-based drum pattern to be played
            measure_length (int): relative length of the drum pattern
        """
        pattern_path = os.path.join(self.DRUM_PATTERNS_PATH, pattern_name + '.json')
        with open(pattern_path, 'r') as fhandle:
            pattern = json.load(fhandle)

        return pattern[pattern_name], int(pattern['measure_length'])

    def get_drum_kit(self, kick_sample, snare_sample, hi_hat_sample):
        """
        This function creates a drum kit to play the patterns
        Args:
            kick_sample (str): the name of the sample for the kick
            snare_sample (str): the name of the sample for the snare
            hi_hat_sample (str): the name of the sample for the hi-hat

        Return:
            drum_kit (dict): dict-based drum kit to play the patterns
        """
        drum_kit = {
            "kick": os.path.join(self.DRUM_KIT_PATH, 'kick', kick_sample + '.wav'),
            "snare": os.path.join(self.DRUM_KIT_PATH, 'snare', snare_sample + '.wav'),
            "hi_hat": os.path.join(self.DRUM_KIT_PATH, 'hi_hat', hi_hat_sample + '.wav'),
        }

        return drum_kit

    def describe_kit(self):
        """
        This function basically retrieves and prints the available samples to build the drum kit.
        """
        kick_dict = {
            'kick': [],
            'snare': [],
            'hi_hat': [],
        }
        for drum_part in os.listdir(self.DRUM_KIT_PATH):
            if '.' not in drum_part:  # Avoid mac invisible files
                for sample in os.listdir(os.path.join(self.DRUM_KIT_PATH, drum_part)):
                    kick_dict[drum_part].append(sample.replace('.wav', ''))

        print('Available drum kit...')
        pprint(kick_dict)

    def list_patterns(self):
        """
        This function lists the available drum pattern to be played.
        """
        print('Available patterns...')
        for pattern in os.listdir(self.DRUM_PATTERNS_PATH):
            if '.json' in pattern:
                print('--> ', pattern.replace('.json', ''))

    def play_sample(self, drum_part, sample_name):
        """
        This function retrieves a certain JSON-based pattern from the patter folder
        Args:
            drum_part (str): the name of the sample for the kick
            sample_name (str): the name of the sample for the snare
        """
        sound = AudioSegment.from_wav(os.path.join(self.DRUM_KIT_PATH, drum_part, sample_name + '.wav'))
        play(sound)
        sleep(1.0)

    def create_pattern(self, pattern_name, measure_length, kick_part, snare_part, hi_hat_part):
        """
        This function creates a JSON-based pattern and write it to disk, into the patterns folder
        Args:
            pattern_name (str): the name of the new pattern
            measure_length (int): relative measure length of the sample
            kick_part (str): score line for kick, represented as an array of bar numbers where to locate the kicks
            snare_part (str): score line for snare, represented as an array of bar numbers where to locate the snares
            hi_hat_part (str): score line for hi-hat, represented as an array of bar numbers where to locate the hats
        """
        pattern = {
            pattern_name: {
                "kick": kick_part,
                "snare": snare_part,
                "hi_hat": hi_hat_part,
            },
            'measure_length': measure_length,
        }

        filename = os.path.join(self.DRUM_PATTERNS_PATH, pattern_name + '.json')
        with open(filename, 'w') as fhandle:
            json.dump(pattern, fhandle, indent=4)

        print('Pattern {} stored at {}'.format(pattern_name, self.DRUM_PATTERNS_PATH))


# Example main funcion to run the code from the source file directly
if __name__ == '__main__':

    hola = EnvironmentalDrumMachine(BPM=200, loops=1)
    hola.describe_kit()
    hola.list_patterns()

    drum_kit = hola.get_drum_kit(
        kick_sample='boom',
        snare_sample='slap',
        hi_hat_sample='coins',
    )

    hola.play_sample(
        drum_part='kick',
        sample_name='boom'
    )

    pattern, measure_length = hola.get_pattern(
        pattern_name='groove_pattern'
    )

    hola.play(
        drum_kit=drum_kit,
        pattern=pattern,
        measure_length=measure_length,
        syncope=True,
    )
