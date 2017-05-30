from random import randint

def create_balls():

    """Creates a list of balls for the pool table. Ball 0 is the cue ball.

        Args:
            N/A

        Returns:
            list: The set of Balls 1-15 (inclusive) and the cue ball.

        """

    list = []
    for i in range(0,16):
        if i == 0 :
            new_ball = Ball(i, 0.17, 0)
        else:
            new_ball = Ball(i, 0.16, 0)
        list.append(new_ball)

    return list

def position_balls(table, balls_list):

    """Assigns a position x and y to balls 1-15 (inclusive) in the balls_list.

        Args:
            table: A table object that can access method place_rack
            balls_list: A list of created balls

        Returns:
            N/A

        """

    ball_diameter = balls_list[0].BALL_DIAMETER
    positions = table.place_rack(ball_diameter)

    for i in range(1,16):
        if i == 1:
            balls_list[i].x = positions[1][0]
            balls_list[i].y = positions[1][1]
            positions[1][2]= True
        elif i == 8:
            balls_list[i].x = positions[5][0]
            balls_list[i].y = positions[5][1]
            positions[5][2] = True

        #This gives poor runtime, find a better solution.
        else:
            assigned = False
            while assigned:
                val = randint(0,15)
                if positions[val][2] == False:
                    balls_list[i].x = positions[val][0]
                    balls_list[i].y = positions[val][1]
                    positions[val][2] = True
                    assigned = True




