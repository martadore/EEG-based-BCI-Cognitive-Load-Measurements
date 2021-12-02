# EEG-based-BCI-Cognitive-Load-Measurements
This project has been developed with the OpenBCI EEG headset with 16 electrodes, Cyton + Daisy Biosensing Board and the Dongle.
Download the OpenBCI Graphical User Interface (GUI) for your operating system. Also, if it’s your first time working with OpenBCI, make sure to install the latest FTDI driver for your operating system. You can find both at the link: https://openbci.com/downloads.
If everything went well, your OpenBCI Board should be showing up with a COM port number. Then, every operating system could show some problems that can be easily fixed with these tips: https://docs.openbci.com/Troubleshooting/TroubleshootingLanding/.
Now you can plug in the dongle, connect electrodes to the Cyton + Daisy board pins. Wear the EEG headset and finally connect the ear clip to SRB. Open the OpenBCI GUI, select the appropriate port number and start streaming data from the Cyton + Daisy board. Go to the networking tab and select the LSL protocol. Select “time-series” data type and start streaming.
Download and install LabRecorder https://github.com/labstreaminglayer/App-LabRecorder follow the READ.ME that suggest to download and install also the latest version of https://github.com/sccn/liblsl/releases
Download and install Neuropype, you can have free access as academic user. Neuropype supports officially OpenBCI hardware, so once set-up everything the stream is directly received as input in Neuropype through the LabRecorder. You can run the pipeline proposed here and process the data, in this way it wil be possible to generate a csv file with your output in order to open it easily in MATLAB or Python.
Another way to process EEG signal is with eeglab toolbox, download at: https://github.com/sccn/eeglab. You need to upload a dataset in eeglab, generated as .set, in order to do this you can download the https://github.com/labstreaminglayer/App-MATLABViewer. After you need to be sure that the recording in LabRecorder is started then type the command "vis_stream" in the MATLAB command window, you will be able to record a file in .set format by pressing the button "record" on the interface, once stopped the recording you will be able to save the file and upload it on eeglab for offline processing with filters and ICA functions etc. 
