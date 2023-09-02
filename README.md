# kthfs_training

This repository contains my attempts at the exercises detailed in the KTH Formula Student training gitbook.

## exercise1

TODO.

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