import pickle

with open("small_mzml.p", "rb") as f:
    state = pickle.load(f)
print(state)
