class CubeRotation:

    def __init__(self, ds, do, d1, d2, d3, d4):

        self.dimension_Selected = ds
        self.dimension_Opposite = do
        self.dimension1 = d1
        self.dimension2 = d2
        self.dimension3 = d3
        self.dimension4 = d4

    def d1_L1_Rotate(self, movement='down'):

        if movement == 'down':

            # Formula ---
            # ↓d1[l1:] = ↓ds[l1:], ↓do[l1:], ↑d3[l3:], ⤵d4

            # All position which would be changed
            l1 = (1, 4, 7)
            l3 = (3, 6, 9)

            # For storing Colors in position
            dsPositionColors = []
            d3PositionColors = []

            # Changing d1, ds colors on position L1
            for position in l1:
                # Storing Color
                a = self.dimension1[position]
                b = self.dimension_Opposite[position]

                # Storing Color of ds on position L1:
                dsPositionColors.append(self.dimension_Selected[position])

                # Changing Color
                self.dimension_Selected[position] = a  # ↓ds[l1:]
                self.dimension1[position] = b  # ↓d1[l1:]

            # Reversing the Colors stored of ds for d3[l3:] position
            dsPositionColors.reverse()

            # Getting Colors of d3 in l3: position
            for y in l3:
                # Storing Color of d3 on position l3:
                d3PositionColors.append(self.dimension3[y])

            # Reversing the Colors stored of d3 for do[l1:] position
            d3PositionColors.reverse()

            # Changing do[l1:] with d3[l3:](Reverse) colors
            for y in range(3):
                self.dimension_Opposite[l1[y]] = d3PositionColors[y]  # ↓do[l1:],

            # Changing d3[l3:] with ds[l1:](Reverse) colors   # ↑d3[l3:]
            self.dimension3[3] = dsPositionColors[0]
            self.dimension3[6] = dsPositionColors[1]
            self.dimension3[9] = dsPositionColors[2]

            # Storing d4 colors in variables
            a1 = self.dimension4[1]
            a2 = self.dimension4[2]
            a3 = self.dimension4[3]
            a4 = self.dimension4[4]
            a5 = self.dimension4[5]
            a6 = self.dimension4[6]
            a7 = self.dimension4[7]
            a8 = self.dimension4[8]
            a9 = self.dimension4[9]

            # Rotating the colors by right curved arrow   # ⤵d4
            self.dimension4[1] = a7
            self.dimension4[2] = a4
            self.dimension4[3] = a1
            self.dimension4[4] = a8
            self.dimension4[5] = a5
            self.dimension4[6] = a2
            self.dimension4[7] = a9
            self.dimension4[8] = a6
            self.dimension4[9] = a3

        elif movement == 'up':
            # Formula ---
            # ↑d1[l1:] = ↑ds[l1:], ↑do[l1:], ↓d3[l3:], ↶d4

            # All position which would be changed
            l1 = (1, 4, 7)
            l3 = (3, 6, 9)

            # For storing Colors in position
            doPositionColors = []
            d3PositionColors = []

            # Changing d1, do colors on position L1
            for position in l1:
                # Storing Color
                a = self.dimension1[position]
                b = self.dimension_Selected[position]

                # Storing Color of do on position L1:
                doPositionColors.append(self.dimension_Opposite[position])

                # Changing Color
                self.dimension_Opposite[position] = a  # ↑do[l1:]
                self.dimension1[position] = b  # ↑d1[l1:]

            # Reversing the Colors stored of do for d3[l3:] position
            doPositionColors.reverse()

            # Getting Colors of d3 in l3: position
            for y in l3:
                # Storing Color of d3 on position l3:
                d3PositionColors.append(self.dimension3[y])

            # Reversing the Colors stored of d3 for ds[l1:] position
            d3PositionColors.reverse()

            # Changing ds[l1:] with d3[l3:](Reverse) colors
            for y in range(3):
                self.dimension_Selected[l1[y]] = d3PositionColors[y]  # ↑ds[l1:],

            # Changing d3[l3:] with do[l1:](Reverse) colors   # ↓d3[l3:]
            self.dimension3[3] = doPositionColors[0]
            self.dimension3[6] = doPositionColors[1]
            self.dimension3[9] = doPositionColors[2]

            # Storing d4 colors in variables
            a1 = self.dimension4[1]
            a2 = self.dimension4[2]
            a3 = self.dimension4[3]
            a4 = self.dimension4[4]
            a5 = self.dimension4[5]
            a6 = self.dimension4[6]
            a7 = self.dimension4[7]
            a8 = self.dimension4[8]
            a9 = self.dimension4[9]

            # Rotating the colors by left curved arrow   # ↶d4
            self.dimension4[1] = a3
            self.dimension4[2] = a6
            self.dimension4[3] = a9
            self.dimension4[4] = a2
            self.dimension4[5] = a5
            self.dimension4[6] = a8
            self.dimension4[7] = a1
            self.dimension4[8] = a4
            self.dimension4[9] = a7

    def d1_L3_Rotate(self, movement='down'):

        if movement == 'down':

            # Formula ---
            # ↓d1[l3:] = ↓ds[l3:], ↓do[l3:], ↑d3[l1:], ↶d4

            l1 = (1, 4, 7)
            l3 = (3, 6, 9)

            dsPositionColors = []
            d3PositionColors = []

            for position in l3:

                a = self.dimension1[position]
                b = self.dimension_Opposite[position]

                dsPositionColors.append(self.dimension_Selected[position])

                self.dimension_Selected[position] = a  # ↓ds[l1:]
                self.dimension1[position] = b  # ↓d1[l1:]

            dsPositionColors.reverse()

            for y in l1:

                d3PositionColors.append(self.dimension3[y])

            d3PositionColors.reverse()

            for y in range(3):
                self.dimension_Opposite[l3[y]] = d3PositionColors[y]  # ↓do[l1:],

            self.dimension3[1] = dsPositionColors[0]
            self.dimension3[4] = dsPositionColors[1]
            self.dimension3[7] = dsPositionColors[2]

            a1 = self.dimension2[1]
            a2 = self.dimension2[2]
            a3 = self.dimension2[3]
            a4 = self.dimension2[4]
            a5 = self.dimension2[5]
            a6 = self.dimension2[6]
            a7 = self.dimension2[7]
            a8 = self.dimension2[8]
            a9 = self.dimension2[9]

            self.dimension2[1] = a3
            self.dimension2[2] = a6
            self.dimension2[3] = a9
            self.dimension2[4] = a2
            self.dimension2[5] = a5
            self.dimension2[6] = a8
            self.dimension2[7] = a1
            self.dimension2[8] = a4
            self.dimension2[9] = a7

        elif movement == 'up':

            l1 = (1, 4, 7)
            l3 = (3, 6, 9)

            doPositionColors = []
            d3PositionColors = []

            for position in l3:

                a = self.dimension1[position]
                b = self.dimension_Selected[position]

                doPositionColors.append(self.dimension_Opposite[position])

                self.dimension_Opposite[position] = a  # ↑do[l1:]
                self.dimension1[position] = b  # ↑d1[l1:]

            doPositionColors.reverse()

            for y in l1:

                d3PositionColors.append(self.dimension3[y])

            d3PositionColors.reverse()

            for y in range(3):
                self.dimension_Selected[l3[y]] = d3PositionColors[y]  # ↑ds[l1:],

            self.dimension3[1] = doPositionColors[0]
            self.dimension3[4] = doPositionColors[1]
            self.dimension3[7] = doPositionColors[2]

            a1 = self.dimension2[1]
            a2 = self.dimension2[2]
            a3 = self.dimension2[3]
            a4 = self.dimension2[4]
            a5 = self.dimension2[5]
            a6 = self.dimension2[6]
            a7 = self.dimension2[7]
            a8 = self.dimension2[8]
            a9 = self.dimension2[9]

            self.dimension2[1] = a7
            self.dimension2[2] = a4
            self.dimension2[3] = a1
            self.dimension2[4] = a8
            self.dimension2[5] = a5
            self.dimension2[6] = a2
            self.dimension2[7] = a9
            self.dimension2[8] = a6
            self.dimension2[9] = a3

    def d1_R1_Rotate(self, movement='left'):

        if movement == 'left':

            for i in range(1, 4):
                a = self.dimension1[i]
                b = self.dimension2[i]
                c = self.dimension3[i]
                d = self.dimension4[i]

                self.dimension2[i] = a
                self.dimension3[i] = b
                self.dimension4[i] = c
                self.dimension1[i] = d

            a1 = self.dimension_Opposite[1]
            a2 = self.dimension_Opposite[2]
            a3 = self.dimension_Opposite[3]
            a4 = self.dimension_Opposite[4]
            a5 = self.dimension_Opposite[5]
            a6 = self.dimension_Opposite[6]
            a7 = self.dimension_Opposite[7]
            a8 = self.dimension_Opposite[8]
            a9 = self.dimension_Opposite[9]

            self.dimension_Opposite[1] = a3
            self.dimension_Opposite[2] = a6
            self.dimension_Opposite[3] = a9
            self.dimension_Opposite[4] = a2
            self.dimension_Opposite[5] = a5
            self.dimension_Opposite[6] = a8
            self.dimension_Opposite[7] = a1
            self.dimension_Opposite[8] = a4
            self.dimension_Opposite[9] = a7

        elif movement == 'right':

            for i in range(1, 4):

                a = self.dimension1[i]
                b = self.dimension2[i]
                c = self.dimension3[i]
                d = self.dimension4[i]

                self.dimension2[i] = c
                self.dimension3[i] = d
                self.dimension4[i] = a
                self.dimension1[i] = b

            a1 = self.dimension_Opposite[1]
            a2 = self.dimension_Opposite[2]
            a3 = self.dimension_Opposite[3]
            a4 = self.dimension_Opposite[4]
            a5 = self.dimension_Opposite[5]
            a6 = self.dimension_Opposite[6]
            a7 = self.dimension_Opposite[7]
            a8 = self.dimension_Opposite[8]
            a9 = self.dimension_Opposite[9]

            self.dimension_Opposite[1] = a7
            self.dimension_Opposite[2] = a4
            self.dimension_Opposite[3] = a1
            self.dimension_Opposite[4] = a8
            self.dimension_Opposite[5] = a5
            self.dimension_Opposite[6] = a2
            self.dimension_Opposite[7] = a9
            self.dimension_Opposite[8] = a6
            self.dimension_Opposite[9] = a3

    def d1_R3_Rotate(self, movement='left'):

        if movement == 'left':

            for i in range(7, 10):

                a = self.dimension1[i]
                b = self.dimension2[i]
                c = self.dimension3[i]
                d = self.dimension4[i]

                self.dimension1[i] = d
                self.dimension2[i] = a
                self.dimension3[i] = b
                self.dimension4[i] = c

            a1 = self.dimension_Selected[1]
            a2 = self.dimension_Selected[2]
            a3 = self.dimension_Selected[3]
            a4 = self.dimension_Selected[4]
            a5 = self.dimension_Selected[5]
            a6 = self.dimension_Selected[6]
            a7 = self.dimension_Selected[7]
            a8 = self.dimension_Selected[8]
            a9 = self.dimension_Selected[9]

            self.dimension_Selected[1] = a7
            self.dimension_Selected[2] = a4
            self.dimension_Selected[3] = a1
            self.dimension_Selected[4] = a8
            self.dimension_Selected[5] = a5
            self.dimension_Selected[6] = a2
            self.dimension_Selected[7] = a9
            self.dimension_Selected[8] = a6
            self.dimension_Selected[9] = a3

        elif movement == 'right':

            for i in range(7, 10):

                a = self.dimension1[i]
                b = self.dimension2[i]
                c = self.dimension3[i]
                d = self.dimension4[i]

                self.dimension1[i] = b
                self.dimension2[i] = c
                self.dimension3[i] = d
                self.dimension4[i] = a

            a1 = self.dimension_Selected[1]
            a2 = self.dimension_Selected[2]
            a3 = self.dimension_Selected[3]
            a4 = self.dimension_Selected[4]
            a5 = self.dimension_Selected[5]
            a6 = self.dimension_Selected[6]
            a7 = self.dimension_Selected[7]
            a8 = self.dimension_Selected[8]
            a9 = self.dimension_Selected[9]

            self.dimension_Selected[1] = a3
            self.dimension_Selected[2] = a6
            self.dimension_Selected[3] = a9
            self.dimension_Selected[4] = a2
            self.dimension_Selected[5] = a5
            self.dimension_Selected[6] = a8
            self.dimension_Selected[7] = a1
            self.dimension_Selected[8] = a4
            self.dimension_Selected[9] = a7

    def d1_Full_Rotate(self, movement='left'):

        if movement == 'right':

            a1 = self.dimension1[1]
            a2 = self.dimension1[2]
            a3 = self.dimension1[3]
            a4 = self.dimension1[4]
            a5 = self.dimension1[5]
            a6 = self.dimension1[6]
            a7 = self.dimension1[7]
            a8 = self.dimension1[8]
            a9 = self.dimension1[9]

            self.dimension1[1] = a7
            self.dimension1[2] = a4
            self.dimension1[3] = a1
            self.dimension1[4] = a8
            self.dimension1[5] = a5
            self.dimension1[6] = a2
            self.dimension1[7] = a9
            self.dimension1[8] = a6
            self.dimension1[9] = a3

            ds = [self.dimension_Selected[1], self.dimension_Selected[2], self.dimension_Selected[3]]
            d4 = [self.dimension4[3], self.dimension4[6], self.dimension4[9]]
            do = [self.dimension_Opposite[7], self.dimension_Opposite[8], self.dimension_Opposite[9]]
            d2 = [self.dimension2[1], self.dimension2[4], self.dimension2[7]]

            self.dimension4[3] = ds[0]
            self.dimension4[6] = ds[1]
            self.dimension4[9] = ds[2]

            self.dimension_Selected[3] = d2[0]
            self.dimension_Selected[2] = d2[1]
            self.dimension_Selected[1] = d2[2]

            self.dimension_Opposite[9] = d4[0]
            self.dimension_Opposite[8] = d4[1]
            self.dimension_Opposite[7] = d4[2]

            self.dimension2[1] = do[0]
            self.dimension2[4] = do[1]
            self.dimension2[7] = do[2]

        elif movement == 'left':

            a1 = self.dimension1[1]
            a2 = self.dimension1[2]
            a3 = self.dimension1[3]
            a4 = self.dimension1[4]
            a5 = self.dimension1[5]
            a6 = self.dimension1[6]
            a7 = self.dimension1[7]
            a8 = self.dimension1[8]
            a9 = self.dimension1[9]

            self.dimension1[1] = a3
            self.dimension1[2] = a6
            self.dimension1[3] = a9
            self.dimension1[4] = a2
            self.dimension1[5] = a5
            self.dimension1[6] = a8
            self.dimension1[7] = a1
            self.dimension1[8] = a4
            self.dimension1[9] = a7

            ds = [self.dimension_Selected[1], self.dimension_Selected[2], self.dimension_Selected[3]]
            d4 = [self.dimension4[3], self.dimension4[6], self.dimension4[9]]
            do = [self.dimension_Opposite[7], self.dimension_Opposite[8], self.dimension_Opposite[9]]
            d2 = [self.dimension2[1], self.dimension2[4], self.dimension2[7]]

            self.dimension4[9] = do[0]
            self.dimension4[6] = do[1]
            self.dimension4[3] = do[2]

            self.dimension_Selected[1] = d4[0]
            self.dimension_Selected[2] = d4[1]
            self.dimension_Selected[3] = d4[2]

            self.dimension_Opposite[7] = d2[0]
            self.dimension_Opposite[8] = d2[1]
            self.dimension_Opposite[9] = d2[2]

            self.dimension2[7] = ds[0]
            self.dimension2[4] = ds[1]
            self.dimension2[1] = ds[2]

    def dimension_Changing(self, main_dim='d1'):

        if main_dim == 'd2':

            colors_do = []
            colors_ds = []
            formula_do = [7, 4, 1, 8, 5, 2, 9, 6, 3]
            formula_ds = [3, 6, 9, 2, 5, 8, 1, 4, 7]

            for f in formula_do:
                colors_do.append(self.dimension_Opposite[f])

            for f in formula_ds:
                colors_ds.append(self.dimension_Selected[f])

            for i in range(1, 10):
                self.dimension_Opposite[i] = colors_do[i-1]
                self.dimension_Selected[i] = colors_ds[i-1]

            d1 = self.dimension2
            d2 = self.dimension3
            d3 = self.dimension4
            d4 = self.dimension1

            self.dimension1 = d1
            self.dimension2 = d2
            self.dimension3 = d3
            self.dimension4 = d4

        elif main_dim == 'd3':

            colors_do = []
            colors_ds = []
            formula_do = [9, 8, 7, 6, 5, 4, 3, 2, 1]
            formula_ds = [9, 8, 7, 6, 5, 4, 3, 2, 1]

            for f in formula_do:
                colors_do.append(self.dimension_Opposite[f])

            for f in formula_ds:
                colors_ds.append(self.dimension_Selected[f])

            for i in range(1, 10):
                self.dimension_Opposite[i] = colors_do[i-1]
                self.dimension_Selected[i] = colors_ds[i-1]

            d1 = self.dimension3
            d2 = self.dimension4
            d3 = self.dimension1
            d4 = self.dimension2

            self.dimension1 = d1
            self.dimension2 = d2
            self.dimension3 = d3
            self.dimension4 = d4

        elif main_dim == 'd4':

            colors_do = []
            colors_ds = []

            formula_do = [3, 6, 9, 2, 5, 8, 1, 4, 7]
            formula_ds = [7, 4, 1, 8, 5, 2, 9, 6, 3]

            for f in formula_do:
                colors_do.append(self.dimension_Opposite[f])

            for f in formula_ds:
                colors_ds.append(self.dimension_Selected[f])

            for i in range(1, 10):
                self.dimension_Opposite[i] = colors_do[i-1]
                self.dimension_Selected[i] = colors_ds[i-1]

            d1 = self.dimension4
            d2 = self.dimension1
            d3 = self.dimension2
            d4 = self.dimension3

            self.dimension1 = d1
            self.dimension2 = d2
            self.dimension3 = d3
            self.dimension4 = d4

    def show_Colors(self, check_color):

        # For storing all colors with dimension without d['color']
        ds = {}
        do = {}
        d1 = {}
        d2 = {}
        d3 = {}
        d4 = {}

        # Checking If The Color Matches:

        if check_color == self.dimension_Selected['color']:
            for z in range(1, 10):

                # Storing value to respective dict
                ds[z] = self.dimension_Selected[z]
            return ds

        elif check_color == self.dimension_Opposite['color']:
            for z in range(1, 10):

                # Storing value to respective dict
                do[z] = self.dimension_Opposite[z]
            return do

        elif check_color == self.dimension1['color']:
            for z in range(1, 10):

                # Storing value to respective dict
                d1[z] = self.dimension1[z]
            return d1

        elif check_color == self.dimension2['color']:
            for z in range(1, 10):

                # Storing value to respective dict
                d2[z] = self.dimension2[z]
            return d2

        elif check_color == self.dimension3['color']:
            for z in range(1, 10):

                # Storing value to respective dict
                d3[z] = self.dimension3[z]
            return d3

        elif check_color == self.dimension4['color']:
            for z in range(1, 10):

                # Storing value to respective dict
                d4[z] = self.dimension4[z]
            return d4

        return self.dimension4['color']