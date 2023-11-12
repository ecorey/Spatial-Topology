import part1a as p1a
import part1b as p1b
import part1c as p1c
import part2a as p2a
import part2b as p2b
import part2c as p2c
import conclusions as c


def print_menu():
    """The print_menu function prints the display menu to screen."""
    print('''1 -> part 1.a
2 -> part 1.b
3 -> part 1.c
4 -> part 2.a
5 -> part 2.b
6 -> part 2.c
7 -> conclusions
8 -> quit
''')


def menu_selection(ch):
    """"""
    if ch == '1':
        p1a.prt1_a_disjoin()
        p1a.prt1_a_embrace()
        p1a.prt1_a_attach()
        p1a.prt1_a_entwined()
        p1a.prt1_a_meet()
        p1a.prt1_a_overlap()
        p1a.prt1_a_coveredBy()
        p1a.prt1_a_covers()
        p1a.prt1_a_inside()
        p1a.prt1_a_equals()
        p1a.prt1_a_contains()

        print_menu()
        selection = input('Enter menu selection: ')
        menu_selection(selection)
    if ch == '2':
        p1b.prt1_b_disjoin()
        p1b.prt1_b_embrace()
        p1b.prt1_b_attach()
        p1b.prt1_b_entwined()
        p1b.prt1_b_meet()
        p1b.prt1_b_overlap()
        p1b.prt1_b_coveredBy()
        p1b.prt1_b_covers()
        p1b.prt1_b_inside()
        p1b.prt1_b_equals()
        p1b.prt1_b_contains()

        print_menu()
        selection = input('Enter menu selection: ')
        menu_selection(selection)
    if ch == '3':
        p1c.prt1_c_disjoin()
        p1c.prt1_c_embrace()
        p1c.prt1_c_attach()
        p1c.prt1_c_entwined()
        p1c.prt1_c_meet()
        p1c.prt1_c_overlap()
        p1c.prt1_c_coveredBy()
        p1c.prt1_c_covers()
        p1c.prt1_c_inside()
        p1c.prt1_c_equals()
        p1c.prt1_c_contains()

        print_menu()
        selection = input('Enter menu selection: ')
        menu_selection(selection)
    if ch == '4':
        p2a.prt2_a_disjoin()
        p2a.prt2_a_embrace()
        p2a.prt2_a_attach()
        p2a.prt2_a_entwined()
        p2a.prt2_a_meet()
        p2a.prt2_a_overlap()
        p2a.prt2_a_coveredBy()
        p2a.prt2_a_covers()
        p2a.prt2_a_inside()
        p2a.prt2_a_equals()
        p2a.prt2_a_contains()

        print_menu()
        selection = input('Enter menu selection: ')
        menu_selection(selection)
    if ch == '5':
        p2b.prt2_b_disjoin()
        p2b.prt2_b_embrace()
        p2b.prt2_b_attach()
        p2b.prt2_b_entwined()
        p2b.prt2_b_meet()
        p2b.prt2_b_overlap()
        p2b.prt2_b_coveredBy()
        p2b.prt2_b_covers()
        p2b.prt2_b_inside()
        p2b.prt2_b_equals()
        p2b.prt2_b_contains()

        print_menu()
        selection = input('Enter menu selection: ')
        menu_selection(selection)
    if ch == '6':
        p2c.prt2_c_disjoin()
        p2c.prt2_c_embrace()
        p2c.prt2_c_attach()
        p2c.prt2_c_entwined()
        p2c.prt2_c_meet()
        p2c.prt2_c_overlap()
        p2c.prt2_c_coveredBy()
        p2c.prt2_c_covers()
        p2c.prt2_c_inside()
        p2c.prt2_c_equals()
        p2c.prt2_c_contains()

        print_menu()
        selection = input('Enter menu selection: ')
        menu_selection(selection)
    if ch == '7':
        c.conclusion()

        print_menu()
        selection = input('Enter menu selection: ')
        menu_selection(selection)

    if ch == '8':
        quit()


def menu_control():
    """Controls main program"""
    print_menu()
    selection = input('Enter menu selection: ')
    menu_selection(selection)
