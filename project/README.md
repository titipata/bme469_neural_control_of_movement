# Final Project

this folder is a place that we put all code to reproduce papers decribed below.


## Proposal

Understanding how the timing of actions is controlled before they reach the motor cortex is crucial in movement planning.

Past experiments have suggested that medial prefrontal cortex (dmPFC) is involved in the timing of actions and the top-down control of motor system in the motor cortex (MC). This process ocurrs by suppressing responses during movement delays.

Here we want to replicate the findings by Nandakumar et. al. [1] and Bekolay et. al. [2] using the nengo simulation system [3]. [1] decribes neural activity in dmPFC and MC using time-series Principle Components Analysis (PCA) across neural populations. They then decribe roles of delay-activity in dmPFC and motor cortex where they propose the top-down control model between both areas. [2]  proposes model to simulate spikes using double-integrator network as a concrete mechanism that would replicate the results in [1].

Concretely, I'll use `nengo` [3], a Python library to simulate spikes trains, to simulate the model described in [2] which explains the results in [1].

**Current status**
I have already set up the software tools and simple experiments. I am currently requesting the experimental data from the authors in [1] and they have agree to provide it.


## References

[1] [Narayanan et. al., _Delay activity in rodent frontal cortex during a simple reaction time task_](http://jn.physiology.org/content/101/6/2859.long), J Neurophysiol, 2009<br>
[2] [Bekolay et. al., _A Spiking Neural Integrator Model of the Adaptive Control of Action by the Medial Prefrontal Cortex_](http://www.jneurosci.org/content/34/5/1892.long), J Neuroscience 2014 with [repository](https://github.com/tbekolay/jneurosci2013)<br>
[3] [Bekolay et. al., _Nengo: a Python tool for building large-scale functional brain models_](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3880998/pdf/fninf-07-00048.pdf) with [repository](https://github.com/nengo/nengo)<br>


## Dependencies

Here are lists of dependencies for final project. Use
`pip install -r requirements.txt --upgrade`
in order to install all dependencies
(assume you have default packages from Anaconda).

- [nengo](https://github.com/nengo/nengo)
- [h5py](http://docs.h5py.org/en/latest/build.html)

## Issues related to project

If anyone has ideas or potential projects just issue
them [here](https://github.com/titipata/bme469_neural_control_of_movement/issues)
