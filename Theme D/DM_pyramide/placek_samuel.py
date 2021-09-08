# -*- coding: utf-8 -*-

PART_SPACING_OFFSET: int = 3


def write(value: str):
	print(value, end="")


def main():
	print("Choisissez un nombre (1-5): ", end="")
	nbr: int = int(input(""))

	# if nbr < 1 or nbr > 5:
	# 	raise ValueError("Invalid input: " + str(nbr))

	# Compute the base spacing for the first part
	spacing: int = -PART_SPACING_OFFSET
	value: int = 2
	for i in range(nbr):
		spacing += value
		spacing += PART_SPACING_OFFSET
		value += 2 if i == 0 else 1
	spacing -= (nbr - 1)

	# Draw every tree part except the last one
	star_offset: int = 0
	for i in range(nbr):
		part_size: int = 3 + i

		if i == (nbr - 1):
			draw_base(nbr, spacing, part_size, star_offset)
			break

		draw_part(spacing, part_size, star_offset)
		star_offset += 2 * (PART_SPACING_OFFSET - 1) + (part_size * 2)

		spacing -= part_size
		spacing -= PART_SPACING_OFFSET - 1


def draw_part(spacing: int, part_size: int, star_offset: int):
	for i in range(part_size):
		star_nbr: int = 1 + (i * 2) + star_offset

		write(" " * spacing)

		write("/")
		write("*" * star_nbr)
		write("\\")

		write("\n")

		spacing -= 1


def draw_base(number: int, spacing: int, part_size: int, star_offset: int):
	door_size: int = 1
	if number > 1:
		door_size += 2
	if number == 5:
		door_size += 2

	door_offset: int = int((door_size - 1) / 2)

	for i in range(part_size):
		star_nbr: int = i + int(star_offset / 2) - door_offset

		write(" " * spacing)

		write("/")

		write("*" * star_nbr)
		if (part_size - i) <= number:
			if number == 5 and i == 4:
				write("|" * 3)
				write("$")
				write("|")
			else:
				write("|" * door_size)
		else:
			write("*" * door_size)
		write("*" * star_nbr)

		write("\\")

		write("\n")

		spacing -= 1


if __name__ == "__main__":
	main()