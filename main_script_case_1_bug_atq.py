# main_script_case_1_bug_atq.py
#
# This script is part of a PsychoPy experiment where a fixation cross is supposed to be displayed
# during certain phases of the trial. Due to an indentation error, the fixation cross does not appear
# as expected during the 'listen' phase.
#
# INPUTS
# ---------
# None (The phases for each trial are randomly selected within the script).
#
# OUTPUTS
# ---------
# None
#
# The script performs the following operations:
# 1. Displays instructions to the participant.
# 2. Randomly assigns one of the phases ('listen', 'silence', 'play') to each of the 10 trials.
# 3. During the 'listen' phase, the fixation cross should appear but does not due to an indentation error.
# 4. During the 'silence' phase, the fixation cross correctly appears for the entire duration.
# 5. During the 'play' phase, the fixation cross is not displayed, which is intended.
#
# NOTE: This script is designed to illustrate how indentation errors can affect the timing and presentation of stimuli
# in a PsychoPy experiment.
#
# -----------------------------------------------------------------------------------------
# Ana Teresa Queiroga, 2024
# PhD student @ Department of Clinical Medicine, Center for Music in the Brain
# Aarhus University, Denmark

# Import necessary libraries
from psychopy import visual, core, event, logging
import os
import random

# Setup window
win = visual.Window(fullscr=False, color='black')

# Define stimuli
fixation_cross = visual.TextStim(win, text='+', color='white', height=0.2)
instructions   = visual.TextStim(win, text='Press any key to start the experiment.', color='white')
listen_win     = visual.TextStim(win, text='Listen', color='white')
play_win       = visual.TextStim(win, text='Play', color='white')
silence_win    = visual.TextStim(win, text='Silence', color='white')

# Display instructions
instructions.draw()
win.flip()
event.waitKeys()

# Define experimental conditions
phases = ['listen', 'silence', 'play']
trials = [{'phase': random.choice(phases)} for _ in range(10)]
print(trials)

# Initialize clock
trial_clock = core.Clock()

# Start experiment
for trial in trials:
    phase = trial['phase']
    trial_clock.reset()
    
    # Display fixation cross based on phase
    if phase == 'listen':
        listen_win.draw()
        win.flip()
        core.wait(2)
        while trial_clock.getTime() < 5:  # Listen phase duration
            continue
        fixation_cross.draw()  # Indentation error: fixation cross is drawn outside the loop
        win.flip()

    elif phase == 'silence':
        silence_win.draw()
        win.flip()
        core.wait(2)
        while trial_clock.getTime() < 5:  # Silence phase duration
            fixation_cross.draw()  # Correctly displaying fixation cross for entire duration
            win.flip()
    elif phase == 'play':
        play_win.draw()
        win.flip()
        core.wait(2)
        while trial_clock.getTime() < 5:  # Play phase duration
            # No fixation cross during play phase, which is correct
            win.flip()

# Close window and clean up
win.close()
core.quit()
