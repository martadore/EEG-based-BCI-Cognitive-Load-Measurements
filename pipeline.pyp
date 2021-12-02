<?xml version='1.0' encoding='utf-8'?>
<scheme description="This artifact removal pipeline can remove some of the common artifacts in bio-signals such as eye movements, blinks, cardiac signals, muscle artifacts, bad channels, and so on. This pipeline requires initial calibration data whose length can be set as via a parameter. The calibration is required as a baseline for the various artifact removal stages.&#10;&#10;Description of processing nodes:&#10;&#10;- LSL input: is used to input the streamed data into the pipeline.&#10;&#10;- Select range: is used to select desired segments of signal. For example if certain channels does not include meaningful EEG data we can exclude them from the data stream.&#10;&#10;tunable parameter:&#10;1. select_axis: indicates the axis to be used for data section.&#10;2. select_range: indicates the selection range along the chosen axis.&#10;&#10;- Assign Channel Locations: is used to assign channel coordinates, this node is essential to be placed before “Bad channel removal” node.&#10;&#10;- IIR filter:  is used to highpass filter the data. The preceding nodes, Bad channel removal, Channel repair filter and Artifact removal, all require that the data is high passed to ensure that the drift has been removed.&#10;&#10;tunable parameter:&#10;1. stopband edge freq.: indicates the stop-band edge frequency for the highness filter, frequencies below this value will be attenuated by default by 60dB.&#10;2. passband edge freq: indicates the pass-band edge frequency for the highness filter, frequencies above this value will pass with no attenuation.&#10;&#10;- Bad Channel Removal: is used to remove channels with abnormal data from a continuous EEG signal, which ensures that the data contains no channels that record only noise for extended periods of time.&#10;&#10;tunable parameters:&#10;1.  correlation threshold : Correlation threshold between 0 and  1. Higher values (above 0.7) are more stringent and will remove more  channels (i.e., moderately bad channels get removed). Values below 0.6 would be considered very lax (i.e., only the worst channels get removed). &#10;2.  noise threshold : High-frequency noise threshold is measured in multiple of standards deviations. Lower values (below 3.5) are more stringent and will remove more channels (i.e., moderately bad channels will get removed). Values above 5 would be considered very lax (i.e., only the worst channels get removed). &#10;&#10;- Channel Repair Filter: is used to identify and repair segments during which a channel yields bad data.&#10;&#10;tunable parameters:&#10;1. min_corr: Correlation threshold between 0 and 1. Higher values (above 0.7) are more aggressive and will cause channels to be repaired even when they have only moderate artifacts. Values below 0.5 would be considered rather lax (i.e., only the worst channel artifacts get repaired). &#10;2. processing-delay  : Signal delay in seconds. If this is value is set to too low values some sharp-onset artifacts will leave brief  knacks in the data.&quot;&#10;&#10;- Artifact Removal : is used to remove various kinds of high-amplitude artifacts from the signal. Artifacts are identified based on a threshold, given in standard deviations relative to (fairly) clean calibration data. This filter will work best on signals with multiple correlated channels, such as EEG or MEG. &#10;&#10;tunable parameters:&#10;1.  cutoff:  indicates the threshold for artifact removal, measured in multiples of standard deviations. Data portions whose amplitude is larger than this threshold (relative to the calibration data) are considered bad data and will be removed. The most aggressive value that can be used without losing too much EEG is  2.5. A quite conservative value would be 5.0&#10;2. lookahead : indicates the delay in output signal in seconds, can be between 0 (no lookahead) and  WindowLength/2 (optimal lookahead). The default value is set to  window_length/2.&#10;3. max_dims : indicates the maximum dimensionality of artifacts to remove can be a value between 0.1 to 1.0. Up to this many dimensions (or up to this fraction of dimensions) can be removed for a given data segment. If the algorithm needs to tolerate extreme artifacts a higher value than the default may be used, the default is set to  0.66." title="Artifact Removal pipeline" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(-677.0, 107.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="d24a7fa4-2a0a-4a2f-9aa7-7537a3f2b5a5" version="1.0.0" />
		<node id="1" name="Time Series Plot" position="(300, 200)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="19ee4761-3281-4bd4-9654-9e5344f817bb" version="1.0.1" />
		<node id="2" name="Bad Channel Removal" position="(-136.0, 105.0)" project_name="NeuroPype" qualified_name="widgets.neural.owbadchannelremoval.OWBadChannelRemoval" title="Bad Channel Removal" uuid="981025b5-c2bf-44a9-8432-1fa884dbcac2" version="1.1.0" />
		<node id="3" name="Assign Channel Locations" position="(-366.0, 100.0)" project_name="NeuroPype" qualified_name="widgets.source_localization.owassignchannellocations.OWAssignChannelLocations" title="Assign Channel Locations" uuid="79fb8578-bb60-458b-8057-4ec9103d40df" version="1.0.0" />
		<node id="4" name="LSL Output" position="(300, 100)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="d2f643fa-6028-4dd9-8729-0f8df9fba6b9" version="1.0.0" />
		<node id="5" name="Time Series Plot" position="(-126.0, 254.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="0ab52571-161f-42e8-b235-1e9021999930" version="1.0.1" />
		<node id="6" name="FIR Filter" position="(-466.0, 100.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="a4edd612-17fa-4946-be47-3ee3b3a4abe6" version="1.0.0" />
		<node id="7" name="Stream Data" position="(-500, 400)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="f9dd23d3-8139-4155-82e5-ef795f141317" version="1.1.0" />
		<node id="8" name="LSL Output" position="(-400, 400)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="96536122-63ab-4733-adfc-a7edf1793970" version="1.0.0" />
		<node id="9" name="Interpolate Missing Channels" position="(100, 100)" project_name="NeuroPype" qualified_name="widgets.neural.owinterpolatemissingchannels.OWInterpolateMissingChannels" title="Interpolate Missing Channels" uuid="5640c9e8-7bd6-48ee-a8c4-2f4db61b4159" version="0.9.0" />
		<node id="10" name="Remove Unlocalized Channels" position="(-266.0, 100.0)" project_name="NeuroPype" qualified_name="widgets.source_localization.owremoveunlocalizedchannels.OWRemoveUnlocalizedChannels" title="Remove Unlocalized Channels" uuid="f21bb531-2746-4798-88be-cfba1f4a0afe" version="1.0.0" />
		<node id="11" name="Extract Channel Names" position="(-100, 0)" project_name="NeuroPype" qualified_name="widgets.utilities.owextractchannels.OWExtractChannels" title="Extract Channel Names" uuid="42252892-07ac-49dc-9450-e445db942f46" version="1.0.0" />
		<node id="12" name="Import File" position="(-600, 400)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportfile.OWImportFile" title="Import File" uuid="39f9935f-c1c2-413e-b807-66e6eb630809" version="1.1.0" />
		<node id="13" name="Artifact Removal" position="(-34.0, 105.0)" project_name="NeuroPype" qualified_name="widgets.neural.owartifactremoval.OWArtifactRemoval" title="Artifact Removal" uuid="4ec33ee0-ae17-48df-a20f-55e03901c437" version="2.0.0" />
		<node id="14" name="Dejitter Timestamps" position="(-566.0, 107.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="2a5d1c62-956d-40fa-ad5e-a97ef716b610" version="1.0.0" />
		<node id="15" name="Record to CSV" position="(309.0, 306.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtocsv.OWRecordToCSV" title="Record task2_data to CSV" uuid="36786216-b358-4d7f-adfc-e3bf6ecedf49" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="8" sink_channel="Desired Channels" sink_node_id="9" source_channel="Channel Names" source_node_id="11" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="14" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="9" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFgAAAAAcQVYDAAAAG1heF9ibG9ja2xlbnEGTQAEWAoAAABtYXhfYnVmbGVucQdL
HlgMAAAAbWF4X2NodW5rbGVucQhLAFgMAAAAbm9taW5hbF9yYXRlcQlYDQAAACh1c2UgZGVmYXVs
dClxClgFAAAAcXVlcnlxC1gVAAAAbmFtZT0nTXlPdXRwdXRTdHJlYW0ncQxYBwAAAHJlY292ZXJx
DYhYFAAAAHJlc29sdmVfbWluaW11bV90aW1lcQ5HP+AAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxD2NzaXAKX3VucGlja2xlX3R5cGUKcRBYDAAAAFB5UXQ0LlF0Q29yZXERWAoAAABRQnl0
ZUFycmF5cRJDLgHZ0MsAAQAAAAADAgAAAWYAAAR5AAAC3AAAAwoAAAGFAAAEcQAAAtQAAAAAAABx
E4VxFIdxFVJxFlgOAAAAc2V0X2JyZWFrcG9pbnRxF4l1Lg==
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKIWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWJWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAwAAABpbml0aWFsX2RpbXNxC11xDChNIANL
Mk28Ak3oA2VYCgAAAGxpbmVfY29sb3JxDVgHAAAAIzAwMDAwMHEOWAoAAABsaW5lX3dpZHRocQ9H
P+AAAAAAAABYDAAAAG1hcmtlcl9jb2xvcnEQWAcAAAAjRkYwMDAwcRFYDAAAAG5hbnNfYXNfemVy
b3ESiVgOAAAAbm9fY29uY2F0ZW5hdGVxE4lYDgAAAG92ZXJyaWRlX3NyYXRlcRRYDQAAACh1c2Ug
ZGVmYXVsdClxFVgMAAAAcGxvdF9tYXJrZXJzcRaIWAsAAABwbG90X21pbm1heHEXiVgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEYY3NpcApfdW5waWNrbGVfdHlwZQpxGVgMAAAAUHlRdDQuUXRDb3Jl
cRpYCgAAAFFCeXRlQXJyYXlxG0MuAdnQywABAAD///1tAAABZP///uQAAAQD///9dQAAAYP///7c
AAAD+wAAAAEAAHEchXEdh3EeUnEfWAUAAABzY2FsZXEgRz+EeuFHrhR7WA4AAABzZXRfYnJlYWtw
b2ludHEhiVgMAAAAc2hvd190b29sYmFycSKJWAsAAABzdHJlYW1fbmFtZXEjWAAAAABxJFgKAAAA
dGltZV9yYW5nZXElSwZYBQAAAHRpdGxlcSZYCwAAAENsZWFuIERhdGEgcSdYCgAAAHplcm9fY29s
b3JxKFgJAAAAIzdGN0Y3RjdGcSlYCAAAAHplcm9tZWFucSqIdS4=
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWA0AAABjYWxpYl9zZWNvbmRzcQFLD1gPAAAAY29vcmRzX292ZXJyaWRlcQJYDQAAACh1
c2UgZGVmYXVsdClxA1gOAAAAY29ycl90aHJlc2hvbGRxBEc/6ZmZmZmZmlgPAAAAaWdub3JlX2No
YW5sb2NzcQWJWBAAAABpZ25vcmVkX3F1YW50aWxlcQZHP7mZmZmZmZpYBwAAAGluaXRfb25xB11x
CFgZAAAAa2VlcF91bmxvY2FsaXplZF9jaGFubmVsc3EJiVgPAAAAbGluZW5vaXNlX2F3YXJlcQqI
WBAAAABtYXhfYmFkX2NoYW5uZWxzcQtHP8MzMzMzMzNYDwAAAG1heF9icm9rZW5fdGltZXEMRz/Z
mZmZmZmaWAgAAABtaW5fY29ycnENRz/gAAAAAAAAWA8AAABub2lzZV90aHJlc2hvbGRxDksEWAsA
AABudW1fc2FtcGxlc3EPS8hYEAAAAHByb3RlY3RfY2hhbm5lbHNxEF1xEVgMAAAAcmVyZWZlcmVu
Y2VkcRKJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRNjc2lwCl91bnBpY2tsZV90eXBlCnEUWAwA
AABQeVF0NC5RdENvcmVxFVgKAAAAUUJ5dGVBcnJheXEWQy4B2dDLAAEAAAAAAwIAAAElAAAEeQAA
A5EAAAMKAAABRAAABHEAAAOJAAAAAAAAcReFcRiHcRlScRpYDgAAAHNldF9icmVha3BvaW50cRuJ
WAsAAABzdWJzZXRfc2l6ZXEcRz/DMzMzMzMzWBAAAAB1c2VfY2xlYW5fd2luZG93cR2JWAoAAAB3
aW5kb3dfbGVucR5LBVgWAAAAd2luZG93X2xlbl9jbGVhbndpbmRvd3EfRz/gAAAAAAAAWA4AAAB3
aW5kb3dfb3ZlcmxhcHEgRz/lHrhR64UfWBEAAAB6c2NvcmVfdGhyZXNob2xkc3EhXXEiKEfADAAA
AAAAAEsFZXUu
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWA4AAABmb3JjZV9vdmVycmlkZXEBiFgHAAAAbW9udGFnZXECWAAAAABxA1gTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDQuUXRDb3Jl
cQZYCgAAAFFCeXRlQXJyYXlxB0MuAdnQywABAAAAAAMCAAABxQAABGkAAAJLAAADAgAAAdsAAARp
AAACSwAAAAAAAHEIhXEJh3EKUnELWA4AAABzZXRfYnJlYWtwb2ludHEMiXUu
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYEQAAAE91dFN0cmVhbS1tYXJrZXJzcQRYEAAAAG1hcmtlcl9zb3VyY2Vf
aWRxBVgAAAAAcQZYDAAAAG1heF9idWZmZXJlZHEHSzxYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFu
Z2VkcQiJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwA
AABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAAAwIAAAFyAAAEaQAA
Ap0AAAMCAAABiAAABGkAAAKdAAAAAAAAcQ2FcQ6HcQ9ScRBYDAAAAHNlbmRfbWFya2Vyc3ERiVgO
AAAAc2V0X2JyZWFrcG9pbnRxEolYCQAAAHNvdXJjZV9pZHETaAZYBQAAAHNyYXRlcRRYDQAAACh1
c2UgZGVmYXVsdClxFVgLAAAAc3RyZWFtX25hbWVxFlgLAAAATXlPdXRTdHJlYW1xF1gLAAAAc3Ry
ZWFtX3R5cGVxGFgDAAAAZWVncRlYEwAAAHVzZV9kYXRhX3RpbWVzdGFtcHNxGohYFgAAAHVzZV9u
dW1weV9vcHRpbWl6YXRpb25xG4l1Lg==
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKIWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWJWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAwAAABpbml0aWFsX2RpbXNxC11xDChLMksy
TbwCTegDZVgKAAAAbGluZV9jb2xvcnENWAcAAAAjMDAwMDAwcQ5YCgAAAGxpbmVfd2lkdGhxD0c/
4AAAAAAAAFgMAAAAbWFya2VyX2NvbG9ycRBYBwAAACNGRjAwMDBxEVgMAAAAbmFuc19hc196ZXJv
cRKJWA4AAABub19jb25jYXRlbmF0ZXETiVgOAAAAb3ZlcnJpZGVfc3JhdGVxFFgNAAAAKHVzZSBk
ZWZhdWx0KXEVWAwAAABwbG90X21hcmtlcnNxFohYCwAAAHBsb3RfbWlubWF4cReJWBMAAABzYXZl
ZFdpZGdldEdlb21ldHJ5cRhjc2lwCl91bnBpY2tsZV90eXBlCnEZWAwAAABQeVF0NC5RdENvcmVx
GlgKAAAAUUJ5dGVBcnJheXEbQy4B2dDLAAEAAP//+5sAAAGZ///9EgAABDj///ujAAABuP///QoA
AAQwAAAAAQAAcRyFcR2HcR5ScR9YBQAAAHNjYWxlcSBHP4R64UeuFHtYDgAAAHNldF9icmVha3Bv
aW50cSGJWAwAAABzaG93X3Rvb2xiYXJxIolYCwAAAHN0cmVhbV9uYW1lcSNYAAAAAHEkWAoAAAB0
aW1lX3JhbmdlcSVLBlgFAAAAdGl0bGVxJlgJAAAAUmF3IERhdGEgcSdYCgAAAHplcm9fY29sb3Jx
KFgJAAAAIzdGN0Y3RjdGcSlYCAAAAHplcm9tZWFucSqIdS4=
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsBSz5lWA0AAABtaW5pbXVtX3BoYXNlcQmIWAQAAABtb2RlcQpY
CAAAAGJhbmRwYXNzcQtYBQAAAG9yZGVycQxYDQAAACh1c2UgZGVmYXVsdClxDVgTAAAAc2F2ZWRX
aWRnZXRHZW9tZXRyeXEOY3NpcApfdW5waWNrbGVfdHlwZQpxD1gMAAAAUHlRdDQuUXRDb3JlcRBY
CgAAAFFCeXRlQXJyYXlxEUMuAdnQywABAAAAAAJeAAABTAAAA9cAAALGAAACZwAAAXIAAAPOAAAC
vQAAAAAAAHEShXETh3EUUnEVWA4AAABzZXRfYnJlYWtwb2ludHEWiVgKAAAAc3RvcF9hdHRlbnEX
R0BOAAAAAAAAdS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWBEAAABoaXRjaF9wcm9iYWJpbGl0eXEBRz+5mZmZmZmaWA4AAABqaXR0ZXJfcGVyY2Vu
dHECSw9YBwAAAGxvb3BpbmdxA4hYCAAAAHJhbmRzZWVkcQRN54ZYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxBWNzaXAKX3VucGlja2xlX3R5cGUKcQZYDAAAAFB5UXQ0LlF0Q29yZXEHWAoAAABRQnl0
ZUFycmF5cQhDLgHZ0MsAAQAAAAACVgAAALsAAAPNAAACbQAAAl4AAADaAAADxQAAAmUAAAAAAABx
CYVxCodxC1JxDFgOAAAAc2V0X2JyZWFrcG9pbnRxDYlYBwAAAHNwZWVkdXBxDkc/8AAAAAAAAFgJ
AAAAc3RhcnRfcG9zcQ9HAAAAAAAAAABYEAAAAHRpbWVzdGFtcF9qaXR0ZXJxEEcAAAAAAAAAAFgG
AAAAdGltaW5ncRFYCQAAAHdhbGxjbG9ja3ESWA8AAAB1cGRhdGVfaW50ZXJ2YWxxE0c/pHrhR64U
e3Uu
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYFgAAAE15T3V0cHV0U3RyZWFtLW1hcmtlcnNxBFgQAAAAbWFya2VyX3Nv
dXJjZV9pZHEFWAAAAABxBlgMAAAAbWF4X2J1ZmZlcmVkcQdLPFgXAAAAcmVzZXRfaWZfbGFiZWxz
X2NoYW5nZWRxCIlYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxCWNzaXAKX3VucGlja2xlX3R5cGUK
cQpYDAAAAFB5UXQ0LlF0Q29yZXELWAoAAABRQnl0ZUFycmF5cQxDLgHZ0MsAAQAAAAAEQwAAAbcA
AAW6AAADYwAABEsAAAHWAAAFsgAAA1sAAAAAAABxDYVxDodxD1JxEFgMAAAAc2VuZF9tYXJrZXJz
cRGJWA4AAABzZXRfYnJlYWtwb2ludHESiVgJAAAAc291cmNlX2lkcRNYFgAAAG15dW5pcXVlc291
cmNlaWQzNDA5MzZxFFgFAAAAc3JhdGVxFVgNAAAAKHVzZSBkZWZhdWx0KXEWWAsAAABzdHJlYW1f
bmFtZXEXWA4AAABNeU91dHB1dFN0cmVhbXEYWAsAAABzdHJlYW1fdHlwZXEZWAMAAABFRUdxGlgT
AAAAdXNlX2RhdGFfdGltZXN0YW1wc3EbiFgWAAAAdXNlX251bXB5X29wdGltaXphdGlvbnEciXUu
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWBAAAABkZXNpcmVkX2NoYW5uZWxzcQFYDQAAACh1c2UgZGVmYXVsdClxAlgHAAAAbW9u
dGFnZXEDWAAAAABxBFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEFY3NpcApfdW5waWNrbGVfdHlw
ZQpxBlgMAAAAUHlRdDQuUXRDb3JlcQdYCgAAAFFCeXRlQXJyYXlxCEMuAdnQywABAAAAAAREAAAC
QgAABbsAAAL1AAAETAAAAmEAAAWzAAAC7QAAAAAAAHEJhXEKh3ELUnEMWA4AAABzZXRfYnJlYWtw
b2ludHENiXUu
</properties>
		<properties format="literal" node_id="10">{'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="literal" node_id="11">{'savedWidgetGeometry': None, 'set_breakpoint': False, 'stream': '', 'verbose': False}</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWBAAAABWaXN1YWxBcnJlc3QueGRmcQhYCwAAAGxvYWRfZXZlbnRzcQmIWAwA
AABsb2FkX3NpZ25hbHNxCohYDgAAAHJldGFpbl9zdHJlYW1zcQtYDQAAACh1c2UgZGVmYXVsdClx
DFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXENY3NpcApfdW5waWNrbGVfdHlwZQpxDlgMAAAAUHlR
dDQuUXRDb3JlcQ9YCgAAAFFCeXRlQXJyYXlxEEMuAdnQywABAAAAAAREAAAB2gAABbsAAANxAAAE
TAAAAfkAAAWzAAADaQAAAAAAAHERhXESh3ETUnEUWAgAAABzZWdtZW50c3EVaAxYDgAAAHNldF9i
cmVha3BvaW50cRaJWBAAAABzaWduYWxfYXV0b3NjYWxlcReIWAwAAABzdGltX2NoYW5uZWxxGGgC
WAsAAAB0aW1lX2JvdW5kc3EZaAxYDwAAAHVzZV9zdHJlYW1uYW1lc3EaiXUu
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWAEAAABhcQFYDQAAACh1c2UgZGVmYXVsdClxAlgBAAAAYnEDaAJYCgAAAGJsb2NrX3Np
emVxBEsKWA0AAABjYWxpYl9zZWNvbmRzcQVLLVgGAAAAY3V0b2ZmcQZHQB4AAAAAAABYDwAAAGVt
aXRfY2FsaWJfZGF0YXEHiFgHAAAAaW5pdF9vbnEIXXEJWAkAAABsb29rYWhlYWRxCmgCWBAAAABt
YXhfYmFkX2NoYW5uZWxzcQtHP8mZmZmZmZpYCAAAAG1heF9kaW1zcQxLAFgUAAAAbWF4X2Ryb3Bv
dXRfZnJhY3Rpb25xDUc/uZmZmZmZmlgHAAAAbWF4X21lbXEOTQABWBIAAABtaW5fY2xlYW5fZnJh
Y3Rpb25xD0c/0AAAAAAAAFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEQY3NpcApfdW5waWNrbGVf
dHlwZQpxEVgMAAAAUHlRdDQuUXRDb3JlcRJYCgAAAFFCeXRlQXJyYXlxE0MuAdnQywABAAAAAAME
AAAAtwAABHsAAANBAAADDAAAANYAAARzAAADOQAAAAAAAHEUhXEVh3EWUnEXWA4AAABzZXRfYnJl
YWtwb2ludHEYiVgNAAAAc3RkZGV2X2N1dG9mZnEZSxRYCQAAAHN0ZXBfc2l6ZXEaRz/JmZmZmZma
WBAAAAB1c2VfY2xlYW5fd2luZG93cRuIWAoAAAB1c2VfbGVnYWN5cRyJWBYAAAB3aW5kb3dfbGVu
X2NsZWFud2luZG93cR1HP+AAAAAAAABYDQAAAHdpbmRvd19sZW5ndGhxHkc/4AAAAAAAAFgOAAAA
d2luZG93X292ZXJsYXBxH0c/5R64UeuFH1gaAAAAd2luZG93X292ZXJsYXBfY2xlYW53aW5kb3dx
IEc/5R64UeuFH1gRAAAAenNjb3JlX3RocmVzaG9sZHNxIV1xIihK+////0sHZXUu
</properties>
		<properties format="literal" node_id="14">{'force_monotonic': True, 'forget_halftime': 90, 'max_updaterate': 500, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'warmup_samples': -1}</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWBcAAABhYnNvbHV0ZV9pbnN0YW5jZV90aW1lc3EBiFgNAAAAY2xvdWRfYWNjb3VudHEC
WAAAAABxA1gMAAAAY2xvdWRfYnVja2V0cQRoA1gRAAAAY2xvdWRfY3JlZGVudGlhbHNxBWgDWAoA
AABjbG91ZF9ob3N0cQZYBwAAAERlZmF1bHRxB1gNAAAAY29sdW1uX2hlYWRlcnEIiFgMAAAAZGVs
ZXRlX3BhcnRzcQmIWAgAAABmaWxlbmFtZXEKWA4AAAByZXN0Ml9kYXRhLmNzdnELWAsAAABvdXRw
dXRfcm9vdHEMWBYAAABDOi9Vc2Vycy9tYXJ0YS9EZXNrdG9wcQ1YCwAAAHJldHJpZXZhYmxlcQ6J
WBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0
NC5RdENvcmVxEVgKAAAAUUJ5dGVBcnJheXESQy4B2dDLAAEAAAAAAwMAAAESAAAEfAAAAtYAAAMM
AAABOAAABHMAAALNAAAAAAAAcROFcRSHcRVScRZYDgAAAHNldF9icmVha3BvaW50cReJWAsAAAB0
aW1lX3N0YW1wc3EYiFgPAAAAdGltZXN0YW1wX2xhYmVscRlYCQAAAHRpbWVzdGFtcHEadS4=
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node7",
            "data",
            "node4",
            "data"
        ],
        [
            "node8",
            "data",
            "node9",
            "data"
        ],
        [
            "node10",
            "data",
            "node5",
            "data"
        ],
        [
            "node10",
            "data",
            "node2",
            "data"
        ],
        [
            "node10",
            "data",
            "node16",
            "data"
        ],
        [
            "node4",
            "data",
            "node11",
            "data"
        ],
        [
            "node11",
            "data",
            "node6",
            "data"
        ],
        [
            "node11",
            "data",
            "node3",
            "data"
        ],
        [
            "node11",
            "data",
            "node12",
            "data"
        ],
        [
            "node12",
            "channel_names",
            "node10",
            "desired_channels"
        ],
        [
            "node13",
            "data",
            "node8",
            "data"
        ],
        [
            "node3",
            "data",
            "node14",
            "data"
        ],
        [
            "node14",
            "data",
            "node10",
            "data"
        ],
        [
            "node1",
            "data",
            "node15",
            "data"
        ],
        [
            "node15",
            "data",
            "node7",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='MyOutputStream'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "d24a7fa4-2a0a-4a2f-9aa7-7537a3f2b5a5"
        },
        "node10": {
            "class": "InterpolateMissingChannels",
            "module": "neuropype.nodes.neural.InterpolateMissingChannels",
            "params": {
                "desired_channels": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "montage": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "5640c9e8-7bd6-48ee-a8c4-2f4db61b4159"
        },
        "node11": {
            "class": "RemoveUnlocalizedChannels",
            "module": "neuropype.nodes.source_localization.RemoveUnlocalizedChannels",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f21bb531-2746-4798-88be-cfba1f4a0afe"
        },
        "node12": {
            "class": "ExtractChannels",
            "module": "neuropype.nodes.utilities.ExtractChannels",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "42252892-07ac-49dc-9450-e445db942f46"
        },
        "node13": {
            "class": "ImportFile",
            "module": "neuropype.nodes.file_system.ImportFile",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "VisualArrest.xdf"
                },
                "load_events": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "load_signals": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "segments": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "signal_autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stim_channel": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "time_bounds": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "39f9935f-c1c2-413e-b807-66e6eb630809"
        },
        "node14": {
            "class": "ArtifactRemoval",
            "module": "neuropype.nodes.neural.ArtifactRemoval",
            "params": {
                "a": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "b": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "block_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 10
                },
                "calib_seconds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 45
                },
                "cutoff": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 7.5
                },
                "emit_calib_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "init_on": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "lookahead": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "max_bad_channels": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "max_dims": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0
                },
                "max_dropout_fraction": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                },
                "max_mem": {
                    "customized": false,
                    "type": "Port",
                    "value": 256
                },
                "min_clean_fraction": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.25
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stddev_cutoff": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "step_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "use_clean_window": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_legacy": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "window_len_cleanwindow": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "window_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "window_overlap": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.66
                },
                "window_overlap_cleanwindow": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.66
                },
                "zscore_thresholds": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        -5,
                        7
                    ]
                }
            },
            "uuid": "4ec33ee0-ae17-48df-a20f-55e03901c437"
        },
        "node15": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 90
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "2a5d1c62-956d-40fa-ad5e-a97ef716b610"
        },
        "node16": {
            "class": "RecordToCSV",
            "module": "neuropype.nodes.file_system.RecordToCSV",
            "params": {
                "absolute_instance_times": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "column_header": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "rest2_data.csv"
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/marta/Desktop"
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_stamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "timestamp_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "timestamp"
                }
            },
            "uuid": "36786216-b358-4d7f-adfc-e3bf6ecedf49"
        },
        "node2": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        800,
                        50,
                        700,
                        1000
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.01
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": ""
                },
                "time_range": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 6
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Clean Data "
                },
                "zero_color": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "#7F7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "19ee4761-3281-4bd4-9654-9e5344f817bb"
        },
        "node3": {
            "class": "BadChannelRemoval",
            "module": "neuropype.nodes.neural.BadChannelRemoval",
            "params": {
                "calib_seconds": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 15
                },
                "coords_override": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "corr_threshold": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.8
                },
                "ignore_chanlocs": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "ignored_quantile": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                },
                "init_on": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "keep_unlocalized_channels": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "linenoise_aware": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_bad_channels": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.15
                },
                "max_broken_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.4
                },
                "min_corr": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "noise_threshold": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 4
                },
                "num_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 200
                },
                "protect_channels": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "rereferenced": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "subset_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.15
                },
                "use_clean_window": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "window_len": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "window_len_cleanwindow": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "window_overlap": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.66
                },
                "zscore_thresholds": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        -3.5,
                        5
                    ]
                }
            },
            "uuid": "981025b5-c2bf-44a9-8432-1fa884dbcac2"
        },
        "node4": {
            "class": "AssignChannelLocations",
            "module": "neuropype.nodes.source_localization.AssignChannelLocations",
            "params": {
                "force_override": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "montage": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "79fb8578-bb60-458b-8057-4ec9103d40df"
        },
        "node5": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "MyOutStream"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "d2f643fa-6028-4dd9-8729-0f8df9fba6b9"
        },
        "node6": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        1000
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.01
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": ""
                },
                "time_range": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 6
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Raw Data "
                },
                "zero_color": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "#7F7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "0ab52571-161f-42e8-b235-1e9021999930"
        },
        "node7": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        1,
                        62
                    ]
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 60.0
                }
            },
            "uuid": "a4edd612-17fa-4946-be47-3ee3b3a4abe6"
        },
        "node8": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "hitch_probability": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.1
                },
                "jitter_percent": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 15
                },
                "looping": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "speedup": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timestamp_jitter": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wallclock"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "f9dd23d3-8139-4155-82e5-ef795f141317"
        },
        "node9": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "MyOutputStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "myuniquesourceid340936"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "MyOutputStream"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "96536122-63ab-4733-adfc-a7edf1793970"
        }
    },
    "version": 1.1
}</patch>
</scheme>
