# Random walks

_Simplictic simulations of various types of random walks._

- Simple random walks
  - [x] Random walk on regular 1D lattice where you can step in any of the two directions {↑, ↓} with the same probability.
  - [x] Random walk on regular 2D lattice where you can step in any of the four directions {↑, ←, ↓, →} with the same probability.

- Restricted random walks
  - [ ] Random walk on regular lattice without immediate return where you can step in three possible directions with the same probability,
      the first step is in any direction.
  - [ ] Random walk on the square lattice without crossing i.e. self-avoiding random walk.

See the examples:

- [random_walk.py module](source/random_walk.py)
- [random_walk.f90 module](source/random_walk.f90)
- [random_walk_main.f90 program](source/random_walk.f90)

![Random walk 1D](images/RandomWalk1D.png "Random walk 1D")
![Random walk 2D](images/RandomWalk2D.png "Random walk 2D")
![Random walk 2D](images/RandomWalk3D.png "Random walk 3D")

## Build and run

### Fortran

Compile and run *main* program:

```powershell
gfortran source\random_walk.f90 source\random_walk_main.f90 -o build\random_walk_main.exe

.\random_walk_main.exe 123 100 1 > data.psv
```

Compile and run *test* program:

```powershell
gfortran source\random_walk.f90 source\random_walk_test.f90 -o build\random_walk_test.exe

.\build\random_walk_test.exe
```

Also, you can execute the `project.bat` with `build` command and then run programs:

```powershell
.\project.bat build

.\build\random_walk_main.exe 123 100 1
.\build\random_walk_test.exe
```

### Python

You need Python version 3.10+.

Create virtual environment.

      py -3.10 -m venv .venv
      .venv\scripts\activate
      pip install seaborn, matplotlib

Run the simulations.

      py source\random_walk.py 100_000 1    # 1D simulation with 100_000 steps
      py source\random_walk.py 100_000 2    # 2D simulation with 100_000 steps

## Statistics/Metrics

- [ ] What is an average distance from origin?
- [ ] How many immediate returns was made?

- TODO Make a subroutine with text and binary output flag.
- TODO `open(newunit=id, file='file_name')`