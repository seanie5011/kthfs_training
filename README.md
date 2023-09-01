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