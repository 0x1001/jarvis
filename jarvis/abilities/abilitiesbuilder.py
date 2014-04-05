################################################################################
################################### Class ######################################
################################################################################
class AbilitiesBuilderException(Exception): pass

class AbilitiesBuilder(object):
    """
        Abilities builder

        Attributes:

    """
    def generate(self):
        """
            Generates abilities list

            Input:
            Nothing

            Returns:
            Abilities
        """
        import os
        import imp
        from abilities import Abilities

        abilities_path = os.path.dirname(os.path.abspath(__file__))

        abilities_list = Abilities()

        counter = 0
        while True:
            abilitie_name = "func_" + str(counter) + ".py"

            try: abilitie_module = imp.load_source(abilitie_name,os.path.join(abilities_path,abilitie_name))
            except IOError: break
            except ImportError as error: raise AbilitiesBuilderException("Cannot load: " + abilitie_name + "Error: " + str(error))

            abilities_list.append(abilitie_module.do)
            counter += 1

        return abilities_list

