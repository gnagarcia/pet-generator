"""Test for my functions and to see if each characteristic of the pet is being randomly generated.

"""

import functions

#test_1 fun fact
test_1 = Pet()
test_1.get_fun_fact()

assert (test_1.get_fun_fact() in Pet.fun_fact)

#test_2 smell
test_2 = Pet()
test_2.get_smell()

assert (test_2.get_smell() in Pet.smell)

#test_3 texture
test_3 = Pet()
test_3.get_texture()

assert (test_3.get_texture() in Pet.texture)