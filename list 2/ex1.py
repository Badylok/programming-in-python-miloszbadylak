class Solution:
    """
    Represents a chemical or biochemical solution.

    Attributes:
        name (str): Name of the given substance.
        concentration (float): Concentration of the solution in mg/mL.
        volume (float): Volume of the solution in mL.
    """

    def __init__(self, name, concentration, volume):
        """
        A constructor which creates a solution.

        Args:
            name (str): Name of the solution.
            concentration (float): Concentration of the solution in mg/mL.
            volume (float): Volume of the solution in mL.

        Raises:
            ValueError: If concentration or volume are non-positive.
            TypeError: If name is not a string. If concentration or volume are not an int or float
        """

        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(concentration, (int, float)) or not isinstance(
            volume, (int, float)
        ):
            raise TypeError("'Concentration' and 'Volume' must be int or float.")

        if concentration <= 0:
            raise ValueError("'Concentration' must be positive!")
        if volume <= 0:
            raise ValueError("'Volume' must be positive!")

        self.name = name
        self.concentration = concentration
        self.volume = volume

    def __str__(self):
        """
        Returns formatted information about the solution.
        """
        return f"Solution: {self.name} ({self.concentration} mg/mL, {self.volume} mL)"

    def add(self, other):
        """
        Combines two solutions of the same solute, updating the concentration and total volume.

        Args:
            other (Solution): The second solution object to combine.

        Raises:
            ValueError: If the given solutes are different.
        """
        if self.name != other.name:
            raise ValueError("You cannot combine different solutes.")

        total_mass = (self.concentration * self.volume) + (
            other.concentration * other.volume
        )
        self.volume += other.volume
        self.concentration = total_mass / self.volume

    def dilute(self, factor):
        """
        Reduces concentration by the given dilution factor.

        Args:
            factor (float): The factor by which the solution will be diluted.

        Raises:
            ValueError: If the factor is non-positive.
        """
        if factor <= 0:
            raise ValueError("'Factor' must be positive!")

        self.concentration = self.concentration / factor
        self.volume = self.volume * factor

    def __eq__(self, other):
        """
        Checks if two solutions have the same name and concentration.
        """
        return self.name == other.name and self.concentration == other.concentration


# Tests


def test_solution():
    """
    Executes a series of tests to verify the class functionality and prints information if all tests have passed.
    """

    roztwor1 = Solution("NaCl", 10, 50)
    roztwor2 = Solution("NaCl", 10, 50)

    assert roztwor1 == roztwor2

    diff_solute = Solution("KCl", 20, 10)
    try:
        roztwor1.add(diff_solute)
        assert False
    except ValueError:
        pass

    try:
        wrong_type = Solution("NaCl", "twenty", 50)
        assert False
    except TypeError:
        pass

    try:
        negative_volume = Solution("NaCl", 20, -10)
        assert False
    except ValueError:
        pass

    try:
        negative_factor = Solution("NaCl", 20, 50).dilute(-5)
        assert False
    except ValueError:
        pass

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()

    roztwor1 = Solution("NaCl", 10, 50)
    roztwor2 = Solution("NaCl", 20, 50)

    print("\nStart:\n", roztwor1)

    roztwor1.add(roztwor2)
    print("\nAfter mix:\n", roztwor1)

    roztwor1.dilute(2)
    print("\nAfter dilution:\n", roztwor1)
