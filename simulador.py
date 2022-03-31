import random
import matplotlib.pyplot as plt


class Simulator_theory:
    def __init__(self, num_bets, init_bet, color, wallet, isGambler):
        self.num_bets = num_bets
        self.init_bet = init_bet
        self.color = color
        self.counter = 0
        self.result = [0 for i in range(num_bets)]
        self.wallet = wallet
        self.isGambler = isGambler
        self.lost = (False, -1)
        self.history = {}


    def alg(self):
        won = False
        current_bet = self.init_bet
        num_of_bets = 1

        wallet = self.wallet

        self.history = {}

        while(not won and not self.lost[0]):
            x = random.randint(0,1)
            
            self.history["initialwallet"] = self.wallet
            
            if(self.color != x): 
                if(self.isGambler):
                    wallet = wallet - current_bet
                    if(wallet < 0):
                        self.wallet = wallet
                        self.lost = (True, num_of_bets)
                        
                        self.history["num_bets"] = num_of_bets
                        self.history["currentWallet"] = self.wallet
                
                current_bet = current_bet * 2
                num_of_bets = num_of_bets + 1
                       
            else:
                won = True
                self.result[self.counter] = num_of_bets
                self.counter = self.counter + 1
                self.wallet = self.wallet + self.init_bet
        
                
    
    def start(self):
        stop = 0
        while(stop < self.num_bets and not self.lost[0]):
            self.alg()
            stop = stop + 1

          

    def plot(self):
        y=self.result
        x=[i+1 for i in range(self.num_bets)]

        fig = plt.figure(figsize=(10,5))
        plt.plot(x,y)
        plt.xlabel('Bet number')
        plt.ylabel('Number of bets until reset')
        plt.yticks(y)
        plt.title("Results")
        fig.savefig('Results.jpg',bbox_inches='tight', dpi=150)
    
    def stats(self):
        avg = round(sum(self.result) / len(self.result), 2)
        min_v = min(self.result)
        max_v = max(self.result)
        print(f'Avg: {avg}')
        print("Min: " +  str(min_v))
        print("Max: " + str(max_v))
        print("Wallet: " + str(self.wallet))

        if(self.lost[0]):
            print("Initial Wallet: " + str(self.history.get("initialwallet")))
            print("Number of bets: " + str(self.history.get("num_bets")))
            print("Current Wallet: " + str(self.history.get("currentWallet")))
            


if __name__ == "__main__":
    obj = Simulator_theory(500, 0.25, 0, 200, True)
    obj.start()
    obj.plot()
    obj.stats()


    