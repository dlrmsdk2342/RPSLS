from RPSLS_player import RPSLS_player

class P19499(RPSLS_player):
  def __init__(self):
    self.round = 0

  def shoot(self):
    self.round += 1
    if self.round < 2:
        return "scissors"
    elif self.round >= 2:
        if self.competitor == "rock":
            return "spock"
        elif self.competitor == "scissors":
            return "rock"
        elif self.competitor == "paper":
            return "lizard"
        elif self.competitor == "lizard":
            return "scissors"
        elif self.competitor == "spock":
            return "paper"
        else:
            return "rock"
  
  def update(self, result: str, competitor_shot: str):
    self.competitor = competitor_shot