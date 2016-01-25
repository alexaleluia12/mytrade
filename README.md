
Aplicação de linha de comando para cálculo de porcentagem.<br/><br/>
``mytrade 20.8 12.34 45.2 -alta 3.2``<br/>
Aplica uma alta de 3.2 % em cada valor respecitivamente e os retorna na mesma na
mesma ordem


uso
```sh
mytrade 15.12 -queda 0.93
mytrade 20.8 12.34 45.2 # padrao queda de 2%
mytrade 20.8 12.34 45.2 -alta 3.2
```

Utiliza python 3 e a biblioteca build in argparse.

--
Rodar<br/>
``python3 mytrade.py 15.12 -queda 0.93``

\-Rodar sem digitar 'python3 mytrade.py' *Posix apenas
- tire a extenção .py
- ``chmod +x mytrade``
- ponhe esse arquivo no bin (poder ser do usuário ou do sistema)



