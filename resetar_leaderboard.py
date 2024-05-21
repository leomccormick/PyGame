try:
    open('leaderboard.txt', 'w').close()
    print("Leaderboard limpo com sucesso.")
except FileNotFoundError:
    print("Nada para limpar, o leaderboard está vazio.")