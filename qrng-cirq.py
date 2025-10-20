import cirq
import time

start_time = time.time()
#do some processing work to determine the timing

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Square root of NOT.
    cirq.measure(qubit, key='m')  # Measurement.
)
print("Circuit:")
print(circuit)

# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)

# elapsed time
end_time = time.time()
elapsed_time = end_time - start_time

print("Results:")
print(result)
print(f"Elapsed time: {elapsed_time:.4f} seconds")