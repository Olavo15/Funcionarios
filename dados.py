from funcionarios import Funcionario

Funcionario = Funcionario ('Olavo' , 'Teste@test.com')

Funcionario .cadastro_hora('Jan', 350)

Funcionario .cadastro_hora('Fev', 100)

Funcionario .cadastro_salario_hora('Jan', 40)

Funcionario .cadastro_salario_hora('Fev', 105)

print(Funcionario)

print(Funcionario .calcula_salario('Jan'))

print(Funcionario  .calcula_salario('Fev'))

