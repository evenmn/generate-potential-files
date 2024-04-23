from genpot import Vashishta

params = {"XXX": {"H": 1.0,
                  "eta": 1.0,
                  "Zi": 0.0,
                  "Zj": 0.0,
                  "r1s": 1.0,
                  "D": 0.0,
                  "r4s": 1.0,
                  "W": 0.0,
                  "rc": 10.0,
                  "B": 0.0,
                  "xi": 0.0,
                  "r0": 0.0,
                  "C": 0.0,
                  "cos(theta)": 0.0}}

potential = Vashishta(params=params, molecule="X")
potential.write("repulsion.vashishta")
