import h5py

def validate_file(fn):
    valid = False
    with h5py.File(fn, "r") as f:
        valid = True
        valid = valid and ("particle_positions" in f)
        valid = valid and ("particle_velocities" in f)
        valid = valid and ("particle_masses" in f)
        shape = f["/particle_positions"].shape
        valid = valid and (shape == f["/particle_velocities"].shape)
        valid = valid and (shape[1] == 3)
        valid = valid and (len(shape) == 2)
        valid = valid and (shape[0] == f["/particle_masses"].shape[0])
        valid = valid and (len(f["/particle_masses"].shape) == 1)
    return valid
