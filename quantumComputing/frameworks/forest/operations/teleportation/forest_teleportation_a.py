# import pyquil.quil as pq
# from pyquil.gates import *
# import pyquil.api as api
#
# qvm = api.SyncConnection()
# p = pq.Program().inst(H(0))
# wvf, _ = qvm.wavefunction(p)
# print( wvf. get_outcome_probs())
#
# p = pq.Program().inst(H(0), H(1))
# wvf, _ = qvm.wavefunction(p)
# alpha, beta, gamma, delta = wvf
# print(alpha, beta, gamma, delta)
#
# p = pq.Program().inst(H(0)).measure(0,0)
# results = qvm.run(p, [0])
# print( results)

# tutorial: ravisankar:
# https://medium.com/@rasa97uchiha/hello-world-s-quantum-teleportation-using-rigettis-forest-64b9afda7fba