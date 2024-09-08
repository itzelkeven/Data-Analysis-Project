# Kevin Ramos
import csv
import matplotlib.pyplot as plt
titles = []
copies = []
genres = []
devs = []
pubs = []
dates = []

# Takes the data file to be opened and organized
def plot_info(data):
   with open(data, 'r') as games:
       games = csv.reader(games)
       next(games)
       for line in games:
           game,sold,date,genre,dev,pub = line
           titles.append(game)
           sold.split()
           space = sold.find(' ')
           sold = float(sold[0:space]) * 1000000
           copies.append(sold)
           devs.append(dev)
           genres.append(genre)
           pubs.append(pub)
           dates.append(date)
           print(f'Game: {game}, Copies: {sold}')


       # Shorten Game Titles for better visibility of graph
       shortened_title_x = [name[:5] for name in titles]

       # Shorten Developer Names for better visibility of graph
       shortened_dev_x = [word[:5] for word in devs]

       plt.figure(figsize=(10, 6))
       plt.ylim(0,20000000)
       plt.bar(shortened_title_x, copies)
       plt.title(f'Game and Copies Sold')
       plt.xlabel('Games')
       plt.ylabel('Copies Sold (Million)')
       plt.xticks(rotation=45)
       plt.yticks([0, 5000000, 10000000, 15000000, 20000000], ['0', '5', '10', '15', '20'])
       plt.savefig('Game Vs Price')
       plt.clf()

       plt.figure(figsize=(10, 6))
       plt.bar(shortened_dev_x, copies)
       plt.title(f'Developers and Sold Games')
       plt.xlabel('Developers')
       plt.ylabel('Copies Sold (Million)')    
       plt.xticks(rotation=45)
       plt.yticks([0, 5000000, 10000000, 15000000, 20000000], ['0', '5', '10', '15', '20'])
       plt.savefig('Developers and Games Sold')
       plt.clf()

# Calculates which game has the most sold copies out of all of them
def calc_max(data):
   with open(data, 'r') as games:
       games = csv.reader(games)
       total_max = 0
       w_dev = ''
       w_game = ''
       next(games)
       for line in games:
           game,sold,_,_,dev,_ = line
           space = sold.find(' ')
           sold = float(sold[0:space]) * 1000000
           if sold > total_max:
               total_max = sold
               w_dev = dev
               w_game = game
   return [w_dev, w_game, total_max]


           
# Main Program
if __name__ == "__main__":
   plot_info('ps4_games.csv')
   ans = calc_max('ps4_games.csv')
   
   print(f'OUTPUT Developer: {ans[0]}')
   print(f'OUTPUT Game: {ans[1]}')
   print(f'OUTPUT # of Copies Sold: {ans[2]}')
