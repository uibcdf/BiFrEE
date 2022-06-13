import os
import openmm as mm
from openmm.app import *
from openmm import unit
from openmm import app
from pdbfixer import PDBFixer
import mdtraj as md
import numpy as np
from math import sqrt
from tqdm import tqdm

def get_binding_potential_energy(filename):

    #Solvate the system
    #------------------

    pdb_c      = PDBFile(filename)
    forcefield = app.ForceField('amber14-all.xml', 'amber14/tip3p.xml')
    modeller   = app.Modeller(pdb_c.topology, pdb_c.positions)

    geompadding = 1.4 * unit.nanometers
    maxSize     = max(max((pos[i] for pos in pdb_c.positions))-min((pos[i] for pos in pdb_c.positions)) for i in range(3))
    vectors     = mm.Vec3(1,0,0), mm.Vec3(1/3,2*sqrt(2)/3,0), mm.Vec3(-1/3,sqrt(2)/3,sqrt(6)/3)
    boxVectors  = [(maxSize+geompadding)*v for v in vectors]

    modeller.addSolvent(forcefield, model='tip3p', boxVectors=boxVectors)

    app.PDBFile.writeFile(modeller.topology, modeller.positions, open('1brs_s.pdb', 'w'))

    #Obtain receptor and ligand from system
    #--------------------------------------

    uu = md.load(filename)

    atoms_in_chain_A = uu.topology.select("chainid == 0")
    atoms_in_chain_B = uu.topology.select("chainid == 1")

    barnase = uu.atom_slice(atoms_in_chain_A)
    barstar = uu.atom_slice(atoms_in_chain_B)

    barnase.save_pdb('barnase.pdb')
    barstar.save_pdb('barstar.pdb')

    #Create system objects
    #---------------------

    pdb_s = PDBFile('1brs_s.pdb')
    pdb_r = PDBFile('barnase.pdb')
    pdb_l = PDBFile('barstar.pdb')

    forcefield = ForceField('amber14-all.xml', 'amber14/tip3p.xml')

    system_s = forcefield.createSystem(pdb_s.topology, nonbondedMethod=PME, nonbondedCutoff=1.2*unit.nanometer, switchDistance=0.9*unit.nanometer,constraints=HBonds)
    system_c = forcefield.createSystem(pdb_c.topology, constraints=HBonds)
    system_r = forcefield.createSystem(pdb_r.topology, constraints=HBonds)
    system_l = forcefield.createSystem(pdb_l.topology, constraints=HBonds)

    ns_particles = pdb_s.topology.getNumAtoms()
    nc_particles = pdb_c.topology.getNumAtoms()
    nr_particles = pdb_r.topology.getNumAtoms()
    nl_particles = pdb_l.topology.getNumAtoms()

    # Definición del estado termodinámico y el integrador, para sistema solvatado

    step_size_s   = 0.002*unit.picoseconds
    temperature_s = 300*unit.kelvin
    friction_s    = 1.0/unit.picosecond # Damping para la dinámica de Langevin

    integrator_s  = mm.LangevinIntegrator(temperature_s, friction_s, step_size_s)

    # Definición del estado termodinámico y el integrador, para sistema vacio

    step_size_c   = 0.002*unit.picoseconds
    temperature_c = 0.0*unit.kelvin
    friction_c    = 0.0/unit.picosecond # Damping para la dinámica de Langevin

    integrator_c  = mm.LangevinIntegrator(temperature_c, friction_c, step_size_c)
    integrator_r  = mm.LangevinIntegrator(temperature_c, friction_c, step_size_c)
    integrator_l  = mm.LangevinIntegrator(temperature_c, friction_c, step_size_c)

    # Creación de la plataforma.

    platform_name = 'CUDA'
    platform_s    = mm.Platform.getPlatformByName(platform_name)
    platform_c    = mm.Platform.getPlatformByName(platform_name)
    platform_r    = mm.Platform.getPlatformByName(platform_name)
    platform_l    = mm.Platform.getPlatformByName(platform_name)

    # Creación del objeto simulacion de los sistemas C, R y L

    simulation_s = Simulation(pdb_s.topology, system_s, integrator_s, platform_s)
    simulation_c = Simulation(pdb_c.topology, system_c, integrator_c, platform_c)
    simulation_r = Simulation(pdb_r.topology, system_r, integrator_r, platform_r)
    simulation_l = Simulation(pdb_l.topology, system_l, integrator_l, platform_l)

    # Condiciones iniciales

    simulation_s.context.setPositions(pdb_s.positions)
    simulation_c.context.setPositions(pdb_c.positions)
    simulation_r.context.setPositions(pdb_r.positions)
    simulation_l.context.setPositions(pdb_l.positions)

    # Minimizacion del sistema

    simulation_s.minimizeEnergy()

    # Parámetros de la simulación.
    simulation_time    = 0.1*unit.nanosecond
    saving_time        = 10.0*unit.picoseconds
    n_steps_per_period = int(saving_time/step_size_c) # número de pasos entre frame de guardado
    n_periods          = int(simulation_time/saving_time) # número de frames guardados

    # Creación de arrays reporteros del tiempo, la posición y la velocidad.

    times                  = np.zeros([n_periods], np.float32) * unit.picoseconds
    positions              = np.zeros([n_periods, ns_particles, 3], np.float32) * unit.angstroms
    pos_aux_c              = np.zeros([nc_particles,3], np.float32) * unit.angstroms
    pos_aux_r              = np.zeros([nr_particles,3], np.float32) * unit.angstroms
    pos_aux_l              = np.zeros([nl_particles,3], np.float32) * unit.angstroms
    potential_energies     = np.zeros([n_periods], np.float32) * unit.kilocalories_per_mole
    potential_energies_c   = np.zeros([n_periods], np.float32) * unit.kilocalories_per_mole
    potential_energies_r   = np.zeros([n_periods], np.float32) * unit.kilocalories_per_mole
    potential_energies_l   = np.zeros([n_periods], np.float32) * unit.kilocalories_per_mole

    # Almacenamiento en reporteros de las condiciones iniciales de sistema Solvatado para tiempo 0

    state_s                 = simulation_s.context.getState(getPositions=True, getEnergy=True)

    times[0]                = state_s.getTime()
    positions[0]            = state_s.getPositions()
    potential_energies[0]   = state_s.getPotentialEnergy()

    # Almacenamiento en reporteros de las condiciones iniciales de sistema C para tiempo 0

    pos_aux_c                = state_s.getPositions()[:nc_particles]

    simulation_c.context.setPositions(pos_aux_c)

    state_c                  = simulation_c.context.getState(getEnergy=True)
    potential_energies_c[0]  = state_c.getPotentialEnergy()

    # Almacenamiento en reporteros de las condiciones iniciales de sistema R para tiempo 0

    pos_aux_r                = state_s.getPositions()[:nr_particles]

    simulation_r.context.setPositions(pos_aux_r)

    state_r                  = simulation_r.context.getState(getEnergy=True)
    potential_energies_r[0]  = state_r.getPotentialEnergy()

    # Almacenamiento en reporteros de las condiciones iniciales de sistema L para tiempo 0

    pos_aux_l                = state_s.getPositions()[nr_particles:nr_particles+nl_particles]

    simulation_l.context.setPositions(pos_aux_l)

    state_l                  = simulation_l.context.getState(getEnergy=True)
    potential_energies_l[0]  = state_l.getPotentialEnergy()

    # Ejecuto el bucle sobre el número de periodos que vamos a simular

    for ii in tqdm(range(1, n_periods)):

        simulation_s.context.getIntegrator().step(n_steps_per_period)
        state_s                    = simulation_s.context.getState(getPositions=True, getEnergy=True)
        times[ii]                  = state_s.getTime()
        positions[ii]              = state_s.getPositions()
        potential_energies[ii]     = state_s.getPotentialEnergy()

        pos_aux_c                  = state_s.getPositions()[:nc_particles]
        simulation_c.context.setPositions(pos_aux_c)

        state_c                    = simulation_c.context.getState(getEnergy=True)
        potential_energies_c[ii]   = state_c.getPotentialEnergy()

        pos_aux_r                  = state_s.getPositions()[:nr_particles]
        simulation_r.context.setPositions(pos_aux_r)

        state_r                    = simulation_r.context.getState(getEnergy=True)
        potential_energies_r[ii]   = state_r.getPotentialEnergy()

        pos_aux_l                  = state_s.getPositions()[nr_particles:nr_particles+nl_particles]
        simulation_l.context.setPositions(pos_aux_l)

        state_l                    = simulation_l.context.getState(getEnergy=True)
        potential_energies_l[ii]   = state_l.getPotentialEnergy()

    # Promedio de energia potencial sobre toda la trayectoria

    binding_pe = potential_energies_c-(potential_energies_r+potential_energies_l)

    return binding_pe.mean()

