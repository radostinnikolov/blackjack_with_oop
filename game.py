from player import Player
from dealer import Dealer

player = Player()
dealer = Dealer()


def print_score():
    print(f"Player has {player.current_score()}")
    print(f"Dealer has {dealer.current_score()}")


def wants_to_play_again():
    wants_to_play_again = input("Do you want to play again - 'y' or 'n'?: ")
    if wants_to_play_again.lower() == "y":
        player.cards = []
        dealer.cards = []
        player.has_bj = False
        dealer.has_bj = False
        return True
    else:
        return False


def game():
    game_is_over = False
    while True:
        player.pick_a_card()
        player.pick_a_card()
        dealer.pick_a_card()
        print_score()
        player.bj_checker()
        if player.has_bj:
            dealer.pick_a_card()
            dealer.bj_checker()
            if not dealer.has_bj:
                print("Player has BlackJack and wins!")
                wants_to_play = wants_to_play_again()
                if wants_to_play:
                    game()
                else:
                    break
                break
            else:
                print("Push")
                break
        else:
            while True:
                player_choice = input("Hit or stand?: ")
                if player_choice.lower() == "hit":
                    player.pick_a_card()
                    if player.current_score() > 21:
                        print("Player loses - went over 21")
                        game_is_over = True
                        wants_to_play = wants_to_play_again()
                        if wants_to_play:
                            game()
                        else:
                            break
                        break
                    elif player.current_score() == 21:
                        print("Player has 21!")
                        break
                    else:
                        print_score()
                elif player_choice.lower() == "stand":
                    print(f"Player stands on {player.current_score()}")
                    print(f"Now it's dealer's turn!")
                    break
            if game_is_over:
                break
            while True:
                dealer.pick_a_card()
                dealer.bj_checker()
                if dealer.has_bj:
                    print("Dealer has BlackJack!")
                    wants_to_play = wants_to_play_again()
                    if wants_to_play:
                        game()
                    else:
                        break
                    break
                if dealer.current_score() < 17:
                    print(f"Dealer has {dealer.current_score()}")
                    continue
                else:
                    if dealer.current_score() > 21:
                        print_score()
                        print("Dealer loses - went over 21")
                        game_is_over = True
                        wants_to_play = wants_to_play_again()
                        if wants_to_play:
                            game()
                        else:
                            break
                        break
                    if dealer.current_score() == 21:
                        print("Dealer has 21!")
                        break
                print_score()
                break
            if game_is_over:
                break
            if player.has_bj or dealer.has_bj:
                break
            else:
                if player.current_score() > dealer.current_score():
                    print("Player wins!")
                elif dealer.current_score() > player.current_score():
                    print("Dealer wins!")
                elif dealer.current_score() == player.current_score():
                    print("Push!")
        wants_to_play = wants_to_play_again()
        if wants_to_play:
            game()
        else:
            break


game()
