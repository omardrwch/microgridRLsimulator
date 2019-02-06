Main modifications with respect to original repository
======================================================

* Included setup.py file so that we can install it as a package;
* case1.json and case1_dataset.csv were moved to the folder microgridRLsimulator/data/
* data paths were modified in simulator.py
    * results are now stored in microgridRLsimulator/results/
    * .json and .csv files are read from microgridRLsimulator/data/
* Created a class `MicrogridEnv` (microgridRLsimulator/gym_wrapper/microgrid_env) that implements `gym.Env`
* File examples/baseline_demo.py shows how to use [baseline RL algorithms](https://github.com/hill-a/stable-baselines) with `MicrogridEnv`


Installation & examples
=======================

After cloning the repository, run  ``pip install -e .``

Examples of how to use the environments can be found in the folder examples/



Installation (according to orginal repository)
==============================================

Be sure you have python 3.6 installed.
Run ``install.sh``. This creates the python environment ``mgenv`` with the necessary requirements to run the application.

Running the application
=======================

Be sure you are using the python environment ``mgenv`` (``source menv/bin/activate``).


Get help::

    python -m microgridRLsimulator -h

Run the application::

    python -m microgridRLsimulator --from_date 20150101T00:00:00 --to_date 20150102T00:00:00 --agent DQN --agent_options agent_options.json case1

This runs the case1 examples located in folder ``examples/data`` using a DQNAgent, that is a agent that uses Deep Q learning.

Documentation
=============

You can generate this documentation yourself:

::

    cd <to the root of the project>
    cd docs; make html; cd ..

The html doc is in ``_build/html``

