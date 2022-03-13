#converter para radianos

import math

a = float(input('Digite o valor do ângulo: '))

print ('O valor do cos é {:.2f}, do seno é {:.2f} e o valor da tangente é {:.2f}'
       .format(math.cos(a),math.sin(a),math.tan(a)))
