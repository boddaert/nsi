# Imporatation du module
from enigma.machine import EnigmaMachine

# Machine enigma configurée avec les rotors III,IV et II, le réflecteur C
# et le tableau de connexions CE DV IO NR ST QX AP
machine = EnigmaMachine.from_key_sheet(rotors = "III IV II",
                                       reflector = "C",
                                       plugboard_settings = "CE DV IO NR ST QX AP")

