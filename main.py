from console.game import Game

if __name__ == '__main__':
    g = Game(True, True, 15, 0.0, -1)
    g.play()
    print(g.player_simulation_algorithms)
    print(g.wins)

