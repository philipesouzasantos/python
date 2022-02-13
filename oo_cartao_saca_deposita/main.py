from conta import Conta
from cliente import Cliente
from datas import Data

# cria conta
conta = Conta(321, "Phil", 100.0, 1000.0)
conta2 = Conta(123, "Lu", 1000.0, 1500.0)

conta2.deposita(1000.0)

conta2.saca(500.0)

conta2.extrato()

conta2.transfere(10.0, conta)

conta2.extrato()

conta.extrato()

# d = Data(21, 11, 2007)

# d.formatada()

