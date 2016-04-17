# Final Project

this folder is a place that we put all code to reproduce papers described below.


## Proposal

See project proposal `tex` and `pdf` in `proposal_manuscript` folder.


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
- [neo](https://pythonhosted.org/neo/index.html)
- [h5py](http://docs.h5py.org/en/latest/build.html)
- [deepdish](https://github.com/uchicago-cs/deepdish)

**note** see structure of `h5` file by using `deepdish` i.e. `$ ddls <file_name>.h5`


## Issues related to project

If anyone has ideas or potential projects just issue
them [here](https://github.com/titipata/bme469_neural_control_of_movement/issues)
