usuario_correto = 'tobias'
senha_correta = 'tobias123'

nome_usuario = input('Digite o nome de usuário: ')
senha = input('Digite sua senha: ')

if nome_usuario == usuario_correto and senha == senha_correta:
  print('Login bem sucedido!\n')
else:
  print('Informações inválidas. Tente novamente.\n')

