import traci
import matplotlib.pyplot as plt
import time

sumoBinary = "/opt/homebrew/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "/opt/homebrew/Cellar/sumo/1.19.0/share/sumo/tools/game/cross.sumocfg"]

# Starting the SUMO simulation with TraCI
traci.start(sumoCmd)

# Visualization loop
while traci.simulation.getMinExpectedNumber() > 0:
    # Advancing simulation by one step
    traci.simulationStep()

# End SUMO simulation
traci.close()