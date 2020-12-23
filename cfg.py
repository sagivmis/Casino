from casino import Player
new_player = Player("Player",100)
opponent = Player("OP", 99999)

colordict = {'Spade': 'Black', 'Club': 'Black', 'Heart': 'Red', 'Diamond': 'Red'}
suits = ('Heart', 'Diamond', 'Spade', 'Club')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10}