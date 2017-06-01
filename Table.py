import math

class Table:

    def __init__(self, material, length, width):
        """Defines the table parameters and determines the positioning of diamond sights. Constant value sight positions are defined along
        the x axis and y axis. The lower left hand corner of the table (viewing down the table) is defined as the origin. The width and length
        values are measured from cushion nose to cushion nose. All lengths are in meters. All masses are in kg.

            Args:
                N/A

            Returns:
                N/A

            """
        self.material = material
        self.length = length
        self.width = width
        self.X_SIGHT1 = length / 4.0
        self.X_SIGHT2 = length / 2.0
        self.X_SIGHT3 = length * 3.0 / 4.0
        self.Y_SIGHT1 = length / 8.0
        self.Y_SIGHT2 = length * 2.0 / 8.0
        self.Y_SIGHT3 = length * 3.0 / 8.0
        self.Y_SIGHT4 = length * 5.0 / 8.0
        self.Y_SIGHT5 = length * 6.0 / 8.0
        self.Y_SIGHT6 = length * 7.0 / 8.0

    def place_rack(self, ball_diameter, cue_x, cue_y):
        """Determines the set of possible initial positions of pool balls based on table geometry and ball diameter.

            Args:
                self, ball_diameter

            Returns:
                list: a set of all initial starting positions for balls 1-15 (inclusive)

            """

        rack_length = math.sqrt((5 * ball_diameter)**2 - (2.5 * ball_diameter)**2)
        center_to_center_length = rack_length - ball_diameter
        length_increment = center_to_center_length / 4.0

        POSITION0 = [cue_x, cue_y]
        POSITION1 = [self.X_SIGHT2, self.Y_SIGHT5, False]
        POSITION2 = [self.X_SIGHT2 - ball_diameter / 2.0, self.Y_SIGHT5 + 1 * length_increment, False]
        POSITION3 = [self.X_SIGHT2 + ball_diameter / 2.0, self.Y_SIGHT5 + 1 * length_increment, False]
        POSITION4 = [self.X_SIGHT2 - ball_diameter, self.Y_SIGHT5 + 2 * length_increment, False]
        POSITION5 = [self.X_SIGHT2, self.Y_SIGHT5 + 2 * length_increment, False]
        POSITION6 = [self.X_SIGHT2 + ball_diameter, self.Y_SIGHT5 + 2 * length_increment, False]
        POSITION7 = [self.X_SIGHT2 - 1.5 * ball_diameter, self.Y_SIGHT5 + 3 * length_increment, False]
        POSITION8 = [self.X_SIGHT2 - 0.5 * ball_diameter, self.Y_SIGHT5 + 3 * length_increment, False]
        POSITION9 = [self.X_SIGHT2 + 0.5 * ball_diameter, self.Y_SIGHT5 + 3 * length_increment, False]
        POSITION10 = [self.X_SIGHT2 + 1.5 * ball_diameter, self.Y_SIGHT5 + 3 * length_increment, False]
        POSITION11 = [self.X_SIGHT2 - 2 * ball_diameter, self.Y_SIGHT5 + 4 * length_increment, False]
        POSITION12 = [self.X_SIGHT2 - 1 * ball_diameter, self.Y_SIGHT5 + 4 * length_increment, False]
        POSITION13 = [self.X_SIGHT2, self.Y_SIGHT5 + 4 * length_increment, False]
        POSITION14 = [self.X_SIGHT2 + 1 * ball_diameter, self.Y_SIGHT5 + 4 * length_increment, False]
        POSITION15 = [self.X_SIGHT2 + 2 * ball_diameter, self.Y_SIGHT5 + 4 * length_increment, False]

        list = [POSITION0, POSITION1, POSITION2, POSITION3, POSITION4, POSITION5, POSITION6, POSITION7, POSITION8, POSITION9, POSITION10, POSITION11, POSITION12, POSITION13, POSITION14, POSITION15]
        return list

    def strike_cue(self, balls_list, strike_vector, strike_strength, strike_proximity):
        """Performs a strike sequence, performs needed calculations, and updates the positions of balls on the table.

            Args:
                balls_list: A list of all balls 0-15 (inclusive), with ball 0 being the cue
                strike_vector: A unit vector in the xy plane that defines where the cue will be hit
                strike_strength: Defines the force (in Newtons) the cue is hit with
                strike_proximity: The strike position relative to the cue ball center

            Returns:
                list: a set of all final positions for balls 0-15 (inclusive)

            """