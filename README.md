# BCI-Typing
Toolbox for BCI assisted computer typing, suing OpenBCI Cyton and EEG Headband

To set up, do the following:
Connect a Cyton Board to the target computer.
Download the BCI GUI and set up the data stream. You Should now be able to see fft Data and some other metrics.
Choose one tab and click the 'networking' option in the drop down menu.
Choose the LSL protocol and verify that you are Streaming FFT type EEG Data
Clone this repo, and run the 'playground_control_practice.py' inside. You may need to install some modules first (using pip3 install module-name)
You should now see a red dot on the screen, that moves according to your brainwave data.
Control is currently impossible, since the interface is still experimental. Changes coming soon.
