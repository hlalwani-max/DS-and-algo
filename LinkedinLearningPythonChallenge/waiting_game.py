import random, time


class Solution:
    def waiting_game(self):
        start = input("Press enter to start the game:")
        if start == "":
            rand = random.randrange(2, 5)
            start_game = input(
                "Press enter in {} seconds. Press enter again to start the timer, and enter to hit the timer.".format(
                    rand))
            start = time.time()
            while True:
                trigger = input()
                if trigger == "":
                    end = time.time()
                    elapsed = end - start
                    diff = elapsed - rand
                    if diff == float(0):
                        print("Win!!")
                        break
                    else:
                        print("Time elapsed: {}".format(elapsed))
                        if diff > 0:
                            print("{} seconds too slow".format(abs(diff)))
                            break
                        else:
                            print("{} seconds too fast".format(abs(diff)))
                            break

'''
  def waiting_game(self):
        start = input("Press enter to start the game:")
        if start == "":
            rand = random.randrange(2, 5)
            start_game = input(
                "Press enter in {} seconds. Press enter again to start the timer, and enter to hit the timer.".format(
                    rand))
            start = time.time()
            while True:
                trigger = input()
                if trigger == "":
                    end = time.time()
                    elapsed = end - start
                    diff = elapsed - rand
                    if diff == float(0):
                        print("Win!!")
                        break
                    else:
                        print("Time elapsed: {}".format(elapsed))
                        if diff > 0:
                            print("{} seconds too slow".format(abs(diff)))
                            break
                        else:
                            print("{} seconds too fast".format(abs(diff)))
                            break
'''




sol = Solution()
sol.waiting_game()
