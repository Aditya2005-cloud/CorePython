import streamlit as s
import time

mp = s.progress(0, text='Download in progress')# create a progress bar with initial value 0
for i in range(1, 11):# loop from 1 to 10
    time.sleep(1) # simulate a delay of 1 second
    percentage = i * 10 # calculate the percentage of completion
    mp.progress(percentage, text='It is in progress') # update the progress bar with the new percentage and text
s.write('Completed the process')
s.balloons()# display balloons animation to celebrate the completion of the process

hm=s.spinner('Loading...')# create a spinner with the text 'Loading...'
with hm:# use the spinner in a context manager
    for i in range(1, 11):
        time.sleep(1)
        percentage = i * 10
        s.progress(percentage, text='It is in progress')
s.write('Completed the process')
s.success('Done!')
s.snow()# display snow animation to celebrate the completion of the process

