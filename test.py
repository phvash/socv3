def killNeighbour(person_with_sword, everyone_left_in_circle):
    first_person_in_circle = everyone_left_in_circle[0]
    last_person_in_circle = everyone_left_in_circle[-1]

    # If there is only one person in the game, no point to continue
    if first_person_in_circle is last_person_in_circle:
        last_person_standing = everyone_left_in_circle[0] # declare the only person left as winner
        print last_person_in_circle
        return None # this ends the recursive loop

    else: # i.e there is at least two people left in the circle
        ''' Note: python US acts tolly Like a straight line
        so we have tell the last person on the line that he's neighbour is the first person on the line'''

        if person_with_sword is last_person_in_circle:
            neighbour = first_person_in_circle # this helps simulate a cicle from our list (which acts normally like straight line)
        else:
            neighbour_index = everyone_left_in_circle.index(person_with_sword) + 1
            neighbour = everyone_left_in_circle[neighbour_index]

    # kill your neighbour and remove his body
    everyone_left_in_circle.remove(neighbour)

    # check to see who is your new nechbau
    try: 
        new_neighbour_index = everyone_left_in_circle.index(person_with_sword) + 1
        new_neighbour = everyone_left_in_circle[new_neighbour_index]
    except IndexError: # i.e. you are the last person on the line
        new_neighbour = everyone_left_in_circle[0] # your new neighbour is now the first person on the list
    
    person_sword_gets_passed_to = new_neighbour # pass the sword to your new neighbour, don't kill him
    
    killNeighbour(person_sword_gets_passed_to, everyone_left_in_circle)

def startgame(number_of_people_in_circle):
    everyone = range(1, number_of_people_in_circle + 1) # form a circle
    person_with_sword = everyone[0] # give sword to number one to start the game
    # sit back and watch everyone kill their neighbour

    killNeighbour(person_with_sword, everyone)

if __name__ == '__main__':
    startgame(100) # pass the mumber of people in the circle
