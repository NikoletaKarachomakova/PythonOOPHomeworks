from GuildSystem.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.list_players = []

    def assign_player(self, player: Player):
        if player in self.list_players:
            return f"Player {player.name} is already in the guild."
        elif player not in self.list_players and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        elif player not in self.list_players and player.guild == "Unaffiliated":
            self.list_players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        list_player_names = [p.name for p in self.list_players]
        if player_name not in list_player_names:
            return f"Player {player_name} is not in the guild."
        player_for_change = self.list_players[list_player_names.index(player_name)]  # player/object to be removed
        player_for_change.name = "Unaffiliated"
        del player_for_change
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for p in self.list_players:
            result += f"{p.player_info()}"
        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())

