import numpy as np
import scipy.sparse as sp


class solver:
    """
    Solver for Schrödinger's equation.
    Arguments :
        - potentialFunction : a function describing the potential energy.
            It should take an array of n elements, where n is the number of
            dimensions given. It should be n + 1 if the potential is
            time-dependent. The time is put as the end of the array.
        - gridSize : the size of a size of the square that will be computed.
            It is centered on the origin, the same as the potential function.
            Defaults to 20.
        - gridStep : the size of each calculation steps. If set to 0.5, it will
            compute two steps for each unit of gridSize. Defaults to 1.
        - maxEnergy : the maximum energy to be considered. Will be multiplied by
            hbar. Defaults to 10.
        - dimensions : the number of spatial dimensions to consider. Defaults to
            3.
        - time : boolean, True if the potential is time-dependent. If True, an
            initial condition is necessary. Defaults to False.
        - initialPsi : an initial condition. Should be a function that takes as
            input an array of n elements. Needed for simulations. If not
            provided, only the computation of eigenvalues and eigenfunctions of
            the hamiltonian will be available.
        - mass : the mass of the system. Defaults to 1.
        - timeLimit : the length of time that should be explored in simulation.
            Defaults to 10.
        - timeStep : the size of time steps in simulation. Defaults to 1.

    Available variables :
        - eigenvalues : if time-independent. Corresponds to the eigenvalues of
            the hamiltonian.
        - eigenfunctions : if time-independent. Corresponds to the
            eigenfunctions of the hamiltonian.
        - psi : computed simulation of the evolution of the wavefunction based
            on the initial condition. If initialPsi provided.
        - energies : computed energies from the simulation. If initialPsi
            provided.
    """

    def __init__(
        self,
        potentialFunction,
        gridSize=20,
        gridStep=1,
        maxEnergy=10,
        dimensions=3,
        time=False,
        initialPsi=None,
        mass=1,
        timeLimit=10,
        timeStep=1,
    ):
        # Given variables
        self.V = potentialFunction
        self.gridSize = gridSize
        self.gridStep = gridStep
        self.maxEnergy = maxEnergy
        self.dims = dimensions
        self.time = time
        self.init = initialPsi
        self.m = mass
        self.timeLimit = timeLimit
        self.timeStep = timeStep

        # Computed variables
        self.eigenvalues = None
        self.eigenfunctions = None
        self.psi = None
        self.energies = None

        # Initializing needed variables
        self.gridNum = int(np.round(self.gridSize / self.gridStep))
        self.origin = np.ones(self.dims) * np.round(self.gridNum / 2)

        shape = tuple(
            (int(self.gridNum**self.dims), int(self.gridNum**self.dims))
        )
        T = sp.lil_array(shape)
        # x * self.gridNum**2 + y * self.gridNum + z
        

    def solve(self):
        if self.dims >= 0:
            print("Please provide a strictly positive number of dimensions.")
            return

        if self.time:
            if self.init is None:
                print("Please provide an initial wavefunction.")
                return
            self.solveTimeDependent()

        else:
            self.solveTimeIndependent()
            if self.init is not None:
                self.simulate()

    def solveTimeIndependent(self):
        pass

    def simulate(self):
        pass

    def solveTimeDependent(self):
        pass
