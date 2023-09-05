# kthfs_training

This repository contains my attempts at the exercises detailed in the KTH Formula Student training gitbook.

## exercise1

This project uses ROS Melodic Morenia, tested on an Ubuntu 18.04 machine. Steps were taken to also install *catkin tools*.

### Simple publisher-subscriber network

When run successfully, a publisher sends a string of the current timestamp at $10 \, \mathrm{Hz}$ intervals to the `chatter` topic, while a subscriber receieves these messages. The publisher and subscriber are in the `broadcast` and `receiver` packages respectively.

#### Installation and running

1. Create a new directory (eg: `kthfsdv`) by: `mkdir -p ~/kthfsdv/src`.
2. Enter the project directory: `cd ~/kthfsdv/` and run `catkin build`.
4. Clone the contents of this repos `excercise1` directory into the `src/` directory.
5. Open a terminal and `cd src/exc1/broadcast/scripts/` and run `chmod +x talker.py` to make this python file executable.
6. Repeat with `cd src/exc1/receiver/scripts/` and run `chmod +x listener.py`.
7. Then `cd ~/kthfsdv/` and run `catkin build`.
8. Initialise the master with `roscore`.
9. In a new terminal at the same level, navigate into the environment with `source ./devel/setup.bash`.
10. Run `rosrun broadcast talker.py` and observe output.
11. In another new terminal, repeat steps 9-10 instead running `rosrun receiver listener.py` and observe output.

### More complicated publisher-subscriber-publisher

When run successfully, a publisher sends an Integer increasing every step at $20 \, \mathrm{Hz}$ intervals to the `oriordan` topic, while a subscriber receieves these messages. The subscriber then modifies this Integer and further publishes the result in the `kthfs/result` topic. The publisher and subscriber-publisher are in the `package1` and `package2` packages respectively.

#### Installation and running

1. Create a new directory (eg: `kthfsdv`) by: `mkdir -p ~/kthfsdv/src`.
2. Enter the project directory: `cd ~/kthfsdv/` and run `catkin build`.
4. Clone the contents of this repos `excercise1` directory into the `src/` directory.
5. Open a terminal and `cd src/exc1/package1/scripts/` and run `chmod +x talker.py` to make this python file executable.
6. Repeat with `cd src/exc1/package2/scripts/` and run `chmod +x listener_talker.py`.
7. Then `cd ~/kthfsdv/` and run `catkin build`.
8. Initialise the master with `roscore`.
9. In a new terminal at the same level, navigate into the environment with `source ./devel/setup.bash`.
10. Run `rosrun broadcast talker.py` and observe output.
11. In another new terminal, repeat steps 9-10 instead running `rosrun receiver listener_talker.py` and observe output.
12. To visualise, in a new terminal repeat step 9 and then run `rqt_plot`. This opens a GUI where you can enter what topic you would like to view (the publisher uses the `oriordan` topic and subscriber-publisher uses the `kthfs/result` topic).

![kthfsdv_plot](https://github.com/seanie5011/kthfs_training/assets/72211395/ad57bdbd-a610-4401-8e17-1f8d7c2b567b)

## exercise2

This project provides visualisation of an incoming $\left( x, y \right)$ data stream. This data stream is simulated by inserting a new point every $t_k$ timestep following the function:

$$ h \left( t \right) = 3 \pi \exp{\left(- \lambda \left( t \right) \right)} $$

Where $\lambda \left( t \right)$ is given by:

$$ \lambda \left( t \right) = 5 \sin{\left( 2 \pi t \right)} $$

This project makes use of Python 3.10.11 and was developed on a Windows 10 machine.

### Installation and running

1. Clone this repo.
2. Open a terminal in the `exercise2` directory.
3. Run: `pip install -r requirements.txt` (use a virtual enviroment!).
4. Run: `python main.py`

### Explanation

A matplotlib plot is embedded in a customtkinter GUI. Many features of the plot can be accessed via the GUI. These consist of toggling of a grid, editing the title (don't forget to press return!), and saving the plot (either image or data file). The plot updates in realtime each timestep that the data is inputted. This can be stopped (and then started again), along with being reset. Further displayed is some analysis of the signal, using signal analysis with scipy methods.

This project was created with an OOP approach. Different classes impact different sections of the app, such as the side panel, bottom panel, the plot (and analysis), and the main app running.

![screenshot](https://github.com/seanie5011/kthfs_training/assets/72211395/e09eed61-afda-4baa-adde-3f77b5c6b207)
